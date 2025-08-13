import subprocess
import re
from typing import List, Tuple, Pattern
from datetime import datetime

# Customize your commit message rules here:
BUMP_RULES: List[Tuple[Pattern[str], str]] = [
    (re.compile(r'BREAKING CHANGE|major:', re.IGNORECASE), 'major'),
    (re.compile(r'feat|minor:', re.IGNORECASE), 'minor'),
    (re.compile(r'fix|patch:', re.IGNORECASE), 'patch'),
]

DEFAULT_BUMP: str = 'patch'

def get_latest_tag() -> str:
    try:
        tag: str = subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0']).decode().strip()
        return tag
    except subprocess.CalledProcessError:
        return 'v0.0.0'

def get_commits_since_tag(tag: str) -> List[str]:
    log: List[str] = subprocess.check_output(['git', 'log', f'{tag}..HEAD', '--pretty=%s']).decode().splitlines()
    return log

def bump_version(version: str, bump_type: str) -> str:
    major: int
    minor: int
    patch: int
    major, minor, patch = map(int, version.lstrip('v').split('.'))
    if bump_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif bump_type == 'minor':
        minor += 1
        patch = 0
    else:
        patch += 1
    return f'v{major}.{minor}.{patch}'

def detect_bump_type(commits: List[str]) -> str:
    for regex, bump_type in BUMP_RULES:
        for msg in commits:
            if regex.search(msg):
                return bump_type
    return DEFAULT_BUMP

def generate_release_notes(commits: List[str], new_version: str) -> str:
    date_str = datetime.now().strftime('%Y-%m-%d')
    features = []
    fixes = []
    breaking = []
    others = []
    for msg in commits:
        msg_lower = msg.lower()
        if 'breaking change' in msg_lower or msg_lower.startswith('major:'):
            breaking.append(msg)
        elif msg_lower.startswith('feat') or msg_lower.startswith('minor:'):
            features.append(msg)
        elif msg_lower.startswith('fix') or msg_lower.startswith('patch:'):
            fixes.append(msg)
        else:
            others.append(msg)

    notes = f"# Release {new_version} ({date_str})\n\n"
    if breaking:
        notes += "## Breaking Changes\n"
        for m in breaking:
            notes += f"- {m}\n"
        notes += "\n"
    if features:
        notes += "## Features\n"
        for m in features:
            notes += f"- {m}\n"
        notes += "\n"
    if fixes:
        notes += "## Fixes\n"
        for m in fixes:
            notes += f"- {m}\n"
        notes += "\n"
    if others:
        notes += "## Other Changes\n"
        for m in others:
            notes += f"- {m}\n"
        notes += "\n"
    return notes

def main() -> None:
    tag: str = get_latest_tag()
    commits: List[str] = get_commits_since_tag(tag)
    if not commits:
        print('No new commits since last tag.')
        return
    bump_type: str = detect_bump_type(commits)
    new_version: str = bump_version(tag, bump_type)
    print(f'Bumping version: {tag} -> {new_version} ({bump_type})')

    # Generate release notes
    notes: str = generate_release_notes(commits, new_version)
    with open('RELEASE_NOTES.md', 'w', encoding='utf-8') as f:
        f.write(notes)
    print(f'Release notes written to RELEASE_NOTES.md')

    subprocess.check_call(['git', 'tag', new_version])
    subprocess.check_call(['git', 'push', 'origin', new_version])

    # Build and upload documentation
    subprocess.check_call(['pip', 'install', 'sphinx'])
    subprocess.check_call(['make', 'html'], cwd='docs')
    subprocess.check_call(['actions/upload-artifact@v4', '--name', 'documentation', '--path', 'docs/_build/html'])

    # Publish to PyPI
    subprocess.check_call(['python', 'setup.py', 'sdist', 'bdist_wheel'])
    subprocess.check_call(['twine', 'upload', 'dist/*', '--username', '__token__', '--password', '${{ secrets.PYPI_API_TOKEN }}'])

    # Run tests
    subprocess.check_call(['pytest'])

    # Lint with flake8
    subprocess.check_call(['pip', 'install', 'flake8'])
    subprocess.check_call(['flake8', '.'])

    # Notify Discord
    subprocess.check_call(['curl', '-X', 'POST', '-H', 'Content-Type: application/json', '-d', '{"content": "🚀 New release ' + new_version + ' published! <' + 'https://github.com/' + 'your_github_repo' + '/releases/tag/' + new_version + '>' + '"}', '${{ secrets.DISCORD_WEBHOOK }}'])
    
    # Notify Slack
    subprocess.check_call(['curl', '-X', 'POST', '-H', 'Content-Type: application/json', '-d', '{"text": "🚀 New release ' + new_version + ' published! <' + 'https://github.com/' + 'your_github_repo' + '/releases/tag/' + new_version + '>' + '"}', '${{ secrets.SLACK_WEBHOOK_URL }}'])

if __name__ == '__main__':
    main()
