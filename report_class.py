class ReportPrinting:
    def __init__(self, results):
        self.results = results
        self.months = {
            '1': 'Jan', '2': 'Feb', '3': 'Apr', '4': 'Mar', '5': 'May', '6': 'Jun',
            '7': 'Jul', '8': 'Aug', '9': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
        }

    def print(self):
        print('\n')
        if isinstance(self.results, str):
            print(self.results)
        else:
            if self.results.year:
                print("Highest:", self.results.year[0])
                print("Lowest:", self.results.year[1])
                print("Humidity:", self.results.year[2])
            else:
                print("Highest Average:", self.results.month[0])
                print("Lowest Average:", self.results.month[1])
                print("Average Mean Humidity:", self.results.month[2])

    def plot_bar_chart(self, all_data, request):
        year_month = request.split('/')
        local_month = self.months[year_month[1]]
        file_name = "lahore_weather_{}_{}".format(year_month[0], local_month)
        max_temp_list = all_data.max_temperature[file_name]
        min_temp_list = all_data.min_temperature[file_name]
        print('\n')
        for index, value in enumerate(max_temp_list):
            print("{}{} {} {}{}".format('\033[91m', index+1, '+'*value, value, 'C'))
            print("{}{} {} {}{}".format('\033[94m', index+1, '+'*min_temp_list[index], min_temp_list[index], 'C'))




