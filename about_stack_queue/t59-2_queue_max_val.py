"""
剑指 Offer 59 - II. 队列的最大值
中等
502
相关企业
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]


限制：

1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5
"""

"""
出队：小于最大值无影响，等于最大值，取下一个最大值
# 分析
入队的时候影响范围为：当前元素到前一个比自己大的值，
核心：实际上就是一个递减的队列，如果后来的值大于以前的max，那么重置这个max递减队列
维护一个递减的max队列
[0,0,0,max,3,4,5,]
[0,0,0,max,3,4,5,max2]
比较过程
3 进来： 3就是max2
4       4就是max2
5       5就是max2
如果进来一个比max大的数
那么pop max， max2
max列表只剩下一个新进来的max
"""

class MaxQueue:

    def __init__(self):
        self.stage_max_list = []
        self.max_list = []
        self.val_list = []


    def max_value(self) -> int:
        if not self.max_list:
            return -1
        return self.max_list[-1]

    def push_back(self, value: int) -> None:
        self.val_list.append(value)
        max_val = max(self.max_value(), value)
        self.max_list.append(max_val)


    def pop_front(self) -> int:
        if not self.val_list:
            return -1
        self.max_list.pop(0)
        return self.val_list.pop(0)



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()