import sys
import os
import pytest

# Ensure the akandes_lsp package is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../akandes_lsp')))
import chips

def test_compiler_tools():
    tools = chips.list_compiler_tools()
    assert 'gcc' in tools
    assert 'armcc' in tools

def test_ide_tools():
    tools = chips.list_ide_tools()
    assert 'keil' in tools
    assert 'mplabx' in tools
    assert 'iar' in tools

def test_programming_tools():
    tools = chips.list_programming_tools()
    assert 'openocd' in tools
    assert 'stlink' in tools
    assert 'impact' in tools
    assert 'quartus_pgm' in tools
    assert 'mplab_ipe' in tools

def test_simulation_tools():
    tools = chips.list_simulation_tools()
    assert 'spectre' in tools
    assert 'ltspice' in tools
    assert 'hspice' in tools
    assert 'vivado_sim' in tools
    assert 'verilator' in tools
    assert 'ghdl' in tools
    assert 'icarus' in tools
    assert 'questa' in tools
    assert 'riviera' in tools
    assert 'cocotb' in tools
    assert 'xsim' in tools
    assert 'vcs' in tools
    assert 'tcad' in tools
    assert 'athena' in tools
    assert 'victory' in tools
    assert 'smartspice' in tools
    assert 'ise' in tools
    assert 'quartus' in tools
    assert 'tanner' in tools
    assert 'redhawk-sc' in tools
    assert 'ads' in tools
    assert 'genesys' in tools
    assert 'empro' in tools
    assert 'hfss' in tools
    assert 'siwave' in tools
    assert 'redhawk' in tools
    assert 'modelsim' in tools
    assert 'hyperlynx' in tools
    assert 'pads' in tools

def test_cli_list_tools_runs():
    # Just check that it runs without error
    chips.cli_list_tools()

def get_ai_completion(provider, prompt, api_key):
    if provider == "openai":
        # ...call OpenAI API...
        pass
    elif provider == "anthropic":
        # ...call Anthropic API...
        pass
    elif provider == "gemini":
        # ...call Gemini API...
        pass
    elif provider == "copilot":
        # ...call Copilot API...
        pass
    else:
        raise ValueError("Unknown provider")

if __name__ == "__main__":
    pytest.main()

{
  "contributes": {
    "configuration": {
      "properties": {
        "akandeAI.provider": {
          "type": "string",
          "description": "Select AI provider"
        },
        "akandeAI.enterpriseLicense": {
          "type": "string",
          "description": "Enter enterprise license key"
        }
      }
    }
  }
}

# server.py
def is_enterprise_license_valid(license_key):
    # Example: check license key format or call validation API
    return license_key.startswith("ENT-") and len(license_key) == 20

def enable_enterprise_features(license_key):
    if is_enterprise_license_valid(license_key):
        # Enable premium features
        return True
    return False
