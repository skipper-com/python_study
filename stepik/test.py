from tkinter import S


s = input()
l = input()
d, j = {}, 0
for i, j in zip('abcdefghijklmnopqrstuvwxyz', s):
    d[i] = j

#print(d)
t = str.maketrans(d)
print(t)
print(l.lower().translate(t))




# import pickle
# import sys

# lines = [x.strip() for x in sys.stdin]

# with open(lines[0], mode='rb') as file:
#     g = pickle.load(file)
#     crc = 0 
#     if type(g) == list:
#         crc = max([i for i in g if type(i) == int]) * min([i for i in g if type(i) == int]) 
#     elif type(g) == dict:
#         crc = sum([g[i] for i in g if type(g[i]) == int])

# if crc == int(lines[1]):
#     print('Контрольные суммы совпадают')
# else:
#     print('Контрольные суммы не совпадают')



# def filter_dump(name, l, datatype):
#     d = [i for i in l if type(i) == datatype]
#     with open(name, mode='wb') as file:
#         pickle.dump(d, file)
# filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)
# with open('numbers.pkl', mode='rb') as file:
#     g = pickle.load(file)
#     print(*g)
# g = pickle.dumps(func)
# # print(pickle.loads(g)('lie', 'a'))

# lines = [x.strip() for x in sys.stdin]
# with open(lines[0], mode='rb') as file:
#     g = pickle.load(file)
#     print(g(*lines[1:]))




# with open('func.pkl', mode='wb') as file:
#     pickle.dump(func, file)

# from zipfile import ZipFile
# with ZipFile('desktop.zip') as zip_file:
#     info = zip_file.infolist()
#     for x in info:
#         level = x.filename.count('/') - 1 
#         filesize = x.file_size
#         i, abbs = 0, ['B', 'KB', 'MB', 'GB']
#         while filesize // 1024 > 0:
#             filesize = filesize / 1024
#             i += 1
#         if x.is_dir():
#             print("  " * level, x.filename.split('/')[-2], sep = '')
#         else:
#             print(f'{"  " * (level+1)}{x.filename.split("/")[-1]} {round(filesize)} {abbs[i]}')

# from datetime import datetime
# pattern = '%Y-%m-%d %H:%M:%S'
# orig_date = datetime.strptime('2021-11-30 14:22:00', pattern)
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     l = []
#     for x in info:
#         if not x.is_dir():
#             l.append((x.filename.split('/')[-1], x.date_time, x.file_size, x.compress_size))
# l = sorted(l, key=lambda x: str.lower(x[0]))
# for i in l:
#     print(f'{i[0]}\n  Дата модификации файла: {datetime(*i[1]).strftime(pattern)}\n  Объем исходного файла: {i[2]} байт(а)\n  Объем сжатого файла: {i[3]} байт(а)\n')


# import json
# with open('food_services.json', encoding='utf8') as fi:
#     j = json.load(fi)
#     d = {}
#     for row in j:
#         d.setdefault(row['TypeObject'], []).append((row['Name'], row['SeatsCount']))
#     for key in sorted(d):
#         print(f'{key}: {max(d[key], key=lambda x: x[1])[0]}, {max(d[key], key=lambda x: x[1])[1]}')


# with open('playgrounds.csv', encoding='utf8') as fi, open('addresses.json', 'w') as fo:
#     _, *playgrounds = csv.reader(fi, delimiter=';')
#     d = {}
#     [d.setdefault(i[1], {}).setdefault(i[2], []).append(i[3]) for i in playgrounds]
#     json.dump(d, fo, indent=3, ensure_ascii=False)
# with open('playgrounds.csv', encoding='utf-8') as file:
#     csv_data = list(csv.reader(file, delimiter=';'))
#     l = []
#     for r in csv_data[1:]:
#         l.append((r[1], r[2], r[3]))
#     m = {}
#     for r in l:
#         m[r[1]] = m.get(r[1], []) + [r[2]]
#     d = {}
#     for r in l:
#         d[r[0]] = d.get(r[0], {}) | {r[1]: m[r[1]]}


# with open('addresses.json', 'w', encoding='utf-8') as f:
#     json.dump(d, f, indent='    ', ensure_ascii=False)



#  for k in json_data:
#     if type(json_data[k]) == list:
#         print(f'{k}: {", ".join(str(x) for x in json_data[k])}')
#     else:
#         print(f'{k}: {json_data[k]}')


# with open('prices.csv', encoding='utf-8') as file:
#     reader = list(csv.reader(file, delimiter=';'))
#     a = reader[0]
#     d = {}
#     for row in reader[1:]:
#         d[row[0]] = [(i, int(j)) for i, j in zip(a[1:], row[1:])]
#         d[row[0]] = min(d[row[0]], key=lambda x: (x[1], x[0]))
#     print(f'{d[min(d, key=lambda x: (d[x][1], d[x][0], x))][0]}: {min(d, key=lambda x: (d[x][1], d[x][0], x))}')



# with open('student_counts.csv', encoding='UTF-8') as f:
#     l = list(csv.reader(f, delimiter=','))
#     r = [list(row) for row in zip(*l)]
#     r = [r[0]] + sorted(r[1:], key=lambda x: (int(x[0].split('-')[0]), x[0]))
#     with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file:
#         writer = csv.writer(file)
#         for i in range(len(r[0])):
#             writer.writerow([v[i] for v in r])







# header, *rows = csv.reader(f)
# d = {i[1]:i for i in sorted(rows, key=lambda x: datetime.strptime(x[2], '%d/%m/%Y %H:%M'))}
# print(*sorted(rows, key=lambda x: datetime.strptime(x[2], '%d/%m/%Y %H:%M')), sep='\n')
# with open('new_name_log.csv', 'w', encoding='UTF-8', newline='') as f:
# 	w = csv.writer(f)
# 	w.writerow(header)
# 	w.writerows(sorted(d.values(), key=lambda x: x[1]))

# with open('name_log.csv', encoding='utf-8') as csv_file:
#     l = list(csv.reader(csv_file, delimiter=','))
#     a = l[0]
#     del l[0]
#     r = {}
#     for row in l:
#         #print(row)
#         r[row[1]] = r.get(row[1], []) + [(row[0], datetime.strptime(row[2], pattern))] 
#     for k in r:
#         r[k] = max(r[k], key=lambda x: x[1])

#     with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(a)
#         for a in sorted(r):
#             writer.writerow([r[a][0], a, datetime.strftime(r[a][1], pattern)])






    # r = {}
    # for row in d:
    #     r[row['district']] = r.get(row['district'], 0) + int(row['number_of_access_points'])
    # r = sorted(r.items(), key=lambda item: (-item[1], item[0]))
    # for row in r:
    #     print(f'{row[0]}: {row[1]}')

    # with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(['domain','count'])
    #     for row in zip(l, [r[a] for a in l]):
    #         writer.writerow(row)



# l = sorted(rows, key=lambda x: x[n-1] if n == 1 else int(x[n-1]))
# for line in l:
#     print(*line, sep=',')


# import sys
# from datetime import datetime
# pattern = '%d.%m.%Y'
# numbers = [int(x) for x in sys.stdin]
# a = numbers[1] - numbers[0]
# q = numbers[1] / numbers[0]
# if all(numbers[i] + a == numbers[i+1] for i in range(len(numbers) - 1)):
#     print('Арифметическая прогрессия')
# elif all(numbers[i] * q == numbers[i+1] for i in range(len(numbers) - 1)):
#     print('Геометрическая прогрессия')
# else:
#     print('Не прогрессия')


# for d in dates:
#     if
#     title, cat, score = line.split('/')
#     if cat.strip() == lines[-1].strip():
#         news.append([float(score.strip()), title.strip()])
# l = sorted(news, key=lambda a: (a[0], a[1]))
# for i in l:
#     print(i[1])

# from datetime import datetime
# pattern = '%Y-%m-%d'
# dates = list(map(lambda x: datetime.strptime(x.strip('\n'), pattern), sys.stdin))

# def get_days_in_month(year, month):
#     month = list(calendar.month_name).index(month)
#     l = [datetime.date(year, month, x) for x in range (1, calendar.monthrange(year, month)[1] + 1)] 
#     return l


# print(get_days_in_month(2021, 'December'))

# d, l = {}, []
# for i in range(int(input())):
#     *name, birthdate = input().split()
#     name, birthdate = ' '.join(name), datetime.strptime(birthdate, pd)
#     d[name] = birthdate
#     if cur_date < birthdate.replace(year=cur_date.year) <= cur_date + timedelta(days=7) or cur_date < birthdate.replace(year=(cur_date + timedelta(days=7)).year) <= cur_date + timedelta(days=7):
#         l.append(birthdate)
# if l:
#     print(*[k for k,v in d.items() if v == max(l)])
# else:
#     print('Дни рождения не планируются')



# t = {}
# for k, v in d.items():
#     if v not in t:
#         t[v] = 0
#     else:
#         t[v] += 1

# print(max(t,key=t.get))



#     data = {}
# youngest = datetime.max
# pattern = '%d.%m.%Y'

# for _ in range(int(input())):
#     *name, birthday = input().split()
#     name, birthday = ' '.join(name), datetime.strptime(birthday, pattern)
#     if birthday < youngest:
#         youngest = birthday
#     data[name] = birthday
    
# oldest = [name for name, bd in data.items() if bd == youngest]

# if len(oldest) > 1:
#     print(youngest.strftime(pattern), len(oldest))
# else:
#     print(youngest.strftime(pattern), oldest[0])
#     if max_date > datetime.strptime(l[2], pd):
#         max_name = f'{l[0]} {l[1]}'
#         max_date = datetime.strptime(l[2], pd)
#     elif(max_date == datetime.strptime(l[2], pd)):
#         cnt += 1
# if cnt > 1:
#     print(max_date.strftime(pd), cnt)
# else:
#     print(max_date.strftime(pd), max_name)

# dt1, dt2 = datetime.strptime(input(), pd), datetime.strptime(input(), pd)
# while (dt1.day + dt1.month) % 2 == 0:
#     dt1 += timedelta(days=1)
# print(dt1)
# while dt1 <= dt2:
#     if dt1.weekday() not in [0, 3]:
#         print(dt1.strftime(pd))
#     dt1 += timedelta(days=3)
# start_date, end_date = datetime(1,1,1,0,0,0), datetime(9999,12,31,0,0,0)
# d = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
# for y in range(1, 10000):
#     for m in range(1, 13):
#         d[datetime(y,m,13,0,0,0).weekday()] += 1
# print(*d.values(), sep = '\n')

# dt = datetime.strptime(input(), "%d.%m.%Y %H:%M")
# if dt.weekday() <= 4:
#     dt2 = datetime(dt.year, dt.month, dt.day, 21, 0, 0)
#     td = dt2 - dt
#     # print(td.total_seconds())
#     if 0 < td.total_seconds() <= 43200:
#         print(int(td.total_seconds() // 60))
#     else:
#         print('Магазин не работает')
# else:
#     dt2 = datetime(dt.year, dt.month, dt.day, 18, 0, 0)
#     td = dt2 - dt
#     # print(td.total_seconds())
#     if 0 < td.total_seconds() <= 28800:
#         print(int(td.total_seconds() // 60))
#     else:
#         print('Магазин не работает')


# for d in data:
#     s += (datetime.strptime(d[1], pt) - datetime.strptime(d[0], pt)).total_seconds()
# print(int(s // 60))