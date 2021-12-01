from star.AbstractStar import AbstractStar


class MockStar(AbstractStar):
    def __init__(self):
        pass

    def set_color(self, r: int, g: int, b: int):
        print("Setting color: (" + str(r) + "," + str(g) + "," + str(b) + ")")
