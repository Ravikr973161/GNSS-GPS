# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 15:26:24 2019

@author: RAVI K R ravikr.973161@gmail.com
"""


import math
import glob
par=[]
read_line=0
flag=0
NO_satlites=list()
time=list()
z=list()
sat=list()
f1=list()

#print("Enter the file Name")
#file=input()
print("Available source files in the current directory")
File=glob.glob('*.*o')
print(File)
for ff in File:
    fh=open(ff,"r")
    def Time():
         time.append(line[1:26])  
         
         NO_satlites.append(line[30:32])
         return  NO_satlites[-1]
     
        
    def read1(read_line):
        f1.append(line[0:14])      
        f1.append(line[17:30])
        f1.append(line[33:46])  
        f1.append(line[49:62])   
        f1.append(line[65:78])    
        
            
            
             
        
    m=0
    c=0
    flag2=0
    flag9=0
    flag8=0
    temp=0
    for line in fh:    
        if m==0:
            if flag2==1:
                n=line[1:3]
                flag2=0                      
            if flag==1 and line[1:3]==n:
                z=Time() 
                sat.append(line[32:35])
                sat.append(line[35:38])
                sat.append(line[38:41])
                sat.append(line[41:44])
                sat.append(line[44:47])
                sat.append(line[47:50])
                sat.append(line[50:53])
                sat.append(line[53:56])
                sat.append(line[56:59])
                sat.append(line[59:62])
                sat.append(line[62:65])
                sat.append(line[65:68])
                c= int(z)//12
                if int(z)%12==0:
                    c-=1
                #print(c)
                if(int(z)>12 and int(z)<=24):
                    m=(int(z)*read_line)+1
                elif(int(z)>24):
                    m=(int(z)*read_line)+2  
                                    
                else:
                    m=int(z)*read_line              
            else:
                line=line.split()
                for data in line:
                    if data=='2.11':
                        print("Valid version:- 2.11")
                    if data=='TYPES':
                        par.append(line) 
                        No_parm=int(par[0][0])
                        read=No_parm/5
                        read_line=math.ceil(read)
                        temp=read_line
                    if data=="HEADER":
                        flag=1 
                        flag2=1
                        
                    
        else:
            if c==0:
                read1(read_line)
            if c!=0:             
                sat.append(line[32:35])
                sat.append(line[35:38])
                sat.append(line[38:41])
                sat.append(line[41:44])
                sat.append(line[44:47])
                sat.append(line[47:50])
                sat.append(line[50:53])
                sat.append(line[53:56])
                sat.append(line[56:59])
                sat.append(line[59:62])
                sat.append(line[62:65])
                sat.append(line[65:68])
                c-=1
            
            m-=1
            
    #removing emty satname from the list             
    newsate=[]
    sum=0       
    for i in sat:
        if i!='' :
            if i!='\n':
                newsate.append(i)
    
    
    
    
    #extracting the parameters
    Read=read_line*5
    fvn=[f1[i*Read:(i+1)*Read] for i in range((len(f1)+Read-1)//Read)]
    
    
    
    
    
    
    #Defult all parametrs printing to a file
    
    
    output=open(ff+".txt","w+")
    
    for pr in par:
       output.write(" ".join(map(str, pr)))
       output.write("\n")
    output.write("\n\n")   
     
    def optionsp12(e):    #parametrs printing
        while range(len(fvn)):
            for d in range(len(fvn[e])):
                output.write(fvn[e][d])
                output.write("  ")
            output.write("\n")
            
            break
        
    def optionsp(stname):  #satelit name printing 
           
        while len(newsate): 
            output.write(newsate[stname])
            output.write("  ")  
            break
    
    i=0 
    stname=0
    e=0
    d=0 
    for st in NO_satlites:   #No sateites in each epoch=st    
        for g in range(int(st)):
                output.write(time[i]+"\t")
                
                optionsp(stname)
                optionsp12(e)
                e+=1
                stname+=1  
        i+=1 
        
    output.close()  
    print(ff," Succesfull")            
      
    #Defult end  
                       
    print("################ Available parameters ###############")
    for pr in par:
       print(" ".join(map(str, pr)))
    del par[:]
    output.close()  

     

