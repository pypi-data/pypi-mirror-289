import sys
from my_topsis_package.topsis import topsis


# Import the topsis function from the topsis module

def main():
    if len(sys.argv) != 5:
        print("Usage: topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    result_file = sys.argv[4]

    topsis(input_file, weights, impacts, result_file)

if __name__ == "__main__":
    main()

