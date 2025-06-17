"""
Purpose: A code to run the self-esteem test on the user and return their score.
File: esteem.py
Author: Kyler Edwards
"""

def main():
    add_answers = []
    sub_answers = []
    questions_list = ["I feel that I am a person of worth, at least on an equal plane with others.", "I feel that I have a number of good qualities.", "All in all, I am inclined to feel that I am a failure.", "I am able to do things as well as most other people.", "I feel I do not have much to be proud of.", "I take a positive attitude toward myself.", "On the whole, I am satisfied with myself.", "I wish I could have more respect for myself.", "I certainly feel useless at times.", "At times I think I am no good at all."]

    print ("Please answer the following 10 statements based on how much you agree with the statement. Choose one of the following answers:\nD (Strongly Disagree)\nd (Disagree)\na (Agree)\nA (Strongly Agree)")

    for i in range(len(questions_list)):
        answer = get_answer(i + 1, questions_list[i])
        if i + 1 in [1, 2, 4, 6, 7]:
            add_to_list(add_answers, answer)
        else:
            add_to_list(sub_answers, answer)
    
    user_total = get_user_sum(add_answers, sub_answers)

    print (f"Your self-esteem score is {user_total}/30.\nA score below 15 may indicate problematic low self-esteem.")

def add_to_list(list, item):
    list.append(item)

def get_answer(question_num, question):
    """ 
    Gets an answer on a scale of Strongly Disagree to Strongly Agree as a number.
    Param: Question
    Return: Answer to question 
    """
    while True:
        str_answer = input (f"{question_num}. {question}\nYour Answer:")
        if str_answer.lower() in ['d', 'a']:
            break
        else:
            print ('\nYou have entered an invalid input. Please answer with "D" (Strongly Disagree),\n"d" (Disagree), "a" (agree), or "A" (Strongly Agree). \nBe aware that it is case sensitive.')

    if str_answer == 'D':
        num_answer = 0
    elif str_answer == 'd':
        num_answer = 1
    elif str_answer == 'a':
        num_answer = 2
    else:
        num_answer = 3
    
    return num_answer

def get_user_sum(add_list, sub_list):
    """ 
    Calculates the user's total self-esteem score
    Params: list of answers to positive questions, list of answers to negative questions
    Return: Sum of those.
    """
    add_total = sum(add_list)
    sub_total = 15 - sum(sub_list)
    total = add_total + sub_total
    return total


if __name__ == "__main__":
    main()