"""
    UNITTESTS
    Tests for the database
    Author:     Niehage, Sebastian
                Konietzka, Lukas
"""
from bikefitting_app.models import Roadbike, Mountainbike, Trekkingbike


class Test_Roadbike:
    r_bike = Roadbike()
    r_bike.step_length = 90
    r_bike._STEP_LENGTH_FACTOR = 1
    r_bike._SADDLE_HEIGHT_FACTOR = 1

    def test_calculate_frame_height(self):
        result = self.r_bike.calculate_frame_height(self.r_bike.step_length, 2)
        expect = 180
        assert result == expect

    def test_calculate_saddle_height(self):
        result = self.r_bike.calculate_saddle_height(self.r_bike.step_length, 3)
        expect = 270
        assert result == expect

    def test_create_roadbike_fitting(self):
        result_frame_height, result_saddle_height = self.r_bike.create_roadbike_fitting("Cube", 180, 90)

        expect_frame_height = 90
        assert result_frame_height == expect_frame_height

        expect_saddle_height = 90
        assert result_saddle_height == expect_saddle_height


class Test_Mountainbike:
    m_bike = Mountainbike()
    m_bike.step_length = 90
    m_bike._STEP_LENGTH_FACTOR = 1
    m_bike._SADDLE_HEIGHT_FACTOR = 1

    def test_calculate_frame_height(self):
        result = self.m_bike.calculate_frame_height(self.m_bike.step_length, 2)
        expect = 180
        assert result == expect

    def test_calculate_saddle_height(self):
        result = self.m_bike.calculate_saddle_height(self.m_bike.step_length, 3)
        expect = 270
        assert result == expect

    def test_create_mountainbike_fitting(self):
        result_frame_height, result_saddle_height = self.m_bike.create_mountainbike_fitting("Cube", 180, 90)

        expect_frame_height = 90
        assert result_frame_height == expect_frame_height

        expect_saddle_height = 90
        assert result_saddle_height == expect_saddle_height


class Test_Trekkingbike:
    t_bike = Trekkingbike("Cube", 180, 90)
    t_bike.step_length = 90
    t_bike._STEP_LENGTH_FACTOR = 1
    t_bike._SADDLE_HEIGHT_FACTOR = 1

    def test_calculate_frame_height(self):
        result = self.t_bike.calculate_frame_height(self.t_bike.step_length, 2)
        expect = 180
        assert result == expect

    def test_calculate_saddle_height(self):
        result = self.t_bike.calculate_saddle_height(self.t_bike.step_length, 3)
        expect = 270
        assert result == expect

    def test_create_trekkingbike_fitting(self):
        result_frame_height, result_saddle_height = self.t_bike.create_trekkingbike_fitting("Cube", 180, 90)

        expect_frame_height = 90
        assert result_frame_height == expect_frame_height

        expect_saddle_height = 90
        assert result_saddle_height == expect_saddle_height





