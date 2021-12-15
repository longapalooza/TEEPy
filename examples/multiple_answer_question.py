import random
import teepy

ind = 0

def PROBLEM(ind):
    '''How Many licks does it take to get to the center of a Tootsie
Pop?'''

    answer = ['3', 'The world may never know.']

    return {'answer': answer}

def CHOICES(ind):
    
    choices = ['1', '2']
    
    choices.extend(teepy.get_answers(PROBLEM(ind)))
    
    return {'choices': choices}

if __name__ == '__main__':
    teepy.display(ind, PROBLEM, CHOICES)