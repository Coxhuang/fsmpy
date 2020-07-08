#!/usr/bin/python3
# -*- coding:UTF-8 -*-
"""
@description  ： 描述
@Time ： 2020/7/7 12:09 AM
@Auth ： Minhang
@File ： hsm.py
@IDE  ： PyCharm
"""

from transitions.extensions import HierarchicalMachine as Machine

def a1():
    states = [
        'standing', # 站立
        'walking', # 不行
        {
            'name': 'caffeinated', # 精神抖擞
            'initial': 'dithering',
            'children':[
                'dithering', # 抖动
                'running', # 跑
            ]
        }
    ]
    transitions = [
        ['walk', 'standing', 'walking'], # 走 : 站立->步行
        ['stop', 'walking', 'standing'], # 停 : 步行->站立
        ['drink', "standing", 'caffeinated'], # 喝 : *->精神抖擞
        ['walk', ['caffeinated', 'caffeinated_dithering'], 'caffeinated_running'], # 走 :
        ['relax', 'caffeinated', 'standing'], # 放松 :
    ]

    machine = Machine(states=states, transitions=transitions, initial='standing', ignore_invalid_triggers=True)

    # machine.walk() # Walking now
    # machine.stop() # let's stop for a moment
    machine.drink() # coffee time
    print(machine.state)

a1()

from transitions.extensions.nesting import NestedState
def a2():
    NestedState.separator = '↦' # 配置状态分隔符, 嵌套的状态会自动加上这个符号
    states = [
        'A',  # 状态 A
        'B', # 状态 B
        {
            'name': 'C', # 状态 C
            'children':[
                '1', '2', # 状态 C↦1 C↦2
                {
                    'name': '3', # 状态 C↦3
                    'children': [
                        'a', 'b', 'c' # 状态 C↦3↦a C↦3↦b C↦3↦c
                    ]
                }
            ]
        }
    ]

    transitions = [ # 状态转移表
        ['reset', 'C', 'A'],
        ['reset', 'C↦2', 'C']  # overwriting parent reset
    ]

    # we rely on auto transitions
    machine = Machine(states=states, transitions=transitions, initial='A')
    machine.to_B()  # exit state A, enter state B
    machine.to_C()  # exit B, enter C
    machine.to_C.s3.a()  # enter C↦a; enter C↦3↦a; # 状态为数字, 前面加上 s 字母
    print(machine.state)

# if __name__ == "__main__":
#     a2()