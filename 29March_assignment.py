'''
1. Write a program which can compute the factorial of a give numbers.
The results should be printed in a comma-separated sequence on a single line. Suppose the
following input is supplied to the program:
8
Then, the output should be:
40320

'''

def factorial(num):
    fact = 1;
    if num == 0:
        return fact;
    else:
        for i in range(1, num+1):
            fact *= i;
    return fact;
number = int(input("Enter the number to calculate factorial: "));
print(factorial(number));

'''
3. Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2*C*D)/H]
Following are the fixed values of C and H:
C is 50 and H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example: Let us assume the following comma-separated input sequence is given to the program:
100, 150, 180
The output of the program should be:
18, 22, 24
'''
import math as maths;

c=50; h=30;
def calculateSquareRoot_Formula(seq):
    result = [];
    for i in seq:
        i = int(i);
        product = (2*c*i)/h;
        result.append(int(maths.pow(product, 1/2)));
    return result;

inputs = input("Enter numbers: ");
seq = inputs.split(",");
#print(seq);
print(calculateSquareRoot_Formula(seq));

'''
4. Write a program that accepts a sequence of whitespace seperated words as input and print the
wprds after removing all the duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

'''
def removeDuplicate(sentence):
    result = set();
    for words in sentence:
        result.add(words);
    return result;

def sortLexicographically(sentenceSet):
    sorted = list(sentenceSet);
    sorted.sort();
    return sorted;

sentence = str(input("Enter the sentence: ")).split(" ");
nonDuplicates = removeDuplicate(sentence);
resultList = sortLexicographically(nonDuplicates);
for item in resultList:
    print(item, end=" ");

'''

5. Write a program which will find all such numbers between 1000 and 3000 (both included) such that
each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence
on a single line.

'''
def printEven():
    for i in range(1000, 3001):
        if i%2 == 0:
            print(i, end=", ")
printEven();

'''
6. Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

def countLetters(seq):
    letters = 0;
    for word in list(seq):
        for char in word:
            if str(char).isalpha():
                letters += 1;
    return letters;

def countDigits(seq):
    digits = 0;
    for word in list(seq):
        for char in word:
            str(char).isupper();
            if str(char).isdigit():
                digits += 1;
    return digits;

inputs = input("Enter the input: ").split(" ");
print("LETTERS ", countLetters(inputs));
print("DIGITS ", countDigits(inputs));

'''
7. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
def calculateUpperCase(seq):
    count = 0;
    for word in seq:
        for char in word:
            if(str(char).isupper()):
                count += 1;
    return count;

def calculateLowerCase(seq):
    count = 0;
    for word in seq:
        for char in word:
            if(str(char).islower()):
                count += 1;
    return count;

inputs = input("Enter the sentence: ").split(" ");
print("UPPER CASE ", calculateUpperCase(inputs));
print("LOWER CASE ", calculateLowerCase(inputs));

'''
8. Write a program that computes the net amount of a bank account based on a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200
D means deposit while W mean withdrawl.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, output should be:
500
'''

def processTransactions(transaction_seq):
    total = 0;
    for transaction in transaction_seq:
        type_transaction = transaction.split(" ");
        if(type_transaction[0] == "D"):
            total += int(type_transaction[1]);
        elif (type_transaction[0] == "W"):
            total -= int(type_transaction[1]);
    return total;

transactions = input("Enter the transaction data: ").splitlines();
print(processTransactions(transactions));

'''
9. A website requires the users to input username and password to register. Write a program to check the
validity of the password input by users. Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma-separated passwords and will check them according to the
above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example: If the following passwords are given as input to the program:
ABd1234@1, aF1#, 2w3E*, 2We3345.
Then, the output of the program should be:
ABd1234@1

'''
import re as regex;

def validatePassword(passwords):
    validPasswords = list();
    for password in passwords:
        if len(password) >=6 and len(password) <=12:
            if regex.findall("[a-zA-Z0-9]", password):
                validPasswords.append(password);
    return validPasswords;

inputs = str(input("Enter the passwords: ")).split(", ");
validPasswords = validatePassword(inputs);
for password in validPasswords:
    print(password, end=", ")

'''

10. You are required to write a program to sort the (name, age, height) tuples by ascending order where the
name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1. Sort based on name;
2. Then sort based on age;
3. Then sort by score.
The priority is that name>age>score.
If the following tuples are given as input to the program:
Tom, 19, 80
John, 20, 90
Jonny, 17, 91
Jonny, 17, 93
Json, 21, 85
Then, the output of the program should be:
[("John", "20", "90"), ("Jonny", "17", "91"), ("Jonny", "17", "93"), ("Json", "21", "85"),
("Tom", "19", "80")]
'''
from operator import itemgetter;
def sortData(dataset):
    dataset.sort(key=itemgetter(2));
    dataset.sort(key=itemgetter(1));
    dataset.sort(key=itemgetter(0));
    return dataset;

rawData = input("Enter the data: ").splitlines();
dataset = list();
for data in rawData:
    data = tuple(data.split(", "));
    dataset.append(data);
print(sortData(dataset));


