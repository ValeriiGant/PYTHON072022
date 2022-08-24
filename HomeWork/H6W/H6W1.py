Transformation = lambda x: x*1
val = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformed_val = list(map(Transformation, val))
if val == transformed_val:
    print('OK')
else:
    print('no')