import sys
import logging
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s :: %(levelname)s :: %(message)s')

def sum(a,b):
  logging.debug("started method sum()")
  logging.info("Got a = {0} of type {1}".format(a,type(a)))
  logging.info("Got b = {0} of type {1}".format(b,type(b)))
  return a+b

if __name__ == "__main__":
  a,b = sys.argv[1], sys.argv[2]
  print("{a}+{b}= {sum}".format(sum=sum(a,b),a=a,b=b))
