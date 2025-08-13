import sys
import os
import pytest
from flask import Flask

# Ensure the akandes_lsp package is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../akandes_lsp')))
import chips

def test_webui_index():
    if not hasattr(chips, 'launch_agentic_web_gui'):
        pytest.skip("Web UI not available")
    app = Flask(__name__)
    client = app.test_client()
    # Simulate a GET request to the index page
    with app.app_context():
        # The actual launch_agentic_web_gui creates its own app, so we just check import and callable
        assert callable(chips.launch_agentic_web_gui)

def test_webui_invoke_tool_form():
    # This is a smoke test to ensure the HTML form is present in the template
    if not hasattr(chips, 'launch_agentic_web_gui'):
        pytest.skip("Web UI not available")
    # Check that the HTML string contains the tool form
    assert 'form method="post" action="/invoke_tool"' in chips.launch_agentic_web_gui.__code__.co_consts[1]
