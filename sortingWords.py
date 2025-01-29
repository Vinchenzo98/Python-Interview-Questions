def order(sentence):
    if sentence == "":
        return ""
    
    split_by_whitespace = sentence.split(" ")
    whitespace_list = list(split_by_whitespace)
    for i in whitespace_list:
        for j in i:
            if j.isdigit():
                set_position = int(j)
                whitespace_list.insert(set_position ,i)
                string_index = whitespace_list.index(i)
                whitespace_list.remove(whitespace_list[string_index])
                print(whitespace_list)
               
     
order("4of Fo1r pe6ople g3ood th5e the2")
