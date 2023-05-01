""" Contains the Datastructur """

from django.db import models


class Fitting(models.Model):
    ID = models.IntegerField
    name = models.CharField(max_length=40)
    height = models.IntegerField
    step_length = models.IntegerField
    saddle_height = models.IntegerField
    frame_height = models.IntegerField

    def get_frame_height(self):
        return self.frame_height

    def get_saddle_height(self):
        return self.saddle_height

    @staticmethod
    def round_to_integer(x):
        roundabout = 0
        return int(round(x, roundabout))

    def calculate_frame_height(self, step_length, factor):
        frame_height = step_length * factor
        return self.round_to_integer(frame_height)

    def calculate_saddle_height(self, saddle_height, factor):
        saddle_height = saddle_height * factor
        return self.round_to_integer(saddle_height)

    def write_in_database(self, data):
        self.name = data[0]
        self.height = data[1]
        self.step_length = data[2]
        self.frame_height = data[3]
        self.saddle_height = data[4]


class Roadbike(Fitting):
    _STEP_LENGTH_FACTOR = 0.665
    _SADDLE_HEIGHT_FACTOR = 1

    def __int__(self, name, height, step_length):
        self.r_name = name
        self.r_height = height
        self.r_step_length = step_length
        self.r_frame_height = self.calculate_frame_height(step_length, self._STEP_LENGTH_FACTOR)
        self.r_saddle_height = self.calculate_saddle_height(step_length, self._SADDLE_HEIGHT_FACTOR)
        data = (self.r_name,
                self.r_height,
                self.r_step_length,
                self.frame_height,
                self.saddle_height)
        self.write_in_database(data)


class Trekkingbike(Fitting):
    _STEP_LENGTH_FACTOR = 1
    _SADDLE_HEIGHT_FACTOR = 1

    def __int__(self, name, height, step_length):
        self.t_name = name
        self.t_height = height
        self.t_step_length = step_length
        self.t_frame_height = self.calculate_frame_height(step_length, self._STEP_LENGTH_FACTOR)
        self.t_saddle_height = self.calculate_saddle_height(step_length, self._SADDLE_HEIGHT_FACTOR)
        data = (self.t_name,
                self.t_height,
                self.t_step_length,
                self.t_frame_height,
                self.t_saddle_height)
        self.write_in_database(data)


class Mountainbike(Fitting):
    _SADDLE_HEIGHT_FACTOR = 0.885
    _STEP_LENGTH_FACTOR = 1

    def __int__(self, name, height, step_length):
        self.m_name = name
        self.m_height = height
        self.m_step_length = step_length
        self.m_frame_height = self.calculate_frame_height(step_length, self._STEP_LENGTH_FACTOR)
        self.m_saddle_height = self.calculate_saddle_height(step_length, self._SADDLE_HEIGHT_FACTOR)
        data = (self.m_name,
                self.m_height,
                self.m_step_length,
                self.m_frame_height,
                self.m_saddle_height)
        self.write_in_database(data)


