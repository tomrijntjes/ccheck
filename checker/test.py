# -*- coding: utf-8 -*-

from contractchecker import ContractChecker

contract = open("voorbeeldcontracten/arbeidsovereenkomst voor bepaalde tijd").read()

c = ContractChecker()
print(c.concurrentiebeding(contract))
