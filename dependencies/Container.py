from star.AbstractStar import AbstractStar


class Container:
    def __init__(self, star: AbstractStar):
        self.star = star

    def get_star(self):
        return self.star
