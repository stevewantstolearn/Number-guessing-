import generator


class machine:

    def guess(self):
        numbers = generator.generator()
        answer = numbers.generateAns()
        unCorrect = True
        print(answer)
        while unCorrect:
            userAnswer = int(input("Alright~ input your guess:\n"))
            print(f"{userAnswer} and {answer}")
            if userAnswer == answer:
                print(f"good job you did it the number is indeed {answer}")
                unCorrect = False
            elif userAnswer > numbers.topNum:
                print(f"a bit too high, keep trying, the number is between {numbers.topNum} and {numbers.lowNum}.")
            elif userAnswer < numbers.lowNum:
                print(f"a bit too low, keep trying, the number is between {numbers.topNum} and {numbers.lowNum}.")
            elif  answer > userAnswer > numbers.lowNum:
                numbers.lowNum = userAnswer
                print(f"GJ closer, the number is between {numbers.topNum} and {numbers.lowNum}")
            elif numbers.topNum> userAnswer>  answer:
                numbers.topNum = userAnswer
                print(f"GJ closer, the number is between {numbers.topNum} and {numbers.lowNum}")
