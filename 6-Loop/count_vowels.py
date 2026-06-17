str = input("enter the string: ")
count1= 0
count2=0

for ch in str:
    if ch in "aeiouAEIOU" :
        count1+=1
    else:
        count2+=1    
print("totel vowels :", count1)
print("total consonant :", count2)