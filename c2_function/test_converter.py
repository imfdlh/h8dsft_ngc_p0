from converter import temp_c_k, temp_to_f, temp_from_f

# from celsius to kelvin or otherwise
print('100 C ->', temp_c_k(100, 'C')[0], temp_c_k(100, 'C')[1])
print('300 K ->', temp_c_k(300, 'kelvin')[0], temp_c_k(300, 'kelvin')[1])
print('80 F ->', temp_c_k(80, 'f'))

# from celsius or kelvin to fahrenheit
print('100 C ->', temp_to_f(100, 'C'), 'F')
print('300 K ->', temp_to_f(300, 'kELVIN'), 'F')
print('80 R ->', temp_to_f(80, 'r'))

# from fahrenheit to celsius or kelvin
print('100 F to celsius ->', temp_from_f(100, 'Celsius')[0], temp_from_f(100, 'Celsius')[1])
print('200 F to kelvin ->', temp_from_f(200, 'k')[0], temp_from_f(200, 'k')[1])
print('80 F to reamur -> ', temp_from_f(80, 'r'))