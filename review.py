# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:38:50 2024

@author: JinQiuyi
"""

# Review 1

def add_to_list(value, my_list = []):
    my_list.append(value)
    return my_list

# Review 2
"""
Comment:
In following code, '{name}' and '{age}' will be directly returned. We need to use {} as placeholder and .format() to fill in the number
"""
def format_greeting(name, age):
    return "Hello, my name is {} and I am {} years old.".format(name, age)
    """
    return "Hello, my name is {name} and I am {age} years old."
    """
 
# Review 3
"""
Comment:
    If we add self. before variable, it refers to the variable of the instance itself, then, every counter will return 1
    If we replace self. with Counter., then it refers to the variable of the class, count will increase 1 when a new counter is created
"""
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
        """
        self.count += 1
        """
    def get_count(self):
        return Counter.count
        """
        return self.count
        """
        
# Review 4

import threading

class SafeCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
    
    def get_count(self):
        return self.count


def worker(counter):
    for _ in range(1000):
        counter.increment()
        print(counter.get_count())

counter = SafeCounter()
threads = []

for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
    
    
# Review 5
"""
=+ means that add value after assignment, it doesn't have any meaning, the count keeps 1.
We need +=, it first adds 1 to count, and then assigns the new value to counts.
"""
def count_occurrences(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
            """
            counts[item] =+ 1
            """
        else:
            counts[item] = 1
    return counts
