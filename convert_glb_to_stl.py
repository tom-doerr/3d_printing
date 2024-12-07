import os
import glob
import argparse
from aspose.threed import Scene

def parse_args():
    parser = argparse.ArgumentParser(description='Convert GLB files to STL format')
    parser.add_argument('--input', '-i',
                      help='Specific GLB file to convert (optional)')
    parser.add_argument('--input-dir',
                      default=os.path.expanduser("~/Downloads"),
                      help='Directory to search for GLB files (default: ~/Downloads)')
    parser.add_argument('--output-dir', '-o',
                      default="output",
                      help='Output directory for STL files (default: output)')
    return parser.parse_args()

def main():
    args = parse_args()
    
    # Determine input file
    if args.input:
        input_file = args.input
        if not os.path.exists(input_file):
            raise Exception(f"Input file not found: {input_file}")
    else:
        # Find the most recent .glb file in input directory
        list_of_glb = glob.glob(os.path.join(args.input_dir, "*.glb"))
        if not list_of_glb:
            raise Exception(f"No .glb files found in directory: {args.input_dir}")
        input_file = max(list_of_glb, key=os.path.getmtime)

    # Create the output folder if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)

    # Load and convert the file
    scene = Scene.from_file(input_file)
    
    # Extract the base name of the input file
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(args.output_dir, f"{base_name}.stl")

    # Save as STL
    scene.save(output_file)
    print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    main()
