class Media(object):
    """
    A model to store a movie
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
        Initializes title, poster url and youtube trailer url for a movie
        :param title:
        :param poster_image_url:
        :param trailer_youtube_url:
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
