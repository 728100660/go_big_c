"""
文件目录大小
题目描述
一个文件目录的数据格式为: 目录id，本目录中文件大小，(子目录id列表)。

其中目录id全局唯一，取值范围[1,200],本目录中文件大小范围[1,1000],子目录
id列表个数[0,10]例如 :
1 20 (2,3)
表示目录1中文件总大小是20，有两人子目录，id分别是2和3

现在输入一个文件系统中所有目录信息，以及待查询的目录
id ，返回这个目录和及该目录所有子目录的大小之和。

输入描述
第一行为两个数字 M, N，分别表示目录的个数和待查询的目录id,

1≤M≤100
1≤N≤200
接下来M行，每行为1个目录的数据:

目录id 本目录中文件大小(子目录id列表)
子目录列表中的子目录
id以逗号分隔。

输出描述
待查询目录及其子目录的大小之和。

样例
输入

3 1
3 15 ()
1 20 (2)
2 10 (3)
输出

45
说明

目录
1大小为
20，包含一个子目录
2(大小为10)，子目录
2包含一个子目录
3(大小为15)，总的大小为
20+10+15=45

输入

4 2
4 20 ()
5 30 ()
2 10 (4,5)
1 40 ()
输出

60
说明

目录2包含2个子目录4和
5，总的大小为
10+20+30=60
"""

"""
广度优先遍历
"""


def main():
    m, target = map(int, input().split())
    children = {}
    cap = {}
    for _ in range(m):
        fa_id, fa_cap, ch_str = input().split(" ")
        children[fa_id] = []
        cap[fa_id] = int(fa_cap)
        if len(ch_str) > 2:
            children[fa_id].extend(ch_str[1:-1].split(","))

    stack = [str(target)]
    total_size = 0
    while len(stack) > 0:
        id = stack.pop()
        if cap.get(id) is None:
            continue
        total_size += cap.get(id)
        stack.extend(children.get(id))
    return total_size


print(main())

#
#
# def main():
#     dir_num, target_id = map(int, input().split())
#     cap = {}
#     children = {}
#     for _ in range(dir_num):
#         dir_id, size, sub_dirs = input().split(" ")
#         dir_id = int(dir_id)
#         size = int(size)
#         cap[dir_id] = size
#         children[dir_id] = []
#         if len(sub_dirs) > 2:
#             children[dir_id].extend(list(map(int, sub_dirs[1:-1].split(","))))
#
#     stack = [target_id]
#     total_size = 0
#     while len(stack) > 0:
#         dir_id = stack.pop()
#         if cap.get(dir_id) is None:
#             continue
#         total_size += cap.get(dir_id)
#         stack.extend(children.get(dir_id))
#     return total_size
#
#
# print(main())





# def main():
#     dir_num, target_id = map(int, input().split())
#     id_info_map = {}    # 目录id映射
#     for _ in range(dir_num):
#         dir_id, size, sub_dirs = input().split(" ")
#         dir_id = int(dir_id)
#         size = int(size)
#         if len(sub_dirs) > 2:
#             sub_dirs = list(map(int, sub_dirs[1:-1].split(",")))
#         else:
#             sub_dirs = []
#         id_info_map[dir_id] = (dir_id, size, sub_dirs)
#
#     my_queue = [target_id]
#     total_size = 0
#     while len(my_queue) > 0:
#         dir_id = my_queue.pop()
#         dir_info = id_info_map.get(dir_id)
#         if not dir_info:
#             continue
#         total_size += dir_info[1]
#         my_queue.extend(dir_info[2])
#     return total_size
#
#
# print(main())


# def main():
#     dir_num, target_id = tuple(map(int, input().split(" ")))
#     id_info_map = {}    # 目录id映射
#     for _ in range(dir_num):
#         dir_id, size, sub_dirs = input().split(" ")
#         dir_id = int(dir_id)
#         size = int(size)
#         if sub_dirs == "()":
#             sub_dirs = []
#         else:
#             sub_dirs = list(map(int, sub_dirs[1:-1].split(",")))
#         id_info_map[dir_id] = (dir_id, size, sub_dirs)
#
#     my_queue = [target_id]
#     total_size = 0
#     while my_queue:
#         dir_id = my_queue.pop()
#         dir_info = id_info_map.get(dir_id)
#         if not dir_info:
#             continue
#         total_size += dir_info[1]
#         my_queue.extend(dir_info[2])
#     return total_size
#
#
# print(main())
