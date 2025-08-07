// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import { activateLanguageClient, deactivateLanguageClient } from './client';

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	// Output diagnostic information
	console.log('Congratulations, your extension "AkandeChips" is now active!');

	// Register Hello World command
	const disposable = vscode.commands.registerCommand('AkandeChips.helloWorld', () => {
		vscode.window.showInformationMessage('Hello World from Akande!');
	});
	context.subscriptions.push(disposable);

	// Activate the language client (connect to Python backend)
	activateLanguageClient(context);

	// Restore last session state if available
	const lastSession = context.workspaceState.get('lastSession');
	if (lastSession) {
		vscode.window.showInformationMessage('Restoring last session...');
		const { lastFile, cursor } = lastSession as { lastFile?: string, cursor?: { line: number, col: number } };
		if (lastFile) {
			vscode.workspace.openTextDocument(lastFile).then(doc => {
				vscode.window.showTextDocument(doc).then(editor => {
					if (cursor) {
						const pos = new vscode.Position(cursor.line, cursor.col);
						editor.selection = new vscode.Selection(pos, pos);
						editor.revealRange(new vscode.Range(pos, pos));
					}
				});
			});
		}
	}

	// Save session state on shutdown or file close
	function saveSession() {
		const editor = vscode.window.activeTextEditor;
		if (editor) {
			const position = editor.selection.active;
			context.workspaceState.update('lastSession', {
				lastFile: editor.document.uri.fsPath,
				cursor: { line: position.line, col: position.character }
			});
		}
	}

	context.subscriptions.push(
		vscode.workspace.onDidCloseTextDocument(saveSession),
		vscode.window.onDidChangeActiveTextEditor(saveSession),
		{ dispose: saveSession }
	);
}

// This method is called when your extension is deactivated
export function deactivate() {
	return deactivateLanguageClient();
}
