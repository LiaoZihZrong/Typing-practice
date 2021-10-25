# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 19:31:20 2021

@author: liaozz
"""
import csv
import time
import random
#英打練習
#抽取n個字
#讀取英文檔
#隨機顯示
#輸入一樣才能跳到下一個
#顯示時間
#結束後3

file_name="500eng.csv"
eng_500=[]
with open(file_name) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        eng_500.append(row)

random.shuffle(eng_500)
#print(eng_500[1])
#print()

n=input("請輸入要寫的單字數量:")
start=time.time()
for i in range(int(n)):
    str_eng= "".join(eng_500[i])
    print(str_eng)
    split_str=str_eng.split("@",2)
    split_word0=split_str[0]
    split_word1=split_str[1]
    print("中文意思:",split_word1)
    print("英文意思:",split_word0)
    print("請輸入:")
    input_eng=input()
    while input_eng!=split_word0:
        input_eng=input("錯誤，請重新輸入:")
        
    print("-------正確!-------")
end=time.time()   
print("=======================")
print("=======程式結束!=======")
print("共耗時:", int(end-start),"秒")   
print("=======================")
input_eng=input("輸入enter，結束程式")
