import * as path from 'path';
import { workspace, ExtensionContext } from 'vscode';
import {
  LanguageClient,
  LanguageClientOptions,
  ServerOptions
} from 'vscode-languageclient/node';

let client: LanguageClient;

export function activateLanguageClient(context: ExtensionContext) {
  // Path to the Python language server script
  const serverScript = context.asAbsolutePath(path.join('..', 'akandes_python_backend', 'server.py'));

  // Server options for launching the Python LSP
  const serverOptions: ServerOptions = {
    command: 'python',
    args: [serverScript],
    options: { cwd: path.dirname(serverScript) }
  };

  // Client options
  const clientOptions: LanguageClientOptions = {
    documentSelector: [{ scheme: 'file', language: 'akandechips' }],
    synchronize: {
      fileEvents: workspace.createFileSystemWatcher('**/.clientrc')
    }
  };

  // Create the language client
  client = new LanguageClient(
    'akandeLanguageServer',
    'AkandeChips Language Server',
    serverOptions,
    clientOptions
  );

  // Start the client
  client.start();
  // Add the client to subscriptions for proper disposal
  context.subscriptions.push(client);
}

export function deactivateLanguageClient(): Thenable<void> | undefined {
  if (!client) {
    return undefined;
  }
  return client.stop();
}
