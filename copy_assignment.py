# create file A.txt , copy data from A.txt to B.txt . Rename A.txt to A_bkp.txt

import os

print(os.getcwd())
os.chdir("D:\\LearnBay_Devops\\Python\\Learnbay_python_workspace\\python_programs\\file_handling")
print(os.getcwd())

text = "hi this is write file example \n this is second line \n India \n Nepal"
fp = open("A.txt" ,'w')
fp.write(text)
print("we have finished writing in file")

fp = open("A.txt" , 'r')
print(fp.read())
fp.close

with open('B.txt','w') as fp1:    
    with open('A.txt','r') as fp2:       
        fp1.write(fp2.read())
        fp2.close()
        fp1.close()
print("file B content is as follows \n",open('B.txt','r').read())


old_file = "D:\\LearnBay_Devops\\Python\\Learnbay_python_workspace\\python_programs\\file_handling\\A.txt"
new_file = "D:\\LearnBay_Devops\\Python\\Learnbay_python_workspace\\python_programs\\file_handling\\A_Bkp.txt"
os.rename(old_file,new_file)

