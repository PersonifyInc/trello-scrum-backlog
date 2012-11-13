# Utility functions to assist with Trello analysis
import datetime

# Whether a card, c, is being worked on day d
def IsCardActive(c, d):
	return c['start_date'] <= d and (c['end_date'] >= d or c['end_date'] == datetime.datetime.min)

# Whether a card, c, is completed on day d
def IsCardCompletedOn(c,d):
	return datetime.datetime(c['end_date'].year, c['end_date'].month, c['end_date'].day) == d
	
def GenerateBacklog(cards, start_date, num_days):
	date_labels = []
	completed_on = []
	mrd_backlog = []
	post_mrd_backlog = []
	defect_backlog = []
	design_backlog = []

	# And now data
	for i in range(num_days):
		test_date = start_date + datetime.timedelta(i)
		cards_completed = [c for c in cards if IsCardCompletedOn(c, test_date)]
		cards_on_date = [c for c in cards if IsCardActive(c, test_date)]
		mrd_on_date = [c for c in cards_on_date if c['category'] == "mrd"]
		postmrd_on_date = [c for c in cards_on_date if c['category'] == "post-mrd"]
		defect_on_date = [c for c in cards_on_date if c['category'] == "defect"]
		design_on_date = [c for c in cards_on_date if c['category'] == "design"]
		
		date_labels.append(test_date.strftime("%Y-%m-%d"))
		completed_on.append(len(cards_completed))
		mrd_backlog.append(len(mrd_on_date))
		post_mrd_backlog.append(len(postmrd_on_date))
		defect_backlog.append(len(defect_on_date))
		design_backlog.append(len(design_on_date))
		
	return [date_labels, completed_on, mrd_backlog, post_mrd_backlog, defect_backlog, design_backlog]
	
def PrintBacklog(cards, start_date, num_days):
	# Print headers
	print "Date\tmrd\tpost-mrd\tdefect\tdesign"
	# And now data
	for i in range(num_days):
		test_date = start_date + datetime.timedelta(i)
		cards_on_date = [c for c in cards if IsCardActive(c, test_date)]
		mrd_on_date = [c for c in cards_on_date if c['category'] == "mrd"]
		postmrd_on_date = [c for c in cards_on_date if c['category'] == "post-mrd"]
		defect_on_date = [c for c in cards_on_date if c['category'] == "defect"]
		design_on_date = [c for c in cards_on_date if c['category'] == "design"]
		print test_date.strftime("%Y-%m-%d") + "\t" + str(len(mrd_on_date)) + "\t" + str(len(postmrd_on_date)) + "\t" + str(len(defect_on_date)) + "\t" + str(len(design_on_date))
		
def PrintBacklogOn(cards, date):
	# Get cards
	test_date = date
	cards_on_date = [c for c in cards if IsCardActive(c, test_date)]
	mrd_on_date = [c for c in cards_on_date if c['category'] == "mrd"]
	postmrd_on_date = [c for c in cards_on_date if c['category'] == "post-mrd"]
	defect_on_date = [c for c in cards_on_date if c['category'] == "defect"]
	design_on_date = [c for c in cards_on_date if c['category'] == "design"]
	
	# Print out backlog
	print "Backlog on " + date.strftime("%Y-%m-%d")
	
	print "=== MRD ==="
	for c in mrd_on_date:
		print "\t" + c['name']
		print "\t\t(" + c['url'] + ")"
	print "\n"

	print "=== Post-MRD ==="
	for c in postmrd_on_date:
		print "\t" + c['name']
		print "\t\t(" + c['url'] + ")"
	print "\n"

	print "=== Defect ==="
	for c in defect_on_date:
		print "\t" + c['name']
		print "\t\t(" + c['url'] + ")"
	print "\n"

	print "=== Design ==="
	for c in design_on_date:
		print "\t" + c['name']
		print "\t\t(" + c['url'] + ")"
	print "\n"

def PrintCompletedCardsOn(cards, date):
	# Get cards
	test_date = date
	cards_on_date = [c for c in cards if IsCardCompletedOn(c, test_date)]
	mrd_on_date = [c for c in cards_on_date if c['category'] == "mrd"]
	postmrd_on_date = [c for c in cards_on_date if c['category'] == "post-mrd"]
	defect_on_date = [c for c in cards_on_date if c['category'] == "defect"]
	design_on_date = [c for c in cards_on_date if c['category'] == "design"]
	
	# Print out backlog
	print "Completed cards on " + date.strftime("%Y-%m-%d")
	
	print "=== MRD ==="
	for c in mrd_on_date:
		print "\t" + c['name']
		print "\t\t(" + c['url'] + ")"
	print "\n"

	print "=== Post-MRD ==="
	for c in postmrd_on_date:
		print "\t" + c['name']
		print "\t\t(" + c['url'] + ")"
	print "\n"

	print "=== Defect ==="
	for c in defect_on_date:
		print "\t" + c['name']
		print "\t\t(" + c['url'] + ")"
	print "\n"

	print "=== Design ==="
	for c in design_on_date:
		print "\t" + c['name']
		print "\t\t(" + c['url'] + ")"
	print "\n"
