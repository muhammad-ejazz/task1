from parsing_class import ParsingFiles
from calculation_class import CalculatingResults
from result_data import ResultData
from report_class import ReportPrinting

if __name__ == "__main__":
    path = "/home/muhammad/new_task/weatherdata/"
    parsing_files = ParsingFiles(path)
    all_weather_readings = parsing_files.reading_files()
    all_years_plus_months = {}

    for file_name in all_weather_readings.max_temperature.keys():
        split_strings = file_name.split('_')
        year = split_strings[2]
        month = split_strings[3]
        if year not in all_years_plus_months:
            all_years_plus_months[year] = []
        all_years_plus_months[year].append(month[0:3])

    calculations_class = CalculatingResults(all_weather_readings, all_years_plus_months)
    request = input("Enter query: ")
    if len(request) == 4:
        calculations_class.year = request
    else:
        year_month = request.split('/')
        calculations_class.year = year_month[0]
        calculations_class.month = year_month[1]

    results = calculations_class.calculations()

    report_print = ReportPrinting(results)
    report_print.print()
    if len(request) > 4 and isinstance(results, ResultData):
        report_print.plot_bar_chart(all_weather_readings, request)