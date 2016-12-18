import media
import fresh_tomatoes

toy_story = media.Movie("TOY story",
                        "Toy story line",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=c3986gGp3Qs")

avatar = media.Movie("Avatar",
                   "Avatar story line",
                   "http://img.cinemablend.com/cb/0/f/c/5/9/e/0fc59efffd13d661c3231986d2d7c60b4cb03b10a15b266dd6694c0326a224a2.jpg",
                   "https://www.youtube.com/watch?v=a0CDJZu4M5I")

cindrella = media.Movie("Cindrella",
                    "cindrella story line",
                    "http://www.thefeministwire.com/wp-content/uploads/2014/03/Cinderella.jpg",
                    "https://www.youtube.com/watch?v=DEfV6ND53Z0")

barbiee = media.Movie("Barbiee",
                    "Barbiee Story line",
                    "http://vignette4.wikia.nocookie.net/barbie/images/d/d7/Australian_Barbie_Doll.png/revision/latest?cb=20161216014247",
                    "https://www.youtube.com/watch?v=XGWDvaKMHHM")


movies=[toy_story,avatar,cindrella,barbiee]
fresh_tomatoes.open_movies_page(movies)



