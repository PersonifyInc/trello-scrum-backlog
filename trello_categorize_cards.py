from msvcrt import getch

task_cats = ["mrd","post-mrd","defect","design"]

def GetCategoryFromUser(categories):
	choices = "("
	for i in range(1,len(categories)+1):
		choices = choices + " " + str(i) + " = " + categories[i-1] + ","
	choices = choices + ") ==> "
	print choices
	
	in_char = getch()
	if (in_char != '\r' and int(in_char) >= 0 and int(in_char) < len(categories)):
		return categories[int(in_char)]
		
	return ""

#untagged_cards = [c for c in cards if c.has_key('category') == False]

def CategorizeCards(cards):
	idx = 1
	for c in cards:
		print "---- " + str(idx) + " of " + str(len(cards)) + " ---------------------------------"
		print c['name'] + " " + c['url']
		c['category'] = GetCategoryFromUser(task_cats)
		idx = idx + 1
