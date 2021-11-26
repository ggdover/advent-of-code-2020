
tests = [
    ("BFFFBBFRRR", 70, 7, 567),
    ("FFFBBBFRRR", 14, 7, 119),
    ("BBFFBBFRLL", 102, 4, 820)
]

# Get Row Column and Seat id
def get_row_col_sid(chars):
    rows = list(range(0,128))
    cols = list(range(0,8))

    row_chars = chars[:7]
    col_chars = chars[7:]

    for c in row_chars:
        if c == 'F':
            rows = rows[:len(rows)//2]
        elif c == 'B':
            rows = rows[len(rows)//2:]
        #print("rows = "+str(rows))

    assert(len(rows) == 1)

    for c in col_chars:
        if c == 'L':
            cols = cols[:len(cols)//2]
        elif c == 'R':
            cols = cols[len(cols)//2:]
    assert(len(cols) == 1)

    sid = rows[0] * 8 + cols[0]
    #print(sid)

    return rows[0], cols[0], sid

######### PART 1 TESTS #########
for chars, trow, tcol, tsid in tests:
    row, col, sid = get_row_col_sid(chars)
    assert(row == trow)
    assert(col == tcol)
    assert(sid == tsid)
    print("Test Passed!")
print("All tests done")

indata = open("input.txt", "r").readlines()

############ PART 1 ############
maxsid = 0
for line in indata:
    egg, spam, sid = get_row_col_sid(line)
    maxsid = max(maxsid, sid)
print("Maxsid = "+str(maxsid))


minsid = float("inf") # Set to number higher than any other int value
for line in indata:
    egg, spam, sid = get_row_col_sid(line)
    minsid = min(minsid,sid)
print("Minsid = "+str(minsid))
    #for line2 in indata:
    #    if (line != line2):
    #        egg, spam, sid = get_row_col_sid(line)
    #        egg2, spam2, sid2 = get_row_col_sid(line2)

    #        if (sid - sid2 == 2):
    #            print("interval is 2 - sid: "+str(sid)+" and sid"+str(sid2))

seats = list(range(96,912))
print(seats)
for line in indata:
    egg, spam, sid = get_row_col_sid(line)
    seats.remove(sid)
print(seats)
