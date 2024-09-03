'''
You are given an unsorted array of integers.
Your task is to find the median of the array. 
The median is the middle value in an ordered list of numbers. 
If the list has an even number of elements, the median is the average of the two middle numbers.
'''
a = [3, 2, 1, 4, 5]
def Median(a):
    l = len(a)
    for i in range(l//2-1):
        j = a.index(min(a))
        a.pop(j)
    if l%2 == 0:
        m = min(a)
        a.pop(a.index(min(a)))
        m += min(a)
        return m/2
    else:
        a.pop(a.index(min(a)))
        return min(a)
n = Median(a)
print(n)