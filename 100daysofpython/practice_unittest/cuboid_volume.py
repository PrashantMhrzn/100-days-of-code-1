def cuboid_volume(l):
    if type(l) not in [int, float]:
        raise TypeError()
    return l*l*l


# length = [2, 1.1, -2.5, 2j, 'two']

# for i in length:
#     print("Result: ", cuboid_volume(i))
