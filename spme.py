
import os
def split_file(input_file, output_dir, chunk_size=20 * 1024 * 1024):
    base_name = os.path.basename(input_file)
    with open(input_file, 'rb') as f:
        chunk_num = 0
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            output_file = f"{output_dir}/{base_name}.{chunk_num}.split"
            with open(output_file, 'wb') as output:
                output.write(chunk)
            chunk_num += 1

    return chunk_num

def merge_file(input_file, num):
    file_list = [input_file + "." + str(i) + ".split" for i in range(num)]
    with open(input_file + ".merged", 'wb') as f:
        for file in file_list:
            with open(file, 'rb') as input:
                f.write(input.read())

# split_file("./checkpoints/checkpoints.zip", "./checkpoints/")
# merge_file("./checkpoints/checkpoints.zip", 199)
# split_file("./demo/demo.zip", "./demo/")
merge_file("./demo/demo.zip", 33)
