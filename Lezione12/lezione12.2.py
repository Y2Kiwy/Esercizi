class MovieCatalog:

    def __init__(self) -> None:
        self.catalog = {}

    def add_movie(self, director_name: str, movies: list) -> None:
        if director_name not in self.catalog:
            self.catalog[director_name] = []
        self.catalog[director_name].extend(movies)

    def remove_movie(self, director_name: str, movie_name: str) -> None:
        if director_name in self.catalog and movie_name in self.catalog[director_name]:
            self.catalog[director_name].remove(movie_name)

    def list_directors(self) -> None:
        print(f"These are the directors in the catalog:")
        for director in self.catalog.keys():
            print(f"\t{director}")

    def get_movies_by_director(self, director_name: str) -> None:
        if director_name in self.catalog:
            print(f"These are the movies for {director_name} in the catalog:")
            for movie in self.catalog[director_name]:
                print(f"\t{movie}")
        else:
            print(f"No movies found for {director_name}")

# Test case
def main():
    catalog = MovieCatalog()

    # Test adding movies
    catalog.add_movie('Christopher Nolan', ['Inception', 'Interstellar'])
    print("After adding movies to Nolan:")
    catalog.get_movies_by_director('Christopher Nolan')
    
    catalog.add_movie('Christopher Nolan', ['Dunkirk'])
    print("After adding more movies to Nolan:")
    catalog.get_movies_by_director('Christopher Nolan')
    
    catalog.add_movie('Quentin Tarantino', ['Pulp Fiction'])
    print("After adding movies to Tarantino:")
    catalog.get_movies_by_director('Quentin Tarantino')

    # Test listing directors
    print("List of directors:")
    catalog.list_directors()

    # Test removing movies
    catalog.remove_movie('Christopher Nolan', 'Inception')
    print("After removing 'Inception' from Nolan:")
    catalog.get_movies_by_director('Christopher Nolan')

    catalog.remove_movie('Quentin Tarantino', 'Pulp Fiction')
    print("After removing 'Pulp Fiction' from Tarantino:")
    catalog.get_movies_by_director('Quentin Tarantino')

    # Test removing movie that doesn't exist
    catalog.remove_movie('Christopher Nolan', 'Nonexistent Movie')
    print("After attempting to remove a nonexistent movie from Nolan:")
    catalog.get_movies_by_director('Christopher Nolan')

    # Test listing directors when catalog is empty
    catalog.remove_movie('Christopher Nolan', 'Interstellar')
    catalog.remove_movie('Christopher Nolan', 'Dunkirk')
    print("List of directors after removing all movies:")
    catalog.list_directors()

if __name__ == "__main__":
    main()
