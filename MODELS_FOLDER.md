## Use this command to open the models folder
```bash
explorer %USERPROFILE%\.ollama\models
```

## To copy only the relevant blob files referenced in your model manifest from Ollama's .ollama\models\blobs folder to your target models\ folder, use the following PowerShell commands in Windows:
```bash
# Source blobs folder
$source = "C:\Users\Amaan M k\.ollama\models\blobs"

# Destination folder
$destination = "D:\0 AMAAN MAIN\0 Codes and Tools\My Python & ML\Ollama Model-Infer\models\"

# List of blob hashes used in the manifest (without sha256- prefix)
$blobs = @(
    "dde5aa3fc5ffc17176b5e8bdc82f587b24b2678c6c66101bf7da77af9f7ccdff",
    "966de95ca8a62200913e3f8bfbf84c8494536f1b94b49166851e76644e966396",
    "fcc5a6bec9daf9b561a68827b67ab6088e1dba9d1fa2a50d7bbcc8384e0a265d",
    "a70ff7e570d97baaf4e62ac6e6ad9975e04caa6d900d3742d37698494479e0cd",
    "56bb8bd477a519ffa694fc449c2413c6f0e1d3b1c88fa7e3c9d88d3ae49d4dcb"
)

# Copy files based on blob hashes from source to destination
foreach ($blob in $blobs) {
    $fileName = "sha256-$blob"
    $srcPath = Join-Path -Path $source -ChildPath $fileName
    $destPath = Join-Path -Path $destination -ChildPath $fileName
    if (Test-Path $srcPath) {
        Copy-Item -Path $srcPath -Destination $destPath -Force
        Write-Host "Copied $fileName to destination."
    } else {
        Write-Host "File not found: $fileName"
    }
}
```