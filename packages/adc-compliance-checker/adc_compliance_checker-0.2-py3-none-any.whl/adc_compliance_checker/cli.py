import argparse
from .checker import check_compliance


def main():
    parser = argparse.ArgumentParser(description='ADC Compliance Checker')
    parser.add_argument('input_file', type=str, help='Path to the input file')

    args = parser.parse_args()

    result = check_compliance(args.input_file)
    print(result)


if __name__ == '__main__':
    main()
