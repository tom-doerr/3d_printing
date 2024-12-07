import os
import glob
from aspose.threed import Scene

# Find the most recent .glb file in Downloads
downloads_path = os.path.expanduser("~/Downloads")
list_of_glb = glob.glob(os.path.join(downloads_path, "*.glb"))
if not list_of_glb:
    raise Exception("No .glb files found in Downloads directory")
    
input_file = max(list_of_glb, key=os.path.getmtime)
scene = Scene.from_file(input_file)

# Create the output folder if it doesn't exist
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

# Extract the base name of the input file
base_name = os.path.splitext(os.path.basename(input_file))[0]
output_file = os.path.join(output_folder, f"{base_name}.stl")

# Save as STL
scene.save(output_file)
