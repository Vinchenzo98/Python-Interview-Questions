
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
    stored_results = list()
    if n == 0 or k > n or k <= 0:
        print("")
    for i in range(n):  
        if i <= k:         
            nope = "nope"
            stored_results.append(nope)
                
            for j in range(len(stored_results)):
                if j < 1:
                    result = stored_results[j]

                if j > 1:
                    result = stored_results[j] + stored_results[j + 1]
                print(result)
       #string_list.append(word_part)
     

longest_consec(['hello', 'guy', 'man', 'person', 'great', 'awesome', 'television'],2)



