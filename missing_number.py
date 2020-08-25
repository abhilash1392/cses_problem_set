# Problem Statement
'''
You are given all numbers between 1,2,…,n except one. 
Your task is to find the missing number.
'''
def missing_number(n,array):
    arr1=list(range(1,n+1))


    print(int(sum(arr1)-sum(array)))


n=int(input())

array=list(map(int,input().split(' ')))

missing_number(n,array)





