''' Seconds to Minute-Seconds
Given an integer seconds, return a tuple (minutes, remaining_seconds) where minutes is the number of full minutes in seconds, and remaining_seconds is the leftover seconds.'''

def seconds_to_minute_seconds(seconds: int) -> tuple:
    min = seconds//60
    rem = seconds%60 
    return (min,rem)

''' Create a dictionary with elements in the list as values and the indices as keys.
Given a list of items, create a dictionary with the indices as keys and the items as items.'''
