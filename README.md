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

1. Save your GLB file(s) in your system's Downloads directory.
2. Run the conversion script:
   ```bash
   python convert_glb_to_stl.py
   ```
3. The script will automatically find the most recently modified GLB file in your Downloads directory and convert it.
4. The converted STL file will be saved in the `output` folder with the same base name as the input GLB file.

## Example

If you have several GLB files in your Downloads folder, the script will automatically select the most recently modified one. For instance, if your newest GLB file is named `model.glb`, running the script will produce `model.stl` in the `output` folder.
