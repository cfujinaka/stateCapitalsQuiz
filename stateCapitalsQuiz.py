#! python3

#stateCapitalsQuiz.py - Prompts user with a state, user types answer, and a score
#is calculated at the end.

#Concepts utilized: shebang line, random module, dictionaries and lists, for and
#if loops, string concatenation.

#Chelsea Fujinaka April 08 2019

import random

#quiz data - states and their capitols

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
   'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
   'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
   'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
   'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
   'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
   'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
   'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
   'Vermont':'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
            

#Cycle through states, prompting user and receiving input from user. Must keep
#track of # correct.
print('''US state capitals quiz! Please enter the corresponding capital for the
        state for which you are prompted. Case does not matter, but
        spelling does! To quit, enter '' at any time. Your score will be
        based on teh number of questions you answer. Good luck!''')

states = list(capitals.keys())
random.shuffle(states)
numCorrect = 0
total = 0

for i in range(len(states)):
    print(states[i] + ':')
    answer = input()
    if answer == '':
        break
    
    if answer.lower() == capitals[states[i]].lower():
        numCorrect += 1
        print('Correct!')
    else:
        print('I\'m sorry. That is incorrect. THe correct answer is ' + capitals[states[i]] + '.')

#Calculate and display score
score = (numCorrect/len(states))*100
print('You scored ' + str(score) + '%.')

if score < 50:
    print('You really need to study your state capitals!')
elif (score >= 50) and (score < 75):
    print('Not bad, but not great.')
elif (score >= 75) and (score < 85):
    print('That\'s not bad!')
elif (score >= 85) and (score < 95):
    print('You did very well!')
elif score >= 95:
    print('Wow that is very impressive!')
