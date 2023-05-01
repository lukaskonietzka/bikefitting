""" Tests for all modules """
import pytest
from src.models import Roadbike, Mountainbike, Trekkingbike
from django.conf import settings


class Test_Roadbike():
    r_bike = Roadbike("Cube", 180, 90)
    r_bike.step_length = 90

    def test_calculate_frame_height(self):
        result = self.r_bike.calculate_frame_height(self.r_bike.step_length, 2)
        expect = 180
        assert result == expect

    def test_calculate_saddle_height(self):
        result = self.r_bike.calculate_saddle_height(self.r_bike.step_length, 3)
        expect = 270
        assert result == expect


class Test_Mountainbike():
    m_bike = Mountainbike("Cube", 180, 90)
    m_bike.step_length = 90

    def test_calculate_frame_height(self):
        result = self.m_bike.calculate_frame_height(self.m_bike.step_length, 2)
        expect = 180
        assert result == expect

    def test_calculate_saddle_height(self):
        result = self.m_bike.calculate_saddle_height(self.m_bike.step_length, 3)
        expect = 270
        assert result == expect


class Test_Trekkingbike():
    t_bike = Trekkingbike("Cube", 180, 90)
    t_bike.step_length = 90

    def test_calculate_frame_height(self):
        result = self.t_bike.calculate_frame_height(self.t_bike.step_length, 2)
        expect = 180
        assert result == expect

    def test_calculate_saddle_height(self):
        result = self.t_bike.calculate_saddle_height(self.t_bike.step_length, 3)
        expect = 270
        assert result == expect





