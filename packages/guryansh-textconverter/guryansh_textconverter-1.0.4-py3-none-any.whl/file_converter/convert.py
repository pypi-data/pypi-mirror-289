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
