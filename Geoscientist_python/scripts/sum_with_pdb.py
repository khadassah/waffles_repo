import sys

def sum(a,h):
  return a+h

if __name__ == "__main__":
  # not some user given numbers
  a = sys.argv[1]
  b = sys.argv[2]
  print("a   = {0}".format(a))
  print("b   = {0}".format(b))
  print("sum = {0}".format(sum(a,b)))
