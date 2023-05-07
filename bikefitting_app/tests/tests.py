"""
    UNITTESTS
    Tests for the database
    Author:     Niehage, Sebastian
                Konietzka, Lukas
"""
from bikefitting_app.models import Roadbike, Mountainbike, Trekkingbike


class Test_Roadbike():
    r_bike = Roadbike()
    r_bike.step_length = 90

    def test_calculate_frame_height(self):
        result = self.r_bike.calculate_frame_height(self.r_bike.step_length, 2)
        expect = 180
        assert result == expect

    def test_calculate_saddle_height(self):
        result = self.r_bike.calculate_saddle_height(self.r_bike.step_length, 3)
        expect = 270
        assert result == expect

    def test_create_roadbike_fitting(self):
        self.r_bike.create_roadbike_fitting("Cube", 180, 90)

        result_name = self.r_bike.name
        expect_name = "Cube"
        assert result_name == expect_name

        result_height = self.r_bike.height
        expect_height = 180
        assert result_height == expect_height

        result_step_length = self.r_bike.step_length
        expect_step_length = 90
        assert result_step_length == expect_step_length

        result_frame_height = self.r_bike.frame_height
        expect_frame_height = 90
        assert result_frame_height == expect_frame_height

        result_saddle_height = self.r_bike.saddle_height
        expect_saddle_height = 90
        assert result_saddle_height == expect_saddle_height


class Test_Mountainbike():
    m_bike = Mountainbike()
    m_bike.step_length = 90

    def test_calculate_frame_height(self):
        result = self.m_bike.calculate_frame_height(self.m_bike.step_length, 2)
        expect = 180
        assert result == expect

    def test_calculate_saddle_height(self):
        result = self.m_bike.calculate_saddle_height(self.m_bike.step_length, 3)
        expect = 270
        assert result == expect

    def test_create_mountainbike_fitting(self):
        self.m_bike.create_mountainbike_fitting("Cube", 180, 90)

        result_name = self.m_bike.name
        expect_name = "Cube"
        assert result_name == expect_name

        result_height = self.m_bike.height
        expect_height = 180
        assert result_height == expect_height

        result_step_length = self.m_bike.step_length
        expect_step_length = 90
        assert result_step_length == expect_step_length

        result_frame_height = self.m_bike.frame_height
        expect_frame_height = 90
        assert result_frame_height == expect_frame_height

        result_saddle_height = self.m_bike.saddle_height
        expect_saddle_height = 90
        assert result_saddle_height == expect_saddle_height


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

    def test_create_trekkingbike_fitting(self):
        self.t_bike.create_trekkingbike_fitting("Cube", 180, 90)

        result_name = self.t_bike.name
        expect_name = "Cube"
        assert result_name == expect_name

        result_height = self.t_bike.height
        expect_height = 180
        assert result_height == expect_height

        result_step_length = self.t_bike.step_length
        expect_step_length = 90
        assert result_step_length == expect_step_length

        result_frame_height = self.t_bike.frame_height
        expect_frame_height = 90
        assert result_frame_height == expect_frame_height

        result_saddle_height = self.t_bike.saddle_height
        expect_saddle_height = 90
        assert result_saddle_height == expect_saddle_height





