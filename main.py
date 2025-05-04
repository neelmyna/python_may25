'''
catogories:

child : 12
teenagers: 12 - 18
adults : 18 - 60
old age : 60

DIstributed the ticket price 
--> child : free (age < 12)
--> teenagers: age >= 12 and age < 18
--> adults : age >= 18 and age <= 60

trace:
1. age = 10

age < 12 True

2. 
---> age = 26

first--> age < 12
         26 < 12 False
second --> age >= 12 and age < 18
           26 >= 12 and 26 < 18 False
third --> age >= 18 and age <= 60
          26 >= 18 and 26 <= 60 True

3. age = 62

first --> age < 12
          62 < 12 False
second --> age >= 12 and age < 18
           62 >= 12 and 62 < 18 #and operator will return true only if both conditions are true
           62 >= 12 and 62 < 18
           True         False        False
third --> age >= 18 and age <= 60
          62 >= 18 and 62 <= 60 
          True         False      False
4. age = 15

first --> age < 12
          15 < 12 False
second --> age >= 12 and age < 18
          15 >= 12 and 15 < 18 True
        
 
We are using and operator.

What AND Operator?

using OR operator:
age = 10

--> age < 12
    10 < 12 True
--> age >= 12  or age < 18
    26 >= 12  or 26 < 18 # or operator returns true if one of them condition satisfies
    True         False      return True
 
using NOT operator:

--> age < 12
    not(age < 12)
    not(10 < 12) not(False) ---> return True
                 not(True) ---> return False
    not(10<12) --> True


'''

age = int(input("Enter a number(1 to 100):"))

if age < 12:
    print("\nThe viewer is Child No need to pay charge")
elif age >= 12 and age < 18:
    print("\nThe viewer is teenager, Ticket charge : rs. 100")
elif age >= 18 and age <= 60:
    print("\n The viewer is adult so he have to pay Full Charge of rs. 150")
else:
    print("\nThe condition is out of range")


