'''选择排序： 10  3  5  2
  选择排序的特点：每一次从待排序的数据元素中选出最小（最大）的一个元素，存放到最开始的位置，直到全部排完'''

dict = {"a": 4, "b": 1, "c": 5, "d": 6}
list1 = []
def mySort(dict):
    for value in dict.values():
        list1.append(value)
    return list1

def selectSort(alist):
    for i in range(len(alist)-1, 0, -1):  # len(alist)-1, 0, -1分别表示开始，结束，步长；反过来进行遍历
        maxone = 0
        # print(i)
        for j in range(1, i + 1):
            # print(j)
            if alist[j] > alist[maxone]:
                maxone = j
            temp = alist[i]
            alist[i] = alist[maxone]
            alist[maxone] = temp
            # print(alist)
            # print('\n')
    return alist
list2 = mySort(dict)
print(list2)
reslut = selectSort(list2)
print(reslut)
print('\n')



'''
## 2.冒泡排序
1，2，4，2，1，5，7，3
冒泡法：
第一趟：相邻两个数进行比较，大的往下沉，最后一个元素是最大值
第二趟：相邻两个数进行比较，大的往下沉，最后一个元素不需要进行比较'''

def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):  # 从最后一个元素开始遍历,步长为-1
        for i in range(passnum):  # 重头开始遍历，相邻的进行比较，较大的不断下沉
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
    return alist
alist = [22, 33, 44, 26, 93, 31, 2]
print(alist)
print(bubbleSort(alist))
