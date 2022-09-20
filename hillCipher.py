import string 
import numpy as np 

def hillEncrypt(A_mat : list, n : int, message: list, intercept : list) -> str:
    A_mat = np.array(A_mat).reshape(n,n)
    message, intercept = np.array(message).reshape(n,1), np.array(intercept).reshape(n,1)
    func = np.add(A_mat @ message, intercept).flatten().tolist()
    letters, numbers = string.ascii_letters[:26], range(26)
    dictionary = {numbers[i]:letters[i] for i in range(26)}
    print(np.array(func) % 26)
    func_str = [ dictionary[elem % 26] for elem in func ]
    return ''.join(func_str)

def hillDecrypt(A_mat : list, n : int, cipher : list, intercept : list) -> str:
    inv_A = np.linalg.inv(np.array(A_mat).reshape(n,n))
    print(type(np.array(A_mat)))
    print(inv_A)
    print(type(inv_A))
    inv_func = (inv_A @ (np.array(cipher).reshape(n,1)- np.array(intercept).reshape(n,1))).flatten().tolist()
    print(inv_func)
    letters, numbers = string.ascii_letters[:26], range(26)
    dictionary = {numbers[i]:letters[i] for i in range(26)}
    fun_string = [ dictionary[val % 26] for val in inv_func]
    return ''.join(fun_string)

A_mat = [ 4, 18, 21, 24, 3, 7, 11, 0, 3 ]
n = 3
message = [ 18, 4, 4 ]
intercept = [ 11, 0, 20 ]

print(hillEncrypt(A_mat,n,message,intercept))

print('=====================================')
cipher = [5,4,22]
print(hillDecrypt(A_mat,n,cipher,intercept))