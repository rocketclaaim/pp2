#ex1
grams = int(input())
def convert_ounces(grams):
    ounces = grams * 28.3495231
    return ounces

result = convert_ounces(grams)
print(result)

#ex2
F=int(input())
def ggg(F):
    C=(5 / 9) * (F – 32)
    return C
result = ggg(F)
print(result)

#ex3
def solve(num_heads, num_legs):
    rab = (num_legs-(2 * num_heads))/2
    chic = num_heads - rab
    return rab, chic

numheads = 35
numlegs = 94

solutions = solve(numheads, numlegs)
print(solutions)

#ex4
def filter_prime(numbers):
    def is_prime(n):
        if n <= 1 or n==2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    return [n for n in numbers if is_prime(n)]

a = [int(x) for x in input().split()]
# a = list(map(int, input().split()))
print(filter_prime(a))


#ex5
def permutation(word, permu=''):
    if len(word)== 0:
        print(permu)
    for i in range(len(word)):
        newpermu = permu + word[i]
        newword = word[0:i] + word[i+1:]

        permutation(newword, newpermu)

s=str(input())
permutation(s)

#ex6
def reversed(s):
    a=list(s.split(" "))
    a.reverse()
    print(' '.join(a))
s="We are ready"
reversed(s)

#ex7
def has_33(nums, cnt = 0):
    for i in range(len(nums)- 1):
        if nums[i] == nums[i+1]:
            cnt += 1 
    if cnt > 0:
        return True
    else:
        return False



a = list(map(int, input().split()))
print(has_33(a))

#ex8
def spy_game(nums, cnt = 0):
    for i in range(len(nums)- 1):
        if nums[i] == 0 and nums[i] == nums[i+1]:
            if nums[i+2] == 7:
                cnt += 1 
    if cnt > 0:
        return True
    else:
        return False



a = list(map(int, input().split()))
print(spy_game(a))

#ex9
import math
def volume(rad):
    return 4/3 * 3.14*math.pow(rad, 3)

print(round(volume(int(input()))))

#ex10
def unique(num):
    b = []
    for i in num:
        if i not in b:
            b.append(i)
    return b

a = list(map(int, input().split()))
print(unique(a))

#ex11
def palindrome(a, cnt=0):
    for i in range(len(a)):
        if a[i] == a[-i]:
            cnt += 1
    if cnt >= len(a)/2:
        return True
    else:
        return False

print(palindrome(str(input())))

#ex12
def histogram(a):
    for i in range(len(a)):
        print("*" * a[i])


a=list(map(int, input().split()))
print(histogram(a))

#ex13
import random
def nice_try(s):
    if s < b:
        print('Your guess is too low.\nTake a guess.')
        
    elif s > b:
        print('Your guess is too big.\nTake a guess.')
    else:
        if s == b:
            print('Good job, '+ a+'! You guessed my number in 3 guesses!')
                
                      
a=str(input("Hello! What is your name?"))
print('Well, '+ a +', I am thinking of a number between 1 and 20. \nTake a guess')
b = random.randint(0, 20)
i = 0
while (i<=3):
    kk = int(input())
    nice_try(kk)








