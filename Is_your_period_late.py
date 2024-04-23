from datetime import date


def period_is_late(last, today, cycle_length):
    tmp = today - last
    return tmp.days > cycle_length


def period_is_late_top(last, today, cycle_length):
    return (today - last).days > cycle_length


def main():
    print(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35))
    print(period_is_late_top(date(2016, 6, 13), date(2016, 7, 16), 35))


if __name__ == "__main__":
    main()
