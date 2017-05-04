import argparse


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-i', type=str, default='myspace', help='path to input dictionary')
    parser.add_argument('-o', type=str, default='out.txt',
                        help='path to output dictionary')
    parser.add_argument('-l', action='store_true',
                        help='list the intersections')

    args = parser.parse_args()
    verify(args)


def verify(args):
    with open("data/" + args.i + "/input.txt", "r") as infile:
        input_data = infile.readlines()
    with open(args.o, "r") as outfile:
        output_data = outfile.readlines()
    intersection = list(set(input_data).intersection(set(output_data)))
    print("Total intersections: %d" % len(intersection))

    if args.l:
        print(intersection)

    p = len(intersection) / len(set(output_data)) * 100
    print("Percentage: %.2f%%" % p)
    return intersection

if __name__ == '__main__':
    main()
