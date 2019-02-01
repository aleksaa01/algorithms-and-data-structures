def max_num_of_activities(activities, total_time):
    activities.sort(key=lambda activity: activity[0])

    used_time = 0
    ending = 0
    res = 0
    for activity in activities:
        start, end = activity[0], activity[1]
        if start >= ending:
            used_time += end - start
            ending = end
            res += 1

        if used_time > total_time:
            return res - 1

    return res


if __name__ == '__main__':
    a = [(1, 2), (3, 4), (3, 6), (5, 7), (8, 9), (5, 9)]
    print(max_num_of_activities(a, 4))
