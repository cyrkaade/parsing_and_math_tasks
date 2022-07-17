# 3

tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]


# Проверяем пересечения между интервалов уроков и учеников.
def lesson_pupil(a, b, c, d):
    if (a < c and d < b) or (a < c and b == d) or (a == c and d < b):
        return c, d
    elif (c < a and b < d) or (c < a and b == d) or (a == c and b < d):
        return a, b
    elif b > c > a:
        return c, b
    elif d > a > c:
        return a, d
    elif a == c and b == d:
        return a, d
    else:
        return 0, 0


# Проверяем пересечения между интервалов уроков, учеников и учителей.
def tutor_pupil(a, b, c, d):
    if a == 0 and b == 0:
        return 0
    if (a < c and d < b) or (a < c and b == d) or (a == c and d < b):
        return d - c
    elif (c < a and b < d) or (c < a and b == d) or (a == c and b < d):
        return b - a
    elif b > c > a:
        return b - c
    elif d > a > c:
        return d - a
    elif a == c and b == d:
        return d - a
    return 0


def appearance(intervals):
    for i in range(len(intervals)):
        lst = []
        lessons = intervals[i]['data']["lesson"]
        pupils = intervals[i]['data']["pupil"]
        tutors = intervals[i]['data']["tutor"]
        lesson_start = lessons[0]
        lesson_end = lessons[1]
        total = 0
        difference = 0

        # Итерируем по ученикам
        for j in range(0, len(pupils), 2):
            pupil_online = pupils[j]
            pupil_offline = pupils[j + 1]
            p_interval = lesson_pupil(lesson_start, lesson_end, pupil_online, pupil_offline)
            lst.append(p_interval)

            # Итерируем по учителям
            for k in range(0, len(tutors), 2):
                tutor_online = tutors[k]
                tutor_offline = tutors[k + 1]
                total += tutor_pupil(p_interval[0], p_interval[1], tutor_online, tutor_offline)

        # Проверяем на разность пользователей итерируя их интервалы.
        for q in range(0, len(lst) - 1):
            starting = lst[q][0]
            ending = lst[q][1]
            for q1 in range(q + 1, len(lst)):
                starting2 = lst[q1][0]
                ending2 = lst[q1][1]
                difference += tutor_pupil(starting, ending, starting2, ending2)
        print(total - difference)


# Запуск
appearance(tests)
