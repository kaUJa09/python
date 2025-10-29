import math as m
# print(2 * (3 - 1))
# print((5-1)*(5+1))
# print(0.3*(4-1))
# print((91-1)/(2+1))
# print(5*4/3 ** 0.5)
# print((1)/(3)+5*(0.2-0.001)/(91))
# print((40-(4.25*7.08+6.768/0.75))*2050)
# print((0.16*(3.2-(3/40))+2*(3/11)*4.125/3*(3/4))/5*(1/6)*0.3-0.3*4.5+(1/3)*0.3)


# x = 24
# y = 31.4
# print(type(x))
# print(type(y))


# a = 12
# b = 7
# diff = abs(a - b)
# print(diff)


# potatoes = 290
# bag = 25
# full_bags = potatoes // bag
# kg = potatoes % bag
# print('Полностью заполненных мешков:', full_bags)
# print('Остаток картошки (кг):', kg)


# h_1 = 13
# m_1 = 25
# h_2 = 19
# m_2 = 40
# start_minutes = h_1 * 60 + m_1
# end_minutes = h_2 * 60 + m_2
# total_minutes = end_minutes - start_minutes
# h = total_minutes // 60
# m = total_minutes % 60
# print('Василий работал:', h, 'часов и', m, 'минут')


# old_price = int(input('Write old price: '))
# new_price = int(input('Write new price: '))
# res = round(abs(new_price - old_price) / old_price * 100, 1)
# print('Изменение цены:', res, '%')


# x = 2
# y = m.exp(1 / (1 + m.cos(x)**2))
# print(y)


# total_parts = 1500
# per_post = 45
# res = m.ceil(total_parts / per_post)
# print(f'Для выполнения заказа необходимо задействовать {res} поста.')


# katet_1 = int(input('Введите длину катета: '))
# katet_2 = int(input('Введите длину катета: '))
# gip = int(input('Введите длину гипотенузы: '))
# smallest_katet = min(katet_1, katet_2)
# sin_angle = smallest_katet / gip
# print('Синус наименьшего угла:', sin_angle)


# katet_1 = int(input('Введите длину катета: '))
# katet_2 = int(input('Введите длину катета: '))
# gip = int(input('Введите длину гипотенузы: '))
# sin_angle = min(katet_1, katet_2) / gip
# angle_rad = m.asin(sin_angle)
# angle_deg = angle_rad * 180 / m.pi
# print('Меньший острый угол равен:', round(angle_deg, 2), 'градусов')
