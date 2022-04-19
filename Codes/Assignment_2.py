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

def main():
    Pr_1 = 2/7  # Probability that balls drawn from bag A are white
    Pr_2 = 1/7  # Probability that balls drawn from bag A are black
    Pr_3 = 4/7  # Probability that the balls drawn are black and white from bag A
    Pr_4 = 5/10 # Probability that the ball drawn from bag B is white given both balls drawn are white
    Pr_5= 3/10  # Probability that the ball drawn from bag B is white given both balls drawn are black
    Pr_6 = 4/10 # Probability that the ball drawn from bag B is white given balls drawn are white and black

    #Output
    print(f"The probability that the ball drawn is white from bag B is {prob(Pr_1,Pr_2,Pr_3,Pr_4,Pr_5,Pr_6)}")
     
def prob(Pr_1,Pr_2,Pr_3,Pr_4,Pr_5,Pr_6) -> float:
        """ Returns the probability that the ball drawn is white from bag B """
        return Pr_1*Pr_4 + Pr_2*Pr_5 + Pr_3*Pr_6

if __name__ == '__main__':
       main()