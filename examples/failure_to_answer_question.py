import random
import teepy

ind = 0

def PROBLEM(ind):
    '''Failure to answer this question results in a 2 point deduction.
Did you answer this question?'''

    answer = 'Yes'

    return {'answer': answer}

def CHOICES(ind):
    
    choices = ['Yes', 'No']
    
    return {'choices': choices}

if __name__ == '__main__':
    teepy.display(ind, PROBLEM, CHOICES)