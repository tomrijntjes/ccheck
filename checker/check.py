#argparse: naam email contract template
# -*- coding: utf-8 -*-

from contractchecker import ContractChecker
import sys

def main():
  naam,email,path,template = sys.argv[1:]
  with open(path) as f:
      contract = f.read()
      c = ContractChecker(naam,email,contract,template)
      c.run()

if __name__ == '__main__':
  main()
