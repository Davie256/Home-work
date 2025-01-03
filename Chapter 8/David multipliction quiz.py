import random, time

print('You will be given 10 questions to answer without delay\n')

def my_multiplication_quiz():
    for questions in range(1,12):
        if questions <= 10:
            numb_1 = random.randint(0,9)
            numb_2 = random.randint(0,9)

            for tries in range(1,5):
                if tries < 4:
                    print(f'{questions}. {numb_1} X {numb_2} ')
                    start_time = time.time()

                    comp_result = numb_1 * numb_2

                    use_result = int(input('Answer: '))
                    end_time = time.time()

                    time_limit = end_time - start_time

                    if use_result == comp_result and time_limit<=8:
                        print('Correct!\n')
                        time.sleep(1)
                        break
                    elif use_result == comp_result and time_limit>8:
                        print('Timeout\n')
                        continue
                    elif use_result != comp_result and time_limit<=8:
                        print('Incorrect\n')
                        continue
                else:
                    print('The number of trials for this question are done\n')
                    break
        else:
            print('The 10 questions are done!!!')


my_multiplication_quiz()



