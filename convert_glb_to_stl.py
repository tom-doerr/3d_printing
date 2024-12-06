from aspose.threed import Scene

# Load the GLB file
scene = Scene.from_file("input.glb")

# Save as STL
scene.save("output.stl")
