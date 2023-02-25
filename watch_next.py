import spacy
# load pre-trained English model from spacy
nlp = spacy.load('en_core_web_md')

# define a function that takes in a description of a movie as a parameter and returns the title of the most similar movie
def suggestion(description):
    similarity = 0
    # loop throuh the list of movie descriptions
    for i, movie_descr in enumerate(description):
        # convert a description to a spacy Doc object
        movie_descr_nlp = nlp(movie_descr)
        # finf the similarity score between descriptions of the film Planet Hulk and films from the list movie_descr
        compare = planet_hulk_nlp.similarity(movie_descr_nlp)
        # update the similarity score and index of the most similar movie
        if compare > similarity:
            similarity = compare   
            y = i
    
    return title[y]

# open a text file movies.txt and read lines from it
movies = open("movies.txt", "r")
lines = movies.readlines()

# initialise empty lists to store titles and descriptions of the movies
title = []
descr = []

# loop through lines in the file
for line in lines:
    # split each line into title and description and append them to the corresponding lists
    movie = line.strip("\n").split(" :")
    title.append(movie[0])
    descr.append(movie[1])

movies.close()


planet_hulk = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati
trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in piece. Unfortunately, Hulk
land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""
# convert the text of the variable planet_hulk into a spacy Doc object
planet_hulk_nlp = nlp(planet_hulk)

# call function suggestion and pass descr as an argument, store the return of the function in a variable and print it out
similar_movie = suggestion(descr)
print(f"The title of the most similar movie is {similar_movie}")