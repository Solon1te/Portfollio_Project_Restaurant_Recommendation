from restaurant_choices import types
from restaurant_choices import restaurant_choices

cuisine_string = ''
for type in types:
    cuisine_string +=  '-------' + '\n' + type + '\n' 

def greet():
    print('Welcome to Marks Restaurant Recommendation Tool')
    print("I'll help you find the cuisine your craving from the following choices: \n {}".format(cuisine_string))

def get_input():
    desired_cuisine_letter = input("Please select the first letter of your desired cuisine")
    if desired_cuisine_letter == 'g':
        return 'german'
    elif desired_cuisine_letter == 'j':
        return 'japanese'
    elif desired_cuisine_letter == 'v':
        return 'vegetarian'
    elif desired_cuisine_letter == 'f':
        return 'french'
    elif desired_cuisine_letter == 'a':
        desired_cuisine_letter += input('You selected {} please enter the next letter of your choice: african, american'.format(desired_cuisine_letter))
        if desired_cuisine_letter == 'af':
            return 'african'
        elif desired_cuisine_letter == 'am':
            return 'american'
        else:
            print('letter not recognized please try again')        
    elif desired_cuisine_letter == 'b':
        return 'barbecue'
    elif desired_cuisine_letter == 'c':
        desired_cuisine_letter += input('You selected {} please enter the next letter of your choice: czech, chinese, cafe'.format(desired_cuisine_letter))
        if desired_cuisine_letter == 'cz':
            return 'czech'
        elif desired_cuisine_letter == 'ch':
            return 'chinese'
        elif desired_cuisine_letter == 'ca':
            return 'cafe'
        else:
            print('letter not recognized please try again')
    elif desired_cuisine_letter == 't':
        return 'thai'
    elif desired_cuisine_letter == 'm':
        return 'mexican'
    elif desired_cuisine_letter == 'i':
        desired_cuisine_letter += input('You selected {} please enter the next letter of your choice: indian, italian'.format(desired_cuisine_letter))
        if desired_cuisine_letter == 'in':
            return 'indian'
        elif desired_cuisine_letter == 'it':
            return 'italian'
        else: 
            print('letter not recognized please try again')
    elif desired_cuisine_letter == 'p':
        return 'pizza'
    else:
        print('No options with starting with: {} please try again.'.format(desired_cuisine_letter))
        get_input()

def restaurant_recomendation():
    greet()
    get_input()
    

restaurant_recomendation()


def get_restaurant_type():
     for resturant in restaurant_choices:
         for cuisine in resturant:
             print(cuisine)