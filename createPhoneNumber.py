def create_phone_number(n):
    turned_string = str(n)
    split_list = turned_string.lstrip("[").rstrip("]").split(",")
    
    new_dict = {
        "part1":{
           
        },
        "part2":{
           
        },
        "part3":{
           
        }
    }
     
    new_list = [split_list[i].strip() for i in range(len(split_list)) if i < len(split_list)]
   
    for j in range(len(new_list)):
        if j < 3:
           new_dict["part1"][j] = new_list[j]
        elif j >=3 and j <= 5:
           new_dict["part2"][j] = new_list[j]
        else:
           new_dict["part3"][j] = new_list[j]
    
    
    combine_part_1 = "".join(new_dict["part1"].values())
    combine_part_2 = "".join(new_dict["part2"].values())
    combine_part_3 = "".join(new_dict["part3"].values())
    
    result = f"({combine_part_1}) {combine_part_2}-{combine_part_3}"

create_phone_number([1,2,3,4,5,6,7,8,9,0]) 