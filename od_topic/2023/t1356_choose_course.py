"""
现有两门选修课，每门选修课都有一部分学生选修，每个学生都有选修课的成绩，需要你找出同时选修了两门选修课的学生，
先按照班级进行划分，班级编号小的先输出，每个班级按照两门选修课成绩和的降序排序，成绩相同时按照学生的学号升序排序。

输入描述

第一行为第一门选修课学生的成绩



第二行为第二门选修课学生的成绩，每行数据中学生之间以英文分号分隔，每个学生的学号和成绩以英文逗号分隔，
学生学号的格式为8位数字(2位院系编号+入学年份后2位+院系内部1位专业编号+所在班级3位学号)，学生成绩的取值范围为[0,100]之间的整数，
两门选修课选修学生数的取值范围为[1-2000]之间的整数。

输出描述

同时选修了两门选修课的学生的学号，如果没有同时选修两门选修课的学生输出NULL，否则，先按照班级划分，班级编号小的先输出，
每个班级先输出班级编号(学号前五位)，然后另起一行输出这个班级同时选修两门选修课的学生学号，
学号按照要求排序(按照两门选修课成绩和的降序，成绩和相同时按照学号升序)，学生之间以英文分号分隔。



示例1

输入:

01202021,75;01201033,95;01202008,80;01203006,90;01203088,100

01202008,70;01203088,85;01202111,80;01202021,75;01201100,88

输出:

01202

01202008;01202021

01203

01203088

说明:

同时选修了两门选修课的学生01202021、01202008、01203088，
这三个学生两门选修课的成绩和分别为150、150、185, 01202021、01202008属于01202班的学生，按照成绩和降序，
成绩相同时按学号升序输出的结果为01202008:01202021,01203088属于01203班的学生，按照成绩和降序，
成绩相同时按学号升序输出的结果为01203088，01202的班级编号小于01203的班级编号，需要先输出。



示例2

输入:

01201022,75;01202033,95;01202018,80;01203006,90;01202066,100

01202008,70;01203102,85;01202111,80;01201021,75;01201100,88

输出:

NULL

说明:

没有同时选修了两门选修课的学生，输出NULL。
"""
def get_num_score_map(course_list): # 学号分数映射表
    num_score_map = {}
    for info_str in course_list:
        tmp_list_i = info_str.split(",")
        st_num_i = tmp_list_i[0]
        score_i = int(tmp_list_i[1])
        num_score_map[st_num_i] = score_i
    return num_score_map
course_1_list = input().split(";")
num_score_map_1 = get_num_score_map(course_1_list)
course_2_list = input().split(";")
num_score_map_2 = get_num_score_map(course_2_list)

class_info = {}     # {class_num: [(st_num, score), (), ()]}
for st_num, score in num_score_map_1.items():
    if st_num not in num_score_map_2:
        continue
    class_num = st_num[:5]
    total_score = score + num_score_map_2[st_num]
    class_info.setdefault(class_num, []).append((st_num, total_score))

def sort_func(x):
    return -x[1], x[0]

sorted_class_key = sorted(class_info.keys())
if not class_info:
    print("NULL")
for class_num in sorted_class_key:
    print(class_num)
    st_score_list = class_info[class_num]
    tmp_list = sorted(st_score_list, key=sort_func)
    tmp_list = [tmp[0] for tmp in tmp_list]
    print(";".join(tmp_list))

