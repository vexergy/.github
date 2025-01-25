# Define paths
$venvPath = ".\.venv\Scripts\Activate.ps1"
$scriptPath = ".\vexergy_status.py"

# Activate virtual environment
& $venvPath

# Run the Python script
python $scriptPath
