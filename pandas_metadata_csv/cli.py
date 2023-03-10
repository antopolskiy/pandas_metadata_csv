"""Console script for pandas_metadata_csv."""
import argparse
import sys


def main():
    """Console script for pandas_metadata_csv."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "pandas_metadata_csv.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
