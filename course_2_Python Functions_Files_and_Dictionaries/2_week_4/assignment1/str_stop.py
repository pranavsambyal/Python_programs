'''Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to
return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches\
 the string “STOP” (it should not contain the string “STOP”).'''

def sublist(s):
    x=0
    rts=[]
    while not s[x]=='STOP':

        rts.append(s[x])
        x = x + 1

     return rts