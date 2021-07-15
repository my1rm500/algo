num = 3
dic = {0:0, 1:1, 2:1}
def fibo(num) :
    if num in dic:
        return dic[num]
    else :
        return fibo(num-1)+fibo(num-2)

print(fibo(num))
