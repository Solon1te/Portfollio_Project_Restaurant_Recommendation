from restaurant_choices import types
from restaurant_choices import restaurant_choices

cuisine_string = ''
for type in types:
    cuisine_string += '\n' + type + '\n' 

def greet():
    print('Welcome to Marks Restaurant Recommendation Tool')
    print("I'll help you find the cuisine your craving from the following choices: \n {}".format(cuisine_string))

def get_input():
    desired_cuisine_letter = input("Please select the first letter of your desired cuisine")
    if desired_cuisine_letter == 'g':
        print()
    elif desired_cuisine_letter == 'j':
        print()
    elif desired_cuisine_letter == 'v':
        print()
    elif desired_cuisine_letter == 'f':
        print()
    elif desired_cuisine_letter == 'a':
        print()
    elif desired_cuisine_letter == 'b':
        print()
    elif desired_cuisine_letter == 'c':
        print()
    elif desired_cuisine_letter == 't':
        print()
    elif desired_cuisine_letter == 'm':
        print()
    elif desired_cuisine_letter == 'i':
        print()
    elif desired_cuisine_letter == 'p':
        print()
    else:
        print('No options with starting with: {} please try again.'.format(desired_cuisine_letter))
        get_input()

def restaurant_recomendation():
    greet()
    

restaurant_recomendation()
