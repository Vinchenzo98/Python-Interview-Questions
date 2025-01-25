def order(sentence):
    if sentence == "":
        return ""
    
    new_list = list()
    
    split_by_whitespace = sentence.split(" ")
    whitespace_list = list(split_by_whitespace)
    for i in whitespace_list:
        for j in i:
            if j.isdigit():
                new_list.append(j)
                new_list.sort()    
                print(new_list)

            
    for k in new_list:
        for h in whitespace_list: 
            if k in h:   
                index_value = whitespace_list.index(h)
                new_list.insert(index_value, h)

        # if k == j:
        #     new_list.insert(index_value, i)
        #     remove_value = index_value + 1
        #     remove_index = new_list[remove_value]
        #     new_list.remove(remove_index)  
        #     print(new_list)

            
order("4of Fo1r pe6ople g3ood th5e the2")



#use mapping to do it in refactor