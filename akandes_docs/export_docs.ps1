# PowerShell script to automate AkandeChips documentation export
# Exports to both HTML and PDF (if PDF engine is available)

$docs = @(
    'README.md',
    'introduction.md',
    'getting_started.md',
    'syntax.md',
    'functions.md',
    'advanced.md',
    'examples.md',
    'best_practices.md',
    'faq.md',
    'cheatsheet.md'
)

$docPaths = $docs | ForEach-Object { "akandes_docs/$_" } | Out-String

# Export to HTML
pandoc -s $docPaths -o akandechips_docs.html

# Export to PDF (if PDF engine is available)
try {
    pandoc -s $docPaths -o akandechips_docs.pdf
    Write-Host "PDF export successful."
} catch {
    Write-Host "PDF export failed. Ensure a TeX distribution (like MiKTeX) is installed."
}

Write-Host "HTML export complete."

.\akandes_docs\export_docs.ps1
