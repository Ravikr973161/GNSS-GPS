# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 16:45:33 2019

@author: RAVI K R
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:16:34 2019

@author: RAVI K R
"""
import glob
par=[]
parm=[]
flag=0
satlite=[]
fg1,fg2,fg3,fg4,fg5,fg6,fg7,fg8,fg9,fg10,fg11,fg12,fg13,fg14,fg15,fg16,fg17,fg18=([] for i in range(18))
fe1,fe2,fe3,fe4,fe5,fe6,fe7,fe8,fe9,fe10,fe11,fe12,fe13,fe14,fe15,fe16,fe17,fe18=([] for i in range(18))
fr1,fr2,fr3,fr4,fr5,fr6,fr7,fr8,fr9,fr10,fr11,fr12,fr13,fr14,fr15,fr16,fr17,fr18=([] for i in range(18))
fs1,fs2,fs3,fs4,fs5,fs6,fs7,fs8,fs9,fs10,fs11,fs12,fs13,fs14,fs15,fs16,fs17,fs18=([] for i in range(18))
fi1,fi2,fi3,fi4,fi5,fi6,fi7,fi8,fi9,fi10,fi11,fi12,fi13,fi14,fi15,fi16,fi17,fi18=([] for i in range(18))

NO_satlites=list()
time=list()
Gpar,Epar,Ipar,Spar,Rpar=([] for i in range(5))
print("Available source files in the current directory")
File=glob.glob('*.*o')
print(File)

#Reading files and skipping the header
brk=0
Gno,Eno,Ino,Sno,Rno=0,0,0,0,0
k,l,m,n,p=0,0,0,0,0
for ff in File:
    fh=open(ff,"r")
    for line in fh:
        for data in line.split():
            if data=='3.03':
               print("Valid version:- 3.03")
        if k!=0:
                Gpar.append(line[7:10])
                Gpar.append(line[11:14])
                Gpar.append(line[15:18])
                Gpar.append(line[19:22])
                Gpar.append(line[23:26])
                Gpar.append(line[27:30])
                Gpar.append(line[31:34])
                Gpar.append(line[35:38])
                Gpar.append(line[39:42])
                Gpar.append(line[43:46])
                Gpar.append(line[47:50])
                Gpar.append(line[51:54])
                Gpar.append(line[55:58])
                k-=1
                
        if l!=0:
                Epar.append(line[7:10])
                Epar.append(line[11:14])
                Epar.append(line[15:18])
                Epar.append(line[19:22])
                Epar.append(line[23:26])
                Epar.append(line[27:30])
                Epar.append(line[31:34])
                Epar.append(line[35:38])
                Epar.append(line[39:42])
                Epar.append(line[43:46])
                Epar.append(line[47:50])
                Epar.append(line[51:54])
                Epar.append(line[55:58])
                l-=1
        if m!=0:
                Ipar.append(line[7:10])
                Ipar.append(line[11:14])
                Ipar.append(line[15:18])
                Ipar.append(line[19:22])
                Ipar.append(line[23:26])
                Ipar.append(line[27:30])
                Ipar.append(line[31:34])
                Ipar.append(line[35:38])
                Ipar.append(line[39:42])
                Ipar.append(line[43:46])
                Ipar.append(line[47:50])
                Ipar.append(line[51:54])
                Ipar.append(line[55:58]) 
                m-=1
        if n!=0:
                Spar.append(line[7:10])
                Spar.append(line[11:14])
                Spar.append(line[15:18])
                Spar.append(line[19:22])
                Spar.append(line[23:26])
                Spar.append(line[27:30])
                Spar.append(line[31:34])
                Spar.append(line[35:38])
                Spar.append(line[39:42])
                Spar.append(line[43:46])
                Spar.append(line[47:50])
                Spar.append(line[51:54])
                Spar.append(line[55:58])
                n-=1
        if p!=0:
                Rpar.append(line[7:10])
                Rpar.append(line[11:14])
                Rpar.append(line[15:18])
                Rpar.append(line[19:22])
                Rpar.append(line[23:26])
                Rpar.append(line[27:30])
                Rpar.append(line[31:34])
                Rpar.append(line[35:38])
                Rpar.append(line[39:42])
                Rpar.append(line[43:46])
                Rpar.append(line[47:50])
                Rpar.append(line[51:54])
                Rpar.append(line[55:58])
                p-=1        
        if line[0:1]=='G':
            if line[74:79]=='TYPES':
                Gno=line[4:6]
                Gpar.append(line[7:10])
                Gpar.append(line[11:14])
                Gpar.append(line[15:18])
                Gpar.append(line[19:22])
                Gpar.append(line[23:26])
                Gpar.append(line[27:30])
                Gpar.append(line[31:34])
                Gpar.append(line[35:38])
                Gpar.append(line[39:42])
                Gpar.append(line[43:46])
                Gpar.append(line[47:50])
                Gpar.append(line[51:54])
                Gpar.append(line[55:58])
                k= int(Gno)//13
                if int(Gno)%13==0:
                    k-=1
        if line[0:1]=='E':
            if line[74:79]=='TYPES':
                Eno=line[4:6]
                Epar.append(line[7:10])
                Epar.append(line[11:14])
                Epar.append(line[15:18])
                Epar.append(line[19:22])
                Epar.append(line[23:26])
                Epar.append(line[27:30])
                Epar.append(line[31:34])
                Epar.append(line[35:38])
                Epar.append(line[39:42])
                Epar.append(line[43:46])
                Epar.append(line[47:50])
                Epar.append(line[51:54])
                Epar.append(line[55:58])
                l= int(Eno)//13
                if int(Eno)%13==0:
                    l-=1
        if line[0:1]=='I':
            if line[74:79]=='TYPES':
                Ino=line[4:6]
                Ipar.append(line[7:10])
                Ipar.append(line[11:14])
                Ipar.append(line[15:18])
                Ipar.append(line[19:22])
                Ipar.append(line[23:26])
                Ipar.append(line[27:30])
                Ipar.append(line[31:34])
                Ipar.append(line[35:38])
                Ipar.append(line[39:42])
                Ipar.append(line[43:46])
                Ipar.append(line[47:50])
                Ipar.append(line[51:54])
                Ipar.append(line[55:58])   
                m= int(Ino)//13
                if int(Ino)%13==0:
                    m-=1
        if line[0:1]=='S':
            if line[74:79]=='TYPES':
                Sno=line[4:6]
                Spar.append(line[7:10])
                Spar.append(line[11:14])
                Spar.append(line[15:18])
                Spar.append(line[19:22])
                Spar.append(line[23:26])
                Spar.append(line[27:30])
                Spar.append(line[31:34])
                Spar.append(line[35:38])
                Spar.append(line[39:42])
                Spar.append(line[43:46])
                Spar.append(line[47:50])
                Spar.append(line[51:54])
                Spar.append(line[55:58]) 
                n= int(Sno)//13
                if int(Sno)%13==0:
                    n-=1
        if line[0:1]=='R':
            if line[74:79]=='TYPES':
                Rno=line[4:6]
                Rpar.append(line[7:10])
                Rpar.append(line[11:14])
                Rpar.append(line[15:18])
                Rpar.append(line[19:22])
                Rpar.append(line[23:26])
                Rpar.append(line[27:30])
                Rpar.append(line[31:34])
                Rpar.append(line[35:38])
                Rpar.append(line[39:42])
                Rpar.append(line[43:46])
                Rpar.append(line[47:50])
                Rpar.append(line[51:54])
                Rpar.append(line[55:58])
                p= int(Rno)//13
                if int(Rno)%13==0:
                    p-=1

    fh.close()
            
            
   
    satliteG,satliteE,satliteR,satliteS,satliteI=([] for i in range(5))  
    def gsat():
         fg1.append(line[5:17])    
         fg2.append(line[20:33])  
         fg3.append(line[36:49])
         fg4.append(line[52:65])
         fg5.append(line[68:81])
         fg6.append(line[84:97])
         fg7.append(line[100:113])
         fg8.append(line[116:129])
         fg9.append(line[132:145])
         fg10.append(line[148:161])
         fg11.append(line[164:177])
         fg12.append(line[179:193])
         fg13.append(line[196:209])
         fg14.append(line[212:225])
         fg15.append(line[228:241])
         fg16.append(line[244:257])
         fg17.append(line[260:273])
         fg18.append(line[276:289])
    
    def Esat():
         fe1.append(line[5:17])    
         fe2.append(line[20:33])  
         fe3.append(line[36:49])
         fe4.append(line[52:65])
         fe5.append(line[68:81])
         fe6.append(line[84:97])
         fe7.append(line[100:113])
         fe8.append(line[116:129])
         fe9.append(line[132:145])
         fe10.append(line[148:161])
         fe11.append(line[164:177])
         fe12.append(line[179:193])
         fe13.append(line[196:209])
         fe14.append(line[212:225])
         fe15.append(line[228:241])
         fe16.append(line[244:257])
         fe17.append(line[260:273])
         fe18.append(line[276:289])
    
    def Isat():
         fi1.append(line[5:17])    
         fi2.append(line[20:33])  
         fi3.append(line[36:49])
         fi4.append(line[52:65])
         fi5.append(line[68:81])
         fi6.append(line[84:97])
         fi7.append(line[100:113])
         fi8.append(line[116:129])
         fi9.append(line[132:145])
         fi10.append(line[148:161])
         fi11.append(line[164:177])
         fi12.append(line[179:193])
         fi13.append(line[196:209])
         fi14.append(line[212:225])
         fi15.append(line[228:241])
         fi16.append(line[244:257])
         fi17.append(line[260:273])
         fi18.append(line[276:289])
                
    def Rsat():
         fr1.append(line[5:17])    
         fr2.append(line[20:33])  
         fr3.append(line[36:49])
         fr4.append(line[52:65])
         fr5.append(line[68:81])
         fr6.append(line[84:97])
         fr7.append(line[100:113])
         fr8.append(line[116:129])
         fr9.append(line[132:145])
         fr10.append(line[148:161])
         fr11.append(line[164:177])
         fr12.append(line[179:193])
         fr13.append(line[196:209])
         fr14.append(line[212:225])
         fr15.append(line[228:241])
         fr16.append(line[244:257])
         fr17.append(line[260:273])
         fr18.append(line[276:289])
            
    def Ssat():
         fs1.append(line[5:17])    
         fs2.append(line[20:33])  
         fs3.append(line[36:49])
         fs4.append(line[52:65])
         fs5.append(line[68:81])
         fs6.append(line[84:97])
         fs7.append(line[100:113])
         fs8.append(line[116:129])
         fs9.append(line[132:145])
         fs10.append(line[148:161])
         fs11.append(line[164:177])
         fs12.append(line[179:193])
         fs13.append(line[196:209])
         fs14.append(line[212:225])
         fs15.append(line[228:241])
         fs16.append(line[244:257])
         fs17.append(line[260:273])
         fs18.append(line[276:289])
                 
         
            
    
    fh=open(ff,"r")
    for line in fh:
        for i in range(len(line)):
            if line[i]=='>':
                flag=1
        if flag==1:
            if line[0]=='>':
                time.append(line[2:29])
                NO_satlites.append(line[33:35])
                continue
            else:
                satlite.append(line[0:3])
                 #satelite slicing
                if 'G' in line[0:3]:
                    satliteG.append(line[0:3])
                    gsat()
                elif 'I' in line[0:3]:
                    satliteI.append(line[0:3])
                    Isat()
                elif 'E' in line[0:3]:
                    satliteE.append(line[0:3])
                    Esat()
                elif 'R' in line[0:3]:
                    satliteR.append(line[0:3])
                    Rsat()
                elif 'S' in line[0:3]:
                    satliteS.append(line[0:3])
                    Ssat()    
    GGpar,EEpar,RRpar,IIpar,SSpar=([] for i in range(5))
    for g in Gpar:
        if g!='   ':
            GGpar.append(g)
    for e in Epar:
        if e!='   ':
            EEpar.append(e)
    for r in Rpar:
        if r!='   ':
            RRpar.append(r)
    for i in Ipar:
        if i!='   ':
            IIpar.append(i)
    for s in Spar:
        if s!='   ':
            SSpar.append(s)        

    fh.close()
    
    output=open(ff[:-4]+"G.txt","w+")
    output.write(str(GGpar))
    output.write("\n")
    def optionsp(stname):
           
        while len(satliteG): 
            output.write("\t")  
            output.write("  ")
            output.write(fg1[stname])
            output.write("  ")
            output.write(fg2[stname])
            output.write("  ")
            output.write(fg3[stname])
            output.write("  ")
            output.write(fg4[stname])
            output.write("  ")
            output.write(fg5[stname])
            output.write("  ")
            output.write(fg6[stname])
            output.write("  ")
            output.write(fg7[stname])
            output.write("  ")
            output.write(fg8[stname])
            output.write("  ")
            output.write(fg9[stname])
            output.write("  ")
            output.write(fg10[stname])
            output.write("  ")
            output.write(fg11[stname])
            output.write("  ")
            output.write(fg12[stname])
            output.write("  ")
            output.write(fg13[stname])
            output.write("  ")
            output.write(fg14[stname])
            output.write("  ")
            output.write(fg15[stname])
            output.write("  ")
            output.write(fg16[stname])
            output.write("  ")
            output.write(fg17[stname])
            output.write("  ")
            output.write(fg18[stname])
            output.write("\n")
            break
    
    stname=0
    for st in range(len(satliteG)):   #No sateites in each epoch=st    
        output.write(satliteG[st])
        optionsp(stname)
        stname+=1
    output.write("\n")
    #end Gpar
    output.close()
    
    output=open(ff[:-4]+"E.txt","w+")    
    output.write(str(EEpar))
    output.write("\n")
    def optionsp(stname):
           
        while len(satliteE): 
            output.write("\t")  
            output.write("  ")
            output.write(fe1[stname])
            output.write("  ")
            output.write(fe2[stname])
            output.write("  ")
            output.write(fe3[stname])
            output.write("  ")
            output.write(fe4[stname])
            output.write("  ")
            output.write(fe5[stname])
            output.write("  ")
            output.write(fe6[stname])
            output.write("  ")
            output.write(fe7[stname])
            output.write("  ")
            output.write(fe8[stname])
            output.write("  ")
            output.write(fe9[stname])
            output.write("  ")
            output.write(fe10[stname])
            output.write("  ")
            output.write(fe11[stname])
            output.write("  ")
            output.write(fe12[stname])
            output.write("  ")
            output.write(fe13[stname])
            output.write("  ")
            output.write(fe14[stname])
            output.write("  ")
            output.write(fe15[stname])
            output.write("  ")
            output.write(fe16[stname])
            output.write("  ")
            output.write(fe17[stname])
            output.write("  ")
            output.write(fe18[stname])
            output.write("\n")
            break
    
    stname=0
    for st in range(len(satliteE)):   #No sateites in each epoch=st    
        output.write(satliteE[st])
        optionsp(stname)
        stname+=1
    output.write("\n")    
    output.close()
    
    output=open(ff[:-4]+"I.txt","w+")        
    output.write(str(IIpar))
    output.write("\n")
    def optionsp(stname):
           
        while len(satliteI): 
            output.write("\t")  
            output.write("  ")
            output.write(fi1[stname])
            output.write("  ")
            output.write(fi2[stname])
            output.write("  ")
            output.write(fi3[stname])
            output.write("  ")
            output.write(fi4[stname])
            output.write("  ")
            output.write(fi5[stname])
            output.write("  ")
            output.write(fi6[stname])
            output.write("  ")
            output.write(fi7[stname])
            output.write("  ")
            output.write(fi8[stname])
            output.write("  ")
            output.write(fi9[stname])
            output.write("  ")
            output.write(fi10[stname])
            output.write("  ")
            output.write(fi11[stname])
            output.write("  ")
            output.write(fi12[stname])
            output.write("  ")
            output.write(fi13[stname])
            output.write("  ")
            output.write(fi14[stname])
            output.write("  ")
            output.write(fi15[stname])
            output.write("  ")
            output.write(fi16[stname])
            output.write("  ")
            output.write(fi17[stname])
            output.write("  ")
            output.write(fi18[stname])
            output.write("\n")
            break
    
    stname=0
    for st in range(len(satliteI)):   #No sateites in each epoch=st    
        output.write(satliteI[st])
        optionsp(stname)
        stname+=1
    output.write("\n")
    output.close()
    
    output=open(ff[:-4]+"S.txt","w+")    
    output.write(str(SSpar))
    output.write("\n")
    def optionsp(stname):
           
        while len(satliteS): 
            output.write("\t")  
            output.write("  ")
            output.write(fs1[stname])
            output.write("  ")
            output.write(fs2[stname])
            output.write("  ")
            output.write(fs3[stname])
            output.write("  ")
            output.write(fs4[stname])
            output.write("  ")
            output.write(fs5[stname])
            output.write("  ")
            output.write(fs6[stname])
            output.write("  ")
            output.write(fs7[stname])
            output.write("  ")
            output.write(fs8[stname])
            output.write("  ")
            output.write(fs9[stname])
            output.write("  ")
            output.write(fs10[stname])
            output.write("  ")
            output.write(fs11[stname])
            output.write("  ")
            output.write(fs12[stname])
            output.write("  ")
            output.write(fs13[stname])
            output.write("  ")
            output.write(fs14[stname])
            output.write("  ")
            output.write(fs15[stname])
            output.write("  ")
            output.write(fs16[stname])
            output.write("  ")
            output.write(fs17[stname])
            output.write("  ")
            output.write(fs18[stname])
            output.write("\n")
            break
    
    stname=0
    for st in range(len(satliteS)):   #No sateites in each epoch=st    
        output.write(satliteS[st])
        optionsp(stname)
        stname+=1
    output.write("\n")
    output.close()
    
    output=open(ff[:-4]+"R.txt","w+")   
    output.write(str(RRpar))
    output.write("\n")
    def optionsp(stname):
           
        while len(satliteR): 
            output.write("\t")  
            output.write("  ")
            output.write(fr1[stname])
            output.write("  ")
            output.write(fr2[stname])
            output.write("  ")
            output.write(fr3[stname])
            output.write("  ")
            output.write(fr4[stname])
            output.write("  ")
            output.write(fr5[stname])
            output.write("  ")
            output.write(fr6[stname])
            output.write("  ")
            output.write(fr7[stname])
            output.write("  ")
            output.write(fr8[stname])
            output.write("  ")
            output.write(fr9[stname])
            output.write("  ")
            output.write(fr10[stname])
            output.write("  ")
            output.write(fr11[stname])
            output.write("  ")
            output.write(fr12[stname])
            output.write("  ")
            output.write(fr13[stname])
            output.write("  ")
            output.write(fr14[stname])
            output.write("  ")
            output.write(fr15[stname])
            output.write("  ")
            output.write(fr16[stname])
            output.write("  ")
            output.write(fr17[stname])
            output.write("  ")
            output.write(fr18[stname])
            output.write("\n")
            break
    
    stname=0
    for st in range(len(satliteR)):   #No sateites in each epoch=st    
        output.write(satliteR[st])
        optionsp(stname)
        stname+=1
    output.write("\n")   
    output.close()
    
    satliteG,satliteE,satliteR,satliteS,satliteI=([] for i in range(5))
    print(ff," Succesfull")  
                 
            
#total parmetrs
print("################:Available parameters:###############")
print(GGpar)
print(EEpar)
print(IIpar)
print(SSpar)
print(RRpar)
