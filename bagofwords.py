'''bag of words'''
import glob
import os
import string

def magnitude(dic):
	k=0
	for x in dic:
		k+=dic[x]*dic[x]
	return k

def wordfreq(l1):
	dic={}
	for i in range(len(l1)):
		c=0
		for j in range(len(l1)):
			if(l1[i]==l1[j]):
				c+=1
		dic[l1[i]]=c
	if '' in dic:
		del dic['']
	return dic

def fileset(f):
	f=f.lower()
	f=f.replace('\n',' ')
	f=f.split(' ')
	f=[word.strip(string.punctuation)for word in f]
	
	return f

def plag(path):
	
	lst=[p for p in os.listdir(path) if p.endswith('.txt')]

	matrix=[]
	
	# lsttemp=[0]
	# lsttemp.extend(lst)
	# matrix.append(lsttemp)
	
	for filenamemain in lst:
	
		file1=open(filenamemain, 'r')
		f1=str(file1.read())
		f1=fileset(f1)

		matrix2=[]

		for filename in lst:	
		
			file2=open(filename, 'r')
			f2=str(file2.read())
			f2=fileset(f2)

			dic1=wordfreq(f1)
			dic2=wordfreq(f2)

			#cosine calculation starts

			s=0

			for x in dic1:
				for y in dic2:
					if(x==y):
						s+=dic1[x]*dic2[y]

			f1sum=magnitude(dic1)
			f2sum=magnitude(dic2)

			percent=(s*100.0)/((f1sum**0.5)*(f2sum**0.5))
			percent=round(percent,2)

			matrix2.append(percent)
		
		matrix.append(matrix2)

		# lsttemp2=[filename]
		# lsttemp2.extend(matrix2)
		# matrix.append(lsttemp2)
		
	return (matrix)
path=raw_input('enter path to check plagiarism for .txt files:\n')
final = (plag(path))
for i in final:
	print (i)