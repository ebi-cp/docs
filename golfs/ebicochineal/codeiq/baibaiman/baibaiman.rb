# l=[1]+[0]*4;eval('puts a+b+c+d+e;a,b,c,d,e=l;l=d+e,d+a,b,e,c;'*100)
# l=[1]+[0]*4;100.times{a,b,c,d,e=l;puts a+b+c+d+e;l=d+e,d+a,b,e,c}

a=b=c=d=1;eval'puts a;a,b,c,d=b,c,d,d-c+b+a;'*100
# a=b=c=d=1;100.times{puts a;a,b,c,d=b,c,d,d-c+b+a}

########################################
# l=[1]*4;eval'puts a;a,b,c,d=b,c,d,d-c+b+a;'*100

# a=b=c=d=1;for i in 0..99{puts a;a,b,c,d=b,c,d,d-c+b+a}


# a=b=c=d=1;100.times{puts a;a,b,c,d=b,c,d,d-c+b+a}



# a=b=c=d=1;eval'puts a;a,b,c,d=b,c,d,d-c+b+a;'*100


# l=[1]*4;100.times{eval'l=[%d-%d+%d+%d,%d,%d,%d];puts %d'%(l*2)}
######################################

