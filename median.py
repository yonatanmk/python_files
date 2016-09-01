def median(seq):
    seq.sort()
    print (seq)
    if len(seq) % 2 == 1:
        print ("Odd number of items")
        print ("the median position is %s" % (int(len(seq) / 2 + 1)))
        return seq[int(len(seq) / 2)]
    else:
        print ("Even number of items")
        print ("the median positions are %s and %s" % (int(len(seq) / 2), int(len(seq) / 2 + 1)))
        print ("the median values are %s and %s" % (seq[int(len(seq) / 2 - 1)], seq[int(len(seq) / 2)]))
        medvalue = float(seq[int(len(seq) / 2 - 1)] + seq[int(len(seq) / 2)]) / 2
        return medvalue

print (median([8, 4, 4, 5, 6, 7]))
