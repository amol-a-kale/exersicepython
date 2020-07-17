def cel_far(cel_temp):
    far_temp = (cel_temp * 9 / 5) + 32
    print('the celcius temp ' + str(cel_temp) + ' is convert into fahrenheit is ' + str(far_temp))


def far_cel(far_temp):
    cel_temp = (far_temp - 32) * 5 / 9
    print('the fahrenheit temp ' + str(far_temp) + ' is convert into celcius temp is ' + str(cel_temp))


cel_far(40)
far_cel(104)

