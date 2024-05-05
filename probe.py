import datetime

# period = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max', 'yyyy-mm-dd, yyyy-mm-dd']
# x, y = period[11].split(',')
# print(x, y)
#
# def fun(**kwargs):
#     print(kwargs)
#
# fun(period=48)
#
# x = datetime.timedelta(days=5, hours=20)
# print(x)
#
# date_string = '2024-05-04'
# format_string = '%Y-%m-%d'
# parse_date = datetime.datetime.strptime(date_string, format_string)
# formatted_date = parse_date.strftime('%d.%m.%y')
# print(formatted_date)
#
# y = input()
# w = y.split(',')
# z = [elem.strip() for elem in w]
# print(z)

period = '2024-04-04, 2024-05-04'
name_file_with_spaces = period.split(',')
name_file_without_spaces = [elem.strip() for elem in name_file_with_spaces]
date_format = '%Y-%m-%d'
parse_date = [datetime.datetime.strptime(elem, date_format) for elem in name_file_without_spaces]
formatted_date_as_list = [elem.strftime('%d.%m.%y') for elem in parse_date]
formatted_date = '-'.join(formatted_date_as_list)
print(formatted_date)
