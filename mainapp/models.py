from django.db import models


# Create your models here.
class Race:
    race_name = 'name_race'
    description = 'description_race'
    bonus = ''

    def __init__(self, *args):
        pass

    def __str__(self):
        return f'{self.race_name}'

    def get_description(self, name_race):
        pass


class Class:
    class_name = ''
    description_name = ''

    def __init__(self, *args):
        pass

    def __str__(self):
        return f'{self.class_name}'
