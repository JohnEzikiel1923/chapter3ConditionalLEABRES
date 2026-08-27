try:
    total_score = input('Enter Total score: ')
    score = float(total_score)
    if 90 <= score <= 100:
        print('Grade: A')
    elif score <= 80:
        print('Grade: B')
    elif score <= 70:
        print('Grade: C')
    elif score <= 69:
        print('Grade: Needs improvement')
    exit()

except ValueError:
    print('Error: Please enter a valid numerical score')
    score = -1
    exit()


