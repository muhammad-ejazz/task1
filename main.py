#!/usr/bin/python3.6
import sys
from parsing_class import ParsingFiles
from calculation_class import CalculatingResults
from result_data import ResultData
from report_class import ReportPrinting

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 4:
        path = argv[1]
        flag = argv[2]
        query = argv[3]

        parsing_files = ParsingFiles(path, flag, query)
        all_weather_readings = parsing_files.reading_files()
        file_names = parsing_files.all_files_names

        calculations_class = CalculatingResults(all_weather_readings, file_names, flag)
        results = calculations_class.calculations()
        report_print = ReportPrinting(results, flag)
        report_print.print()
    else:
        path = argv[1]
        count = 0
        queries = []
        flags = []
        for arg in argv:
            if count == 0 or count == 1:
                count = count + 1
                continue
            if count % 2 == 0:
                flags.append(arg)
            else:
                queries.append(arg)
            count = count + 1

        for index, flag in enumerate(flags):
            parsing_files = ParsingFiles(path, flag, queries[index])
            all_weather_readings = parsing_files.reading_files()
            file_names = parsing_files.all_files_names

            calculations_class = CalculatingResults(all_weather_readings, file_names, flag)
            results = calculations_class.calculations()
            report_print = ReportPrinting(results, flag)
            report_print.print()