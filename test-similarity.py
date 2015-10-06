import sys
from django.db import models


searching_keywords = "petroleum engineers,supplementary assessment,balance techniques,flow line,advanced knowledge,administrative offices,hydrocarbon flow,develop understanding,multiphase flows,production system,production forecast,academic learning,gas reservoirs,production logging,early january,english language,gain skills,numeracy skills,balance analysis,flow performance,stimulation operations,skills,stimulation,analysis,performance,interpretation,reservoir,participate,availability,completion,description,remaining"
database_keywords = "academic learning,internationalisation theories,numeracy skills,marketing concerns,early january,administrative offices,distribution decisions,political influences,global environment,make sense,export procedures,make product,english language,marketing environments,major methods,cultural issues,cultural,paperback,register,texts,consult,communication,asterisk,cross,services,petroleum engineers,supplementary assessment"

def search(keywords, database_keywords):
	num_keywords = 0
	count = 0

	for keyword in keywords.split(','):
		#splits the big keyword string into small keywords
		for k in keyword.split(' '):
			num_keywords += 1
			#split it down so each word is here
			print(k)
			if k in database_keywords:
				count += 1


	print('Number of keywords %s' % num_keywords)
	print('count: %s' % count)

	
	similarity = (0.500 + ( (count*1.0) / (num_keywords * 1.0) * 0.50 )) * 100.0

	print('similarity = %.2f' % similarity)



search(searching_keywords, database_keywords)
