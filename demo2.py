#!/usr/bin/python3
# -*- coding:UTF-8 -*-
"""
@description  ： 描述
@Time ： 2020/7/1 10:49 PM
@Auth ： Minhang
@File ： demo2.py
@IDE  ： PyCharm
"""
from transitions import Machine
from transitions import State
# Our old Matter class, now with  a couple of new methods we
# can trigger when entering or exit states.
class Matter(object):

    def say_hello(self):
        print("say_hello")

    def say_goodbye(self):
        print("say_goodbye")

lump = Matter()

# Same states as above, but now we give StateA an exit callback
states = [
    # State(name='solid', on_exit=['say_goodbye']), # solid
    "solid",
    'liquid', # liquid
    {'name':'gas'} # gas
]

machine = Machine(
    model=lump,
    states=states
)
machine.add_transition('sublimate', 'solid', 'gas') # 添加状态转化表

# Callbacks can also be added after initialization using
# the dynamically added on_enter_ and on_exit_ methods.
# Note that the initial call to add the callback is made
# on the Machine and not on the model.
# machine.on_enter_gas('say_hello')
# machine.on_enter_gas('say_hello')

# Test out the callbacks...
machine.set_state('solid') # 设置状态 : solid
lump.sublimate()
print(lump.state)
lump.to_solid()
print(lump.state)