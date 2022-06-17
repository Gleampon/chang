from multiprocessing import Process


source_dict = {'key0': 'a', 'key1': 'b', 'key2': {'inner_key0': 'c', 'inner_key1': 'd'}}
update_dict = {'key1': 'x', 'key2': {'inner_key0': 'y'}}


def merge_dict(source_dict, update_dict):  # 1.合并dict
    for i in source_dict:
        if i in update_dict:
            if type(source_dict[i]) == dict:
                source_dict[i].update(update_dict[i])
            else:
                source_dict[i] = update_dict[i]

    return source_dict


dicts = {"1": [""], "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
         "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"],}


def combination(strs):  # 2. 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
    b = []
    for i in str(strs):
        if i not in dicts:
            return "请传2-9范围内的数据"
    result = dicts[str(strs)[0]]
    count = 0
    for k in range(0, len(strs)-1):
        count += 1
        for i in result:
            b.extend([i+j for j in dicts[str(strs)[count]]])
        result = b
        b = []
    return result


def leak():  # 3.内存泄漏
    count = 0
    while True:
        count += 1
        print(count)
        t = Process(target=leak)

        t.start()


if __name__ == "__main__":
    # 慎用
    # 内存泄漏，是指程序中己动态分配的堆内存由于某种原因程序未释放或无法释放，造成系统内存的浪费，导致程序运行速度减慢甚至系统崩溃等严重后果
    # 有对象一直循环引用，产生了堆积，使得JVM不能回收
    # 内存泄漏是一直向内存中申请空间并使用，导致内存被占满，导致系统崩溃，
    # leak()

    # 合并dict
    result = merge_dict(source_dict, update_dict)
    print(result)

    # 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
    data = combination("2345")
    print(data)

    # result = {
    # 'key0': 'a',
    # 'key1': 'x', # overridden by update_dict
    # 'key2': {
    # 'inner_key0': 'y', # overridden by update_dict
    # 'inner_key1': 'd'
    # }
    # }
