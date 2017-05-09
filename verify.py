import argparse
from numpy import random

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', type=str, default='myspace',
                        help='path to input dictionary')
    parser.add_argument('-o', type=str, default='out.txt',
                        help='path to output dictionary')
    parser.add_argument('-l', type=int,
                        help='length of sample', default=10000)
    parser.add_argument('-r', type=int,
                        help='repeat time', default=10)
    # parser.add_argument('-list', action='store_true',
    #                     help='list the intersections')

    args = parser.parse_args()
    verify(args)


def verify(args):
    with open("data/" + args.i + "/input.txt", "r") as infile:
        input_data = infile.readlines()
    with open(args.o, "r") as outfile:
        output_data = outfile.readlines()

    average = 0
    for _ in range(args.r):
        count = 0
        arr_index = random.randint(1, len(input_data), size=[args.l])
        index = list(arr_index)
        for i in index:
            if input_data[i] in output_data:
                count = count + 1

        p = count / args.l * 100
        average = average + p

    print("Percentage: %.2f%%" % average / args.r)

    # intersection = list(set(input_data).intersection(set(output_data)))
    # print("Total intersections: %d" % len(intersection))
    #
    # if args.list:
    #     print(intersection)
    #
    # p = len(intersection) / len(set(output_data)) * 100
    # print("Percentage: %.2f%%" % p)
    # return intersection

if __name__ == '__main__':
    main()
