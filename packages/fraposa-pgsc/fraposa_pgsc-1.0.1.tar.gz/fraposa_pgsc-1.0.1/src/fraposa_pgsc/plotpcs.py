import argparse
import fraposa_pgsc.fraposa as fp


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ref_filepref', help='Prefix of binary PLINK file for the reference data.')
    parser.add_argument('stu_filepref', help='Prefix of binary PLINK file for the study data.')
    args = parser.parse_args()

    fp.plot_pcs(args.ref_filepref, args.stu_filepref)


if __name__ == '__main__':
    main()