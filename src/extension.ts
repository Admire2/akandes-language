// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import { activateLanguageClient, deactivateLanguageClient } from './client';

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {
	// Register Run GHDL Simulation command
	const runGHDLSimDisposable = vscode.commands.registerCommand('AkandeChips.runGHDLSim', async () => {
		const vhdlDir = vscode.Uri.joinPath(vscode.workspace.workspaceFolders?.[0].uri!, 'hdl_projects').fsPath;
		const fs = require('fs');
		const path = require('path');
		let vhdlFiles: string[] = [];
		try {
			vhdlFiles = fs.readdirSync(vhdlDir).filter((f: string) => f.endsWith('.vhd')).map((f: string) => path.join(vhdlDir, f));
		} catch (e) {
			vscode.window.showErrorMessage('No VHDL files found. Please generate HDL first.');
			return;
		}
		if (vhdlFiles.length === 0) {
			vscode.window.showErrorMessage('No VHDL files found. Please generate HDL first.');
			return;
		}
		const ghdlCmd = 'ghdl';
		const exec = require('child_process').execFile;
		// Analyze all VHDL files
		vscode.window.withProgress({ location: vscode.ProgressLocation.Notification, title: 'Running GHDL Simulation...' }, (progress) => {
			return new Promise((resolve) => {
				exec(ghdlCmd, ['-a', ...vhdlFiles], { cwd: vhdlDir }, (error: any, stdout: string, stderr: string) => {
					if (error) {
						vscode.window.showErrorMessage(`GHDL analyze failed: ${stderr || error.message}`);
						resolve(undefined);
						return;
					}
					// Try to elaborate and run the first entity (as a demo)
					const entity = path.basename(vhdlFiles[0], '.vhd');
					exec(ghdlCmd, ['-e', entity], { cwd: vhdlDir }, (error2: any, stdout2: string, stderr2: string) => {
						if (error2) {
							vscode.window.showErrorMessage(`GHDL elaborate failed: ${stderr2 || error2.message}`);
							resolve(undefined);
							return;
						}
						exec(ghdlCmd, ['-r', entity, '--stop-time=10ns'], { cwd: vhdlDir }, (error3: any, stdout3: string, stderr3: string) => {
							if (error3) {
								vscode.window.showErrorMessage(`GHDL run failed: ${stderr3 || error3.message}`);
							} else {
								vscode.window.showInformationMessage(`GHDL simulation output:\n${stdout3}`);
							}
							resolve(undefined);
						});
					});
				});
			});
		});
	});
	context.subscriptions.push(runGHDLSimDisposable);

	// Output diagnostic information
	console.log('Congratulations, your extension "AkandeChips" is now active!');

	// Register Hello World command
	const disposable = vscode.commands.registerCommand('AkandeChips.helloWorld', () => {
		vscode.window.showInformationMessage('Hello World from Akande!');
	});
	context.subscriptions.push(disposable);

	// Register Select Backend and Generate HDL command
	const selectBackendDisposable = vscode.commands.registerCommand('AkandeChips.selectBackend', async () => {
		const backend = await vscode.window.showQuickPick([
			{ label: 'VHDL', description: 'Generate VHDL code', value: 'vhdl' },
			{ label: 'SystemVerilog', description: 'Generate SystemVerilog code', value: 'sv' },
			{ label: 'Verilog', description: 'Generate Verilog code (future)', value: 'verilog' }
		], {
			title: 'Select HDL Backend',
			placeHolder: 'Choose a backend for code generation'
		});
		if (!backend) {
			vscode.window.showInformationMessage('Backend selection cancelled.');
			return;
		}
		const pythonPath = 'python'; // Or use vscode.workspace.getConfiguration('python').get('pythonPath')
		const scriptPath = vscode.Uri.joinPath(vscode.workspace.workspaceFolders?.[0].uri!, 'akandes_python_backend', 'generate_hdl.py').fsPath;
		const backendArg = backend.value;
		const args = [scriptPath, backendArg];
		const exec = require('child_process').execFile;
		vscode.window.withProgress({ location: vscode.ProgressLocation.Notification, title: `Generating HDL (${backend.label})...` }, (progress) => {
			return new Promise((resolve) => {
				exec(pythonPath, args, { cwd: vscode.workspace.workspaceFolders?.[0].uri.fsPath }, (error: any, stdout: string, stderr: string) => {
					if (error) {
						vscode.window.showErrorMessage(`HDL generation failed: ${stderr || error.message}`);
					} else {
						vscode.window.showInformationMessage(`HDL generation complete!\n${stdout}`);
					}
					resolve(undefined);
				});
			});
		});
	});
	context.subscriptions.push(selectBackendDisposable);
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
