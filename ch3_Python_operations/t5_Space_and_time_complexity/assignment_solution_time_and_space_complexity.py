# -*- coding: utf-8 -*-
"""Assignment  Solution- Time and Space Complexity.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jK7l2HTtY5WwT7M6hPYO7VAZ_U6_ko4H

## <u>While doing this assignment only use those concepts which have been taught till now</u>

# Problem 1

Write a Python function which takes a string as an input and returns the reversed string as an output.


*   Do not use any inbuilt funtion or method. Use `for` loops only.
*   Also, do the time and space complexity analysis.
"""

# Write your code here


def recerse_string(my_string):
    '''Reverse the string'''
    rev_string=''
    for char in range(len(my_string)-1,-1,-1):                                  #concatenates string from last
        rev_string+=my_string[char]
    return rev_string

my_string='While doing this assignment only use those concepts which have been taught till now'
recerse_string(my_string)

# Time Complexity : O(N)
# Space Complexity : O(N)
# Auxiliary Space : O(N)

"""# Problem 2

Write a Python function which takes a list of `n` lists as an input. Each of the `n` lists have `m` non-zero integers each. The function should return a list which contains `n` integers corresponding to the square of the maximum of each of the `n` lists in the list of lists.

Example:
Inputs
```
n = 2
m = 3
list_of_lists = [[1, 2, 3], [5, 7, 6]]
```
Output:
```
[9, 49]
```

*   Do not use any inbuilt funtion or method. Use `for` loops only.
*   Also, do the time and space complexity analysis.

"""

# Write your code here
def max_square(list_of_list):
    '''Finds the square of maximums in iinner lists'''
    output_list=[]                                                              #output list
    for inner_list in list_of_list:
        maximum=0
        for num in inner_list:
            if num> maximum :                                                   # calculates maximum
                maximum=num
        output_list.append(maximum**2)
    return output_list




# Time Complexity : O(m*n)
# Space Complexity : O(N*M)
# Auxiliary Space : O(N)

max_square([[1, 2, 3],[1, 2, 13], [4,15, 7, 6], [5, 7, 6]])

