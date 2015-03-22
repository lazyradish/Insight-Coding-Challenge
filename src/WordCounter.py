__author__ = 'Thomas Schreiter'

from collections import Counter


class WordCounter:
    def __init__(self, report_filename='wc_result'):
        self.report_filename = report_filename
        self.counts = Counter()

    @staticmethod
    def clean(word):
        return word.strip(';,.!?-:(){}[]"1234567890 ').lower()

    def update(self, word):
        cleaned = self.clean(word)
        self.counts[cleaned] += 1

    def report(self):
        with open(self.report_filename, 'w') as f:
            for word in sorted(self.counts):
                f.write('{}\t{}\n'.format(word, self.counts[word]))