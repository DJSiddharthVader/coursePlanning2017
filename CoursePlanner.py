#!/usr/bin/python
#used to plan course schedule based on terminal courses, weight by number of prereqs
import courseList as cl
import itertools

def mkpowset(s):
    powset=[]
    x = len(s)
    for i in range(1 << x):
       powset.append([s[j] for j in range(x) if (i & (1 << j))])
    return powset

def filterpowset(powset):
    filt1 = filter(lambda x: len(x) < 8 and len(x) > 2, powset)
    return powset

def expandpowset(weightlst, max_load):
    filt2=[]
    for list in weightlst:
        exps = []
        for ll in list:
            sched = ll
            while sched:
                if sched.str() not in exps:
                    exps += [sched.str()]
                if sched.tail2 != None and sched.tail2.str() not in exps:
                    exps += [sched.tail2.str()]
                sched = sched.tail
        if len(exps) == max_load: 
            filt2.append([exps])
    return filt2

courselists = cl.courseLists 

#sortedsets = expandpowset(filterpowset(mkpowset(eval('cl.statsMath'))),7)
#sortedsets = sorted([sorted(x) for x in sortedsets])
#sortedsets = [x for x,_ in itertools.groupby(sortedsets)]
#file = open('statsMath.txt', 'w')
#file.truncate()
#for lst in sortedsets:
#    file.write(str(lst)+'\n')
#file.close()

for name in courselists:
    sortedsets = expandpowset(filterpowset(mkpowset(eval('cl.' + name))),7)
    sortedsets1 = [sorted(x) for x in sortedsets] 
    sortedsets2 = sorted(sortedsets)
    sortedsets3 = [x for x,_ in itertools.groupby(sortedsets2)]
    file = open(name + '.txt', 'w')
    file.truncate()
    for lst in sortedsets3:
        file.write(str(lst)+'\n')
    file.close()

