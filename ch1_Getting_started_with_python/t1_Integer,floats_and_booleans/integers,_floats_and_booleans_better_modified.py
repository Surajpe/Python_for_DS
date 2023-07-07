# -*- coding: utf-8 -*-
"""Assignment Solution - Integers, Floats and Booleans.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OttbJe_E7mFP59faSfeoX8ykB1gqBO7R

## <u>While doing this assignment only use those concepts which have been taught till now</u>

## <u>Problem 1</u>

In a cricket tournament, based on the outcome of a particular match a team gets following points:
* <code>wins</code> gets <code>3</code> points
* <code>draws</code> gets <code>1</code> points
* <code>losses</code> gets <code>0</code> points

Team Aravali plays <code>8</code> matches in this tournament. It wins <code>4</code> matches, loses <code>3</code> matches and draws <code>1</code>. What is the total number of points gained by the Team Aravali?
"""

# The outcome variables are defined below
wins = 4
losses = 3
draws = 1

# Calculate the total points gained by Team Aravali
aravali_points = 3*wins + 0*losses + 1*draws

# Print the variable aravali_points
aravali_points

"""## <u>Problem 2 </u>

* Root of a function $f(x)$ is defined as the value $x$ where $f(x)=0$
* Consider a quadratic function $ f(x) = x^2 + 3x - 4$

### Find the value of the function $f(x)$ at points   $x=2,x=-1, x=1$.
"""

# Calculate the value of the function f(x) at x = 2
func_evaluated_at_2 = 2**2 + 3*2 - 4

# Print the value below
print(func_evaluated_at_2)

# Calculate the value of the function f(x) at x = -1
func_evaluated_at_minus1 = (-1)**2 + 3*(-1) - 4

# Print the value below
print(func_evaluated_at_minus1)

# Calculate the value of the function f(x) at x = 1
func_evaluated_at_1 = 1**2 + 3*1 - 4

# Print the type of the variable below
print(func_evaluated_at_1)
type(func_evaluated_at_1)

"""### Return the boolean for each value of $x$ to find out whether that value is a root of $f(x)$"""

# Check whether 2 is a root of f(x)
func_evaluated_at_2 == 0

# Check whether -1 is a root of f(x)
func_evaluated_at_minus1 == 0

# Check whether 1 is a root of f(x)
func_evaluated_at_1 == 0

"""## <u> Problem 3 </u>

A bag contains <code>45</code> apples, <code>65</code> oranges and <code>30</code> bananas. Find the percentage of each type of food items in the bag.
"""

# Calculate the percentage of apples and print the variable
apples = 45
oranges = 65
bananas = 30

percentage_apples = apples*100/(apples+ oranges + bananas)
print(percentage_apples)

# Calculate the percentage of oranges and print the variable
percentage_oranges = oranges*100/(apples+ oranges + bananas)
print(percentage_oranges)

# Calculate the percentage of bananas and print the variable

percentage_bananas = bananas*100/(apples + oranges + bananas)
print(percentage_bananas)

"""## <u>Problem 4</u>

You were playing a fun guessing game during your school break. There were a total of 100 participants excluding you. Out of these 100 people, 30 were Maths Majors, 45 were Economics Majors and 25 were Physics Majors.

The game was divided into three rounds.

* In the first round, you had to guess the number of Maths Majors and you <b>correctly</b> guessed 20 of them.
* In the second round, you had to guess the number of Economics Majors and you <b>correctly</b> guessed 30 of them.
* In the final third round, you had to guess the number of Physics Majors and you <b>correctly</b> guessed 20 of them.

### Accuracy is defined as the number of correct guesses upon total number of people in the group (expressed in percentage)

* ### Define your variables
"""

# Store the number of Maths majors
maths_majors = 30

# Store the number of Economics majors
economics_majors = 45

# Store the number of Physics majors
physics_majors = 25

# Store the number of your correct guesses of Maths majors
correctly_guessed_maths_majors = 20

# Store the number of your correct guesses of Economics majors
correctly_guessed_economics_majors = 30

# Store the number of your correct guesses of Physics majors
correctly_guessed_physics_majors = 20

"""* ### Calculate your accuracy in each of the three rounds"""

# Print the Maths accuracy

maths_accuracy = correctly_guessed_maths_majors*100/maths_majors
print(maths_accuracy)

# Print the Economics accuracy

economics_accuracy = correctly_guessed_economics_majors*100/economics_majors
print(economics_accuracy)

# Print the Physics accuracy
physics_accuracy = correctly_guessed_physics_majors*100/physics_majors
print(physics_accuracy)

"""* ### Calculate your overall accuracy in the entire game"""

# Print the overall accuracy
total_correct_guesses = correctly_guessed_maths_majors + correctly_guessed_physics_majors + correctly_guessed_economics_majors
total_majors = maths_majors + economics_majors + physics_majors
overall_accuracy = (total_correct_guesses)*100/(total_majors)
print(overall_accuracy)
