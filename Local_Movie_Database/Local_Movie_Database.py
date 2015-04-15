##CS 101
##Program 7 - Local Movie Database
##JJC7WB@mail.umkc.edu
##John Clement
##
##PROBLEM: Take the data from 3 separate csv files and display one of two sets of data.  The first is the top 10 rated movies from imdb critics of
## a specific actor or actress.  The second is to type in two separate genres and have the top 10 rated movies that are in both genres.
##
##
##ALGORITHM:  
##
##Loop from beginning in order to be able to start the code execution from the beginning
##
##    get main menu choice and validate it
##    get all the actor names
##    
##    if menu_choice == "1":
##        get all the movie genres
##        get the two movie genres to intersect from the user
##        get all the movies that are in both of the genres entered
##        pop the top ten rows off of the sorted results of the like movies found in both and display to the user by looping over tuples with "Movie name","Year made","Rating"
##        restart from the main menu
##    elif menu_choice == "2":
##        get all the actor names
##        get the actor name that the user wants to search for their movie history
##        search for all the films by that actor
##        pop the top ten rows off of the sorted results of the movies by this actor and display in descending order from greatest to least. 
##        loop over the tuples found.  a tuple in this case is the same as above: "Movie name","Year Made","Rating"
##        restart from the main menu
##    else:
##        display exit message
##        prompt if the user wants to quit the application
##Error Handling:
##
##############################################################################################################################################################


 


import csv

def validate_main_menu_choice(input1):
    done = "n"
    while done == "n":
        if input1 == "1" or input1 == "2" or input1 == "Q":
            return "y"
        else:
            return "n"    

##get the main menu choice from the user        
def main_menu():
    done = "n"
    while done == "n":
        input1 = input("Local Movie Database\n"\
                       "\n1. Find highest rated movies for 2 genres\n"\
                       "2. Show movies and ratings for a given actor\n"\
                       "Q. Quit\n\n"\
                       "==> ")
        isvalid = validate_main_menu_choice(input1)
        if isvalid == "y":
            return input1
        else:
            print("You must enter a valid choice from 1,2,Q\n\n")
            continue

##get all the movie genre names
def collect_movie_genres_from_csv():
    genres = set()
    temp_line = []
    try:
        with open("C:\\Users\\centd_000\\Desktop\\Program7\\genre.csv") as file_handle:
            reader = csv.reader(file_handle)
            for line in reader:
                if line[1] not in genres:
                    genres.add(line[1])
            return genres
    except Exception:
        print("Something went wrong when opening genre.csv")
        exit()

##validate the users movie genre entry    
def validate_movie_genre(movie_genre,movie_genres):
    if movie_genre in movie_genres:
        return "valid"
    else:
        return "invalid"

##ask the user to input movie genres
def ask_for_movie_genres(movie_genres):
    done = "n"
    while done == "n":
        print("\n")
        input1 = input("Please enter a movie genre ")
        if validate_movie_genre(input1,movie_genres) == "valid":
            input2 = input("Please enter a movie genre ")
            if validate_movie_genre(input2,movie_genres) == "valid":
                return input1,input2
        else:
            print("That genre was not found.  Please enter another one.")
            continue

##get all the actor names
def collect_actor_names():
    actors = set()
    temp_line = []
    try:    
        with open("C:\\Users\\centd_000\\Desktop\\Program7\\actor_movie.csv") as file_handle:
            reader = csv.reader(file_handle)
            for line in reader:
                if line[0] not in actors:
                    actors.add(line[0])
            return actors
    except Exception:
        print("Something went wrong when opening actor_movie.csv")
        exit()

##validate the actor name inputted by the user
def validate_actor_name(actor_name,actor_names):
    if actor_name in actor_names:
        return "valid"
    else:
        return "invalid"

##ask the user to input an actor name to search for their movie list
def ask_for_actor_name(actor_names):
    done = "n"
    while done == "n":
        print("\n")
        input1 = input("Enter the name of an actor.  It has to match exactly last, first ==> ") 
        if validate_actor_name(input1,actor_names) == "valid":
            return input1
        else:
            print("That name was not found")
            continue

##get all the movie name that this actor was in
def get_movies_for_actor(actor_name):
    movies = set()
    temp_dict = {}
    temp_line = []
    try:
        with open("C:\\Users\\centd_000\\Desktop\\Program7\\actor_movie.csv") as file_handle:
            reader = csv.reader(file_handle)
            for line in reader:
                if line[0] == actor_name:
                    if line[1] not in movies:
                        movies.add(line[1])
    except Exception:
        print("Something went wrong when opening actor_movie.csv")
        exit()
    return movies

##sort the top 10 rated movies that his actor was in
def get_top_10_movies_for_actor(movie_list):
    ordered_movies = []
    movies = set()
    temp_line = []
    try:
        with open("C:\\Users\\centd_000\\Desktop\\Program7\\movies.csv") as file_handle:
            reader = csv.reader(file_handle)
            for line in reader:
                if line[0] in movie_list:
                    movies.add((line[0],line[1],line[2]))
    except Exception:
        print("Something went wrong when opening movies.csv")
        exit()
    ordered_movies = sorted(movies,key=lambda t: t[2])
    chopped_set = ordered_movies[::-1]
    chopped_further = []
    for i in range(0,10):
        chopped_further.append(chopped_set.pop())
    return chopped_further[::-1]



##get all the movie names for both genres entered by the user 
def get_movies_from_both_genres(movie_genres_input):
    movies1 = set()
    movies2 = set()
    ordered_movies = []
    temp_dict = {}
    temp_line = []
    try:
        with open("C:\\Users\\centd_000\\Desktop\\Program7\\genre.csv") as file_handle:
            reader = csv.reader(file_handle)
            for line in reader:
                if line[1] == movie_genres_input[0]:
                    movies1.add(line[0])
                elif line[1] == movie_genres_input[1]:
                    movies2.add(line[0])
    except Exception:
        print("Something went wrong when opening genre.csv")
        exit()
    return movies1.intersection(movies2)



##intersect all the movie names gotten from the above function to see which movies that both genres have in common, and sort the top 10 list of these movie names by rating.    
def get_top_movies_from_both_genres(movies_of_both_genres):
    movies_set = set()
    ordered_movies = []
    temp_dict = {}
    temp_line = []
    try:
        with open("C:\\Users\\centd_000\\Desktop\\Program7\\movies.csv") as file_handle:
            reader = csv.reader(file_handle)
            for line in reader:   
                if line[0] in movies_of_both_genres:
                    if line[0] not in movies_set:
                        movies_set.add((line[0],line[1],line[2]))
    except Exception:
        print("Something went wrong when opening movies.csv")
        exit()
    sorted_set = sorted(movies_set,key=lambda t: t[2])
    chopped_set = sorted_set[::-1]
    chopped_further = []
    for i in range(0,10):
        chopped_further.append(sorted_set.pop())
    return chopped_further
   
    
done = "n"
while done == "n":
    menu_choice = main_menu()
    actor_names = []
    actor_name = ""
    movies_for_actor = []

    if menu_choice == "1":
        movie_genres = collect_movie_genres_from_csv()
        movie_genres_input = ask_for_movie_genres(movie_genres)
        movies_of_both_genres = get_movies_from_both_genres(movie_genres_input)
        top_movies_of_both_genres = get_top_movies_from_both_genres(movies_of_both_genres)
        print("Title\t\t\t\t\t\t\t\t   Rating")
        print("============================================================================")
        for movie in top_movies_of_both_genres:
            print(str(movie[0])+(" "*(68-len(str(movie[0]))))+str(movie[2]))
        print("\n\n")
        continue
    elif menu_choice == "2":
        actor_names = collect_actor_names()
        actor_name = ask_for_actor_name(actor_names)
        movies_for_actor = get_movies_for_actor(actor_name)
        movies_by_rating_for_actor = get_top_10_movies_for_actor(movies_for_actor)
        print("\nThe movies of {}".format(actor_name))
        print("Title\t\t\t\t\t\t\t\t   Rating")
        print("============================================================================")
        for movie in movies_by_rating_for_actor:
            print(str(movie[0])+(" "*(68-len(str(movie[0]))))+str(movie[2]))
        print("\n\n")
        continue
    else:
        print("Goodbye")
        exit()














