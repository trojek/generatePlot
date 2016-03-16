"""
Prepare plots from data (file)
"""

import matplotlib.pyplot as plt
import sys


def draw_plot(data, mean, median, title):
    """Draw plot and save in on disk"""
    plt.plot(data)
    plt.title('%s, mean %1.3f, median %1.3f' % (title, mean, median))
    plt.ylabel('aspect ratio: circularity')
    plt.xlabel('sample number')
    plt.ylim([0, 1])
    plt.savefig('plots/%s.png' % title)

def count_mean(data):
    """Count mean value from data from file"""
    data_copy = list(data)
    data_copy.sort()
    return sum(data_copy)/len(data_copy)

def count_median(data):
    """Count median value from data from file"""
    data_copy = list(data)
    data_copy.sort()
    return data_copy[(len(data_copy) / 2) + 1]


def parse_data(file_name):
    """Open file and prepare data further calculations"""
    with open("%s/%s.txt" % (file_name, file_name)) as dfile:
        data = dfile.read()

    data = data.split(';')
    del data[-1]

    parsed_data = [float(i) for i in data]
    cleared_data = a = [i for i in parsed_data if i >= 0.5]

    return cleared_data

def main():
    """Generates plot from text file"""
    data = parse_data(sys.argv[1])
    mean = count_mean(data)
    median = count_median(data)
    draw_plot(data, mean, median, sys.argv[1])

if __name__ == '__main__':
    main()
