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
        print('You Selected German')
        return 'german'
    elif desired_cuisine_letter == 'j':
        print('You Selected Japanese')
        return 'japanese'
    elif desired_cuisine_letter == 'v':
        print('You Selected Vegetarian')
        return 'vegetarian'
    elif desired_cuisine_letter == 'f':
        print('You Selected French')
        return 'french'
    elif desired_cuisine_letter == 'a':
        desired_cuisine_letter += input('You selected {} please enter the next letter of your choice: african, american'.format(desired_cuisine_letter))
        if desired_cuisine_letter == 'af':
            print('You Selected African')
            return 'african'
        elif desired_cuisine_letter == 'am':
            print('You Selected American')
            return 'american'
        else:
            print('letter not recognized please try again')        
    elif desired_cuisine_letter == 'b':
        print('You Selected Barbecue')
        return 'barbecue'
    elif desired_cuisine_letter == 'c':
        desired_cuisine_letter += input('You selected {} please enter the next letter of your choice: czech, chinese, cafe'.format(desired_cuisine_letter))
        if desired_cuisine_letter == 'cz':
            print('You Selected Czech')
            return 'czech'
        elif desired_cuisine_letter == 'ch':
            print('You Selected Chinese')
            return 'chinese'
        elif desired_cuisine_letter == 'ca':
            print('You Selected Cafe')
            return 'cafe'
        else:
            print('letter not recognized please try again')
    elif desired_cuisine_letter == 't':
        print('You Selected Thai')
        return 'thai'
    elif desired_cuisine_letter == 'm':
        print('You Selected Mexican')
        return 'mexican'
    elif desired_cuisine_letter == 'i':
        desired_cuisine_letter += input('You selected {} please enter the next letter of your choice: indian, italian'.format(desired_cuisine_letter))
        if desired_cuisine_letter == 'in':
            print('You Selected Indian')
            return 'indian'
        elif desired_cuisine_letter == 'it':
            print('You Selected Italian')
            return 'italian'
        else: 
            print('letter not recognized please try again')
    elif desired_cuisine_letter == 'p':
        print('You Selected Pizza')
        return 'pizza'
    else:
        print('No options with starting with: {} please try again.'.format(desired_cuisine_letter))
        get_input()

def print_output(list):
    for print_resturant in list:
        print('----------------------------\n'
             'Restaurant Name: {}\n'.format(print_resturant[1]) +
             'Star Rating: {}\n'.format(print_resturant[2]) +
             'Price : {}\n'.format(print_resturant[3]) +
             'Address: {}'.format(print_resturant[4])
             )    

def get_restaurant_type():
    desired_cuisine = get_input()
    desired_cuisine_list = []
    for resturant in restaurant_choices:
        if resturant[0] == desired_cuisine:
            desired_cuisine_list.append(resturant)
    return print_output(desired_cuisine_list)



def try_again():
    loop = input('Would you Like to see recomendations for another Cusine? Press Y for yes and N for no')
    if loop == 'y':
        restaurant_recomendation()
    elif loop == 'n':
        print('Thank you for using Marks Restaurant Recommendation Tool...Goodbye.')
    else:
        print('input not recognized.. try again..')
        try_again()

def restaurant_recomendation():
    greet()
    get_restaurant_type()
    try_again()


restaurant_recomendation()