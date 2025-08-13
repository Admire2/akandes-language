# Compile Xilinx Vivado VHDL libraries for GHDL
# Usage: Run this script in PowerShell as Administrator if needed
# Adjust $vivadoLibPath to your Vivado installation

$vivadoLibPath = "C:\Xilinx\Vivado\2020.2\data\vhdl\src"
$ghdlLibPath = "C:\GHDL\lib\xilinx"

if (!(Test-Path $ghdlLibPath)) {
    New-Item -ItemType Directory -Path $ghdlLibPath
}

$libs = @("unisim", "unisims_ver", "unimacro", "unimacro_ver", "secureip")

foreach ($lib in $libs) {
    $src = Join-Path $vivadoLibPath $lib
    if (Test-Path $src) {
        Write-Host "Compiling $lib..."
        ghdl -i --work=$lib --workdir=$ghdlLibPath $src\*.vhd
        ghdl -m --work=$lib --workdir=$ghdlLibPath $lib
    } else {
        Write-Host "$lib not found in Vivado library path."
    }
}
Write-Host "Xilinx Vivado VHDL libraries compilation complete."
