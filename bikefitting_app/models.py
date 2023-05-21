"""
    BACKEND
    Contains the Database for all Fittings

    Example:
        - To create a new fitting type:
            r_bike = Roadbike()
            r_bike.creat_roadbike_fitting()
        - To get the created date in python use:
            print(r_bike) or use the database language from django

    Author:     Niehage, Sebastian
                Konietzka, Lukas
"""
from django.db import models


class Fitting(models.Model):
    """
        Contains the Database from this app
        The fields are the columns in the database
        Child-class from:   Model
        Parent-class for:   Terkkingbike,
                            Roadbike,
                            Mountainbike
    """
    name = models.CharField(max_length=40, name='Name', null=False)
    height = models.IntegerField(name='Height', null=False)
    step_length = models.IntegerField(name='Step Length', null=False)
    frame_height = 0
    saddle_height = 0
    #frame_height = models.IntegerField(name='Frame Height', null=False)
    #saddle_height = models.IntegerField(name='Saddle Height', null=False)

    @property
    def show_frame_height(self):
        """
        Calculated Field
        :return:
        """
        return self.get_frame_height()

    @property
    def show_saddle_height(self):
        """
        Calculated Field
        :return:
        """
        return self.get_saddle_height()

    def get_frame_height(self):
        """
        Geter method for the field frame_height
        :return: the field frame_height
        """
        return self.frame_height

    def get_saddle_height(self):
        """
        Geter-method for the field saddle_height
        :return:    the field saddle_height
        """
        return self.saddle_height

    def round_to_integer(self, x):
        """
        round the given argument to an integer
        :param x:   number that must be round
        :return:    rounded number
        """
        roundabout = 0
        return int(round(x, roundabout))

    def calculate_frame_height(self, step_length, factor):
        """
        Calculate the frame height depending on the given argument
        and a given factor
        :param step_length: the step length of the user
        :param factor:      factor depending on the bike
        :return:            the calculated frame height depending on the bike
        """
        frame_height = step_length * factor
        return self.round_to_integer(frame_height)

    def calculate_saddle_height(self, step_length, factor):
        """
        Calculate the saddle height depending on the given argument
        and a given factor
        :param step_length: the step length of the user
        :param factor:      factor depending on the bike
        :return:            the calculated saddle height depending on the bike
        """
        step_length = step_length * factor
        return self.round_to_integer(step_length)

    def write_in_database(self, data):
        """
        Write the current datas into the data-model
        :param data:    Tupel made out of 5, current datas
        :return:        None
        """
        self.name = data[0]
        self.height = data[1]
        self.step_length = data[2]
        self.frame_height = data[3]
        self.saddle_height = data[4]

    # def __str__(self):
    #     """
    #     Method from objekt, is called when an object
    #     of Fitting should be printed via print()
    #     :return: fields of Fitting that should be printed
    #     """
    #     return f"name: {self.name}\n\
    #             height: {self.height} \n\
    #             step length: {self.step_length}\n\
    #             frame height: {self.frame_height}\n\
    #             saddle height: {self.saddle_height}\n"


class Roadbike(Fitting):
    """
        Create a Roadbike-Fitting depending on the following fields
        Child-class from:   Fitting
    """
    _STEP_LENGTH_FACTOR = 1
    _SADDLE_HEIGHT_FACTOR = 1

    def create_roadbike_fitting(self, name, height, step_length):
        """
        Get and calculate all required datas and write them into
        the database
        :param name:        user_name
        :param height:      user_height
        :param step_length: user_step_length
        :return:            None
        """
        self.r_name = name
        self.r_height = height
        self.r_step_length = step_length
        self.r_frame_height = self.calculate_frame_height(step_length, self._STEP_LENGTH_FACTOR)
        self.r_saddle_height = self.calculate_saddle_height(step_length, self._SADDLE_HEIGHT_FACTOR)
        data = (self.r_name,
                self.r_height,
                self.r_step_length,
                self.r_frame_height,
                self.r_saddle_height)
        self.write_in_database(data)
        return data


class Trekkingbike(Fitting):
    """
        Create a Trekkingbike-Fitting depending on the following fields
        Child-class from:   Fitting
    """
    _STEP_LENGTH_FACTOR = 1
    _SADDLE_HEIGHT_FACTOR = 1

    def create_trekkingbike_fitting(self, name, height, step_length):
        """
        Get and calculate all required datas and write them into
        the database
        :param name:        user_name
        :param height:      user_height
        :param step_length: user_step_length
        :return:            None
        """
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
        return data


class Mountainbike(Fitting):
    """
        Create a Mountainbike-Fitting depending on the following fields
        Child-class from:   Fitting
    """
    _SADDLE_HEIGHT_FACTOR = 1
    _STEP_LENGTH_FACTOR = 1

    def create_mountainbike_fitting(self, name, height, step_length):
        """
        Get and calculate all required datas and write them into
        the database
        :param name:        user_name
        :param height:      user_height
        :param step_length: user_step_length
        :return:            None
        """
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
        return data


