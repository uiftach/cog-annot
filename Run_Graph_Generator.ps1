param(
    [string]$Section
)

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

$python = "python"
try {
    & $python --version | Out-Null
} catch {
    Write-Host "Python not found. Please install Python from https://www.python.org/downloads/" -ForegroundColor Red
    Write-Host "Then re-run this script." -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

$textFile = Join-Path $root "Aristoteles\HA\HA raw text to 491.14.txt"
if (!(Test-Path $textFile)) {
    Write-Host "Text file not found at: $textFile" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "Listing sections..." -ForegroundColor Cyan
& $python "generate_graph.py" "$textFile" --list

$section = $Section
if ([string]::IsNullOrWhiteSpace($section)) {
    $section = Read-Host "Enter section ID (e.g., 487b.15)"
}

if ([string]::IsNullOrWhiteSpace($section)) {
    Write-Host "No section entered. Exiting." -ForegroundColor Yellow
    exit 0
}

Write-Host "Generating graph for section $section..." -ForegroundColor Cyan
& $python "generate_graph.py" "$textFile" -s "$section"

$dotFile = Join-Path $root ("graphs\graph_{0}.dot" -f ($section -replace '\.', '_'))
if (Test-Path $dotFile) {
    Write-Host "DOT file created: $dotFile" -ForegroundColor Green
    $pngFile = Join-Path $root ("graphs\graph_{0}.png" -f ($section -replace '\.', '_'))
    $dotCmd = $null
    $dotCmdResolved = Get-Command dot -ErrorAction SilentlyContinue
    if ($dotCmdResolved) {
        $dotCmd = $dotCmdResolved.Source
    } elseif (Test-Path "C:\msys64\mingw64\bin\dot.exe") {
        $dotCmd = "C:\msys64\mingw64\bin\dot.exe"
    } elseif (Test-Path "C:\Program Files\Graphviz\bin\dot.exe") {
        $dotCmd = "C:\Program Files\Graphviz\bin\dot.exe"
    }

    if ($dotCmd) {
        $dotOutput = & $dotCmd -Tpng "$dotFile" -o "$pngFile" 2>&1 | Out-String
        if (Test-Path $pngFile) {
            Write-Host "PNG created: $pngFile" -ForegroundColor Green
        } else {
            Write-Host "PNG creation failed." -ForegroundColor Red
            if (-not [string]::IsNullOrWhiteSpace($dotOutput)) {
                Write-Host "GraphViz output:" -ForegroundColor Yellow
                Write-Host $dotOutput -ForegroundColor Yellow
            }
            Write-Host "Try manually:" -ForegroundColor Yellow
            Write-Host "dot -Tpng `"$dotFile`" -o `"$pngFile`"" -ForegroundColor Yellow
        }
    } else {
        Write-Host "GraphViz not found in PATH. To render a PNG, run:" -ForegroundColor Yellow
        Write-Host "dot -Tpng `"$dotFile`" -o `"$pngFile`"" -ForegroundColor Yellow
    }
} else {
    Write-Host "DOT file was not created. Check the section ID." -ForegroundColor Red
}

Read-Host "Press Enter to exit"
