input = 20


def find_prime_list_under_number(number):
    prime_number_list = []
    for n in range(2, number+1):
        for i in prime_number_list:
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_number_list.append(n)

    return prime_number_list


result = find_prime_list_under_number(input)
print(result)