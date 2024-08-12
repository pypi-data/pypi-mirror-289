import argparse
from file_converter import topsis


def main():
    if len(sys.argv) != 5:
        print("Error: Incorrect number of parameters.")
        print("Usage: python topsis.py <inputFileName> <Weights> <Impacts> <resultFileName>")
    else:
        inputFileName = sys.argv[1]
        weights = sys.argv[2]
        impacts = sys.argv[3]
        resultFileName = sys.argv[4]
        topsis(inputFileName, weights, impacts, resultFileName)


if __name__ == "__main__":
    main()
