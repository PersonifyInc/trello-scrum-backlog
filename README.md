Introduction
============

These utilities are used to create our scrum burndown chart (along with code churn from a git repository)

Installation and Dependencies
=============================

It's Python, so you basically need to satisfy the Python module dependencies. I didn't keep a complete list of what all I installed, but I run these under what can be considered [PyLab](http://www.scipy.org/PyLab).

You may also need to install some python modules:

* oauth2
* pandas

The git_code_churn.py script assumes cygwin is installed with git available at c:\cygwin\bin\git.exe

The git_code_churn.py script also has a hard-coded repository location, at present ;-).

Regarding the assumed Trello structure, we assume that cards are stories and that the board lists, from left-to-right, are:

* Back Burner
* Known Bugs
* New Features
* To Do
* Doing
* Test
* Done
* (Archived Dones)

Basic Analysis Flow
===================

I do this using IPython with the working directory set to the repository.

	%run trello_get_cards

	%run trello_categorize_cards
	CategorizeCards(cards)

	import datetime
	%run trello_analysis_utils
	[date_labels, completed_on, mrd_backlog, post_mrd_backlog, defect_backlog, design_backlog] = GenerateBacklog(cards, datetime.datetime(startdate), numdays)

	%run git_code_churn
	%runlog extract_git_code_churn

	%run plot_burndown
	PlotBurndown(date_labels, completed_on, churn_slice_list_ma, mrd_backlog, post_mrd_backlog, defect_backlog, design_backlog)

