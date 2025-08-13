# Compile Microsemi Libero VHDL libraries for GHDL
# Usage: Run this script in PowerShell as Administrator if needed
# Adjust $liberoLibPath to your Libero installation

$liberoLibPath = "C:\Microsemi\Libero_SoC_v12.6\Designer\lib\vhdl"
$ghdlLibPath = "C:\GHDL\lib\microsemi"

if (!(Test-Path $ghdlLibPath)) {
    New-Item -ItemType Directory -Path $ghdlLibPath
}

$libs = @("smartfusion2", "proasic3")

foreach ($lib in $libs) {
    $src = Join-Path $liberoLibPath $lib
    if (Test-Path $src) {
        Write-Host "Compiling $lib..."
        ghdl -i --work=$lib --workdir=$ghdlLibPath $src\*.vhd
        ghdl -m --work=$lib --workdir=$ghdlLibPath $lib
    } else {
        Write-Host "$lib not found in Libero library path."
    }
}
Write-Host "Microsemi Libero VHDL libraries compilation complete."
