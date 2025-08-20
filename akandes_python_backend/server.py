# Minimal, version-agnostic pygls LSP server for AkandeChips
from pygls.server import LanguageServer
from pygls.lsp.types import (
    InitializeParams, TextDocumentSyncKind, TextDocumentSyncOptions, DidOpenTextDocumentParams,
    CompletionParams, CompletionItem, CompletionList, Diagnostic, DiagnosticSeverity, Position, Range, Hover, MarkupContent
)
)

class AkandeLanguageServer(LanguageServer):
    def __init__(self):
        super().__init__()

server = AkandeLanguageServer()

@server.feature('initialize')
def on_initialize(ls, params):
    sync_kind = getattr(TextDocumentSyncKind, 'FULL', 1)
    return {
        'capabilities': {
            'textDocumentSync': TextDocumentSyncOptions(
                open_close=True,
                change=sync_kind
            ),
            'hoverProvider': True,
            'completionProvider': {'resolveProvider': False}
        }
    }

@server.feature('textDocument/didOpen')
def did_open(ls, params):
    ls.show_message('AkandeChips LSP: File opened!')
    text = getattr(params.textDocument, 'text', None)
    diagnostics = []
    if text:
        for i, line in enumerate(text.splitlines()):
            if 'todo' in line.lower():
                sev = getattr(DiagnosticSeverity, 'Warning', getattr(DiagnosticSeverity, 'WARNING', 2))
                diagnostics.append(Diagnostic(
                    range=Range(start=Position(line=i, character=0), end=Position(line=i, character=len(line))),
                    message="Found TODO in code.",
                    severity=sev
                ))
    ls.publish_diagnostics(params.textDocument.uri, diagnostics)

@server.feature('textDocument/completion')
def completions(ls, params):
    # AkandeChips language keywords
    import requests
    keywords = [
        'chip', 'input', 'output', 'connect', 'simulate', 'clock', 'reset', 'wire', 'module', 'testbench', 'AkandeAI'
    ]
    doc = ls.workspace.get_document(params.textDocument.uri)
    # Get current line and prefix
    try:
        current_word = doc.word_at_position(params.position)
    except AttributeError:
        line = doc.lines[params.position.line]
        prefix = line[:params.position.character]
        import re
        match = re.search(r'(\w+)$', prefix)
        current_word = match.group(1) if match else ''
    items = []
    # --- AkandeAI Multi-Provider Integration ---
    context_window = 20
    start_line = max(0, params.position.line - context_window)
    file_context = '\n'.join(doc.lines[start_line:params.position.line+1])
    prompt = (
        "You are AkandeAI, the AI engine for AkandeChips language. "
        "Given the following code context, suggest the next line or code completion in AkandeChips style. "
        "Respond only with the code suggestion.\n"
        f"Context:\n{file_context}\nCompletion:"
    )
    # Provider API keys
    openai_api_key = "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"
    anthropic_api_key = "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"
    google_api_key = "AIzaSyDBq-TLoYpCeFzIuHWtrox-B9uj2nCUFOs"
    # Provider selection: 'openai', 'anthropic', 'gemini', or 'all'
    ai_provider = 'all'  # Change to 'openai', 'anthropic', 'gemini', or 'all' for options
    # Collect completions from all providers
    def get_openai_completions():
        try:
            response = requests.post(
                "https://api.openai.com/v1/completions",
                headers={"Authorization": f"Bearer {openai_api_key}", "Content-Type": "application/json"},
                json={
                    "model": "text-davinci-003",
                    "prompt": prompt,
                    "max_tokens": 32,
                    "n": 3,
                    "stop": None,
                    "temperature": 0.3
                }
            )
            if response.status_code == 200:
                completions = response.json().get("choices", [])
                return [c.get("text", "").strip() for c in completions if c.get("text", "").strip()]
        except Exception:
            return []
        return []
    def get_anthropic_completions():
        try:
            response = requests.post(
                "https://api.anthropic.com/v1/complete",
                headers={
                    "x-api-key": anthropic_api_key,
                    "Content-Type": "application/json"
                },
                json={
                    "model": "claude-2",
                    "prompt": prompt,
                    "max_tokens_to_sample": 32,
                    "stop_sequences": ["\n"]
                }
            )
            if response.status_code == 200:
                completion = response.json().get("completion", "").strip()
                return [completion] if completion else []
        except Exception:
            return []
        return []
    def get_gemini_completions():
        try:
            response = requests.post(
                f"https://generativelanguage.googleapis.com/v1beta2/models/gemini-pro:generateText?key={google_api_key}",
                headers={"Content-Type": "application/json"},
                json={
                    "prompt": {"text": prompt},
                    "maxOutputTokens": 32
                }
            )
            if response.status_code == 200:
                candidates = response.json().get("candidates", [])
                return [c.get("output", "").strip() for c in candidates if c.get("output", "").strip()]
        except Exception:
            return []
        return []
    # Merge completions
    ai_completions = []
    if ai_provider in ('openai', 'all'):
        ai_completions += get_openai_completions()
    if ai_provider in ('anthropic', 'all'):
        ai_completions += get_anthropic_completions()
    if ai_provider in ('gemini', 'all'):
        ai_completions += get_gemini_completions()
    # Add AI completions to items
    for suggestion in ai_completions:
        items.append(CompletionItem(label=suggestion, kind=7, detail="AkandeAI (AI completion)", documentation="Suggested by AkandeAI (multi-provider)", sort_text="100"))
    # Always include the default keywords except 'chip'
    items.extend([CompletionItem(label=kw, kind=1, detail='AkandeChips keyword') for kw in keywords if kw != 'chip'])
    return CompletionList(is_incomplete=False, items=items)

@server.feature('textDocument/hover')
def hover(ls, params):
    doc = ls.workspace.get_document(params.textDocument.uri)
    try:
        word = doc.word_at_position(params.position)
    except AttributeError:
        line = doc.lines[params.position.line]
        prefix = line[:params.position.character]
        import re
        match = re.search(r'(\w+)$', prefix)
        word = match.group(1) if match else ''
    try:
        markup = MarkupContent(kind='markdown', value=f'**{word}**: AkandeChips language keyword.')
    except Exception:
        markup = {'kind': 'markdown', 'value': '**print**: Output text to the console.'}
    if word == 'print':
        return Hover(contents=markup)
    return None

## Removed duplicate completion feature registration

if __name__ == '__main__':
    server.start_io()
