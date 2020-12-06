
indata = open("input.txt", "r").readlines()


for line in indata:
    bla = set()
    #print(line)
    for c in line:
        bla.add(c)
    print(bla)

print("kuksfdakgjsajgf")

###### PART 1 ######
def p1():
    yes_ans = set()
    _sum = 0
    i = 0
    for line in indata:
        i += 1
        print("i = "+str(i)+" line = "+line)

        for c in line:
            if c != '\n':
                yes_ans.add(c)
        
        print("yes_ans = "+str(yes_ans))

        if '\n' in line and len(line) == 1:
            print("len(yes_ans) = "+ str(len(yes_ans)))
            _sum += len(yes_ans)
            yes_ans = set()
        
        #yes_ans = set()

    _sum += len(yes_ans)
    print("sum = "+str(_sum))

###### PART 2 ######
def p2():
    group_yes_ans = list()
    _sum = 0
    for line in indata:
        yes_ans = set()
        #i += 1
        #print("i = "+str(i)+" line = "+line)

        for c in line:
            if c != '\n':
                yes_ans.add(c)
        
        print("yes_ans = "+str(yes_ans))
        if len(yes_ans) > 0:
            group_yes_ans.append(yes_ans)

        if '\n' in line and len(line) == 1:
            #print("len(yes_ans) = "+ str(len(yes_ans)))
            print(group_yes_ans)
            print("group yes ans:")
            for g in group_yes_ans:
                print(g)
            
            if len(group_yes_ans) == 1:
                _union = group_yes_ans[0]
            elif len(group_yes_ans) == 2:
                _union = group_yes_ans[0].intersection(group_yes_ans[1])
            elif len(group_yes_ans) > 2:
                _union = group_yes_ans[0].intersection(*group_yes_ans)
            else:
                _union = set()
            print("union = "+str(_union))
            _sum += len(_union)
            group_yes_ans = list()

    #_sum += len(yes_ans)
    if len(group_yes_ans) == 1:
        _union = group_yes_ans[0]
    elif len(group_yes_ans) == 2:
        _union = group_yes_ans[0].intersection(group_yes_ans[1])
    elif len(group_yes_ans) > 2:
        _union = group_yes_ans[0].intersection(*group_yes_ans)
    else:
        _union = set()
    print("union = "+str(_union))
    _sum += len(_union)
    print("sum = "+str(_sum))

#p1()
p2()
