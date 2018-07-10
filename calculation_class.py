from result_data import ResultData


class CalculatingResults:
    def __init__(self, all_weather_readings, all_years_plus_months):
        self.all_weather_readings = all_weather_readings
        self.all_years_plus_months = all_years_plus_months
        self.year = None
        self.month = None
        self.months = {
            '1': 'Jan', '2': 'Feb', '3': 'Apr', '4': 'Mar', '5': 'May', '6': 'Jun',
            '7': 'Jul', '8': 'Aug', '9': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
        }

    def calculations(self):
        if self.year is not None and self.month is None:
            if self.year not in self.all_years_plus_months:
                return "Weather data for this year is not available!"

            months_in_year = self.all_years_plus_months[self.year]
            max_temperature = -1000
            min_temperature = 1000
            max_humidity = -1000
            max_temp_day = ''
            min_temp_day = ''
            max_humid_day = ''
            max_temp_month = ''
            min_temp_month = ''
            max_humid_month = ''

            for month in months_in_year:
                file_name = "lahore_weather_{}_{}".format(self.year, month)

                if self.all_weather_readings.max_temperature[file_name]:
                    prev_max_temp = max_temperature
                    prev_min_temp = min_temperature
                    prev_max_humid = max_humidity
                    max_temperature = max(max_temperature, max(self.all_weather_readings.max_temperature[file_name][:]))
                    min_temperature = min(min_temperature, min(self.all_weather_readings.min_temperature[file_name][:]))
                    max_humidity = max(max_humidity, max(self.all_weather_readings.max_humidity[file_name][:]))

                    if prev_max_temp != max_temperature:
                        max_temp_day = self.all_weather_readings.max_temperature[file_name].index(max_temperature)
                        max_temp_month = month

                    if prev_min_temp != min_temperature:
                        min_temp_day = self.all_weather_readings.min_temperature[file_name].index(min_temperature)
                        min_temp_month = month

                    if prev_max_humid != max_humidity:
                        max_humid_day = self.all_weather_readings.max_humidity[file_name].index(max_humidity)
                        max_humid_month = month

            results = ResultData()
            results.year.append("{}C on {} {}".format(max_temperature, max_temp_month, max_temp_day+1))
            results.year.append("{}C on {} {}".format(min_temperature, min_temp_month, min_temp_day+1))
            results.year.append("{}% on {} {}".format(max_humidity, max_humid_month, max_humid_day+1))

            return results
        else:
            if self.year not in self.all_years_plus_months:
                return "Weather data for this year is not available!"

            local_month = self.months[self.month]
            if local_month not in self.all_years_plus_months[self.year]:
                return "Weather data for this month of {} is not available!".format(self.year)

            file_name = "lahore_weather_{}_{}".format(self.year, local_month)
            if self.all_weather_readings.max_temperature[file_name]:
                max_temp_sum = sum(self.all_weather_readings.max_temperature[file_name][:])
                avg_max_temp = max_temp_sum / len(self.all_weather_readings.max_temperature[file_name])

                min_temp_sum = sum(self.all_weather_readings.min_temperature[file_name][:])
                avg_min_temp = min_temp_sum / len(self.all_weather_readings.min_temperature[file_name])

                mean_humidity_sum = sum(self.all_weather_readings.mean_humidity[file_name][:])
                avg_mean_humidity = mean_humidity_sum / len(self.all_weather_readings.mean_humidity[file_name])

                results = ResultData()
                results.month.append("{}C".format(avg_max_temp))
                results.month.append("{}C".format(avg_min_temp))
                results.month.append("{}%".format(avg_mean_humidity))
                return results
            else:
                return "Weather data for this month of {} is not available!".format(self.year)




