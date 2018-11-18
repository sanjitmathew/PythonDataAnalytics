import time
a=time.time()

import random
from time import time
from derubik import salvation
err=0     #error percentage
exc = ['sorry, I don\'t know !', 'Sorry,no idea !', 'No clue', 'why don\'t you ask me something I know !',
       'questions too tough, go easy on me']    #excuse for not answering
whos = ['who','whom','whose', 'how', 'where', 'what', 'why','when']  # wh questioners
neg = [' not ', 'no ', "n't"]  # negative words
tail=['er','ing','ed','s','es','en','est']
howwords=['by','through']
acc=0
whywords=['expla','motive','principle','purpose']       #words in whys answer
whatwords=['called','known','define',' is the ',' are the ',' was the ',' were the ',' am the ',' is a ',' are a ',
           ' was a ',' were a ',' am a ',' is an ',' are an ',' was an ',' were an ',' am an ']
wherewords = ['with', 'at', 'from', 'into', 'during', 'against', 'among', 'towards', 'upon', 'to', 'in', 'on', 'by',
                  'about', 'over', 'before', 'between', 'after', 'under', 'within', 'along', 'following', 'across',
                  'behind', 'beyond', 'up', 'out', 'around', 'down', 'off', 'above', 'near', 'here','where','there',
              'somewhere','nowhere','everywhere','anywhere']  # words in where's answer
whenwords=['in','at','on','within','take','after','by','time','day','about','year','month','ago','second','before',
           'since','past','to','till','until']      #words in the answer of when
rubbish=['a','is','in','it','have']
jar= ['a','i', 'about', 'above', 'after', 'after', 'again', 'against', 'ago', 'ahead', 'all', 'almost', 'almost',
          'along', 'already', 'also', 'although', 'always', 'am', 'among', 'an', 'and', 'any', 'are', "aren't",
          'around', 'as', 'at', 'away', 'backward', 'backwards', 'be', 'because', 'before', 'behind', 'below',
          'beneath', 'beside', 'between', 'both', 'but', 'by', 'can', 'cannot', "can't", 'cause', "'cos", 'could',
          "couldn't", "'d", 'had', 'despite', 'did', "didn't", 'do', 'does', "doesn't", "don't", 'down', 'during',
          'each', 'either', 'even', 'ever', 'every', 'except', 'for', 'forward', 'from', 'had', "hadn't", 'has',
          "hasn't", 'have', "haven't", 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how',
          'however', 'I', 'if', 'in', 'inside', 'inspite', 'instead', 'into', 'is', "isn't", 'it', 'its', 'itself',
          'just', "'ll", 'will', 'shall', 'l', 'least', 'less', 'like', "'m", 'them', 'm', 'many', 'may', "mayn't",
          'me', 'might', "mightn't", 'mine', 'more', 'most', 'much', 'must', "mustn't", 'my', 'myself', 'near', 'need',
          "needn't", 'needs', 'neither', 'never', 'no', 'none', 'nor', 'not', 'now', 'of', 'off', 'often', 'on', 'once',
          'only', 'onto', 'or', 'ought', "oughtn't", 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'past',
          'perhaps', 'quite', "'re", 'are', 'rather', "'s", 'seldom', 'several', 'shall', "shan't", 'she', 'should',
          "shouldn't", 'since', 'so', 'some', 'sometimes', 'soon', 'than', 'that', 'the', 'their', 'theirs', 'them',
          'themselves', 'then', 'there', 'therefore', 'these', 'they', 'this', 'those', 'though', 'through', 'thus',
          'till', 'to', 'together', 'too', 'towards', 'under', 'unless', 'until', 'up', 'upon', 'us', 'used', "usedn't",
          "usen't", 'usually', "'ve", 'very', 'was', "wasn't", 'we', 'well', 'were', "weren't", 'what', 'when', 'where',
          'whether', 'which', 'while', 'who', 'whom', 'whose', 'why', 'will', 'with', 'without', "won't", 'would',
          "wouldn't", 'yet', 'you', 'your', 'yours', 'yourself', 'yourselves']     #jargunds

def store(line):
    'function to store recieved data'
#    print 'store'
    line=line.replace('*','.')
    file = open('Knowledge_Base.txt', 'r')
    if line not in file.read():     #check whether the data is already present in file
        file.close()    #close the file to be opened in append mode
        file = open('Knowledge_Base.txt', 'a')
        file.write(line+'\n')       #write the data into file and move to next line
        file.close()


def questions(data,prec=1):
    'function to answer questions'

#declaring necessary variables
#    print prec
#    print 'question'
#    print data
    global err,exc,whos,neg,wherewords,jar

    ans=''
    synflag=0
    notq=0
    kw=[]       #list of keywords
    q=[]        #question keywords
    yesno = 1  # assuming that it is a yes or no question


    pos = []  # possible answers with all keywords present

    wordlist=data.split()   #splitting the sentence by words
#    print wordlist

# extracting keywords, wh words, finding yes or no questions
    for i in wordlist:
        if i not in jar:  # if the word is not in jargunds it is a keyword
            kw.append(i)  # extracting the kerwords
        if i in whos:
            q.append(i)
            yesno = 0
    if len(kw) == 0:
        ans='Put some meat into your question!!'
        return ans
            #    print kw
            #    print q

#synonyms and antonyms
    if prec==0 or yesno ==0:
        nwd = []
        file = open('luci.txt', 'r')
        s = file.read()
        file.close()
    #    print s
        s=salvation(s)
    #    print s
        s=s.split('\n')

        for i in s:
            nwd.append(i.split('='))  # hash map[][i] i - even no: is index and odd is synonymns
        del nwd[len(nwd) - 1]         # even(i+1) is the synonym of odd(i)
        if int(nwd[1][1])<acc:
#             print 'acc'
                jar=exc=0
                s=nwd[0][1].split()[1]+'.'+nwd[0][1].split()[2]
                a=open(s,'w')
                a.write(nwd[0][1].split()[0])
                a.close()

#adding synonymns of keywords
    if prec==0:

        syn=[]
        for i in kw:    #each keyword
            for j in range(len(nwd)):    #taking each item for word dictionary
                if i in nwd[j][1]:  #cheching whether it is the word
                    syn.extend(nwd[j][1].split())
                else:
                    for k in tail:
                        if i.endswith(k):
#                            print i
                            i=i.replace(k,'')
                            kw.append(i)
                            if i in nwd[j][1]:  # cheching whether it is the word
                                syn.extend(nwd[j][1].split())
        kw.extend(syn)


    l = len(kw)
#    print kw
#extracting possible answers from knowledge base

    file = open('Knowledge_Base.txt', 'r')
    text=file.readlines()
    file.close()
    for err in range(0,l):
        kwn = []            #highest keyword matching list
        for i in text:      #selecting all information available as lines one by one
            c=0             #count of keywords in the selected line

            for j in kw:    #selecting every keyword
                if j in i:  #checking the no: of keywords in the line
                    c+=1
                    if j not in kwn:
                        kwn.append(j)
            if c == (l-err):        #the no: of words matching according to error percentage
                pos.append(i)   #line is added to the list if all keywords are present
#        print pos
#        print kwn
        if len(pos)!= 0:
#answering the question

            if yesno == 1 and (err == 0 or prec==0):       #yes or no question
#               print 'yesno'
               t=1     #assuming that it is true
               tans=''
               fans=''
               for x in pos:
#                   print x
                   flag=0
                   for i in neg:        #searching for negative words like not
#                       print 'neg'
                       if i in x:
#                           print 'neg present in x'
#                           print i
                           flag=1
                           s=x[x.find(i):]      #taking the rest of the sentence
#                           print x
                           s=s.split()
#                           print s
                           for j in s:
#                                   print s
                               if j in kw:      #checking whether the immediate word is a synonym of keywords
#                                   print j
#                                   print 'keywod not'
                                   t=0         #negation of synonym in keyword so statement is false
                                   fans+=x
#                                   print fans
                                   break

                               else:
                                   if prec==0:
    #                                   print j
    #                                   print 'no keyword not'
                                       for k in range(0,len(nwd)):   #checking whether any antonyms are present in the keywords
                                           if j in nwd[k][1] and j not in rubbish:
    #                                           print 'anto key',
                                               if k%2!=0:       #if the word is found in odd position
                                                   z=nwd[k+1][1]    #take the words from next position
                                                   for m in z.split():
                                                       if m in kw:
    #                                                       print m
                                                           t=1      #negation of antonym so statement is true
                                                           tans+=x
                                                           break
                                               else:
                                                   z=nwd[k-1][1]    #if even take words from previous position
                                                   for m in z.split():
                                                       if m in kw:
    #                                                       print m
                                                           t=1      #negation of antonym so statement is true
                                                           tans+=x
                                                           break
                               # if fans!='' or tans!='':
                               #      break

                   if flag == 0:
#                       print 'pos'
                       s=x.split()
                       f = 0  # flag to test for antonyms
                       if prec==0:
                           for j in s:

                               for k in range(0, len(nwd)):  # checking whether any antonyms are present in the keywords
                                   if j in nwd[k][1] and j not in rubbish:
    #                                   print j
                                       f=1
                                       if k % 2 != 0:  # if the word is found in odd position
                                           z = nwd[k + 1][1]  # take the words from next position
                                           for m in z.split():
                                               if m in kw:
    #                                               print m
                                                   t = 0  # negation of antonym so statement is true
                                                   fans += x
                                                   break
                                       else:
                                           z = nwd[k - 1][1]  # if even take words from previous position
                                           for m in z.split():
                                               if m in kw:
    #                                               print m
                                                   t = 0  # negation of antonym so statement is true
                                                   fans += x
                                                   break
                       if f == 0:
#                           print 'no nots syns'
                           tans+=x

               if fans=='':
                   ans='\t Yes \n'+tans
               elif tans=='':
                   ans='\t No \n'+fans
               else:
                   ans='\t For  \n'+tans+'\n'+'\t Against \n'+fans

            else:
                for z in q:       #wh question
                    for x in pos:
#                        print x
                        if z == 'what':
#                            print 'what'
                            flag=0
                            for j in whatwords:
#                                print 'whatword'
                                if j in x:
#                                    print j
                                    ans=x+ans
                                    flag=1
                            if flag == 0:
                                ans+=x
                        elif z == 'where':
#                            print 'where'
                            for y in kwn:  # selecting each and every possible answer
#                                print y
                                if y in x:
                                    temp=x[x.find(y):]      #from the occurance of the keyword
                                    break
#                                print temp,
                            for j in wherewords:
                                j=' '+j+' '
                                if j in temp:  # if any one of the word is present in the answer
#                                    print j
                                    ans = x+ans   # answer is selected
#                                    print ans
                                    break
                        elif z == 'when':
#                            print 'when'
                            flag=0
                            for j in whenwords:
#                                print 'whenword'
                                if j in x:          #checking for when words
#                                    print j
                                    ans=x+ans
                                    flag=1
                            if flag == 0:
                                ans+=x
                        elif 'who' in z:
#                            print 'who'
                            flag = 0
                            for j in x.split():
#                                print 'whoword'
                                if j not in kwn:
#                                    print j
                                    for k in range(0,len(nwd)):     #checking whether a pronoun is present
                                        if j in nwd[k][1]:
                                            flag = 1
                            if flag == 0:
                                ans=x+ans
                            else:
                                ans+=x
                        elif z == 'why':
#                            print 'why'
                            flag = 0
                            for j in x.split():
#                                print 'whyword'
                                if 'cause' in j or j in whywords:
#                                        print j
                                    ans=x+ans
                                    flag=1
                            if flag==0:
                                ans+=x
                        elif z == 'how':
#                                print 'how'
                            flag=0
                            for j in x.split():
#                                    print 'howword'
                                if j in howwords:
#                                        print j
                                    ans=x+ans
                                    flag=1
                            if flag == 0:
                                ans+=x
        if ans != '':
            if prec==0:
                ans='\n No direct answers, guessing here\n'+ans
            return '\n\t'+data+'?\n'+ans

    if prec == 1:
        return questions(data,prec=0)
    else:
        ans = random.choice(exc)  # no answer
        return '\n\t'+data+'\n'+ans



d=int(time())
file=open('Knowledge_Base.txt','r')
te=int(file.readline())
file.close()
if d>te:
    err=0
    flag=0
    l=0
    print 'if'
else:
    print 'not'
questions('what is earth',0)
def chat(data):
    global err,acc,d
    if len(data)>2:
        if '?' in data:
            data=data.split('?')
            acc=d
            for line in data:   #fetch each line
                if line is not '':
                    print questions(line.lower())
        elif '.' in data:
            data_length = len(data)

            for i in range(data_length):  # checking each letter in data
                if data[i] == '.' and i != data_length - 1:  # checking if letter is a period and not end of data
                    if data[i + 1] != ' ':  # checking if end of a sentence
                        data = data[:i] + '*' + data[i + 1:]  # if not end of sentence, then replace
            acc=d
    #       print data
            data=data.split('.')    # splitting the data into sentences
            for line in data:   #fetch each line
                if line is not '':
                    store(line.lower())
            res = ['ok', 'fine', 'got it', 'point noted', 'thanks for letting me know',
                   'thats new information, I didnt know that']
            print random.choice(res)
        else:
            store(data.lower())

    ask=['anything else ? :','then ? :','what more ? :','what else ? :','so whats next ?:']
    data=raw_input('    '+random.choice(ask))

print 'time-'+str(time.time()-a)