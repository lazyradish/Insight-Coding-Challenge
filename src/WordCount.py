__author__ = 'Thomas Schreiter'

import argparse
import os
from WordCounter import WordCounter
import RunningMedian


def main(indir='wc_input',
         outdir='wc_output',
         word_count_report='wc_result.txt',
         running_median_report='med_result.txt',
         running_median_method='hashtracker'):

    # create output directory
    try:
        os.mkdir(outdir)
    except WindowsError:
        pass

    # initialize data structures
    wc = WordCounter(report_filename=os.path.join(outdir, word_count_report))
    rm = RunningMedian.factory(running_median_method, report_filename=os.path.join(outdir, running_median_report))

    for file in os.listdir(indir):
        if not file.endswith('.txt'):
            continue

        with open(os.path.join(indir, file), 'r') as f:
            for line in f:
                words = line.split()

                # count each word
                for w in words:
                    wc.update(w)

                # count number of words
                rm.update(len(words))
                rm.report()

    # report word count after everything is done
    wc.report()


def parse_args():
    # setup parser and its important options
    parser = argparse.ArgumentParser(description='Counts words and line lengths of textfiles.')
    parser.add_argument('-i', '--indir', action='store', default='wc_input',
                        help='directory of the input text files')
    parser.add_argument('-o', '--outdir', action='store', default='wc_output',
                        help='directory of the output report files')
    parser.add_argument('-w', '--word_count_report', action='store', default='wc_result.txt',
                        help='filename of word count report')
    parser.add_argument('-m', '--running_median_report', action='store', default='med_result.txt',
                        help='filename of word count report')
    parser.add_argument('--running_median_method', action='store', default='hashtracker',
                        help='filename of word count report')

    # actual parsing
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    main(**vars(args))