array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

def merge(array1, array2):
    # n = len(array1)
    # m = len(array2)
    # for i in range(0, n-1):
    #     for j in range(0, m-1):
    #         if array1[i] < array2[j]:
    #             array_c.append(array1[i])
    #             i += 1
    #         else:
    #             array_c.append(array2[j])
    array_c = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            array_c.append(array1[array1_index])
            array1_index += 1
        else:
            array_c.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            array_c.append(array2[array2_index])
            array2_index += 1
    elif array2_index == len(array2):
        while array1_index < len(array1):
            array_c.append(array1[array1_index])
    return array_c


print(merge(array_a, array_b))