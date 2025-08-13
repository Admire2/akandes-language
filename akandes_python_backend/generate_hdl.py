
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/..'))

from chips import VHDLBackend, SystemVerilogBackend, test_vhdl_greet, test_vhdl_counter, test_vhdl_fsm, test_sv_complex, test_sv_mux, test_sv_register, test_vhdl_adder, test_sv_adder

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_hdl.py [vhdl|sv] <module> ...")
        sys.exit(1)
    backend_type = sys.argv[1].lower()
    backend = None
    if backend_type == "vhdl":
        backend = VHDLBackend()
    elif backend_type in ("sv", "systemverilog"):
        backend = SystemVerilogBackend()
    else:
        print("Unknown backend. Use 'vhdl' or 'sv'.")
        sys.exit(1)
    # Example: generate greet, counter, fsm, etc.
    if len(sys.argv) == 2 or sys.argv[2] == "all":
        print("Generating all example modules...")
        if backend_type == "vhdl":
            test_vhdl_greet()
            test_vhdl_counter()
            test_vhdl_fsm()
            test_vhdl_adder()
        else:
            test_sv_complex()
            test_sv_mux()
            test_sv_register()
            test_sv_adder()

    # List all files in the hdl_projects directory after generation
    hdl_dir = os.path.join(os.path.dirname(__file__), '..', 'hdl_projects')
    hdl_dir = os.path.abspath(hdl_dir)
    print(f"\nHDL output files in {hdl_dir}:")
    if os.path.isdir(hdl_dir):
        for fname in sorted(os.listdir(hdl_dir)):
            fpath = os.path.join(hdl_dir, fname)
            if os.path.isfile(fpath):
                print(f"  {fname}  ({os.path.getsize(fpath)} bytes)")
    else:
        print("  [No hdl_projects directory found]")

    # GHDL simulation automation: analyze all VHDL files
    print("\nGHDL analysis results:")
    ghdl_found = False
    try:
        import shutil
        ghdl_path = shutil.which("ghdl")
        if ghdl_path:
            ghdl_found = True
    except Exception:
        pass
    if not ghdl_found:
        print("  [GHDL not found in PATH. Skipping VHDL analysis.]")
    else:
        for fname in sorted(os.listdir(hdl_dir)):
            if fname.lower().endswith(".vhd"):
                fpath = os.path.join(hdl_dir, fname)
                print(f"  Analyzing {fname} ...", end=" ")
                rc = os.system(f'ghdl -a "{fpath}"')
                if rc == 0:
                    print("OK")
                else:
                    print("ERROR")

if __name__ == "__main__":
    main()
