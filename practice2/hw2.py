import sys
import math


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open("C:/Users/varda/OneDrive/Documents/COLLEGE COURSEWORK/cs-540-projects/cs 540/assignments/hw2/practice2/e.txt",encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open("C:/Users/varda/OneDrive/Documents/COLLEGE COURSEWORK/cs-540-projects/cs 540/assignments/hw2/practice2/s.txt",encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    X=dict()
    diff=ord('a')-ord('A')
    upperLower=ord('Z')-ord('A')
    with open (filename,encoding='utf-8') as f:
        for line in f:
            for c in list(line.strip()):
                index=ord(c)-ord('A')
                if(index<=upperLower and index>=0):
                    X[c]=1 if c not in X else X[c]+1
                elif(index-diff>=0 and index-diff<=upperLower):
                    c=chr(ord(c)-diff)
                    X[c]=1 if c not in X else X[c]+1
                else:
                    continue
    for i in range(diff):
        if chr(ord('A')+i) not in X:
            X[chr(ord('A')+i)]=0
    Y=dict(sorted(X.items()))
    return Y
def findProb(filename):
    print('Q1')
    X=shred(filename)
    for i,j in X.items():
        print(i," ",j)
    print('Q2')
    x1=X['A']
    e,s=get_parameter_vectors()
    e1=e[0]
    s1=s[0]
    print(round(math.log(e1)*x1,4))
    print(round(math.log(s1)*x1,4))
    print('Q3')
    prob_e=0.6
    prob_s=1-prob_e
    sum_e=0
    sum_s=0
    for i in range(26):
        sum_e+=X[chr(i+ord('A'))]*math.log(e[i])
        sum_s+=X[chr(i+ord('A'))]*math.log(s[i])
    F_e=math.log(prob_e)+sum_e
    F_s=math.log(prob_s)+sum_s
    print(round(F_e,4))
    print(round(F_s,4))
    print('Q4')
    difference=F_s-F_e
    if(difference>=100):
        print(round(0,4))
    elif(difference<=-100):
        print(round(1,4))
    else:
        print(round(1/(1+math.exp(difference)),4))
findProb("C:/Users/varda/OneDrive/Documents/COLLEGE COURSEWORK/cs-540-projects/cs 540/assignments/hw2/practice2/samples/letter4.txt")
