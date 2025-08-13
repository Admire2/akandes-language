# Compile Lattice Diamond VHDL libraries for GHDL
# Usage: Run this script in PowerShell as Administrator if needed
# Adjust $diamondLibPath to your Diamond installation

$diamondLibPath = "C:\lscc\diamond\3.12\ispfpga\vhdl"
$ghdlLibPath = "C:\GHDL\lib\lattice"

if (!(Test-Path $ghdlLibPath)) {
    New-Item -ItemType Directory -Path $ghdlLibPath
}

$libs = @("pmi", "pmi_work")

foreach ($lib in $libs) {
    $src = Join-Path $diamondLibPath $lib
    if (Test-Path $src) {
        Write-Host "Compiling $lib..."
        ghdl -i --work=$lib --workdir=$ghdlLibPath $src\*.vhd
        ghdl -m --work=$lib --workdir=$ghdlLibPath $lib
    } else {
        Write-Host "$lib not found in Diamond library path."
    }
}
Write-Host "Lattice Diamond VHDL libraries compilation complete."
