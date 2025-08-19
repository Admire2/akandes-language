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
    keywords = [
        'chip', 'input', 'output', 'connect', 'simulate', 'clock', 'reset', 'wire', 'module', 'testbench'
    ]
    doc = ls.workspace.get_document(params.textDocument.uri)
    # pygls Document may not have word_at_position, so fallback to manual extraction
    try:
        current_word = doc.word_at_position(params.position)
    except AttributeError:
        # Fallback: extract word manually
        line = doc.lines[params.position.line]
        prefix = line[:params.position.character]
        import re
        match = re.search(r'(\w+)$', prefix)
        current_word = match.group(1) if match else ''
    items = []
    if current_word and current_word.startswith('chip'):
        items.append(CompletionItem(label='chips', kind=1, detail='AkandeChips keyword'))
        items.append(CompletionItem(label='AkandeChips', kind=7, detail='AkandeChips class'))
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
