# -*- coding: utf-8 -*-

from contractchecker import ContractChecker
import sys
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='/home/jens/check.log',
                    filemode='w')

def main():
  logging.info(sys.argv[1:])
  naam_klant, naam_advocaat, email, contract, template_success, template_warning = sys.argv[1:]
  with open(contract) as f:
      contract = f.read()
      c = ContractChecker(naam_klant, naam_advocaat ,email, contract, template_success, template_warning)
      c.run()

if __name__ == '__main__':
  try:
      main()
  except Exception as e:
    logging.exception(e)
    raise
