def convert(string):
    alpha_to_num = dict()
    for i in range(65,91):
        alpha_to_num[chr(i)] = i-64
    
    return number

if __name__ == '__main__':
    L = int(input())
    string = input()
    print(convert(string))
    