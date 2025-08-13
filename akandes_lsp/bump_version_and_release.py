import subprocess
import re

def get_latest_tag():
    try:
        tag = subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0']).decode().strip()
        return tag
    except subprocess.CalledProcessError:
        return 'v0.0.0'

def get_commits_since_tag(tag):
    log = subprocess.check_output(['git', 'log', f'{tag}..HEAD', '--pretty=%s']).decode().splitlines()
    return log

def bump_version(version, bump_type):
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

def detect_bump_type(commits):
    for msg in commits:
        if 'BREAKING CHANGE' in msg or msg.lower().startswith('major:'):
            return 'major'
    for msg in commits:
        if 'feat' in msg or msg.lower().startswith('minor:'):
            return 'minor'
    return 'patch'

def main():
    tag = get_latest_tag()
    commits = get_commits_since_tag(tag)
    if not commits:
        print('No new commits since last tag.')
        return
    bump_type = detect_bump_type(commits)
    new_version = bump_version(tag, bump_type)
    print(f'Bumping version: {tag} -> {new_version} ({bump_type})')
    subprocess.check_call(['git', 'tag', new_version])
    subprocess.check_call(['git', 'push', 'origin', new_version])

if __name__ == '__main__':
    main()