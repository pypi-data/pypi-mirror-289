import argparse
import time

def to_uppercase(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            outfile.write(line.upper())

def main():
    parser = argparse.ArgumentParser(description="Convert the content of a file to uppercase.")
    parser.add_argument("input_file", help="The input file to be processed")
    parser.add_argument("output_file", help="The output file to save the processed content")
    args = parser.parse_args()

    start_time = time.time()
    to_uppercase(args.input_file, args.output_file)
    end_time = time.time()

    print(f"{args.input_file} processed in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
