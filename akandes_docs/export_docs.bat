@echo off
REM Batch file to automate AkandeChips documentation export
REM Exports to both HTML and PDF (if PDF engine is available)

setlocal
set DOCS=README.md introduction.md getting_started.md syntax.md functions.md advanced.md examples.md best_practices.md faq.md cheatsheet.md
set DOCSPATH=
for %%f in (%DOCS%) do set DOCSPATH=!DOCSPATH! akandes_docs/%%f

REM Export to HTML
pandoc -s %DOCSPATH% -o akandechips_docs.html

REM Export to PDF (if PDF engine is available)
pandoc -s %DOCSPATH% -o akandechips_docs.pdf

if exist akandechips_docs.pdf (
    echo PDF export successful.
) else (
    echo PDF export failed. Ensure a TeX distribution (like MiKTeX) is installed.
)

echo HTML export complete.
endlocal
pause
