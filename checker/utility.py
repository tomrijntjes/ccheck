"""
basisklasse voor gedeelde functionaliteit: dbconnectie, uitgaande email, parser jurispudentie, parser contract
"""

class ContractUtility():
	def __init__(self):
		pass

	def connect():
		pass
	
	def sendMail(self,contract,valkuil):
		if valkuil:
			print("""Beste {0}, u heeft in het verleden een contract geupload bij onze contractencheck-service dat nu uw aandacht kan gebruiken. Vanwege veranderingen in {1} is er ruimte voor een update in contract {2}: {3} Als we daarbij van dienst kunnen zijn, hoor ik het graag. 

Met vriendelijke groet,

{4}""".format(valkuil.relatie,valkuil.artikel,contract.naam,contract.specificatie,contract.kantoor))

			

	def parseContract():
		pass
		
	def parse():
		pass
