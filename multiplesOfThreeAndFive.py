def solution(number):
    result_list_five = list()
    result_list_three = list()
    for i in range(1, number):
        multiple_five = i % 5
        multiple_three = i % 3
        if multiple_five < 0 or multiple_three < 0:
            return 0
        if multiple_five == 0 and i != 0:   
            result_list_five.append(i)
            print(f"{i} is a multiple of {number}")
        elif multiple_three == 0:  
            result_list_three.append(i)
            print(f"{i} is a multiple of {number}")
        else:
            print(f"{i} is not a multiple of {number}")
    result_list_five.extend(result_list_three)
    
    
    count = 0
    for i in result_list_five:
        count += i
    print(f"number of {number} equals {count}")
   
solution(15)