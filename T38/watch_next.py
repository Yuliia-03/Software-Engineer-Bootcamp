import spacy
nlp = spacy.load('en_core_web_md')


class Movie:

    def __init__(self, name: str, description: str) -> None:

        # in this function, you must initialise the following attributes:
        #    ● name,
        #    ● description
        self.name = name
        self.description = description
    
    # returns the description similarity of two movies
    def movie_similarity(self, other: "Movie") -> float:
        return nlp(self.description).similarity(nlp(other.description))

# reads in the movies.txt file
# saves every film in the list as a Movie object
# returns a list of Movie objects
def read_file(file_name: str) -> list:
    
    films = []
    with open(f'./{file_name}.txt', 'r')as f:
        for line in f:
            
            name = line.split(':')[0][:-1]
            description = line.split(':')[1][:-1]
            films.append(Movie(name, description))
    
    return films

# returns the name of the next recommended movie to watch 
# that is most similar to the previously watched movie 
# among all the movies in the list
def find_next_film(films: list, previous_film: Movie) -> str:
    
    max_similarity = 0
    next_film = previous_film

    for i in films:
        
        similarity = i.movie_similarity(previous_film)
        #print(i.name, ' - ', similarity, ' - ', i.description)

        if similarity > max_similarity:
            next_film = i
            max_similarity = similarity

    return next_film.name

film = 'Planet Hulk'
description = '''Will he save their world or destroy it? 
                When the Hulk becomes too  dangerous for 
                the Earth, the Illuminati trick Hulk into 
                a shuttle and launch him into space to a 
                planet where the Hulk can live in peace. 
                Unfortunately, Hulk land on the planet 
                Sakaar where he is sold into slavery and 
                trained as a gladiator.'''


films = read_file('movies')

# prints out the result
print(find_next_film(films, Movie(film, description)))

    