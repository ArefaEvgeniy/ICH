from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('-i', '--input', help='Path to input file')
parser.add_argument('-o', '--output', help='Path to output file')
args = parser.parse_args()

print(args.input)
print(args.output)
