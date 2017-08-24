import os
#import string
import re
class bag_of_words:                  #using class called bag_ofwords
    def word_freq(self,s):           #convert string to ditionary using method name word_freq
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        if ''in d:
            del d['']
        print(d)
        return d
    
    def split_word(self,sett):       #split_word is to split into words and removing punctuation
        sett=sett.lower()           # to convert uppercase letters to lowercase
        sett=re.sub('[@#$%^&*(){}?|/\:"-+=!~`;,.<>]', '', sett) # to delete special characters
        sett=sett.replace("\n"," ").replace("\t"," ")   #to replace \n and tab space with space
        sett=sett.split(" ")            
        #sett=[punct.strip(string.punctuation)for punct in sett]
        return sett

    def mod(self,d):                 # used mod method to get the n denominator
        n=0
        for i in d:
            n+=d[i]*d[i]
        n=n**0.5
        return (n)

    def vector(self,dict1,dict2):    # used vector method to get the values of numerator
        temp=0
        for i in dict1:
            for j in dict2:
                if i==j:
                    temp+=dict1[i]*dict2[j]
        return temp

    def plagiarism(self,path_dir):  # this method is used to call the other methods to get the plagiarism percent
        l=[i for i in os.listdir(path_dir) if i.endswith('.txt')]
        os.chdir(path_dir)
        x1=[]
        for file1 in l:
            T1=open(file1,'r')
            f1=str(T1.read())
            f1=F.split_word(f1)
            x2=[]
            for file2 in l:
                T2=open(file2,'r')
                f2=str(T2.read())
                f2=F.split_word(f2)
                dict1=F.word_freq(f1)
                dict2=F.word_freq(f2)
                """calculations"""
                f1mod=F.mod(dict1)
                f2mod=F.mod(dict2)
                n=F.vector(dict1,dict2)
                plag_percent=(n)*100/((f1mod)*(f2mod))
                plag_percent=round(plag_percent,2)
                if(file1 == file2):
                    plag_percent = None
                x2.append(plag_percent)
                #print(x2)
            x1.append(x2)
            #print(x1)
        return x1
    
    def input1(self):
        path_dir=input("enter the path directory:/n")
        x=F.plagiarism(path_dir)
        l=[i for i in os.listdir(path_dir) if i.endswith('.txt')]
        #print(l)
        os.chdir(path_dir)
        k=0
        for i in x:
            print("F/N:",l[k],":","plagiarism check with all files")
            print (i)
            print(" ")
            k=k+1

            
F=bag_of_words()
F.input1()


    
    
    
    
