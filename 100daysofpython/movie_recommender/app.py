from utils.movies import Movie


def heading():
    print("%"*90)
    print("\t"*4, "Python Movie Recommender")
    print("%"*90)


def prompt_all_movies(movies):
    for movie in movies:
        print(f"Movie: {movie.get('movie')}")
        print(f"Genre:{movie.get('genre')}")
        print(f"Ratings: {movie.get('ratings')}\n")


def prompt_random_movie(movies):
    print(f"Movie: {movies.get('movie')}")
    print(f"Genre:{movies.get('genre')}")
    print(f"Ratings: {movies.get('ratings')}\n")


def main():
    heading()
    choice = int(input(
        "1. Get all movies between provided year\n2. Get a random movie between provided year\n:"))
    if choice in [1, 2]:
        from_year = int(input("From Year: "))
        to_year = int(input("To Year: "))
        if from_year and to_year:
            movies = Movie(from_year, to_year)
            if choice == 1:
                print(f"Movies between year {from_year} - {to_year}")
                prompt_all_movies(movies.get_all_movies())
            elif choice == 2:
                prompt_random_movie(movies.get_random_movie())
    else:
        print("Options were 1 and 2")


if __name__ == '__main__':
    main()
