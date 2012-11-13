# Modified from script at https://gist.github.com/1202507
from dateutil import parser
import subprocess
import os
import re
import sys

import numpy as np

from pandas import *

repo_path = '/home/dscherba/StagePresence'
githist = ('c:\\cygwin\\bin\\git log --pretty=format:\"%h %ad | %s%d [%an]\" --date=short ' +
           repo_path + ' > githist.txt')

def rungithist():
    os.system(githist)

def get_commit_history():
    # return TimeSeries

    rungithist()

    githist = open('githist.txt').read()
    os.remove('githist.txt')

    sha_date = []
    for line in githist.split('\n'):
        sha_date.append(line.split()[:2])

    shas, dates = zip(*sha_date)

    dates = [parser.parse(d) for d in dates]

    return Series(dates, shas)

def get_commit_churn(sha, prev_sha):
	stdout = subprocess.Popen(['c:\\cygwin\\bin\\git', 'diff', sha, prev_sha, '--stat', 'NuvixaLive', 'Presenter_Shared', 'StagePresence'],
                              stdout=subprocess.PIPE).stdout

	git_diff_out = stdout.read()
	if git_diff_out != '':
		statline = git_diff_out.split('\n')[-2]

		match = re.match('.*\s(.*)\sinsertions.*\s(.*)\sdeletions', statline)

		insertions = int(match.group(1))
		deletions = int(match.group(2))
		if insertions > 10000 or deletions > 10000:
			print "evaluating churn between sha " + prev_sha + " and " + sha
			print statline
			print "insertions " + str(insertions) + " del " + str(deletions)
	else:
		insertions = 0
		deletions = 0
	
	return insertions, deletions


def get_code_churn(commits):
    shas = commits.index

    prev = shas[0]

    insertions = [np.nan]
    deletions = [np.nan]

    for cur in shas[1:]:
        i, d = get_commit_churn(cur, prev)
        insertions.append(i)
        deletions.append(d)

        prev = cur

    return DataFrame({'insertions' : insertions,
                      'deletions' : deletions}, index=shas)

if __name__ == '__main__':
    commits = get_commit_history()
    churn = get_code_churn(commits)

    by_date = churn.groupby(commits).sum()

    # clean out days where I touched Cython

    #by_date = by_date[by_date.sum(1) < 5000]
