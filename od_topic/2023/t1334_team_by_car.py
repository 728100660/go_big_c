"""
代表团坐车
题目描述
某组织举行会议，来了多个代表团同时到达，接待处只有一辆汽车，可以同时接待多个代表团，为了提高车辆利用率，
请帮接待员计算可以坐满车的接待方案，输出方案数量。

约束:

一个团只能上一辆车，并目代表团人数(代表团数量小于30，每个代表团人数小于30)
小于汽车容量(汽车容量小于100)
需要将车辆坐满
输入描述
第一行 代表团人数，英文逗号隔开，代表团数量小于
30，每个代表团人数小于30。

第二行 汽车载客量，汽车容量小于100

输出描述
坐满汽车的方案数量 如果无解输出
0

样例
输入

5,4,2,3,4,6
10
输出

4
说明

解释以下几种方法都可以坐满车，所有，优先接待输出为
4

[2,3,5]

[2,4,4]

[2,3,5]

[2,4,4]
"""


"""
感觉像动态规划
dp[i][j]   表示选择的旅游团下标为i，车内容量为j 的方案数目
dp[i][j] = dp[i-1]
dp[i] 表示汽车容量为i的时候的方案数

dp[i] = dp[i - cur_val] + 1     # cur_val为当前旅游团人数
"""

def main():
    team_num_list = list(map(int, input().split(",")))
    team_num_list.sort()
    total_cap = int(input())

    dp = [0] * total_cap
    for cap in range(total_cap):
        for cur_team in team_num_list:
            if cur_team > cap:
                continue
            if cap == cur_team:
                dp[cap] += 1
                continue
            if dp[cap - cur_team] != 0:     # 当前容量有响应路径走过来
                dp[cap] = dp[cap - cur_team] + 1
    return dp[total_cap - 1]


print(main())
