from datetime import date


class Comment(object):
    def __init__(self, text, date):
        super(Comment, self).__init__()
        self.text = text
        self.date = date

    def __repr__(self):
        return "Comment: {}, Time: {},".format(
            self.text, 
            self.date
            )

COMMENTS = []
COMMENTS.append(Comment("I don't want to earn my living; I want to live.", date.today().strftime("%Y-%m-%d")))
COMMENTS.append(Comment("Life is a one time offer, use it well.", date.today().strftime("%Y-%m-%d")))
COMMENTS.append(Comment("Love the life you live, and live the life you love.", date.today().strftime("%Y-%m-%d")))