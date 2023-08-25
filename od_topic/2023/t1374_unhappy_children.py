"""
题目描述
游乐场里增加了一批摇摇车，非常受小朋友欢迎，但是每辆摇摇车同时只能有一个小朋友使用，
如果没有空余的摇摇车，需要排队等候，或者直接离开，最后没有玩上的小朋友会非常不开心。 请根据今天小朋友的来去情况，统计不开心的小朋友数量。

摇摇车数量为
N，范围是:
1≤N<10:
每个小朋友都对应一个编码，编码是不重复的数字，今天小朋友的来去情况，可以使用编码表示为:
1 1 2 3 2 3。(若小朋友离去之前有空闲的摇摇车，则代表玩耍后离开:不考虑小朋友多次玩的情况)。小朋友数量

≤100
题目保证所有输入数据无异常且范围满足上述说明
输入描述
第一行: 摇摇车数量 第二行: 小朋友来去情况

输出描述
返回不开心的小朋友数量

样例
输入

1
1 2 1 2
输出

0
说明

第一行，
1个摇摇车

第二行，
1号来2号来(排队)1号走2号走(1号走后摇摇车已有空闲，所以玩后离开)

输入

1
1 2 2 3 1 3
输出

1
说明

第一行，
1个摇摇车

第二行，
1号来
2号来(排队)
2号走(不开心离开)
3号来(排队)
1号走
3号走(1号走后摇摇车已有空闲，所以玩后离开)
"""

"""
模拟:
一个map存储来去情况，编号为num， 车数量为cap
如果num在map里面，则将num删除，并判断它的状态
如果不在则加入，并且根据是否能玩摇摇车来设置它的状态

注意，list执行pop的时候指明下标，不要使用默认的，因为你自己也不清楚pop的是啥
默认pop(-1)
"""
from collections import deque
#
# def main():
#     car_num = int(input())
#     people_list = list(map(int, input().split()))
#     people_map = {}     # key，编号，val：
#     happy, un_happy = 0, 1  # 状态，0开心，1不开心
#     play_num = 0        # 正在玩的小朋友数目
#     un_happy_num = 0
#     wait_queue = deque()  # 等待队列
#     for people in people_list:
#         if people in people_map:        # 离开
#             state = people_map.pop(people)
#             # 排队过程中离开
#             if state == un_happy:   # 不开心，说明在排队，从排队列表删除
#                 wait_queue.remove(people)
#                 un_happy_num += 1       # 不开心数目 + 1
#                 continue
#             # 玩完了摇摇车离开
#             play_num -= 1       # 注意变化
#             # 排队的继续玩
#             if wait_queue:
#                 people = wait_queue.popleft()
#                 people_map[people] = happy
#                 play_num += 1
#             continue
#         if play_num != car_num: # 有车玩
#             people_map[people] = happy
#             play_num += 1
#             continue
#         # 没车玩就去排队
#         people_map[people] = un_happy  # 默认不开心
#         wait_queue.append(people)
#     return un_happy_num
#
#
# print(main())



def main():
    car_num = int(input())
    people_list = list(map(int, input().split()))
    people_map = {}     # key，编号，val：
    happy, un_happy = 0, 1  # 状态，0开心，1不开心
    play_num = 0        # 正在玩的小朋友数目
    un_happy_num = 0
    wait_list = []  # 等待队列
    for people in people_list:
        if people in people_map:        # 离开
            state = people_map.pop(people)
            # 排队过程中离开
            if state == un_happy:   # 不开心，说明在排队，从排队列表删除
                wait_list.remove(people)
                un_happy_num += 1       # 不开心数目 + 1
                continue
            # 玩完了摇摇车离开
            play_num -= 1       # 注意变化
            # 排队的继续玩
            if wait_list:
                people = wait_list.pop(0)
                people_map[people] = happy
                play_num += 1
            continue
        people_map[people] = un_happy  # 默认不开心
        if play_num != car_num: # 有车玩
            people_map[people] = happy
            play_num += 1
            continue
        # 没车玩就去排队
        wait_list.append(people)
    return un_happy_num


print(main())
