import math

def g1(x) :
   """
   g(x) = (1/2 + tan(pi*x/2)**2 
   """
   return ( 0.5 + math.tan( math.pi * x * 0.5) )**2



def g2(x) :
   """
   Model function from Philips et al
   g(x) = (1.3 / (x + 1.3) )**2 

   """
   return (1.3 / (x + 1.3) )**2 


def g3(x) :
   """

   g(x) = 0.3 +  0.5*x + 0.8*x**2

   """
   return 0.3 +  0.5*x + 0.8*x**2
