#!/usr/bin/python3
# -*- coding:UTF-8 -*-
"""
@description  ： 有限状态机 demo
@Time ： 2020/6/29 4:28 PM
@Auth ： Minhang
@File ： demo.py
@IDE  ： PyCharm
"""


from transitions import Machine

class Matter(object):
    pass

model = Matter()

#The states argument defines the name of states
states=['solid', 'liquid', 'gas', 'plasma']

# The trigger argument defines the name of the new triggering method
transitions = [
    {'trigger': 'melt', 'source': 'solid', 'dest': 'liquid' },
    {'trigger': 'evaporate', 'source': 'liquid', 'dest': 'gas'},
    {'trigger': 'sublimate', 'source': 'solid', 'dest': 'gas'},
    {'trigger': 'ionize', 'source': 'gas', 'dest': 'plasma'}]

machine = Machine(model=model, states=states, transitions=transitions, initial='solid')

# Test
print(model.state)    # solid
model.melt()
print(model.state)   # liquid
model.evaporate()
print(model.state)