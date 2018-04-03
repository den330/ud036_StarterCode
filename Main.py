import Model
import fresh_tomatoes

# Serves as starting point running this program.

movie_2012 = Model.Media("2012",
                         "A story about the end of the world",
                         "https://upload.wikimedia.org/wikipedia/en/d/dd/2012_Poster.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=ce0N3TEcFw0")

movie_the_silence_of_the_lambs = Model.Media("The Silence of the Lambs",
                                             "A story about seriel killer",
                                             "https://upload.wikimedia.org/wikipedia/en/8/86/The_Silence_of_the_Lambs_poster.jpg",  # NOQA
                                             "https://www.youtube.com/watch?v=ZWCAf-xLV2k")  # NOQA
movie_the_last_jedi = Model.Media("Star Wars: The Last Jedi",
                                  "Star Wars",
                                  "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg",  # NOQA
                                  "https://www.youtube.com/watch?v=Q0CbN8sfihY")  # NOQA


movies = [movie_2012, movie_the_silence_of_the_lambs, movie_the_last_jedi]

fresh_tomatoes.open_movies_page(movies)


