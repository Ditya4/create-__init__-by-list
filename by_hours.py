from os import path
from datetime import date
from datetime import timedelta


class Streams:
    def __init__(self, index=None, switch_id=None, switch_name=None, stream_id=None,
                 stream_name=None):
        self.index = index
        self.switch_id = switch_id
        self.switch_name = switch_name
        self.stream_id = stream_id
        self.stream_name = stream_name

    def __str__(self):
        '''
        we return a string which almost looks like a list with str value
        of every field in record
        '''
        list_of_values = [str((t)) for name, t in self.__dict__.items()
                          if type(t).__name__ != "function" and
                          not name.startswith("__")]
        line_to_return = "[" + " , ".join(list_of_values) + "]"
        return line_to_return

def read_streams(folder, file_name):
    streams_file_name = path.join(folder, file_name)
    streams_file = open(streams_file_name)
    streams_lines = streams_file.readlines()
    size_of_streams_list = len(streams_lines)
    for index in range(size_of_streams_list):
        streams_lines[index] = (
               streams_lines[index].rstrip())
    streams = [None] * size_of_streams_list
    in_streams_list_index = 0
    out_streams_list_index = 0
    while in_streams_list_index < size_of_streams_list:
        line_split = (
               streams_lines[in_streams_list_index].split("    "))
        if line_split[-1] == "\n":
            line_split.pop()
        # print(in_streams_list_index, "line_split =", line_split)
        if len(line_split) == 4:
            streams[out_streams_list_index] = (
                            Streams(out_streams_list_index,
                            *line_split))
            in_streams_list_index += 1
            out_streams_list_index += 1
        else:
            print(f"Error in line from file = {file_name}",
                  f"with index = {in_streams_list_index}",
                  f"with value {line_split}",
                  f"wait for 4 parameters",
                  f"and got {len(line_split)}")
            size_of_streams_list -= 1
            in_streams_list_index += 1
            streams.pop()
    return streams


class ByHours:
    def __init__(self, index=None, name=None, hour_0=None, date=None,
                 hour_1=None, hour_2=None, hour_3=None,
                 hour_4=None, hour_5=None, hour_6=None,
                 hour_7=None, hour_8=None, hour_9=None,
                 hour_10=None, hour_11=None, hour_12=None,
                 hour_13=None, switch_id=None, hour_14=None,
                 hour_15=None, hour_16=None, hour_17=None,
                 hour_18=None, hour_19=None, hour_20=None,
                 hour_21=None, hour_22=None, hour_23=None,
                 rs_id=None):
        self.index = index
        self.name = name
        self.hour_0 = hour_0
        self.date = date
        self.hour_1 = hour_1
        self.hour_2 = hour_2
        self.hour_3 = hour_3
        self.hour_4 = hour_4
        self.hour_5 = hour_5
        self.hour_6 = hour_6
        self.hour_7 = hour_7
        self.hour_8 = hour_8
        self.hour_9 = hour_9
        self.hour_10 = hour_10
        self.hour_11 = hour_11
        self.hour_12 = hour_12
        self.hour_13 = hour_13
        self.switch_id = switch_id
        self.hour_14 = hour_14
        self.hour_15 = hour_15
        self.hour_16 = hour_16
        self.hour_17 = hour_17
        self.hour_18 = hour_18
        self.hour_19 = hour_19
        self.hour_20 = hour_20
        self.hour_21 = hour_21
        self.hour_22 = hour_22
        self.hour_23 = hour_23
        self.rs_id = rs_id
        # calculated fields
        self.date_date = None

    def __str__(self):
        '''
        we return a string which almost looks like a list with str value
        of every field in record
        '''
        list_of_values = [str((t)) for name, t in self.__dict__.items()
                          if type(t).__name__ != "function" and
                          not name.startswith("__")]
        line_to_return = "[" + " , ".join(list_of_values) + "]"
        return line_to_return

    def date_to_date(self):
        '''
        we transform self.date from string into date format
        '''
        # print("we here", self.date[:self.date.find(",")])
        self.date_date = to_date(self.date[:self.date.find(",")])


def read_by_hours(folder, file_name):
    by_hours_file_name = path.join(folder, file_name)
    by_hours_file = open(by_hours_file_name)
    by_hours_lines = by_hours_file.readlines()
    size_of_by_hours_list = len(by_hours_lines)
    for index in range(size_of_by_hours_list):
        by_hours_lines[index] = (
               by_hours_lines[index].rstrip())
    by_hours = [None] * size_of_by_hours_list
    in_by_hours_list_index = 0
    out_by_hours_list_index = 0
    while in_by_hours_list_index < size_of_by_hours_list:
        line_split = (
               by_hours_lines[in_by_hours_list_index].split(";"))
        if line_split[-1] == "\n":
            line_split.pop()
        # print(in_by_hours_list_index, "line_split =", line_split)
        if len(line_split) == 28:
            by_hours[out_by_hours_list_index] = (
                            ByHours(out_by_hours_list_index,
                            *line_split))
            in_by_hours_list_index += 1
            out_by_hours_list_index += 1
        else:
            print(f"Error in line from file = {file_name}",
                  f"with index = {in_by_hours_list_index}",
                  f"with value {line_split}",
                  f"wait for 28 parameters",
                  f"and got {len(line_split)}")
            size_of_by_hours_list -= 1
            in_by_hours_list_index += 1
            by_hours.pop()
    return by_hours


def to_date(str_date):
    date_to_return = date(year=get_year(str_date),
                          month=get_month(str_date),
                          day=get_day(str_date))
    return date_to_return


def get_dates_from_input_file(
        file_name='D:\python\double_dno\d_by_hours\input_dates.txt'):
    in_file = open(file_name, "r")
    date_start_str, date_end_str = in_file.read().split()
    date_start = to_date(date_start_str)
    date_end = to_date(date_end_str)
    return date_start, date_end


def get_year(str_date):
    '''
    we get
    01.01.2022
    10.01.2022
    date format dd.mm.yyyy
    '''
    year = str_date[6:]
    print("year =", year)

    # print(str_date("."))
    return int(year)


def get_month(str_date):
    '''
    we get
    01.01.2022
    10.01.2022
    date format dd.mm.yyyy
    '''
    month = str_date[3:5]
    print("month =", month)
    return int(month)


def get_day(str_date):
    '''
    we get
    01.01.2022
    10.01.2022
    date format dd.mm.yyyy
    '''
    day = str_date[:2]
    print("day =", day)
    return int(day)


def print_date(date_to_print):
    if date_to_print.day < 10:
        day_to_print = '0' + str(date_to_print.day)
        # print("day less than 10")
    else:
        day_to_print = date_to_print.day
    if date_to_print.month < 10:
        month_to_print = '0' + str(date_to_print.month)
        # print("month less than 10")
    else:
        month_to_print = date_to_print.month
    print(day_to_print, month_to_print, date_to_print.year, sep='.')
    pass


# main for by_hours part():
by_hours_folder = "D:\python\double_dno\d_by_hours"
by_hours_file_name = "data_utf-8_v3.txt"
list_of_by_hours = read_by_hours(by_hours_folder, by_hours_file_name)

# main for streams part():
streams_folder = "D:\python\double_dno\d_by_hours"
streams_file_name = "streams.txt"
list_of_streams = read_streams(streams_folder, streams_file_name)
print("streams_list:")
for record in list_of_streams:
    print(record)


# print(str(list_of_by_hours[0].name))

if str(list_of_by_hours[0].name) in ("nazva potoky zapusiv"):
    start_line = 1
    print('file with headers')
else:
    start_line = 0
    print('file w/o headers')

print("by_hours_list:")
for index in range(start_line, len(list_of_by_hours)):
    list_of_by_hours[index].date_to_date()
    print(list_of_by_hours[index])
print()

date_start, date_end = get_dates_from_input_file(
    'D:\python\double_dno\d_by_hours\input_dates.txt')
print(date_start, date_end)
print_date(date_start)
print_date(date_end)
print(date_start.weekday(), date_end.weekday())

print_date(date_start + timedelta(days=1))
print_date(date_start + timedelta(days=2))


# print(date_set)
