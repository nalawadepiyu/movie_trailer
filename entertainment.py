import media
import fresh_tomatoes

# creating instances of media type
toy_story = media.Movie("TOY story",
"Toy story line",
"https://goo.gl/JjMqjd",
"https://www.youtube.com/watch?v=c3986gGp3Qs")

avatar = media.Movie("Avatar",
"Avatar story line",
"https://goo.gl/zNTwNP",
"https://www.youtube.com/watch?v=a0CDJZu4M5I")

cindrella = media.Movie("Cindrella",
"cindrella story line",
"https://goo.gl/4DgTEK",
"https://www.youtube.com/watch?v=DEfV6ND53Z0")

barbiee = media.Movie("Barbiee",
"Barbiee Story line",
"https://goo.gl/DWLqrP",
"https://www.youtube.com/watch?v=XGWDvaKMHHM")

#add elements in an array
movies=[toy_story,avatar,cindrella,barbiee]

#calling method to open page with list of movies
fresh_tomatoes.open_movies_page(movies)
