__author__ = 'Thomas Schreiter'

import unittest
import os
import filecmp
import WordCount


class TestWordCount(unittest.TestCase):

    exp_wc_filename = 'wc_result.txt'
    exp_rm_filename = 'med_result.txt'
    test_dir = os.path.dirname(os.path.realpath(__file__))

    def assertFilesEqual(self, expected, actual):
        self.assertTrue(os.path.exists(expected))
        self.assertTrue(os.path.exists(actual))
        self.assertTrue(filecmp.cmp(expected, actual))

    def _test_word_count(self, projname, running_median_method):

        # call
        WordCount.main(indir=self._indir(projname),
                       outdir=self._outdir(projname),
                       running_median_method=running_median_method)

        # assert
        self.assertFilesEqual(os.path.join(self._expdir(projname), self.exp_wc_filename),
                              os.path.join(self._outdir(projname), self.exp_wc_filename))
        self.assertFilesEqual(os.path.join(self._expdir(projname), self.exp_rm_filename),
                              os.path.join(self._outdir(projname), self.exp_rm_filename))

    def _indir(self, projname):
        return os.path.join(self.test_dir, '{}_input'.format(projname))

    def _outdir(self, projname):
        return os.path.join(self.test_dir, 'actual_{}_output'.format(projname))

    def _expdir(self, projname):
        return os.path.join(self.test_dir, 'expected_{}_output'.format(projname))

    def test_example_simple(self):
        self._test_word_count('example', 'simple')

    def test_example_hashtracker(self):
        self._test_word_count('example', 'hashtracker')

    def test_multiple_hashtracker(self):
        self._test_word_count('multiple', 'hashtracker')

    def test_missing_input_directory(self):
        with self.assertRaises(WindowsError):
            WordCount.main(indir='does_not_exist')
