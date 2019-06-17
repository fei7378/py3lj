

class Athlete:
    def __init__(self, value=0):
        self.thing = value
    def how_big(self):
        return (len(self.thing))


if __name__ == '__main__':
    athlete = Athlete()
    print(athlete.how_big())