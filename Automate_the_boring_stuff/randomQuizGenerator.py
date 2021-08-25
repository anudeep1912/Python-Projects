#! python3
import random
import pathlib

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
   'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNumber in range(35):
    quizFile = open(f'Quiz_{quizNumber+1}.txt', 'w')
    quizAns = open(f'QuizAns_{quizNumber+1}.txt', 'w')
    quizFile.write('Name: ______\nRoll no: _____\nDate: _____\n\n')
    quizFile.close()
    quizAns.write(f'Answers for Quiz_{quizNumber+1}\n\n')
    quizAns.close()
    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):
        quizFile = open(f'Quiz_{quizNumber+1}.txt', 'a')
        quizAns = open(f'QuizAns_{quizNumber+1}.txt', 'a')
        quizFile.write(f'{questionNum+1}. What is the capital of {states[questionNum]}? \n')
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        quizFile.write(f'a) {answerOptions[0]}   b) {answerOptions[1]}   c) {answerOptions[2]}   d) {answerOptions[3]}\n\n')
        quizAns.write(f'{questionNum+1}. {correctAnswer}\n')
        quizFile.close()
        quizAns.close()






