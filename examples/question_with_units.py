import random
import teepy

ind = 0

def PROBLEM(ind):
    '''If points A, B, and C lie along a straight line in that order,
and the distance between point A and B is $ {L1} $, and the distance
between point B and C is $ {L2} $, what is the distance between point
A and C?'''

    L1s = [1, 2, 3, 4]
    L2s = [5, 6, 7, 8]
    
    L1 = teepy.define_unit(L1s[ind], 'ft')
    L2 = teepy.define_unit(L2s[ind], 'cm')
    
    L = L1 + L2

    answer = L.to('m')
    given = {'L1': L1,
             'L2': L2}

    return {'answer': answer, 'given': given}

def CHOICES(ind):
    N = 10
    choice_format = '{:0.3f}'
    step = random.uniform(0.01, 0.05)
    ans = teepy.get_answers(PROBLEM(ind))
    
    choices = teepy.generate_choices(N, ans, step)
    return {'choices': choices, 'choice_format': choice_format}

if __name__ == '__main__':
    teepy.display(ind, PROBLEM, CHOICES)