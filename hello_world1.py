print ("hello_world")

def mean (listsofnumbers):
    return sum(listsofnumbers)/ len(listsofnumbers)

def median(morenumbers):
    morenumbers = sorted(morenumbers)
    n = len(morenumbers)
    if n % 2 == 0:
        return (morenumbers[n//2 - 1] + morenumbers[n//2]) / 2
    else:
        return morenumbers[n//2]