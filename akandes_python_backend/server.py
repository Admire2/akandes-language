
# Minimal, version-agnostic pygls LSP server for AkandeChips
from pygls.server import LanguageServer
from pygls.lsp.types import (
    InitializeParams, TextDocumentSyncKind, TextDocumentSyncOptions, DidOpenTextDocumentParams,
    CompletionParams, CompletionItem, CompletionList, Diagnostic, DiagnosticSeverity, Position, Range, Hover, MarkupContent
)

class AkandeLanguageServer(LanguageServer):
    def __init__(self):
        super().__init__("akandechips-lsp", "0.1.0")

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

@server.feature('textDocument/hover')
def hover(ls, params):
    doc = ls.workspace.get_document(params.textDocument.uri)
    word = doc.word_at_position(params.position)
    try:
        markup = MarkupContent(kind='markdown', value='**print**: Output text to the console.')
    except Exception:
        markup = {'kind': 'markdown', 'value': '**print**: Output text to the console.'}
    if word == 'print':
        return Hover(contents=markup)
    return None

@server.feature('textDocument/completion')
def completions(ls, params):
    items = [
        CompletionItem(label='print', detail='Print statement'),
        CompletionItem(label='def', detail='Function definition'),
        CompletionItem(label='if', detail='If statement')
    ]
    return CompletionList(is_incomplete=False, items=items)

if __name__ == '__main__':
    server.start_io()
