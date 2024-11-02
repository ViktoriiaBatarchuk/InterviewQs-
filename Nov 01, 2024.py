'''
Number: 147
Taks: Is drawing a red card and drawing an ace independent?
Hint: Drawing an ace (event A) and drawing a red card (event B) are two separate events
-- think of a way to prove (using probability theory) that knowing whether event A occurred
impacts the probability of event B occuring.
'''

#Define the probabilities
P_A = 4/52 #probability of drawing the Ace
P_B = 26/52 #probability of drawing a Red card
P_A_and_B = 2/52 #probability of drawing a red Ace

#The probability of P(A) and P(B)
P_A_times_P_B = P_A*P_B

#Check the independence
independent = P_A_and_B == P_A_times_P_B

#Display the results
print("P(A):", P_A)
print("P(B):", P_B)
print("P(A and B):", P_A_and_B)
print("P(A)*P(B):", P_A_times_P_B)
print("Are events A and B independent?", independent)

