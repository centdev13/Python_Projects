import csv

##functions
def get_csv_file():
    done = "n"
    while done == "n":
        try:
            input1 = input("Enter the name of the rating csv file ==>")
            csv_handle = open(input1)
            csv_handle.close()
            return "valid"
        except Exception:
            print("Try again.")

def get_user_names():
    with open("C:\\Users\\centd_000\\Desktop\\tvrating.csv") as file_handle:
        reader = csv.reader(file_handle)
        counter1a = 0
        counter4 = 0
        names = []
        for line in reader:
            if counter4 == 0:
                counter4+=1
                continue
            else:
                for index in line:                    
                    names.append(index)
                    break
        return names

def get_show_names():
    with open("C:\\Users\\centd_000\\Desktop\\tvrating.csv") as file_handle:
        reader = csv.reader(file_handle)
        counter1 = 0
        counter2 = 0
        listshows = []
        for line in reader:
            if counter1 == 0:                
                for index in line:
                    if counter2 == 0:
                        counter2+=1
                        continue
                    else:
                        listshows.append(index)
                counter1+=1
            else:
                break
        
        return listshows

def validate_csv_user_name(names):
    done = "n"
    while done == "n":
        name = input("Enter the name of the user to get recommendations for ==>  ")
        if name in names:
            return name
        else:
            print("You've entered a name that is not in our list of names.  Try again.")
            continue

def get_other_users_names(name,names):
    new_list = names.copy()
    new_list.remove(name)
    return new_list



    

def get_row(name,show_names):
    with open("C:\\Users\\centd_000\\Desktop\\tvrating.csv") as file_handle:
        reader = csv.reader(file_handle)
        counter1 = 0
        counter2 = 0
        counter3 = 0
        row = {}
        for line in reader:
            row["Name"] = name
            if counter1 == 0:
                counter1+=1
                continue
            elif counter1 > 0:                
                for index in line:
                    if index == name:                        
                        for index2 in line:
                            if counter2 == 0:
                                counter2+=1
                                continue
                            else:
                                row[show_names[counter3]] = index2
                                counter3+=1
                    else:
                        break
        return row



def get_compared_to_rows(names_list,show_names):
    list_of_dictionaries = []
    for name in names_list:
        list_of_dictionaries.append(get_row(name,show_names))
    return list_of_dictionaries



##get menu options, and validate them...
def get_menu_choice():
    done = "n"
    while done == "n":
        main_menu_choice = input("Do you want to show\n"\
                                 "1. All Movies\n"\
                                 "2. Movies that the user has not seen\n"\
                                 "==> (1 or 2)  ")
        if main_menu_choice == '1' or '2':
            return main_menu_choice
        else:
            continue

##def reset_keys_in_line_dict(fresh_line_dict):
##    with open("C:\\Users\\centd_000\\Desktop\\tvrating.csv") as file_handle:
##        reader = csv.reader(file_handle)
##        counter1a = 0
##        fresh_line_dict = {}
##        for line in reader:
##            if counter1a == 0:
##                for index in line:
##                    print(index)
##                    fresh_line_dict[index] = ""
##                counter1a+=1
##            else:
##                break
##    return fresh_line_dict

def get_all(single_row_compared_against,other_rows):
    master_list = []
    temp_dict = {}
    temp_val = ""
    row_total = 0
    temp_var = ""
    temp_var2 = ""
    for dict1 in other_rows:
        temp_var = dict1["Name"]
        temp_var2 = ""
        temp_dict["Name"] = temp_var
        for key,value in dict1.items():
##            temp_dict[key] = single_row_compared_against[key]*value
            try:
                temp_val = int(single_row_compared_against[key])
                temp_val2 = int(value)

##                print("\n")
##                print("key from compared against row: {}".format(single_row_compared_against[key]))
##                print("current row index: {}".format(value))
##                print("result of index quantation: {}".format(int(single_row_compared_against[key])*int(value)))
                row_total += int(single_row_compared_against[key])*int(value)
##                print("\n")
            except Exception:
                pass
##        print("{} compared to -> {}".format(single_row_compared_against["Name"],temp_dict["Name"],))
##        print("row total: {}".format(row_total))
        temp_dict[temp_dict["Name"]] = row_total
        del temp_dict["Name"]
        row_total = 0
        
    return temp_dict        

def get_unseen(row_dictionary):
    shows_unseen = []
    for key,value in row_dictionary.items():
        if value == "0":
            shows_unseen.append(key)
        continue

    return shows_unseen

def get_top_5_rows(new_top_5,all_other_rows):
    ##all_other_rows = list of dictionaries
    row = {}
    master_list = []
    for dict1 in all_other_rows:
        if dict1["Name"] in new_top_5:
            row["Name"]=dict1["Name"]
            for key,value in dict1.items():
                row[key]=value
            master_list.append(row)
            row = {}
    return master_list
        
    
            
    

##def make_comparisons(show_names,menu_choice,top_5,all_other_users):
##    results = get_all()
##    output_tuples = tuple()
##    columns = []
##    if menu_choice == "1":
##            
##    elif menu_choice == "2":
##        results = get_unseen()        
##    return None


def avg_column(name,show_name,list_of_dictionaries):
    
    listall = []
    dictionary1 = {}
    sum_list = 0
    test_var = 0
    avg_likeness = ""
    avg_total = ""
    for dictionary in list_of_dictionaries:
        for key,value in dictionary.items():
            if key == "Name":
                pass
            elif key == show_name:
                listall.append(int(dictionary[show_name]))
                break

    dictionary1[show_name] = sum(listall)/len(listall)
    return dictionary1[show_name]
        
        
                

##        for key,value in dictionary.items():
##            try:
##                listit.append(int(dictionary[show_name]))
##            except Exception:
##                pass
##    dictionary1[show_name] = sum(listit)/len(listit)  
##    return dictionary1
    return listall
      

def generate_tuples(name,show_names,top_5_rows,other_rows):
    avgs = []
    avgs_done = []
    tup = tuple()
    tup2 = tuple()
    
    for show in show_names:
        avg_likeness = avg_column(name,show,top_5_rows)
        avg_total = avg_column(name,show,other_rows)
        tup = (show,avg_likeness,avg_total)
        avgs.append(tup)

##    for avg in avgs:
##        print(avg)
##    print("\n")
##    print("Avg likeness of {} is {}".format(show,avg_likeness[show]))
##    print("Avg total of {} is {}".format(show,avg_total2))
##    print("\n")
##        sorted_results = sorted(tup,key=lambda t: t[1])
##        sorted_descending = sorted_results[::-1]
##        avgs_done.append(sorted_descending)

    return avgs


def re_play():
    print("\n\n")
    input1 = input("Do you want to play again? (Y, YES, N or NO) ==>  ")
    print("\n\n")
    if input1.upper() == "Y" or input1.upper() == "YES":
        return "loop"
    else:
        print("Goodbye..")
        exit()

##passed to this list will be a list of dictionaries with this format...
##[{""},{},{},{},{},etc..]
def generate_output_stage_1(csv_user_name,list_tuples,top_5):
    temp_list = []
    new_tuples_list = []
    print("\nRecommended Shows for user {}\n"\
          "Like users {}, {}, {}, {}, {}\n"\
          "Show\t\t\t\t\t   Avg_Likeness\t\tAvg Total\n"
          "========================================================================="\
          .format(csv_user_name,top_5[0],top_5[1],top_5[2],top_5[3],top_5[4]))
    for a,b,c in list_tuples:
        new_tuples_list.append((a, b, str(round(c,4))))
    for a,b,c in new_tuples_list:
        print(str(a)+(" "*(43-len(str(a))))+str(b)+(" "*(21-len(str(b))))+str(c))       
##    for line in range(0,9):
##        print(str(a)+(" "*(43-len(a)))+str(b)+(" "*(21-len(b)))+str(c))





##passed to this list will be a list of dictionaries with this format...
##[{""},{},{},{},{},etc..]
def generate_output_stage_2(csv_user_name,list_tuples,top_5,shows_unseen):
    new_tuples_list = []
    print("\nRecommended Shows for user {}\n"\
          "Like users {}, {}, {}, {}, {}\n"\
          "Show\t\t\t\t\t   Avg_Likeness\t\tAvg Total\n"
          "========================================================================="\
          .format(csv_user_name,top_5[0],top_5[1],top_5[2],top_5[3],top_5[4]))
    counter1 = 0
    for aa,bb,cc in list_tuples:
        if aa in shows_unseen:
            temp_list2.append((aa, bb, str(round(cc,4))))
            counter1+=1
        else:
            counter1+=1
            continue  
    for a,b,c in temp_list2:
        print(str(a)+(" "*(43-len(str(a))))+str(b)+(" "*(21-len(str(b))))+str(c))       
##    for line in range(0,9):
##        print(str(a)+(" "*(43-len(a)))+str(b)+(" "*(21-len(b)))+str(c))







done = "n"
while done == "n":
    ##logic
    names = []
    other_users_names = []
    show_names = []
    csv_user_name = ""
    menu_choice = ""
    output_ready = ""
    csv_file = get_csv_file()
    sorted_results = []
    avgs_dict = []
    shows_unseen = []
    new_dict1 = {}
    top_5 = []
    new_top_5 = []
    output_list = []
    output_list2 = []
    output_dict1 = {}
    temp_list = []
    temp_list2 = []
    ask_replay = ""
    
    if csv_file == "valid":
        names = get_user_names()
        show_names = get_show_names()
        csv_user_name = validate_csv_user_name(names)
        other_users_names = get_other_users_names(csv_user_name,names)
        single_row_compared_against = get_row(csv_user_name,show_names)
        shows_unseen = get_unseen(single_row_compared_against)
        shows_unseen2 = shows_unseen.copy()
        other_rows = get_compared_to_rows(other_users_names,show_names)
        for key,value in single_row_compared_against.items():
            if value != 0:
                shows_unseen.append(key)
        menu_choice = get_menu_choice()
        comparisons = get_all(single_row_compared_against,other_rows)
        sorted_results = sorted(comparisons.items(),key=lambda t: t[1])
        sorted_descending = sorted_results[::-1]
        top_5 = sorted_descending[0:5]
        for a,b in top_5:
            new_top_5.append(a)
        top_5_rows = get_top_5_rows(new_top_5,other_rows)
    ##    print("top_5_rows type = {}".format(type(top_5_rows)))
    ##    print("top_5_rows member type = {}".format(type(top_5_rows[0])))
    ##    print("other rows type = {}".format(type(other_rows)))
    ##    print("other rows member type = {}".format(type(other_rows[0])))
    ##    print("number of rows in other rows = {}".format(len(other_rows)))
    ##    print("number of rows in top 5 rows = {}".format(len(top_5_rows)))
    ##    print("".format())
        
        show_tuple_list = []
        
        ##if menu choice is 1
        if menu_choice == "1":
            for show in show_names:
                show_tuple_list.append((show,avg_column(csv_user_name,show,top_5_rows),avg_column(csv_user_name,show,other_rows)))
            ##        generate_tuples(csv_user_name,show_names,top_5_rows,other_rows)                          
            
    ##            avg_column(csv_user_name,show,other_rows)
            sorted_results = sorted(show_tuple_list,key=lambda t: t[1])
            sorted_descending = sorted_results[::-1]
            generate_output_stage_1(csv_user_name,sorted_descending,new_top_5)
            ask_replay = re_play()
            if ask_replay == "loop":
                continue
        elif menu_choice == "2":
            for show in show_names:
                show_tuple_list.append((show,avg_column(csv_user_name,show,top_5_rows),avg_column(csv_user_name,show,other_rows)))
            ##        generate_tuples(csv_user_name,show_names,top_5_rows,other_rows)                          
            
    ##            avg_column(csv_user_name,show,other_rows)
            sorted_results = sorted(show_tuple_list,key=lambda t: t[1])
            sorted_descending = sorted_results[::-1]
            generate_output_stage_2(csv_user_name,sorted_descending,new_top_5,shows_unseen2)
            ask_replay = re_play()
            if ask_replay == "loop":
                continue
    ##        sorted_results = sorted(show_tuple_list,key=lambda t: t[1])
    ##        sorted_descending = sorted_results[::-1]
    ##        generate_output_stage_(csv_user_name,sorted_descending,new_top_5)   


                
    ##    print("inner containers for top_5_rows are: {}".format(type()))
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
    ##    print("".format())
            
        ##if menu choice is 2






    
    

        

    
    
##    output_ready = generate_output_stage_1(menu_choice)
##    print(get_all(single_row_compared_against,other_rows))
##compared_to_rows = get_other_users_rows(other_users_names)
##menu_choice = get_menu_choice()
##output_ready = generate_output_stage_1(menu_choice)
