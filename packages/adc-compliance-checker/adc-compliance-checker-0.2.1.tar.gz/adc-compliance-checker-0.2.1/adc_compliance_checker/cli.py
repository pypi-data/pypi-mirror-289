import argparse
from .checker import check_compliance
import adc_compliance_checker


def main():
    parser = argparse.ArgumentParser(description='ADC Compliance Checker')
    parser.add_argument('input_file',
                        type=str,
                        help='Path to the input NetCDF file')
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'%(prog)s {adc_compliance_checker.__version__}')

    args = parser.parse_args()

    result = check_compliance(args.input_file)
    print(result)


if __name__ == '__main__':
    main()
