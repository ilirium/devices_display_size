# Lib
from calcs import calc_height_width

if __name__ == '__main__':
    kindle_11 = calc_height_width(1448, 1072, 6)
    kindle_paperwhite5 = calc_height_width(1648, 1236, 6.8)
    kindle_oasis3 = calc_height_width(1680, 1264, 7)

    print(f'Kindle 11 = {kindle_11}')
    print(f'Kindle Paperwhite 5 = {kindle_paperwhite5}')
    print(f'Kindle Oasis 3 = {kindle_oasis3}')
    