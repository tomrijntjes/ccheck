# -*- coding: utf-8 -*-

from contractchecker import ContractChecker
import sys
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='/temp/check.log',
                    filemode='w')

def main():
  naam,email,path,template = sys.argv[1:]
  with open(path) as f:
      contract = f.read()
      c = ContractChecker(naam,email,contract,template)
      c.run()

if __name__ == '__main__':
  try:
      main()
  except Exception as e:
    logger.exception(e)
    raise
