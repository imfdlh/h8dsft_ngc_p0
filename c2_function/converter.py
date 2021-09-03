def temp_c_k(temp, scale):
    '''
    convert temperature from celsius to kelvin or otherwise
    input parameter should be celsius or kelvin
    '''
    lower_scale = scale.lower()
    if lower_scale == 'c' or lower_scale == 'celsius':
        # convert from celsius to kelvin
        new_temp = round(temp + 273.15, 2)
        new_scale = 'K'
    elif lower_scale == 'k' or lower_scale == 'kelvin':
        # convert from kelvin to celsius
        new_temp = round(temp - 273.15, 2)
        new_scale = 'C'
    else:
        # send an error message if input is not in celsius or kelvin
        return 'scale is not in celsius or kelvin'
    return new_temp, new_scale

def temp_to_f(temp, scale):
    '''
    convert temperature to fahrenheit
    input parameter should be celsius or kelvin
    '''
    lower_scale = scale.lower()
    if lower_scale == 'c' or lower_scale == 'celsius':
        # convert from celsius to fahrenheit
        new_temp = round(((9/5) * temp) + 32, 2)
    elif lower_scale == 'k' or lower_scale == 'kelvin':
        # convert from kelvin to fahrenheit
        new_temp = round((9/5) * (temp - 273.15) + 32, 2)
    else:
        # send an error message if input is not in celsius or kelvin
        return 'scale is not in celsius or kelvin'
    return new_temp

def temp_from_f(temp, to_scale):
    '''
    convert temperature from fahrenheit
    output parameter should be celsius or kelvin
    '''
    lower_to_scale = to_scale.lower()
    if lower_to_scale == 'c' or lower_to_scale == 'celsius':
        # convert from fahrenheit to celcius
        new_temp = round((5/9) * (temp - 32), 2)
    elif lower_to_scale == 'k' or lower_to_scale == 'kelvin':
        # convert from fahrenheit to kelvin
        new_temp = round((5/9) * (temp - 32) + 273.15, 2)
    else:
        # send an error message if expected output is not in celsius or kelvin
        return 'expected scale is not in celsius or kelvin'
    return new_temp, to_scale.capitalize()