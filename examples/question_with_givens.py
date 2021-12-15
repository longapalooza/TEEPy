import random
import teepy

ind = 0

def PROBLEM(ind):
    '''A {object} is an example of what?'''
    
    obj = ['dog', 'carrot', 'diamond'] 

    answers = ['Animal', 'Vegatable', 'Mineral']
    
    given = {'object': obj[ind]}

    return {'answer': answers[ind], 'given': given}

def CHOICES(ind):
    
    choices = ['Animal', 'Vegatable', 'Mineral']
    
    return {'choices': choices}

if __name__ == '__main__':
    teepy.display(ind, PROBLEM, CHOICES)