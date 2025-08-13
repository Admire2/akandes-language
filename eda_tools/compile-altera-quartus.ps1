# Compile Intel/Altera Quartus VHDL libraries for GHDL
# Usage: Run this script in PowerShell as Administrator if needed
# Adjust $quartusLibPath to your Quartus installation

$quartusLibPath = "C:\intelFPGA_lite\20.1\quartus\libraries\vhdl"
$ghdlLibPath = "C:\GHDL\lib\altera"

if (!(Test-Path $ghdlLibPath)) {
    New-Item -ItemType Directory -Path $ghdlLibPath
}

$libs = @("altera_mf", "lpm", "sgate", "maxv")

foreach ($lib in $libs) {
    $src = Join-Path $quartusLibPath $lib
    if (Test-Path $src) {
        Write-Host "Compiling $lib..."
        ghdl -i --work=$lib --workdir=$ghdlLibPath $src\*.vhd
        ghdl -m --work=$lib --workdir=$ghdlLibPath $lib
    } else {
        Write-Host "$lib not found in Quartus library path."
    }
}
Write-Host "Altera Quartus VHDL libraries compilation complete."
