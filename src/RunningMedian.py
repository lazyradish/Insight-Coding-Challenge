__author__ = 'Thomas Schreiter'

import numpy
from heapq import heappush, heappop


def factory(typestr, **kwargs):
    if typestr == 'simple':
        return RunningMedianSimple(**kwargs)
    elif typestr == 'hashtracker':
        return RunningMedianHashTracker(**kwargs)
    else:
        raise Exception


class RunningMedian(object):
    def __init__(self, report_filename='wc_result.txt'):
        self.report_filename = report_filename
        open(self.report_filename, 'w').close()
        self.data = []

    def report(self):
        with open(self.report_filename, 'a') as f:
            f.write('{}\n'.format(float(self.median())))

    def median(self):
        pass

    def update(self, elem):
        pass


class RunningMedianSimple(RunningMedian):
    def __init__(self, **kwargs):
        super(RunningMedianSimple, self).__init__(**kwargs)
        self.data = []

    def update(self, elem):
        self.data.append(elem)

    def median(self):
        return numpy.median(self.data)


class RunningMedianHashTracker(RunningMedian):
    def __init__(self, **kwargs):
        super(RunningMedianHashTracker, self).__init__(**kwargs)
        self._counts = dict()
        self._lower_heap = []
        self._current = None
        self._upper_heap = []
        self._nlower = 0
        self._ncurrent = 0
        self._nupper = 0

    def update(self, elem):
        # edge case for first entry
        if not self._counts:
            self._counts[elem] = 1
            self._current = elem
            self._ncurrent = 1
            return

        # normal behavior
        is_new_elem = self._update_counts(elem)
        self._update_tracker(elem, is_new_elem)

    def _update_counts(self, elem):
        '''
        update the counts dictionary and return whether the inserted element is new
        :param elem:
        :return:
        '''
        try:
            self._counts[elem] += 1
            return False
        except KeyError:
            self._counts[elem] = 1
            return True

    def _update_tracker(self, elem, is_new_elem):
        if is_new_elem:
            if elem > self.median():
                heappush(self._upper_heap, elem)
            else:
                heappush(self._lower_heap, -elem)

        if elem == self._current:
            self._ncurrent += 1
        elif self._upper_heap and elem >= self._upper_heap[0]:
            self._nupper += 1
        else:
            self._nlower += 1

        self._update_current()

    def _update_current(self):
        if self._current is not None:
            if self._nlower + self._ncurrent == self._nupper:
                heappush(self._lower_heap, -self._current)
                self._current = None
                self._nlower += self._ncurrent
                self._ncurrent = 0
                return

            if self._nlower == self._ncurrent + self._nupper:
                heappush(self._upper_heap, self._current)
                self._current = None
                self._nupper += self._ncurrent
                self._ncurrent = 0
                return

        else:
            if self._nlower < self._nupper:
                self._current = heappop(self._upper_heap)
                self._ncurrent = self._counts[self._current]
                self._nupper -= self._ncurrent
                return

            else:
                self._current = -heappop(self._lower_heap)
                self._ncurrent = self._counts[self._current]
                self._nlower -= self._ncurrent

    def median(self):
        if self._current is not None:
            return self._current
        else:
            try:
                return numpy.mean([-self._lower_heap[0], self._upper_heap[0]])
            except IndexError:
                return None
