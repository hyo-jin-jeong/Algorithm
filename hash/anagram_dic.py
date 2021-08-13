import sys
sys.stdin = open("/Users/hyojinjeong/Algorithm/hash/anagram.txt", "r")
first_word = input()
second_word = input()
dic = dict()

for s in first_word:
    dic[s] = dic.get(s, 0) + 1
for s in second_word:
    dic[s] = dic.get(s, 0) - 1
for value in dic.values():
    if value != 0 :
        print("No")
        break
else:
    print("Yes") 