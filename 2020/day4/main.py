
import re

f = open("input.txt", "r")
puzzle_input = f.read()

def validate_pp_p1(pp):
    req_props = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    props = re.findall(r"(?:^|\n| )(\w+)(?::)", pp)
    print(props)
    return all(p in props for p in req_props)

def validate_pp_p2(pp):
    valid_props = {"byr":False, "iyr":False, "eyr":False, "hgt":False, "hcl":False, "ecl":False, "pid":False}
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    props = re.findall(r"(?:^|\n| )(\w+):([\w\d#]+)(?=$|\n| )", pp)
    #print("basdf")
    #print(props)
    #names,vals = zip(*props)
    #print(names)
    #print(vals)

    for n,v in props:
        #print("--n={} v={}".format(n,v))

        if n == "byr" and 1920 <= int(v) <= 2002:
            print("valid byr: " + v+" (1920-2002)")
            valid_props["byr"] = True
        elif n == "iyr" and 2010 <= int(v) <= 2020:
            print("valid iyr: "+v+" (2010-2020)")
            valid_props["iyr"] = True
        elif n == "eyr" and 2020 <= int(v) <= 2030:
            print("valid eyr: "+v+" (2020-2030)")
            valid_props["eyr"] = True
        elif n == "hgt":
            mtch = re.match(r"(\d+)(in|cm)", v)
            if mtch != None:
                val,unit = mtch.groups()
                #print("val={} unit={}".format(val,unit))
                if (unit == "cm" and 150 <= int(val) <= 193) or (unit == "in" and 59 <= int(val) <= 76):
                    print("valid hgt: {}.{} (cm: 150-193, in: 59-76)".format(val,unit))
                    valid_props["hgt"] = True
        elif n == "hcl" and re.match(r"#[\da-f]{6}", v) != None:
            print("valid hcl: "+v)
            valid_props["hcl"] = True
        elif n == "ecl" and v in eye_colors:
            print("valid ecl: "+v+" "+str(eye_colors))
            valid_props["ecl"] = True
        elif n == "pid" and re.match(r"^\d{9}$", v) != None:
            print("valid pid: "+v+" count="+str(len(v)))
            valid_props["pid"] = True
            if (len(v) != 9):
                assert(False)
        #else:
        #    if n == "byr":
        #        print("invalid {}: {} (1920-2002)".format(n,v))
        #    elif n == "iyr":
        #        print("invalid {}: {} (2010-2020)".format(n,v))
        #    elif n == "eyr":
        #        print("invalid {}: {} (2020-2030)".format(n,v))
        #    elif n == "ecl":
        #        print("invalid {}: {} {}".format(n,v,eye_colors))
        #    elif n == "hgt":
        #        print("invalid {}: {} (cm 150-193, in 59-76)".format(n,v))
        #    else:    
        #        print("invalid {}: {}".format(n,v))
    
    print("valid_props.values = " + str(valid_props.values()))
    return all(valid_props.values())

valid_count = 0
pps = str(puzzle_input).split("\n\n")
for pp in pps:
    print("----------------")
    print(pp)
    valid = validate_pp_p2(pp)
    if valid:
        valid_count += 1
    print("------ " + str(valid))
    #input("press enter")

print("valid count = " + str(valid_count))
