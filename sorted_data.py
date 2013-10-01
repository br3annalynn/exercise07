"""
We need to get the file from the command line.
We need to open the file and read it line by line.
We need to split each line on the :

We need to create a dictionary of names and ratings.
We need to alphabetize the dictionary key values
We need to print the restaurants and their corresponding ratings.
"""

from sys import argv
script, file_name = argv
file_name = open(file_name)



def main(file_name):
    restaurant_dict = {}
    for line in file_name:

        clean_line = normalize(line)

        one_restaurant = clean_line.split(":")
        restaurant_dict[one_restaurant[0]] = one_restaurant[1]

    alpha_restaurant_list = alphabetize(restaurant_dict)
    print_restaurants(alpha_restaurant_list, restaurant_dict)


def normalize(line):
    clean_line = line.strip("\n")
    return clean_line


def alphabetize(restaurant_dict):
    restaurant_names = restaurant_dict.keys()
    return sorted(restaurant_names)
        
def print_restaurants(alpha_restaurant_list, restaurant_dict):
    for name in alpha_restaurant_list:
        print "Restarant %r is rated at %s." %(name, restaurant_dict.get(name))

main(file_name)