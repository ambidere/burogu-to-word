import argparse

parser = argparse.ArgumentParser(description='Archives blogs to word documents')
# TODO for loops converters (when already refactored) and then gets their static names and add them as arguments

parser.add_argument('-s')
parser.add_argument('-m', '--mode', dest='mode', default='page')
print parser.parse_args()