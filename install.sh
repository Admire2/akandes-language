#!/bin/bash

echo "🔧 Installing Akandes Language VS Code Plugin..."

# Check for VS Code CLI availability
if ! command -v code &> /dev/null; then
    echo "❌ VS Code CLI ('code') not found."
    echo "➡️ Please install VS Code and enable the command-line interface."
    exit 1
fi

VSIX_FILE="./akandes-language.vsix"

if [ -f "$VSIX_FILE" ]; then
    code --install-extension "$VSIX_FILE"
    echo "✅ Akandes Language plugin installed successfully!"
else
    echo "⚠️ VSIX file not found."
    echo "➡️ Run 'vsce package' to generate it or download from GitHub Releases."
    exit 2
fi
