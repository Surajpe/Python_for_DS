# -*- coding: utf-8 -*-
"""Assignment Solution - List Comprehension.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/149sm6CdGHL0RV1_ZkzzfKutEviwI24CA

# <u>Problem 1</u>

## The price of a house depends upon a lot of factors. These factors could be the geography, the area of house, the number of bedrooms in the house, proximity to necessary amenities etc. A simplistic model would assume that the price of a house depends on a single factor let's say area of the house.

## You are given a dictionary where the keys correspond to the area of a house (in sq. ft) and the value for each key is the price of the house (in lakh ₹) of 6 houses of a certain locality in Bengaluru
"""

# Dictionary of house area and house prices of 6 houses in
house_area_price_dict = {1056 : 39, 2600 : 120 , 1520 : 95, 1200 : 50, 2700 : 200, 1100 : 40}

"""### The values of this dictionary are actual prices. You want to make a simple model which takes the house area as input and outputs the predicted price.

### This model can be written as : <b><code>predicted_price(area) = 0.05*area + 10</code></b>

## Using the concept of list comprehension, create a list of predicted house prices using the above formula
"""

# Create a list of house areas
house_areas = list(house_area_price_dict.keys())


# Use list comprehension to store the predicted house prices in a list
predicted_house_prices = [0.05*area + 10 for area in house_areas]

# Print the list of predicted house prices
print(predicted_house_prices)

"""## Create another list which contains the squares of differences of each element of the two price lists : the actual prices and the predicted prices

"""

# List of actual house prices
actual_prices = list(house_area_price_dict.values())

# Create a list of tuples
price_tuples = list(zip(actual_prices,predicted_house_prices))

# List of squared differences between each element of the two lists
squared_difference_in_prices = [(predicted_price - actual_price)**2 for actual_price,predicted_price in price_tuples]
print(squared_difference_in_prices)

"""# <u> Problem 2</u>

## A sigmoid function is a mathematical function having a characteristic "S"-shaped curve or sigmoid curve. A common example of a sigmoid function is the logistic function shown in the first figure and defined by the formula:

$$ h(x) =  \frac{\mathrm{1} }{\mathrm{1} + e^{-x} }  $$


## Range is defined as all the possible values which the function $h(x)$ can take. Domain is defined as all the possible values which $x$ can take. In this case, range of the function is between 0 to 1 and the domain of the function is all real numbers

![Logistic Function.png](data:image/png;base64,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)

### You are given a list of values of $x$. You need to use list comprehension to calculate the corresponding transformation according to the sigmoid function defined above
"""

# List of the values of x

x = [3, 9, 10, -4, -2, 1, 0, 4, 5, 7]


# Calculate the corresponding sigmoid functions values using list comprehension. Take the value of e as 2.718
sigmoid_of_x = [round((1/(1+((2.718)**(-elem)))),2) for elem in x]
print(sigmoid_of_x)

# Return a list of boolean values if the sigmoid_of_x is greater than or equal to 0 and less than or equal to 1

list_of_booleans = [(elem>=0.0 or elem <=1.0) for elem in sigmoid_of_x]
print(list_of_booleans)

# Create a list of those values which are greater than 0.5
list_greater_0_point_5 = [elem for elem in sigmoid_of_x if elem>0.5]
print(list_greater_0_point_5)

"""# <u> Problem 3</u>

## You are given a sentence : <code>"I have been walking and running and dancing and smiling and laughing all my life, yet it all seems pointless."</code>

## You are required to extract all those words from this sentence in a list which ends with <code>ing</code>
"""

# Your sentence
my_sentence = "I have been walking and running and dancing and smiling and laughing all my life, yet it all seems pointless."

# Using list comprehension, extract those words which ends with ing

all_words_in_sentence = my_sentence.split(' ')


# Words ending with ing
words_ending_with_ing =  [word for word in all_words_in_sentence if word[-3:] == 'ing']


# Print those words
print(words_ending_with_ing)

"""# <u> Problem 4</u>

#### Natural Language Processing or NLP is one of the most promising fields in Machine Learning. Most of the times in NLP we deal with the textual data (a bunch of strings). Sometimes when we are processing the text, it is a common practice to get rid of some set of stop words from our original text. By default stop words are very common words used in English language such as and, or, punctuations etc.

#### In this exercise, you are provided with a default set of stop words and you need to add some extra set of custom words and remove these words from the given sentence and obtain the sentence without the stop words
"""

# A sample sentence
sentence = 'Hello, good morning folks! Today we will announce the half yearly performance results of the company. Due to the ongoing COVID-19 pandemic, our profits have declined by 60% as compared to the last year'

# Print your sentence
print(sentence)

# Default set of stop words
stop_words = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
              "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
              "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because",
              "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into",
              "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out",
              "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where",
              "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no",
              "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just",
              "don", "should", "now"}

# Update the set of stop words by adding the custom stop words
custom_stop_words = ["hello","good","morning","half","year"]

# Your code here
stop_words.update(custom_stop_words)

# Print the stop words in a sorted manner
print(stop_words)

# Create the list of words in the given sentence.
words_in_sentence = sentence.split(' ')

# Use list comprehension to remove the set of updated stop words from the list of words
words_to_keep = [word for word in words_in_sentence if word not in stop_words]

# Finally using the join() method, get the sentence without the stop words. Keep in mind that every word in the sentence will be separated by space
modified_sentence = " ".join(words_to_keep)

# Print the modified sentence
print(modified_sentence)