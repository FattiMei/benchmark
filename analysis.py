import numpy as np
import sys


def parse_file(filename):
    with open(filename, 'r') as f:
        title = f.readline()
        data  = np.array([float(line) for line in f.readlines()])

    return (title, data)


def compute_statistics(data):
    return {
        'mean'    : np.mean(data),
        'median'  : np.median(data),
        'min'     : np.min(data),
    }


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No files were given to analyze... quitting')
        sys.exit(1)


    for bench_report_filename in sys.argv[1:]:
        title, data = parse_file(bench_report_filename)

        print(title)
        print(compute_statistics(data))
        print()
