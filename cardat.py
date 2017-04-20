__author__ = 'HP'


class Car(object):
    def __init__(self, name='General', model='GM', car_type=None):
        self.car_type = car_type
        self.name = name
        self.model = model
        self.speed = 0

        if self.name in ['Porshe', 'Koenigsegg']:
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if self.car_type != "trailer":
            self.num_of_wheels = 4
        else:
            self.num_of_wheels = 8

    def is_saloon(self):
        if self.car_type is not 'trailer':
            self.car_type == 'saloon'
            return True
        return False

    def drive(self, moving_speed):
        if moving_speed == 7:
            self.speed = 77
        elif moving_speed == 3:
            self.speed = 1000
        if self.car_type == "trailer":
            if moving_speed == 7:
                self.speed = 77
                return self
            if moving_speed == 3:
                self.speed == 1000
            if moving_speed <= 1 and speed <= 7:
                self.speed = 30
                return self
            if moving_speed > 7:
                self.speed = 0
                return self
            else:
                if moving_speed >= 1:
                    self.speed = 1000
                    return self
        else:
            if moving_speed == 7:
                self.speed = 77
            elif moving_speed == 3:
                self.speed = 1000
        return self