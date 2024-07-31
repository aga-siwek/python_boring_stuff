if __name__ == '__main__':
    import random
    import pyinputplus as pyip
    import time
    number_of_questions = 10
    # correct_answers = 0 




    try:
        for question_num in range(number_of_questions):
            random_num_1 = random.randrange(1,10)
            random_num_2 = random.randrange(1,10)
            result = random_num_1*random_num_2
            answer = pyip.inputNum(f"the rezult of {random_num_1}x{random_num_2}: ", allowRegexes=[("^%s$" % result)], blockRegexes=[(".*")], timeout=10, limit=3)
            if answer == result:
                # correct_answers += 1
                print("correct")
            elif answer != result:
                print(f"Wrong answer, it should be {result}.")
        
    except pyip.TimeoutException:
        print("Time out")
    except pyip.RetryLimitException:
        print("Out of fires")
