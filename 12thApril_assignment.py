'''
Twice the larger of two numbers is three more than five times the smaller and the sum of
four times the larger and three times the smaller is 71.
What are the numbers?
'''

def calculateLarger(larger, smaller) :
    #2*larger - 5*smaller - 3;
    while (larger != ((3 + 5*smaller)/2)):
        larger += 1;
        smaller = calculateSmaller(larger, smaller);
    return larger;


def calculateSmaller(larger, smaller) :
    #4*larger + 3*smaller - 71;
    return int((71 - 4*larger)/3);

larger = 1;
smaller = 1;
larger = calculateLarger(larger, smaller);
smaller = calculateSmaller(larger, smaller);

print("Numbers are: ", larger, "and", smaller);