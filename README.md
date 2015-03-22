# Insight-Coding-Challenge
Count number of occurances of each word in text files and calculate median of number of words per line.

How-To
------
Put input text files into `wc_input`. Call `run.sh` to execute the word counter and the running median. Results are written to `wc_output`.

Implementation
--------------

Word counter uses a simple dictionary to count occurances.

Running median uses a dictionary to cound the number of words/line. To calculate the median quickly, 2 heaps incl. counters are used to keep track of the middle location. For details, see `doc/`.
