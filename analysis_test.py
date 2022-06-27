import unittest
import analysis


class Analysis(unittest.TestCase):

    def test_sell_signal(self):
        data = [12973.0, 12943.0, 12923.0, 12916.0, 12885.0, 12889.0]
        analyzed = analysis.Analysis(data)
        self.assertEqual(analyzed.sell_signal(), True)
        self.assertEqual(analyzed.buy_signal(), False)

    def test_buy_signal(self):
        data = [12973.0, 12993.0, 13023.0, 13035.0, 13055.0, 13089.0]
        analyzed = analysis.Analysis(data)
        self.assertEqual(analyzed.buy_signal(), True)
        self.assertEqual(analyzed.sell_signal(), False)



    # def test_signal(self):
    #     data = [12973.0, 12943.0, 12923.0, 12916.0, 12885.0, 12889.0]
    #     analyzed = analysis.Analysis(data)
    #     self.assertEqual(analyzed.sell_signal(), "sell")
    

if __name__ == '__main__':
    unittest.main()