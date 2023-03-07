import numpy as np

a = np.array([[2,3], [5,2]])
print(a)

d = np.array([2,3,4,5,6])
print(d)

print(d.shape)
print("a.shape>> ", a.shape)

e = np.array([[1,2,3,4], [5,6,7,8]])
print("e.shape>> ", e.shape)
print("e.dtype>> ", e.dtype)
print(np.zeros((2,10)))
print(np.ones((2,10)))
print(np.arange(2,10)) # 2 이상 10 미만의 원소로 이루어진 1차원배열

a = np.ones((2,3))
print(a , a.shape)
b = np.transpose(a) # 행과 열이 바뀜
print(b , b.shape)

arr1 = np.array([[1,2,3],[6,7,8]])
arr2 = np.array([[12,22,33],[16,17,18]])
#배열 덧샘 ==> 같은 자리의 원소끼리 덧셈
print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)

###################
print(">>>>>>>>>>>>")
d = np.array([[1,2,3,4,5,6],[2,3,4,5,6,7],[5,6,7,8,9,9]])
d_list=[[1,2,3,4,5],[2,3,4,5,6,7],[5,6,7,8,9,9]]
print(d.shape)
print(d_list)
print(d_list[:2])
# d_list[:2] = 0 ==> error
d[:2] = 0
print(d)
print(type(d_list))
print(type(d))
print('-------------------')
print(np.arange(10)) # [0 1 2 3 4 5 6 7 8 9]

arr4 = np.arange(10)+10 # 각 원소에 10 더해짐 
print(arr4)
print(arr4[:5])
print(arr4[-3:])
print('-------------------')
print(arr1)
print(arr1[1,2])
print(arr1[:,2])
print(arr1[1,:])
print(arr1[1])
