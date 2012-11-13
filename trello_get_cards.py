import os
import sys
import datetime
import re

import trello

def ParseCard(card, markAsDone):
	card.fetch_actions('createCard')
	creator = card.actions[0]['memberCreator']['username']
	if markAsDone:
		card.fetch_actions('updateCard:idList')
		if len(card.actions) > 0:
			date_str = card.actions[0]['date'][:-5]
			end_date = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
		else:
			print "Unable to find end date for card " + card.id + " " + card.name + ", using creation date."
			end_date = card.create_date
	else:
		# TODO: figure out if this is a smart idea
		end_date = datetime.datetime.min
	
	cardStruct = {}
	cardStruct['id'] = card.id
	cardStruct['url'] = card.url
	cardStruct['creator'] = creator
	cardStruct['name'] = card.name
	cardStruct['start_date'] = card.create_date
	cardStruct['end_date'] = end_date
	cardStruct['done'] = markAsDone
		
	#print card.id + " " + card.url + " " + creator + " " + card.name + " " + card.create_date.strftime("%m-%d-%Y")
	return cardStruct

def ParseList(l, markAsDone):
	return map(lambda x: ParseCard(x, markAsDone), l)
	#for a in l:
	#	ParseCard(a, markAsDone)

if __name__ == '__main__':
	sys.path.append(os.getcwd() + "\py-trello")

	if len(sys.argv) >= 3:
		TRELLO_API_KEY = sys.argv[1]
		TRELLO_RO_TOKEN = sys.argv[2]
	else:
		print "Usage: trello_get_cards TRELLO_API_KEY TRELLO_RO_TOKEN"
		sys.exit(1)

	t = trello.TrelloClient(TRELLO_API_KEY, TRELLO_RO_TOKEN)
	client_board = t.list_boards()[1]

	todo_list = client_board.all_lists()[3].list_cards()
	doing_list = client_board.all_lists()[4].list_cards()
	test_list = client_board.all_lists()[5].list_cards()
	done0_list = client_board.all_lists()[6].list_cards()
	done1_list = client_board.all_lists()[7].list_cards()
	done2_list = client_board.all_lists()[8].list_cards()
	done3_list = client_board.all_lists()[9].list_cards()
	done4_list = client_board.all_lists()[10].list_cards()

	cards = ParseList(todo_list, False) +\
		ParseList(doing_list, False) +\
		ParseList(test_list, True) +\
		ParseList(done0_list, True) +\
		ParseList(done1_list, True) +\
		ParseList(done2_list, True) +\
		ParseList(done3_list, True) +\
		ParseList(done4_list, True)

