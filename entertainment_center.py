import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://de.wikipedia.org/wiki/Toy_Story",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print (toy_story.trailer_youtube_url)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.avatarmovie.com/index.html",
                     "https://www.youtube.com/watch?time_continue=6&v=1EnL7vUmvQ4")
#print (avatar.storyline)

# avatar.open_trailer()

just_like_heaven = media.Movie("Just like Heaven",
                               "Car accident of a young emergency medicine physician whose work is her whole life",
                               "https://en.wikipedia.org/wiki/Just_like_Heaven_(film)",
                               "https://www.youtube.com/watch?v=WPyJTNzzizw")
print (just_like_heaven.title, just_like_heaven.storyline)
just_like_heaven.open_trailer()



