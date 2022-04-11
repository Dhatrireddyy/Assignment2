# ICSE 2019 Grade 12
# Question 10

# Name: Velma Dhatri Reddy
# Roll number: AI21BTECH11030

""" Problem Statement
Bag A contains 4 white balls and 3 black balls, while Bag B contains 3 white balls and 5 black balls.
Two balls are drawn from Bag A and placed in Bag B. Then, what is the probability of drawing a white
ball from Bag B?
"""

from math import comb
from fractions import Fraction
from decimal import Decimal

def main():
    Pr_X1 = comb(4,2)/comb(7,2)  # Probability that both balls drawn are white from bag A
    Pr_X2 = comb(3,2)/comb(7,2)  # Probability that both balls drawn are black from bag A
    Pr_X3 = (comb(4,1)*comb(3,1))/comb(7,2)  # Probability that balls drawn are black and white from bag A
    Pr_X4_1 = 5/10  # Probability that the ball drawn from bag B is white given event X_1 occured
    Pr_X4_2 = 3/10  # Probability that the ball drawn from bag B is white given event X_2 occured
    Pr_X4_3 = 4/10  # Probability that the ball drawn from bag B is white given event X_3 occured

    #Output
    print(f"The probability that the ball drawn is white from bag B is {prob(Pr_X1,Pr_X2,Pr_X3,Pr_X4_1,Pr_X4_2,Pr_X4_3)}")
     
def prob(Pr_X1,Pr_X2,Pr_X3,Pr_X4_1,Pr_X4_2,Pr_X4_3) -> float:
        """ Returns the probability that the ball drawn is white from bag B """
        return Pr_X1 * Pr_X4_1 + Pr_X2 * Pr_X4_2 + Pr_X3 * Pr_X4_3

if __name__ == '__main__':
       main()