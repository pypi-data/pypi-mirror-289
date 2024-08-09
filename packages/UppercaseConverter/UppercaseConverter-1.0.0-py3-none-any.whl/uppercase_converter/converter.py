import sys

def convert_to_upper(input_file, output_file):
    with open(input_file, 'r') as infile:
        content = infile.read()

    with open(output_file, 'w') as outfile:
        outfile.write(content.upper())

def main():
    if len(sys.argv) != 3:
        print("Usage: convert-to-upper <input_file> <output_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_to_upper(input_file, output_file)

if __name__ == "__main__":
    main()
