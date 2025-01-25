
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
    string_list = list()
    stored_results = list()
    if n == 0 or k <= 0 or k <= 0:
        print("")
    for i in range(0,n):  
        word_part = strarr[i]
        string_list.append(word_part)
        if len(string_list) == k:
            for j in range(0, len(string_list)):
                if j == k - 1:
                    if j < n:
                       result = string_list[j - 1]  + string_list[j]
                    elif j == n:
                       result = string_list[n - 1] + string_list[n] 
                    stored_results.append(result)
            
            print(stored_results)
            string_list.clear()

longest_consec(['hello', 'guy', 'man', 'person', 'great', 'awesome', 'television'],2)





