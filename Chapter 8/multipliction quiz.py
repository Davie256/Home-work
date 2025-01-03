import random, time

print('You will be given 10 questions to answer without delay')

start_time = time.time()

for questions in range(1,12):
    if questions <= 10:
        numb_1 = random.randint(0,9)
        numb_2 = random.randint(0,9)

        for count in range(1,4):

            use_result = int(input(f'{questions}. {numb_1} X {numb_2} = '))
            comp_result = numb_1 * numb_2

            current_time = time.time()
            time_limit = current_time - start_time

            if use_result == comp_result and count<3 and time_limit<=5:
                print('Correct')
                break
            elif use_result == comp_result and count<3 and time_limit>5:
                print('Timeout')
                continue
            elif use_result != comp_result and count<3 and time_limit<=5:
                print('Incorrect')
                continue
            else:
                print('Your number of trials are done')
                break
    else:
        print('The questions are done!!!')



