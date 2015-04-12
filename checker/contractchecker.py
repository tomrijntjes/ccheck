#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
from gmail import Gmail
import re

class ContractChecker:
	"""Dear reader, the intended architecture relies on machine learning to generate a probability a contract contains some flaw. Due to the lack of training data, a heuristic approach is used. Future implementations will include more sophisticated text mining techniques.
	"""
	def __init__(self, name_customer, name_lawyer, email,contract,template_success,template_warning):
		self.numbers = {'een':1,'Een':1,'één':1,'Eén':1,'twee':2,'Twee':2,'Drie':3,'drie':3,None:0,1:1}
		self.gm = Gmail('ccheckmasters@gmail.com', 'hackathonmasters')
		self.name_customer = name_customer
		self.name_lawyer = name_lawyer
		self.email = email
		self.contract = contract
		self.subject = 'Betreffende uw contract'
		with open(template_success) as f:
			self.template_success = f.read()
		with open(template_warning) as f:
			self.template_warning = f.read()


	def run(self):
		message = self.generate_template(self.name_customer, self.concurrentiebeding(self.contract), self.proeftijd(self.contract))
		self.gm.send_message(self.email, self.subject, message)

	def generate_template(self,name_customer,cb,pt):
		if cb and pt:
			template = self.template_warning
			template = re.sub("__KLANT__",self.name_customer,template)
			template = re.sub("__VERANDERING WET__","de wijziging van Wet Werk en Zekerheid per januari dit jaar", template)
			template = re.sub("__NAAM CONTRACT__","Arbeidsovereenkomst #1001",template)
			template = re.sub("__AANDACHTSPUNT__","de proeftijd is mogelijk te lang. Daarnaast heeft het concurrentiebeding uitgebreidere uitleg nodig",template)
			return re.sub("__UW NAAM__",self.name_lawyer,template)
		if cb:
			template = self.template_warning
			template = re.sub("__KLANT__",self.name_customer,template)
			template = re.sub("__VERANDERING WET__","de wijziging van Wet Werk en Zekerheid per januari dit jaar", template)
			template = re.sub("__NAAM CONTRACT__","Arbeidsovereenkomst #1034",template)
			template = re.sub("__AANDACHTSPUNT__","het concurrentiebeding heeft uitgebreidere uitleg nodig",template)
			return re.sub("__UW NAAM__",self.name_lawyer,template)
		if pt:
			template = self.template_warning
			template = re.sub("__KLANT__",self.name_customer,template)
			template = re.sub("__VERANDERING WET__","de wijziging van Wet Werk en Zekerheid per januari dit jaar", template)
			template = re.sub("__NAAM CONTRACT__","Arbeidsovereenkomst #1029",template)
			template = re.sub("__AANDACHTSPUNT__","de vastgelegde proeftijd is mogelijk te lang",template)
			return re.sub("__UW NAAM__",self.name_lawyer,template)
		template = self.template_success
		template = re.sub("__KLANT__",self.name_customer,template)
		template = re.sub("__NAAM CONTRACT__","Arbeidsovereenkomst #2098",template)
		return re.sub("__UW NAAM__",self.name_lawyer,template)

	def concurrentiebeding(self,contract):
		fd = nltk.FreqDist(nltk.word_tokenize(contract))
		bepaaldeTijd = fd['bepaalde']>fd['onbepaalde']
		concurrentiebeding = fd['concurrentiebeding']>0 or fd['Concurrentiebeding']>0
		return bepaaldeTijd and concurrentiebeding

	def proeftijd(self,contract):
		if "proeftijd" not in contract:
			return False
		contractduur = re.match("duur van (\w+) maanden", contract, flags=re.IGNORECASE)
		if "eerste maand van de arbeidsovereenkomst geldt als proeftijd" in contract:
			proeftijd = 1
		if not proeftijd:
			proeftijd = re.match("proeftijd van (\w+) maand", contract, flags=re.IGNORECASE)
		if not proeftijd:
			proeftijd = re.match("\w+\smaand", contract, flags=re.IGNORECASE)
		proeftijd = self.numbers[proeftijd]
		contractduur = self.numbers[contractduur]
		print("Proeftijd: {0} Contractduur: {1}".format(proeftijd,contractduur))
		if contractduur < 6:
			return proeftijd > 0
		if contractduur > 12:
			return proeftijd > 1
		if contractduur >= 24:
			return proeftijd > 2
		return False
