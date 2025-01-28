def descending_order(num):
    num_as_string = f"{num}"
    numbers = list()
    for i in num_as_string:
        numbers.append(int(i))
        numbers.sort(reverse=True)
    result = int("".join(map(str, numbers)))
    print(result)
   
#descending_order(12345)

# -1429,-1581

#-619010.0


def get_sum(a,b):
    if a == b:
        return a
    
    store_list = list()
    new_list = list()
    new_list.append(a)
    new_list.append(b)
    if b < a and b < 0 and a < 0:
        new_list
    else: 
        new_list.sort()

    start_list = new_list[0]
    end_list = new_list[1]

    if start_list < 0 and end_list < 0 and end_list < start_list:
        iterations = end_list - 1
        start_index = start_list
        step = - 1

    else:
        iterations = end_list + 1
        start_index = start_list 
        step = 1
    
    for i in range(start_index, iterations, step):
        store_list.append(i)
        print("list so far:", store_list, "SUM: ", sum(store_list))
    
    print("sum of list is", sum(store_list))


get_sum(-595, -3087)

