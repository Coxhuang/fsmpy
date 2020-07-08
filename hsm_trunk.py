#!/usr/bin/python3
# -*- coding:UTF-8 -*-
"""
@description  ： 描述
@Time ： 2020/7/8 11:09 AM
@Auth ： Minhang
@File ： hsm_trunk.py
@IDE  ： PyCharm
"""

from transitions.extensions import HierarchicalMachine as Machine

class Matter(object):
    def __init__(self): self.set_environment()
    def set_environment(self, temp=0, pressure=101.325):
        self.temp = temp
        self.pressure = pressure
    def print_temperature(self): print("Current temperature is %d degrees celsius." % self.temp)
    def print_pressure(self): print("Current pressure is %.2f kPa." % self.pressure)

states = [ # 状态
    "idle", # 状态1 : 空闲
    "error", # 状态2 : 异常
    "locked", # 状态3 : 锁定
    {
        "name": "work", # 状态4 : 工作
        "initial":"targetset", # 默认状态 : 状态4-1 : 工作->目的地已设定
        "children": [
            "targetset", # 状态4-1 : 工作->目的地已设定
            "driving", # 状态4-2 : 工作->行驶中
            "stop", # 状态4-3 : 工作->停止
            "calibrate", # 状态4-4 : 工作->对位
            "arrived", # 状态4-5 : 工作->到达
        ]
    }
]

def after_advance():
    print("I am in state B now!")

transitions = [ # 状态转移表
    ["settarget", "idle", "work"], # 空闲 -> 工作
    ["arrived", "work", "idle"], # 工作 -> 空闲
    ["cancel", "work", "idle"], # 工作 -> 空闲
    ["error", "work", "error"], # 工作 -> 异常
    ["recover", "error", "work"], # 异常 -> 工作
    ["lock", "work", "locked"], # 工作 -> 锁定
    ["resume", "locked", "work"], # 锁定 -> 工作

    ["driving", "work_targetset", "work_driving"], # 工作->目的地已设定 -> 工作->行驶中
    ["stop", "work_driving", "work_stop"], # 工作->行驶中 -> 工作->停止
    ["calibrate", "work_stop", "work_calibrate"], # 工作->停止 -> 工作->对位
    ["arriving", "work_calibrate", "work_arrived"], # 工作->对位 -> 工作->到达
    ["arriving", "work_stop", "work_arrived"], # 工作->停止 -> 工作->到达
]

l = Matter()

machine = Machine(
    states=states,
    transitions=transitions,
    initial='idle',
    ignore_invalid_triggers=True,
    model=l,
)

print(machine.state)
machine.settarget()
print(machine.state)

# while True:
#     print("当前状态: {}".format(machine.state))
#     in_str = input("设置: ")
#     eval("machine.{}()".format(in_str))

