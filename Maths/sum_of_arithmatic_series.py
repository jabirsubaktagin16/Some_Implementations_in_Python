def sum_of_series(first_term, common_diff, number_of_terms):
    sum=(number_of_terms/2) * (2*first_term+(number_of_terms-1)*common_diff)
    return sum

if __name__ == '__main__':
    print(sum_of_series(1, 1, 10))
