from aspose.threed import Scene

# Load the GLB file
scene = Scene.from_file("/home/tom/Downloads/780de11f-2099-4110-9acd-2e24f8df1f6c.glb")

# Save as STL
scene.save("output.stl")
