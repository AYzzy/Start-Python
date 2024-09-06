def biggest_odd(number):
    largest_odd = 0
    for num in number:
        if int(num) > largest_odd and int(num) % 2 == 1:
            largest_odd = int(num)
    return largest_odd


def biggest_odd2(number):
    largest_odd = 0
    largest = [num for num in number if int(num) > largest_odd and int(num) % 2 == 1]
    return largest
