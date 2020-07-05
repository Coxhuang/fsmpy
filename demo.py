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
from transitions import State
from pprint import pprint


class Matter(object):
    pass

model = Matter()

states=[State(name='solid'), 'liquid', 'gas', 'plasma'] # 定义四种状态 : 固体 液体 气体 等离子体

# trigger参数定义新触发方法的名称
transitions = [
    {
        'trigger': 'melt',
        'source': 'solid',
        'dest': 'liquid'
    }, # 固体 融化 变成 液体
    {
        'trigger': 'evaporate',
        'source': 'liquid',
        'dest': 'gas'
    }, # 液体 融化 变成 气体
    {
        'trigger': 'sublimate',
        'source': 'solid',
        'dest': 'gas'
    }, # 固体 升华 变成 气体
    {
        'trigger': 'ionize',
        'source': 'gas',
        'dest': 'plasma'
    }, # 气体 电离 变成 等离子体
]

machine = Machine(
    model=model,
    states=states, # 状态
    transitions=transitions, # 状态转化表
    initial='solid' # 初始状态
)

# Test
print(model.state)    # solid
model.melt()
print(model.state)   # liquid
# model.evaporate()
# print(model.state)
