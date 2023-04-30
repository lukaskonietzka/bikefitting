""" Tests for all modules """
import pytest
from src.models import Trekkingbike, Roadbike, Mountainbike, Fitting
from django.conf import settings


def pytest_config():
    settings.configure()


class Test_Trekkingbike():
    t_bike = Trekkingbike("Cube", 180, 90)
    t_bike._STEP_LENGTH_FACTOR = 1
    t_bike._SADDLE_HEIGHT_FACTOR = 1

    def test_calculate_frame_height(self):
        pytest_config()
        self.t_bike.calculate_frame_height()
        result = self.t_bike.frame_height
        expect = 90
        assert result == expect

    def test_calculate_saddle_height(self):
        pytest_config()
        self.t_bike.calculate_saddle_height()
        result = self.t_bike.saddle_height
        expect = 90
        assert result == expect


class Test_Roadbike():
    r_bike = Roadbike("Cube", 180, 90)
    r_bike._STEP_LENGTH_FACTOR = 1
    r_bike._SADDLE_HEIGHT_FACTOR = 1

    def test_calculate_frame_height(self):
        pytest_config()
        self.r_bike.calculate_frame_height()
        result = self.r_bike.frame_height
        expect = 90
        assert result == expect

    def test_calculate_saddle_height(self):
        pytest_config()
        self.r_bike.calculate_saddle_height()
        result = self.r_bike.saddle_height
        expect = 90
        assert result == expect


class Test_Mountainbike():
    m_bike = Mountainbike("Cube", 180, 90)
    m_bike._STEP_LENGTH_FACTOR = 1
    m_bike._SADDLE_HEIGHT_FACTOR = 1

    def test_calculate_frame_height(self):
        pytest_config()
        self.m_bike.calculate_frame_height()
        result = self.m_bike.frame_height
        expect = 90
        assert result == expect

    def test_calculate_saddle_height(self):
        pytest_config()
        self.m_bike.calculate_saddle_height()
        result = self.m_bike.saddle_height
        expect = 90
        assert result == expect





