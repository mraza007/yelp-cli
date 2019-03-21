from __future__ import print_function, unicode_literals
import regex
import os
from pprint import pprint
import emoji
from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_2
import json
from termcolor import colored
from yelpapi import YelpAPI
api_key = os.environ['API_KEY']
yelp_api = YelpAPI(api_key) 

questions = [
    {
        'type': 'input',
        'name': 'food',
        'message': emoji.emojize('What are you looking to eat ? :sushi:,:pizza:,:hamburger:'),


    },

    {
        'type': 'list',
        'name': 'city',
        'message': 'Choose your City',
        'choices': [
                "New York City",
                "Los Angeles",
                "Chicago",
                "Houston",
                "Philadelphia",
                "Phoenix",
                "San Antonio",
                "San Diego",
                "Dallas",
                "San Jose",
                "Austin",
                "Jacksonville",
                "San Francisco",
                "Indianapolis",
                "Columbus",
                "Fort Worth",
                "Charlotte",
                "Detroit",
                "El Paso",
                "Seattle ",
                "Denver ",
                "Washington",
                "Memphis",
                "Boston ",
                "Nashville-Davidson",
                "Baltimore",
                "Not Listed"
        ]
    },

]
answers = prompt(questions, style=custom_style_2)
if answers['city'] == 'Not Listed':
    x = input("What\'s your city: ")
    search_results = yelp_api.search_query(
        term=answers['food'],
        location=answers['city'],
        sort_by='rating',
        limit=5)
    print('Here are few restaurants I found ')
    for nums in search_results['businesses']:
            print('Name : ' +
                  colored(nums['name'], 'white', attrs=['bold']) +
                  '\n' +
                  'Phone: ' +
                  colored(nums['phone'], 'green', attrs=['bold']) +
                  '\n' +
                  'Address: ' +
                  colored(nums['location']['address1'],'cyan',attrs=['bold']) +
                  '\n' +
                  colored('Yelp url: ','red',attrs=['bold']) +
                  nums['url']
                  )
else:
    search_results = yelp_api.search_query(
        term=answers['food'],
        location=answers['city'],
        sort_by='rating',
        limit=5)
    print('Here are few restaurants I found ')
    for nums in search_results['businesses']:
            print('Name : ' +
                  colored(nums['name'], 'white', attrs=['bold']) +
                  '\n' +
                  'Phone: ' +
                  colored(nums['phone'], 'green', attrs=['bold']) +
                  '\n' +
                  'Address: ' +
                  colored(nums['location']['address1'],'cyan',attrs=['bold']) +
                  '\n' +
                  colored('Yelp url: ','red',attrs=['bold']) +
                  nums['url']
                  )
