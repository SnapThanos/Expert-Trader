class MovingAverage:

    def calculate_moving_average(data, period):

        temp_container = []
        count = period
        while len(temp_container) != period:
            temp_container.append(data[-count])
            count -= 1


        return sum(temp_container) / period




