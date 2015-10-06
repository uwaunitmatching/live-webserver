import sys

searching_keywords = "petroleum engineers,supplementary assessment,balance techniques,flow line,advanced knowledge,administrative offices,hydrocarbon flow,develop understanding,multiphase flows,production system,production forecast,academic learning,gas reservoirs,production logging,early january,english language,gain skills,numeracy skills,balance analysis,flow performance,stimulation operations,skills,stimulation,analysis,performance,interpretation,reservoir,participate,availability,completion,description,remaining"


def search(text):
	for keyword in text.split(','):
		#splits the big keyword string into small keywords
		for k in keyword.split(' '):
			#split it down so each word is here
			print k


search(searching_keywords)
