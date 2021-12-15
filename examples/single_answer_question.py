import random
import teepy

ind = 0

def PROBLEM(ind):
    '''What color is the sky?'''

    answer = 'Blue'

    return {'answer': answer}

def CHOICES(ind):
    
    choices = teepy.get_answers(PROBLEM(ind))
    
    choices.extend(['Red',
                    'Green',
                    'Yellow',
                    'Orange'])
    
    random.shuffle(choices)
    
    return {'choices': choices}

if __name__ == '__main__':
    teepy.display(ind, PROBLEM, CHOICES)