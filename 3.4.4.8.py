def is_rightangled(a, b, c):
    return abs((a ** 2 + b ** 2) - (c ** 2)) < 0.001

# test cases and expected results
is_rightangled(1.5, 2.0, 2.5) #True
is_rightangled(4.0, 8.0, 16.0) #False
is_rightangled(4.1, 8.2, 9.1678787077) #True
is_rightangled(4.1, 8.2, 9.16787) #True
is_rightangled(4.1, 8.2, 9.168) #False
is_rightangled(0.5, 0.4, 0.64031) #True