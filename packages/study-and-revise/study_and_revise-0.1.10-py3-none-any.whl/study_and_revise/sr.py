# 如需保存为utf-8文件,必须指定编码为utf-8

import sys
import json
import datetime
import os
from os.path import sep
from pathlib import Path

import pytz

USER_HOME = str(Path.home())
STUDY_FILE_PATH = USER_HOME + sep + "study.json"


def read_json_file(file_name):
    # 读取已经有的数据
    if not os.path.exists(file_name):
        return {}
    f = open(file_name, encoding="utf-8")
    contents = f.read()
    # print(contents)
    f.close()
    all_study_contents = json.loads(contents)
    return all_study_contents


def record(name, position):
    # 获取北京时间并格式化输出
    utc_tz = pytz.timezone('Asia/Shanghai')
    now = datetime.datetime.now(tz=utc_tz)

    one_minute = datetime.timedelta(minutes=1)
    one_hour = datetime.timedelta(hours=1)
    one_day = datetime.timedelta(days=1)

    # print (n_days.strftime('%Y-%m-%d %H:%M:%S'))

    # 读取已经有的数据
    all_study_content = read_json_file(STUDY_FILE_PATH)

    id = now.strftime("%Y_%m_%d_%H_%M_%S")

    study_time = now.strftime("%Y-%m-%d %H:%M:%S")
    # 5分钟后 20分钟后 1小时后 9小时后
    review_time = [now + 5 * one_minute, now + 20 * one_minute, now + one_hour, now + 9 * one_hour]
    # 取斐波那契数列的奇数项 1,1,2,3,5,8
    a = 1
    b = 1
    while a < 36500:
        review_time.append(now + a * one_day)
        a = a + b
        b = a + b
    # print(review_time[-1])

    # 将datetime类型转为字符串类型
    for index, value in enumerate(review_time):  # 遍历时获取索引和项
        review_time[index] = value.strftime("%Y-%m-%d %H:%M:%S")

    # 构造一次学习的信息的字典
    one_item = {
        "name": name,
        "position": position,
        "study_time": study_time,
        "review_time": review_time
    }
    all_study_content[id] = one_item
    # 获取改文件所在目录的路径
    this_dir_path = os.path.dirname(os.path.realpath(__file__)) + os.sep
    f = open(STUDY_FILE_PATH, "w", encoding="utf-8")
    # 以标准格式缩进4空格写入json文件
    f.write(json.dumps(all_study_content, indent=4, ensure_ascii=False))
    f.close()


def cmp(t1str, t2str):
    t1 = datetime.datetime.strptime(t1str, "%Y-%m-%d %H:%M:%S")
    t2 = datetime.datetime.strptime(t2str, "%Y-%m-%d %H:%M:%S")
    return t1 < t2


def get_today_review():
    all_study_content = read_json_file(STUDY_FILE_PATH)

    result = []
    for key in all_study_content:
        one_study_info = all_study_content[key]
        review_time_tmp = one_study_info["review_time"]

        utc_tz = pytz.timezone('Asia/Shanghai')
        now = datetime.datetime.now(tz=utc_tz)
        now_str = now.strftime("%Y-%m-%d")

        for t in review_time_tmp:
            if now_str == t.split()[0]:
                tmp_couple = (one_study_info["name"], one_study_info["position"], t)
                # 构造一个元组数组
                result.append(tmp_couple)
    # print(result)
    # 将元组数组按升序排序
    # 用冒泡排序
    for j in range(len(result)):
        for i in range(len(result) - j - 1):
            if not cmp(result[i][2], result[i + 1][2]):
                # print(cmp(result[i][2],result[i+1][2]))
                # print(result[i][2],result[i+1][2])
                tmp = result[i]
                result[i] = result[i + 1]
                result[i + 1] = tmp

    # print
    for item in result:
        print(item[0], end="")
        print("\t" + item[1], end="")
        print("\t" + item[2], end="")
        print()


def main():
    if len(sys.argv) == 3:
        name = sys.argv[1]
        position = sys.argv[2]
        print(name, position)
        record(name, position)
        print("Done")
    elif len(sys.argv) == 1:
        get_today_review()
    else:
        print("XX")


if __name__ == "__main__":
    main()
