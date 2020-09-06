#intially pip install wikipedia

#import the Module
import wikipedia 


#search value from User
search = input("Enter the Wiki Search : ") 

#users sentance limitations
sent = int(input("Enter the Number of Sentences : "))

#printing summary as Output
print(wikipedia.summary(search,sentences=sent))
