import unittest
import moving_average as m_v


class MovingAverageTestCases(unittest.TestCase):

    def test_simple_moving_average(self):
        data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
        period = 5
        movingAverage = m_v.MovingAverage

        self.assertEqual(8.0, movingAverage.calculate_moving_average(data, period))


    def test_simple_moving_average_invalid(self):
        data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
        period = 5
        movingAverage = m_v.MovingAverage

        self.assertEqual(7.0, movingAverage.calculate_moving_average(data, period))


if __name__ == '__main__':
    unittest.main()