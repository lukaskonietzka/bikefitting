""" Contains the Datastructur """

from django.db import models


class Fitting(models.Model):
    ID = models.IntegerField
    name = models.CharField(max_length=30)
    height = models.IntegerField
    step_length = models.IntegerField
    saddle_height = models.FloatField
    frame_height = models.FloatField

    def get_frame_height(self):
        return self.frame_height

    def get_saddle_height(self):
        return self.saddle_height


class Roadbike(Fitting):
    _STEP_LENGTH_FACTOR = 0.665
    _SADDLE_HEIGHT_FACTOR = 1

    def __int__(self, name, height, step_length):
        self.name = name
        self.height = height
        self.step_length = step_length
        self.calculate_frame_height()
        self.calculate_saddle_height()

    def calculate_frame_height(self):
        self.frame_height = self.step_length * self._STEP_LENGTH_FACTOR

    def calculate_saddle_height(self):
        self.saddle_height = self.step_length * self._SADDLE_HEIGHT_FACTOR


class Trekkingbike(Fitting):
    _STEP_LENGTH_FACTOR = 1
    _SADDLE_HEIGHT_FACTOR = 1

    def __int__(self, name, height, setp_lenght):
        self.name = name
        self.height = height
        self.step_length = setp_lenght
        self.calculate_frame_height()
        self.calculate_saddle_height()

    def calculate_frame_height(self):
        self.frame_height = self.step_length * self._STEP_LENGTH_FACTOR

    def calculate_saddle_height(self):
        self.saddle_height = self.step_length * self._SADDLE_HEIGHT_FACTOR


class Mountainbike(Fitting):
    _SADDLE_HEIGHT_FACTOR = 0.885
    _STEP_LENGTH_FACTOR = 1

    def __int__(self, name, height, step_length):
        self.name = name
        self.height = height
        self.step_length = step_length
        self.calculate_frame_height()
        self.calculate_saddle_height()

    def calculate_frame_height(self):
        self.frame_height = self.step_length * self._STEP_LENGTH_FACTOR

    def calculate_saddle_height(self):
        self.saddle_height = self.step_length * self._SADDLE_HEIGHT_FACTOR
