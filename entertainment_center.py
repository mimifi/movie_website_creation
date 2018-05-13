import fresh_tomatoes
import media

rubber = media.Movie("Rubber",
                     "A tire that comes to life and kills people with its psychic powers",
                     "https://images-na.ssl-images-amazon.com/images/I/81ixc5%2BQjQL._SL1500_.jpg",
                     "https://www.youtube.com/watch?v=eLJljwH_wR0")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://images-na.ssl-images-amazon.com/images/I/81Nh4sSvSaL._SL1500_.jpg",
                     "https://www.youtube.com/watch?time_continue=6&v=1EnL7vUmvQ4")

just_like_heaven = media.Movie("Just like Heaven",
                               "Car accident of a young emergency medicine physician whose work is her whole life",
                               "https://reliancehvg.co.in/store/images/P/Just%20Like%20Heaven%20DVD%20inlay1.jpg",
                               "https://www.youtube.com/watch?v=WPyJTNzzizw")

zoomania = media.Movie("Zoomania",
                       "A story of rabbit to make her career",
                       "http://t1.gstatic.com/images?q=tbn:ANd9GcQDoqIP_EsdSZjJmMVWa6DQnv_bXt1G9V12FBjXljWU98oIkzqr",
                       "https://www.youtube.com/watch?v=GIshH9EXIUA")

the_intouchable = media.Movie("The Intouchable",
                              "A story of best two friends",
                              "https://images-na.ssl-images-amazon.com/images/I/51po9WM6HKL._SY355_.jpg",
                              "https://www.youtube.com/watch?v=QNDSMwyGswg")

matrix = media.Movie("Matrix",
                     "Cybercriminal and computer programmer Neo learns this truth and is drawn into a rebellion against the machines",
                     "https://gfx.videobuster.de/archive/v/cunXirXpVaV3oXrC6jOckGwcz0lMkawMDklMkYwMSUyRmltYZklMkZqcGVnJTJGYWQ1ZWU2ZjdjvqtlYjZlYWXgs7c2ZDFj1mUuanBnJnI9d-84/matrix.jpg",
                     "https://www.youtube.com/watch?v=e1XqKDdFxng")

movies = [rubber, avatar, just_like_heaven, zoomania, the_intouchable, matrix]
fresh_tomatoes.open_movies_page(movies)

print (media.Movie.__doc__)
