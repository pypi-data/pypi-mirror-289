import argparse
import time

def convert(input_file, output_file):
    start_time = time.time()

    with open(input_file, 'rb') as f:
        data = f.read()

    upper_data = data.upper()

    with open(output_file, 'wb') as f:
        f.write(upper_data)

    end_time = time.time()
    et = end_time - start_time

    return output_file, et

def main():
    parser = argparse.ArgumentParser(description="Convert a file's content to uppercase.")
    parser.add_argument('input_file', type=str, help="Input file name")
    parser.add_argument('output_file', type=str, help="Output file name")

    args = parser.parse_args()

    output_file, elapsed_time = convert(args.input_file, args.output_file)
    print(f"Output File: {output_file}, Elapsed Time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
