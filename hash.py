#coding:utf-8
import sys
from hashlib import sha1
import time
import threading
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--pwd',type=str, default='b7a875fc1ea228b9061041b7cec4bd3c52ab3ce2', help='hash')
parser.add_argument('--mode', default=1, type=int, help='mode 1 one password mode 2 salted mode3 concatenated with space')
parser.add_argument('--hint', type=str, default='', help='hint for mode 2')
parser.add_argument('--multi', default=0, type=int, help='multi thread')
args = parser.parse_args()


reload(sys)
sys.setdefaultencoding('utf-8')

def crack(pwd,word):
    li = word.strip()
    s1 = sha1()
    s1.update(li.encode())
    result = s1.hexdigest()
    if result == pwd:
        return 1
    else:
        return 0

def break_hash(pwd,mode=1,hint=''):
    i = 0.
    t = time.time()
    if mode == 1:
        for line in open('password.txt'):
            i += 1
            res = crack(pwd,line)
            if res == 1:
                ta = time.time() - t
                print 'time',ta,'try',i,'find',line
                return
        print 'crack fail'
        return

    elif mode == 2:
        if hint != '':
            for line in open('password.txt'):
                i += 1
                hint = hint.strip()
                res = crack(hint,line)
                if res == 1:
                    ta = time.time() - t
                    print 'time', ta, 'try', i, 'find hine', line
                    break

            for line1 in open('password.txt'):
                i += 1
                li = line.strip() + line1.strip()
                res = crack(pwd,li)
                if res == 1:
                    ta = time.time() - t
                    print 'time', ta, 'try', i, 'find', line1
                    return

        else:            
            for line1 in open('password.txt'):
                for line2 in open('password.txt'):
                    i += 1
                    li = line1.strip()+line2.strip()
                    res = crack(pwd, li)
                    if res == 1:
                        ta = time.time() - t
                        print 'time', ta, 'try', i, 'find', line1
                        return
    elif mode == 3:
        for line1 in open('password.txt'):
            for line2 in open('password.txt'):
                i += 1
                li = line1.strip()+' '+ line2.strip()        
                s1 = sha1()
                s1.update(li.encode())
                result = s1.hexdigest()
                if result == pwd:
                    ta = time.time() - t
                    print 'try',i,'time',ta,'pwd',li
                    return i,li
    ta = time.time() - t
    print 'try',i,'time',ta,'fail'        
    return 0,'fail'



def crack_m(arg,pwd):
    global done
    f = open('password.txt')
    lines = f.readlines()[10000*arg:min(10000*(arg+1)-1,999999)]
    for line1 in lines:
        for line2 in open('password.txt'):
            if done != 1:
                li = line1.strip()+line2.strip()
                s1 = sha1()
                s1.update(li.encode())
                result = s1.hexdigest()
                if result == pwd:
                    done = 1
                    print 'pwd',li, 'thread', arg
                    return li
            else:
                return 'error'
                 

def break_hash_m(pwd):
    i = 0    
    for i in xrange(100):
        t =threading.Thread(target=crack,args=(i,pwd))
        t.start()
   

if args.multi == 0:
    break_hash(args.pwd,args.mode,args.hint)
else:
    done = 0
    break_hash_m(args.pwd)

# pwd='b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3'
# pwd1='801cdea58224c921c21fd2b183ff28ffa910ce31'
# pwd2='f0744d60dd500c92c0d37c16174cc58d3c4bdd8e'
# pwd3='ece4bb07f2580ed8b39aa52b7f7f918e43033ea1'
# pwd4='34302959e138917ce9339c0b30ec50e650ce6b40'
#
# done = 0
# break_hash(pwd)


