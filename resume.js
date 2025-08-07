// Resume logic for restoring last session and progress
const Store = require('electron-store');
const fs = require('fs');
const path = require('path');

const store = new Store();

// Restore last session and progress
const lastSession = store.get('lastSession');
const lastProgress = store.get('lastProgress');

if (lastSession) {
    console.log('Restoring last session:', lastSession);
    // Example: open last edited file or restore state
    // You can expand this logic to restore cursor, open editors, etc.
}
if (lastProgress) {
    console.log('Restoring last progress:', lastProgress);
    // Restore progress (e.g., file, cursor, build state)
} else if (!lastSession) {
    console.log('No previous session found. Starting fresh.');
}

// Helper to save session and progress
function saveSessionAndProgress(sessionData = {}, progressData = {}) {
    store.set('lastSession', {
        ...sessionData,
        timestamp: new Date().toISOString()
    });
    store.set('lastProgress', {
        ...progressData,
        timestamp: new Date().toISOString()
    });
}

// Save session and progress on exit (single handler)
process.on('exit', () => {
    // Example: Save last edited file, cursor, etc.
    saveSessionAndProgress(
        {
            lastFile: 'src/main.ak', // Replace with actual logic
            cursor: { line: 10, col: 5 }
        },
        {
            buildStep: 'compile',
            lastTest: 'test1'
        }
    );
});

// For VS Code extension: use the Memento API for workspace/global state
// Example (pseudo-code, not Node.js):
// const vscode = get_vscode_api('memento');
// context.workspaceState.update('lastSession', sessionData);
// context.workspaceState.update('lastProgress', progressData);