import numpy as np
import sys


def parse_chunk(chunk):
    lines = chunk.split('\n')

    title = lines[0]
    data  = [float(entry) for entry in lines[1:] if entry]

    return {
        'title' : title,
        'mean'  : np.mean(data),
        'median': np.median(data),
        'min'   : np.min(data)
    }


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No files were given to analyze... quitting')
        sys.exit(1)

    for filename in sys.argv[1:]:
        with open(filename, 'r') as f:
            tests = [parse_chunk(x) for x in f.read().split('# ') if x]

            print(f"Test filename: {filename}")
            print(tests)
