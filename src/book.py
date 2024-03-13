class Book:
    def __init__(self, title, author, length, ratings, avg_rating, genre=None):
        self.title = title
        self.author = author
        self.length = length
        self.ratings = ratings
        self.avg_rating = avg_rating
        self.genre = genre

    def calculate_rating(self):
        if len(self.rating) == 0:
            return 0
        return sum(self.rating) / len(self.rating)

    def update_rating(self, new_rate):
        self.ratings.append(new_rate)
        self.calculate_rating()

    def add_genre(self, new_genre):
        self.genre.append(new_genre)
