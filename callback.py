#!/usr/bin/python3
# -*- coding:UTF-8 -*-
"""
@description  ： 描述
@Time ： 2020/7/8 2:40 PM
@Auth ： Minhang
@File ： callback.py
@IDE  ： PyCharm
"""
from transitions import Machine

class Matter(object):
    def make_hissing_noises(self):
        print("aaaaaaaaaaa")

    def disappear(self):
        print("bbbbbbbbbbb")

states = ["solid","liquid","gas",]

transitions = [
    { 'trigger': 'melt', 'source': 'solid', 'dest': 'liquid', 'before': 'make_hissing_noises'},
    { 'trigger': 'evaporate', 'source': 'liquid', 'dest': 'gas', 'after': 'disappear' }
]

# lump = Matter()
machine = Machine(states, transitions=transitions, initial='solid')
machine.melt()
print(machine.state)
# lump.evaporate()
# print(lump.state)