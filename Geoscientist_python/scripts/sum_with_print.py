import sys

def sum(a,h):
  return a+h

if __name__ == "__main__":
  # first some tests
  print("2 = {0}".format(sum(1,1)))
  print("5 = {0}".format( sum(1,4)))
  print("4 = {0}".format(sum(2,2)))

  # not some user given numbers
  a = sys.argv[1]
  b = sys.argv[2]
  print("a   = {0}".format(a))
  print("b   = {0}".format(b))
  print("sum = {0}".format(sum(a,b)))
