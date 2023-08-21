"""
题目描述
一个设备由N种类型元器件组成(每种类型元器件只需要一个，类型
type编号从0~N−1),

每个元器件均有可靠性属性
reliability，可靠性越高的器件其价格
price越贵。

而设备的可靠性由组成设备的所有器件中可靠性最低的器件决定。

给定预算
S，购买N种元器件( 每种类型元器件都需要购买一个)，在不超过预算的情况下，请给出能够组成的设备的最大可靠性。

输入描述
S N    //S总的预算，N元器件的种类
total // 元器件的总数，每种型号的元器件可以有多种:

此后有total行具体器件的数据
type reliability price
//type 整数类型，代表元器件的类型编号 从0 ~N−1:
reliabilty 整数类型，代表元器的可靠性:
price整教类型，代表元器件的价格

输出描述
符合预算的设备的最大可靠性，如果预算无法买齐
N种器件，则返回
−1

备注
0≤s,price≤10000000
0≤N≤100
0≤type≤N−1
0≤total≤100000
0≤reliability≤100000
样例
输入

500 3
6
0 80 100
0 90 200
1 50 50
1 70 210
2 50 100
2 60 150
输出

60
说明

预算
500，设备需要
3种元件组成，方案类型
0的第一个(可靠性80),类型
1的第二个(可靠性70),类型
2的第二个(可靠性60),可以使设备的可靠性最大60

输入

100 1
1
0 90 200
输出

-1
说明

组成设备需要
1个元件，但是元件价格大于预算，因此无法组成设备，返回
−1
"""

"""
枚举
"""

def main():
    total_price, type_num = tuple(map(int, input().split()))
    type_map = {}       # 种类信息映射表
    component_num = int(input())
    for _ in range(component_num):
        type1, reliability, price = tuple(map(int, input().split()))
        if type1 not in type_map:
            type_map[type1] = []
        type_map[type1].append({"r": reliability, "price": price})
