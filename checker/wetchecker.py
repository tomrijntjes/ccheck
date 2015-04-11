"""
warme module
in: nieuwe 'bekende valkuil' 
proces: vergelijk met alle contracten in database
uit: waarschuwingsemail naar mkb'ers met lekke contracten en een aanbieding voor maatwerk.
"""

class WetChecker(ContractUtility):
	def __init__(self):
		self.contracten = None

	def valkuilCheck(self):
		#loop over contracten
		for contract in contracten:
			for valkuil in self.v:
				if valkuil in contract:
					super.sendMail(contract,valkuil)


class Contract:
	def __init__(self):
		self.relatie = "Fantasie BV"
		self.contract = "Overeenkomst Tijdelijke Arbeidsrelatie #102" 
		self.afzender = "Mike eks"

class Valkuil:
	def __init__(self):	
		self.wijziging = "Artikel 100 arbeidsrecht"
		self.specificatie = "artikel 7 moet aangescherpt worden om te voldoen aan nieuwe wetseisen."

