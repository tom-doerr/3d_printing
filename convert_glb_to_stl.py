import os
from aspose.threed import Scene

# Load the GLB file
input_file = "/home/tom/Downloads/780de11f-2099-4110-9acd-2e24f8df1f6c.glb"
scene = Scene.from_file(input_file)

# Create the output folder if it doesn't exist
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

# Extract the base name of the input file
base_name = os.path.splitext(os.path.basename(input_file))[0]
output_file = os.path.join(output_folder, f"{base_name}.stl")

# Save as STL
scene.save(output_file)
