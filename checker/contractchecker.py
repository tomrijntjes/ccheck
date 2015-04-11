"""
lauwe module
in: upload van contract door mkb'er
proces: vergelijk met lijst bekende valkuilen
uit: email (na een korte periode) met risico's, indien aanwezig, plus de belofte om voortdurend het contract te vergelijken met wijzigingen in de wet
"""

from utility import ContractUtility
import nltk
from gmail import Gmail
import re

class ContractChecker(ContractUtility):
"""Dear reader, the intended architecture relies on machine learning to generate a probability a contract contains some flaw. Due to the lack of training data, a heuristic approach is used. Future implementations will include more sophisticated text mining techniques.
"""
	def __init__(self):
		self.gm = Gmail('Your Email', 'Password')

	def run(self, contract):
		message = generate_template(concurrentiebeding(contract),proeftijd(contract))
		gm.send_message(receiver,subject, message)

	def generate_template(self,cb,pt):
		if cb and pt:
			return template
		if cb:
			return template
		if pt:
			return template
		return template

	def concurrentiebeding(self,contract):
		fd = nltk.FreqDist(nltk.word_tokenize(contract))
		bepaaldeTijd = fd['bepaalde']>fd['onbepaalde']
		concurrentiebeding = fd['concurrentiebeding']>0 or fd['Concurrentiebeding']>0
		return bepaaldeTijd and concurrentiebeding

	def proeftijd(self,contract):
		proeftijd = re.match(pattern, contract, flags=re.IGNORECASE)

		if contractduur < 6:
			return proeftijd > 0
		if contractduur > 12:
			return proeftijd > 1
		if contractduur >= 24: 
			return proeftijd > 2
	
	
		

	



