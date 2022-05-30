TIMESLOTS = [
    {'client': 'Ivanov', 'since': 20, 'till': 22},
    {'client': 'Lurye', 'since': 8, 'till': 16},
    {'client': 'Shmidt', 'since': 12, 'till': 16},
    {'client': 'Nikolarnko', 'since': 14, 'till': 23},
    {'client': 'Buzova', 'since': 14, 'till': 19},
    {'client': 'Katcz', 'since': 16, 'till': 20},
    {'client': 'Zulova', 'since': 16, 'till': 17},
    {'client': 'Schtolcz', 'since': 13, 'till': 18},
    {'client': 'Gotye', 'since': 23, 'till': 23},
    {'client': 'Borisov', 'since': 9, 'till': 11},
    {'client': 'Kalrisova', 'since': 6, 'till': 23},
    {'client': 'Dunkan', 'since': 16, 'till': 18},
    {'client': 'McLaud', 'since': 20, 'till': 23}
]


def lenght(x, y):
    m = {'hour': x, 'count': len(y)}
    final_list.append(m)


H0 = []
H1 = []
H2 = []
H3 = []
H4 = []
H5 = []
H6 = []
H7 = []
H8 = []
H9 = []
H10 = []
H11 = []
H12 = []
H13 = []
H14 = []
H15 = []
H16 = []
H17 = []
H18 = []
H19 = []
H20 = []
H21 = []
H22 = []
H23 = []
final_list = []

for d in TIMESLOTS:
    client_hours = []
    for i in range(d.get('since'), (d.get('till') + 1)):
        client_hours.append(i)
        if i == 0:
            H0.append(i)
        elif i == 1:
            H1.append(i)
        elif i == 2:
            H2.append(i)
        elif i == 3:
            H3.append(i)
        elif i == 4:
            H4.append(i)
        elif i == 5:
            H5.append(i)
        elif i == 6:
            H6.append(i)
        elif i == 7:
            H7.append(i)
        elif i == 8:
            H8.append(i)
        elif i == 9:
            H9.append(i)
        elif i == 10:
            H10.append(i)
        elif i == 11:
            H11.append(i)
        elif i == 12:
            H12.append(i)
        elif i == 13:
            H13.append(i)
        elif i == 14:
            H14.append(i)
        elif i == 15:
            H15.append(i)
        elif i == 16:
            H16.append(i)
        elif i == 17:
            H17.append(i)
        elif i == 18:
            H18.append(i)
        elif i == 19:
            H19.append(i)
        elif i == 20:
            H20.append(i)
        elif i == 21:
            H21.append(i)
        elif i == 22:
            H22.append(i)
        elif i == 23:
            H23.append(i)
    client_hours = tuple(client_hours)
    dic = {'hours': client_hours}
    d.update(dic)

lenght(0, H0)
lenght(1, H1)
lenght(2, H2)
lenght(3, H3)
lenght(4, H4)
lenght(5, H5)
lenght(6, H6)
lenght(7, H7)
lenght(8, H8)
lenght(9, H9)
lenght(10, H10)
lenght(11, H11)
lenght(12, H12)
lenght(13, H13)
lenght(14, H14)
lenght(15, H15)
lenght(16, H16)
lenght(17, H17)
lenght(18, H18)
lenght(19, H19)
lenght(20, H20)
lenght(21, H21)
lenght(22, H22)

final_list.sort(key=lambda x: (-x['count']))
print('Наибольшее количество клиентов (', final_list[0].get('count'),
      ') может принять груз в', final_list[0].get('hour'), 'часов.')
print('Их имена:')
for s in TIMESLOTS:
    for v in s.get('hours'):
        if v == final_list[0].get('hour'):
            print(s.get('client'))
