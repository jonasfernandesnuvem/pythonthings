spam = 0
while spam < 10:
    spam = spam + 1
    if spam in (6,5):
        break
    print('spam is ' + str(spam))