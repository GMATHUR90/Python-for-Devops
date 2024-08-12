
# 1. String Concat

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)

# 2. String-len
text = "Python is awesome"
length = len(text)
print("Lenght of the text: ", text)

# 3. String-lowercase
text1 = "Python is awesome"
uppercase = text.upper()
lowercase = text.lower()
print("Uppercase: ", uppercase)
print("Lowercase: ", lowercase)

# 4. String replace
text2 = "Python is awesome"
new_text = text.replace("awesome","great")
print("Modified text: ", new_text)


# 5. String split
text3 = "Python is lovely"
word = text3.split()
print("Words: ", word)

# 6. String strip
text4 = "     Python is gorgeous   "
word1 = text4.strip()
print("Strip words:", word1)

# 7. String-substring

text5 = "Python is awesome"
substring = "is"
if substring in text:
    print("Found in the text: ", substring)

# 8. Float variable

num1 = 5.0
num2 = 2.0

# Basic Arithmetic

result1 = num1 + num2
print("Addition: ", result1)

result2 = num1 - num2
print("Subtraction: ", result2)

result3 = num1 * num2
print("Multiplication: ", result3)

result4 = num1 / num2
print("Division: ", result4)

# Rounding
result5 = round(3.14159265359) # Round to 2 decimal places
print("Rounded: ", result5)

# Integer Variable

num3 = 10
num4 = 5

# Integer Division
result6 = num3 // num4
print("Integer Division :", result6 )

#Modulus Remainder(%)
result7 = num3 % num4
print("Modulus Remainder: ", result7)

#Absolute Value
result8 = abs(-7)
print("Absolute Value: ", result8)

# regex search
import re

text6 = "The quick brown fox"
pattern1 = r"brown"
# re.search(): searches for entire string for a match and returns the first occurence
search = re.search(pattern1, text6)
if search:
    print("Pattern found: ", search.group())
else:
    print("Pattern not found")

 # regex match
# Check for the match at the beginning of the string
match = re.match(pattern1, text)
if match:
    print("Match found: ", match.group())
else:
    print("No Match")

# regex replace
text7_A = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text_a = re.sub(pattern, replacement, text7_A)
print("Modified text: ", new_text_a)

# regex-findall

matches_A = re.findall(pattern, text7_A)
if matches_A:
    print("Pattern found: ", matches_A)
else:
    print("Pattern not found")

# regex-split
text8 = "apple,grapes,orange,banana,pinaple"
pattern_b = r","
split_result = re.split(pattern_b, text8)
print("Split result: ", split_result)


"""
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents$ /home/gauravmtwt1/Documents/git-demo/.venv/bin/python "/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Data_type_examples.py"
Hello World
Lenght of the text:  Python is awesome
Uppercase:  PYTHON IS AWESOME
Lowercase:  python is awesome
Modified text:  Python is great
Words:  ['Python', 'is', 'lovely']
Strip words: Python is gorgeous
Found in the text:  is
Addition:  7.0
Subtraction:  3.0
Multiplication:  10.0
Division:  2.5
Rounded:  3
Integer Division : 2
Modulus Remainder:  0
Absolute Value:  7
Pattern found:  brown
No Match
Modified text:  The quick red fox jumps over the lazy red dog
Pattern found:  ['brown', 'brown']
Split result:  ['apple', 'grapes', 'orange', 'banana', 'pinaple']

"""
    