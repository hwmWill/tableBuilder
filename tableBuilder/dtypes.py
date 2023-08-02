import math

def round_half_up(x, roundTo=2):
    mutliplier = 10**roundTo 
    return math.floor(x * mutliplier + 0.5) / mutliplier

def formatCol(series, dtype, roundTo=2):
    try:
        return [dtype(x, roundTo) for x in series]
    except TypeError:
        return [dtype(x) for x in series]
    
def percent(x, roundTo=2):
    return f'{round_half_up(x, roundTo):,.{roundTo}f}%'

def decimal(x, roundTo=2):
    return f'{round_half_up(x, roundTo):,.{roundTo}f}'

def integer(x):
    return f'{round_half_up(x, roundTo=0):,}'

def money(x, roundTo=2):
    if x >= 0:
        return f'${round_half_up(x, roundTo):,.{roundTo}f}'
    else:
        return f'$({round_half_up(x, roundTo):,.{roundTo}f})'
