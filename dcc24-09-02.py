'''
You are given an unsorted array of integers and a positive integer K. 
Your task is to find the Kth largest element in the array. 
The Kth largest element is the element that would appear in the Kth position if the array were sorted in descending order.
You need to implement a function that returns this Kth largest element without explicitly sorting the entire array.
'''
a = [3, 2, 1, 5, 6, 4]
k = 2
def KthLargest(a,k):
    for i in range(k-1):
        j = a.index(max(a))
        a.pop(j)
    return max(a)
n = KthLargest(a,k)
print(n)
