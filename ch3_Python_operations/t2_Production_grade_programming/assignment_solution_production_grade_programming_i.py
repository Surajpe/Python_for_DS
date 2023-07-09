# -*- coding: utf-8 -*-
"""Assignment Solution - Production Grade Programming I.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZXFdUZs_I8x8iy_6O1sAaUXAcBmvJEE4

## <u>While doing this assignment only use those concepts which have been taught till now</u>

# <u> Problem 1</u>

### Create a class <code>Cylinder</code> which takes two attributes <code>radius</code> and <code>height</code>.

### Create the following methods in this class:

* ### method <code>volume()</code> which calculates the volume of the cyinder which is defined as $V  = \pi r^2 h$

* ### method <code>surface_area()</code> which calculates the area of the cyinder which is defined as $S  = 2\pi r h$
"""

# Write your code below. Take pi as 3.14
class Cylinder:
  def __init__(self,radius,height):
    self.radius = radius
    self.height = height

  def volume(self):
    return 3.14*(self.radius)**2 * (self.height)

  def surface_area(self):
    return 2*3.14 *(self.radius) * (self.height)

sample_cylinder = Cylinder(2,4)

sample_cylinder.surface_area()

sample_cylinder.height

sample_cylinder.volume()

"""## <u>Problem 2</u>

### You started your own money wallet where your customers can create their accounts and they can either deposit or withdraw money from this wallet.

### Write a Python class <code>BankAccount</code> which takes the balance as an attribute. You can initialize the balance with 0 because any new account will have 0 rupees in their wallet. Next write two methods for your class :

* #### <code>withdraw()</code> method which takes the amount to be withdrawn as an argument and returns the balance after the withdrawal

* #### <code>deposit()</code> method which takes the amount to be deposited as an argument and returns the balance after the deposit.

### Keep in mind that if the balance to be withdrawn exceeds the current balance, it should display a message that "Not enough balance in your account"

"""

# Write your BankAccount class below

class BankAccount:
  def __init__(self, balance=0):
    self.balance = balance

  def deposit(self,amount):
    # balance = self.balance
    self.balance += amount
    return self.balance

  def withdraw(self,amount):
    # balance = self.balance
    if self.balance < amount :
      print("Not enough balance in your account")
    else:
      self.balance -= amount
    return self.balance

# Create two instances of this class for two customers
john_account = BankAccount()
david_account = BankAccount(balance=10000)

"""### Next add some amount and withdraw some another amount for both the customers."""

# Deposit some amount and withdrawing some amount from John's account
john_account.deposit(100)

john_account.balance

john_account.withdraw(150)

john_account.withdraw(50)

#  Deposit some amount and withdrawing some amount from David's account
david_account.deposit(200)

david_account.withdraw(50)

"""## <u>Problem 3 </u>

### Create a class <code>Time </code> which takes two attributes hours and minutes.
*  #### Make a method <code>DisplayTime()</code> which displays the time in AM/PM formats. For example if the input is 14 hours and 45 mins, then this method will print "The time is 2:45 PM". If the inputted hours exceeds 23 then print the message "The input hours should be less than 24" and if the inputted minutes exceeds 59 then print the message "The input minutes should be less than 60." . Also if the input is 12 hours 30 minutes, then the displayed time would be 12:40 PM
* #### Construct a method <code>DisplayRatio()</code> which should display the ratio of minutes to hours. For example, (8 hours and  16 mins) should display 2. Use <code>try</code>, <code>except</code> block to account for ZeroDivisionError.
"""

class Time:

  def __init__(self, hours, mins):
    self.hours = hours
    self.mins = mins


  def displayTime(self):
    if (self.hours > 23) or (self.mins > 59):
      print("The input hours should be less than 24 and the input minutes should be less than 60")
    else:
      if (self.hours < 12) and (self.mins < 60):
        time_to_display = str(self.hours) + ":" + str(self.mins) + " AM"
        print(f"The time is {time_to_display}")
      elif (self.hours ==12) and (self.mins < 60):
        time_to_display = str(self.hours) + ":" + str(self.mins) + " PM"
        print(f"The time is {time_to_display}")
      else:
        time_to_display = str(self.hours - 12) + ":" + str(self.mins) + " PM"
        print(f"The time is {time_to_display}")


  def displayRatio(self):
    try:
      print(self.mins/self.hours)
    except:
      print("The argument 'hours' should not be zero.")

# Check for few sample inputs of hours and mins
hour_min_list = [(23,45), (34,50), (12,34), (14,67),(19,20), (2,15), (0, 10)]

# Using a for loop display the corresponding 12 hour time format for the above hour_min_list

for hour,min in hour_min_list :
  A = Time(hour,min)
  A.displayTime()

# Also display the corresponding ratios for the above list

for hour,min in hour_min_list :
  A = Time(hour,min)
  A.displayRatio()

