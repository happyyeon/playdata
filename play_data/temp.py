def convert(num,b):
    answer = 0
    alpha_to_num = dict()

    for i in range(65,b+55):
        alpha_to_num[chr(i)] = i-55
    
    for i in range(len(num)):
        try:
            answer += int(num[i])*(b**(len(num)-1-i))
        except:
            answer += alpha_to_num[num[i]]*(b**(len(num)-1-i))
    return answer

if __name__ == '__main__':
    N,B = input().split()
    print(convert(N,int(B)))