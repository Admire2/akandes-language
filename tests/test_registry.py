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

if __name__ == "__main__":
    pytest.main()
