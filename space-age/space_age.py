class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.year = 365.25
        self.segundo = 86400

    def on_earth(self):
        return round(self.seconds/31557600, 2)

    def on_mercury(self):
        return round(self.seconds/((0.2408467*self.year)*self.segundo), 2)

    def on_venus(self):
        return round(self.seconds/((0.61519726*self.year)*self.segundo), 2)

    def on_mars(self):
        return round(self.seconds/((1.8808158*self.year)*self.segundo), 2)

    def on_jupiter(self):
        return round(self.seconds/((11.862615*self.year)*self.segundo), 2)

    def on_saturn(self):
        return round(self.seconds/((29.447498*self.year)*self.segundo), 2)

    def on_uranus(self):
        return round(self.seconds/((84.016846*self.year)*self.segundo), 2)

    def on_neptune(self):
        return round(self.seconds/((164.79132*self.year)*self.segundo), 2)
