import functools
import math
def start():

  [print(x, end=" ") for x in range(2000,3201) if x % 7 == 0 and x % 5 != 0]

  nb=int(input("Give me a number: "))
  print(functools.reduce(lambda a,b: a*b, range(2,nb+1)))

  nb=int(input("Give me a number: "))
  r = {i:i*i for i in range(1,nb+1)}
  print(r)
  
  def f(d):
    return math.sqrt((2*50*d)/30)

  [print(round(f(int(d)))) for d in input("Type your list: ").split(",")]


