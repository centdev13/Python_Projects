##CS 101
##Program 5 - Image Stacking
##JJC7WB@mail.umkc.edu
##John Clement
##
##PROBLEM: We allow the user to specify a specific file directory on their system and then we average the rgb values of all the pictures in a certain way so that we get a clearer picture that we can then output to the user.
##
##ALGORITHM:
##main code goes here:
##
##function for returning the users menu choice
##function for returning the handle to the directory supplied by the user
##function for creating a list of the folder's ppm files
##
##function for creating a list of content lists containing all the contents of each ppm file.  used for validation and averaging.
##loop until the user enters a valid file name to save the output as.
##    -ask for file path until no exception.
##    -if exception, start the loop over..
##
##generate an averages list of all the rgb values in all the contents lists inside the folder specified.  this is the list that will be used to generate the output ppm file.
##open file handle with new ppm output file name
##    -write everything in this rgb averages list to the new file.
##close the newly outputed file.
##inform the user that the file has been written.
##ERROR HANDLING:
##Whenever anything could go wrong, it will save me time to use exception handlers to output the error messages for the user not entering a valid directory, not more than 4ppm files in the directory, not a valid name for the output file,
## 
########################################################################################################################################################################################################################################				


##API Help:
##
##import os
##os.path.isdir ( path ) Given
##       a path as a string returns True if the path is a valid directory.
##os.path.isfile ( file ) Given
##       a string as a string returns True if file is an actual file..
##os.listdir( path ) Returns
##       a list of strings of filenames in the path given. If no Path is given the current working directory is used.
##os.path.splitext ( file ) Given
##       a filename it splits the extension off. You get a tuple of 2 strings. The first part being the portion before
##       the extension, and the second is the file extension.
##os.path.join( value, [value]... ) Takes
##       any number of strings and returns a concatenated string separated by the default file system separator.
##       ( / for Unix and mac, \ for Windows )
##
## Example:   C:\Users\centd_000\Desktop\Program5\Image1
## Example:   C:\Users\centd_000\Desktop\fun.ppm



##modules:
import os
import string

##check each file's contents for valid p3 headers
def validate_p3_header(listlists):
    done = "n"
    temp_list1 = []
    testvar = ""
    for filecontents in listlists:
        temp_list1.append(filecontents[0])
    if temp_list1.count("P3") != len(listlists):
        return "Not all the files have a valid P3 header."
    else:
        return "valid"
##check each file's contents for the same resolution
def validate_resolution(listlists):
    done = "n"
    temp_list2 = []
    testvar = ""
    for filecontents in listlists:
        temp_list2.append(filecontents[1])
    while done == "n":
        for i in temp_list2:
            testvar = i
            done = "y"
    if temp_list2.count(i) != len(listlists):
        return "The resolution was not the same on all images."
    else:
        return "valid"
##check each file's contents for the same color depth
def validate_color_depth(listlists):
    done = "n"
    temp_list3 = []
    testvar = ""
    for filecontents in listlists:
        temp_list3.append(filecontents[2])
    while done == "n":
        for i in temp_list3:
            testvar = i
            done = "y"
    if temp_list3.count(i) != len(listlists):
        return "The color depth was not the same on all the images."
    else:
        return "valid"
##put file names of type ___ in a list and return it
def enumerate_dir_ppm_file_names(directory_path,file_ext):
    all_ppm_files = []
    ##walk the subdirectories and files starting at the directory path that is specified by a parameter
    ## passed to the function
    for dirfile in os.listdir(directory_path):
        name = os.path.splitext(dirfile)[0]
        ext = os.path.splitext(dirfile)[1]
        joined = dirfile
        if ext == ".PPM" or ext == ".ppm":
            all_ppm_files.append(directory_path+"\\"+dirfile)
    if len(all_ppm_files) < 4:
        return "The directory must have 4+ files of extension .ppm"
    return all_ppm_files
##create a list of content lists containing the content of all the ppm files, getting ready to validate p3 header, color resolution, and color depth
def enumerate_file_content_lists(list_of_filenames):
    counter1 = 0
    listlists = []
    temp_list = []
    for filename in list_of_filenames:
        filehandle = open(filename)
        for line in filehandle:
            temp_list.append(line)
        listlists.append(temp_list)
        filehandle.close()
        counter1+=1
        temp_list = []
    if len(listlists) < 4:
        return Exception
    return listlists
##is this a valid directory path?
def validate_directory_path(dir_search):
    return os.path.isdir(dir_search)

##get the folder the user wants to enumerate a list of ppm files for
def get_path():
    done = "n"
    while done == "n":
        try:
            a = ask_for_directory()
            return a
        except FileNotFoundError:
            print("You must enter a valid image directory.")
            continue
    

##ask the user to input the folder to enumerate
def ask_for_directory():
    done1 = "n"
    while done1 == "n":
        try:    
            dir_search = input("\n\n\nEnter a valid image directory ==>  ")
            dir_path = validate_directory_path(dir_search) 
            if dir_path == True:
                return dir_search
            else:
                raise Exception
        except Exception:
            print("Invalid input")
            continue
##get the average number in a list, used for averaging pixels across all ppm files
def get_list_avg(list_name):
    temp_list = []
    temp_list2 = []
    for char in list_name:
        temp_list.append(char.replace('\n',''))
    for char2 in temp_list:
        temp_list2.append(int(char2))
    return sum(temp_list2)/len(temp_list2)

##create final list of averaged values to be written to a new ppm file.
def parse_rgb_file_list_contents(listlists):
    temp_list = []
    rgb_avgs_list = []
    header = listlists[0][:3]
    counter = 4
    length = len(listlists[0])

    ##for each index of the file contents of a filecontents list:
    for num in range(3,length):
        for file in listlists:
            temp_list.append(file[num])
        avg = get_list_avg(temp_list)
        rgb_avgs_list.append(avg)
        temp_list = []
    for i in header[::-1]:
        stripit = i.replace("\n","")
        rgb_avgs_list.insert(0,stripit)
    
    return rgb_avgs_list

##get the initial menu choice
def get_choice():
    final_result = ""
    done = "n"
    while done == "n":    
        menu_choice = input("""\t\t\tImage Stacker Menu\n
        1. Image Stack PPM
        Q. Quit\n
        ==> """).upper()
        if menu_choice not in ["1","2","Q"]:
            print("You must enter a valid choice to continue")
            continue
        else:
            if menu_choice == "1":
                final_result = ".ppm"
            elif menu_choice == "2":
                final_result = ".jpeg"
            elif menu_choice == "Q":
                exit()
            return final_result


    

##main code goes here:
##get the main menu choice
choice = get_choice()
##loop until directory fully validated, compiling content lists of each of the ppm files
loopit = "y"
while loopit == "y":
    path = get_path()
    filename_list = enumerate_dir_ppm_file_names(path,choice)
    try:
        listlists = enumerate_file_content_lists(filename_list)
        loopit = "n"
    except Exception:
        print("You must specify a directory with at least 4 files of file type .ppm")
        continue
done = "n"
##loop until the output file name is validated
while done == "n":
    try:
        output_name = input("What would you like the output file to be saved as?  ==>  ")
        done = "y"
    except Exception:
        print("You entered invalid input for the name.")
        continue

##average the content lists of all the ppm files into one list, which we will use to create the final ppm file.
done = parse_rgb_file_list_contents(listlists)
##just in case, if the output name the user supplies does not include the .ppm file extension, add it and then open the new file, write to it, and inform the user when the file has been fully written.
if output_name[-4:] != ".ppm":
    output_name += ".ppm"
file_handle = open(output_name,"w")
for i in range(0,1600000):
    try:
        print(done[i],file=file_handle)
    except IndexError:
        break
file_handle.close()
print("file written")




































































