from moving_average import MovingAverage as mv 

class Analysis:
    def __init__(self, data):
        self.data = data 
        self.sma20 = mv.calculate_moving_average(data, 2)
        self.sma50 = mv.calculate_moving_average(data, 4)
        self.sma200 = mv.calculate_moving_average(data, 6)


    def signal(self):
        if self.buy_signal(self):
            return 'buy'
        elif self.sell_signal(self):
            return "sell"

    def buy_signal(self):
        return (self.sma20 > self.sma50  
                and self.sma20 > self.sma200
                and self.sma50 > self.sma200) 

    def sell_signal(self):
        return (self.sma20 < self.sma50  
                and self.sma20 < self.sma200
                and self.sma50 < self.sma200)