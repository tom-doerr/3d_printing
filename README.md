# GLB to STL Converter

This project provides a Python script to convert GLB files to STL files using the Aspose.3D library.

## Prerequisites

- Python 3.x
- Aspose.3D library

## Installation

1. Install the Aspose.3D library using pip:
   ```bash
   pip install aspose-3d
   ```

## Usage

The script can be run in several ways:

1. Basic usage (converts newest GLB from Downloads):
   ```bash
   python convert_glb_to_stl.py
   ```

2. Convert a specific GLB file:
   ```bash
   python convert_glb_to_stl.py --input path/to/your/file.glb
   ```

3. Search for newest GLB in a different directory:
   ```bash
   python convert_glb_to_stl.py --input-dir /path/to/directory
   ```

4. Specify a custom output directory:
   ```bash
   python convert_glb_to_stl.py --output-dir /path/to/output
   ```

### Command Line Arguments

- `--input`, `-i`: Specify a specific GLB file to convert
- `--input-dir`: Directory to search for GLB files (default: ~/Downloads)
- `--output-dir`, `-o`: Output directory for STL files (default: output)

## Example

If you have several GLB files in your Downloads folder, running the script without arguments will automatically select the most recently modified one. For instance, if your newest GLB file is named `model.glb`, running the script will produce `model.stl` in the `output` folder.

You can also specify exact files:
```bash
python convert_glb_to_stl.py -i ~/Downloads/model.glb -o ~/3d_prints
```
