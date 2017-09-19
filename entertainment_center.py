from media import Media

movies_data = [
    {'title': 'The Lion King',
     'poster_image_url': 'http://www.lionking.org/~uzuri/pics/tlkcomic.jpg',
     'trailer_youtube_url': 'https://www.youtube.com/watch?v=4sj1MT05lAA'},
    {'title': 'Frozen',
     'poster_image_url': 'https://images-na.ssl-images-amazon.com/images/I/81nvdo8sThL.jpg',
     'trailer_youtube_url': 'https://www.youtube.com/watch?v=TbQm5doF_Uc'},
    {'title': 'Kung Fu Panda',
     'poster_image_url': 'https://i.pinimg.com/originals/aa/62/13/aa621386ec9931a612a2544f40818b61.jpg',
     'trailer_youtube_url': 'https://www.youtube.com/watch?v=PXi3Mv6KMzY'},
    {'title': 'Storks',
     'poster_image_url': 'https://www.tribute.ca/news/wp-content/uploads/2016/12/Storks-movie-poster-711x900.jpg',
     'trailer_youtube_url': 'https://www.youtube.com/watch?v=ZVzL94jZNdU'},
    {'title': 'The Incredibles',
     'poster_image_url': 'https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg',
     'trailer_youtube_url': 'https://www.youtube.com/watch?v=eZbzbC9285I'},
    {'title': 'The Boss Baby',
     'poster_image_url': 'http://i0.kym-cdn.com/entries/icons/original/000/022/861/the-boss-baby.70675.jpg',
     'trailer_youtube_url': 'https://www.youtube.com/watch?v=Ud8j5GaqH3c'},
]


def create_movie_objects():
    movies = []
    for movie in movies_data:
        movie_info = Media(movie['title'], movie['poster_image_url'], movie['trailer_youtube_url'])
        movies.append(movie_info)
    return movies
