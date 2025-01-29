
def xo(s):
    o = ""
    x = ""
    x_list = list()
    o_list = list()
    for i in s:
        if i == 'x' or i == 'X':
            x = i.lower()
            x_list.append(x)
            if x_list.count(x) <= 2:
                print(x_list.count(x))
        elif i == 'o' or i == 'O':
            o = i.lower()
            o_list.append(o)
            if o_list.count(o) <= 2:
                print(o_list.count(o))
    if x_list.count(x) == o_list.count(o):
        print("true")
    elif x_list.count(x) > o_list.count(o) or o_list.count(o) > x_list.count(x):
        print("false")
    else:
        print("true")
    print(s)



def digital_root(n):

    x = str(n)
    new_list = list()
    for i in x:
        new_list.append(i)
        print(new_list)
    
    print(sum(new_list))

def longest_consec(strarr, k):
    n = len(strarr)
    stored_values = list()
    if n == 0 or k > n or k <= 0:
        return ""
    for i in range(n):
        print(i)
        #new_list = list(filter(lambda i: i <= k, strarr))
        #stored_values.append(new_list)
    # print(new_list)
    # print(stored_values)
    
longest_consec(['hello', 'guy', 'man', 'person', 'great', 'awesome', 'television'],3)



