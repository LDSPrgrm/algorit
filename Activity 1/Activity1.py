import random

# Function definitions
# Declare the length of the binary digit
def get_binary_length():
    return random.randint(3, 10)

# Declare the binary digit
def get_binary_digit(binary_length):
    binary_digit = ""
    for _ in range(binary_length):
        binary_digit += str(random.randint(0, 1))
    return binary_digit

# Get the user answer
def get_user_answer():
    while True:
        user_answer = input("Your answer is: ")
        if user_answer.isdigit():
            return int(user_answer)
        else:
            print("\nInvalid input. Please enter a valid number.\n")
            continue

# Get the result of the question
def get_result(binary_digit, user_answer):
    correct_answer = int(binary_digit, 2)
    print("The correct answer is:", correct_answer)
    
    is_correct = user_answer == correct_answer
    print("Your answer is", "correct!" if is_correct else "wrong!")
    return is_correct

# Get the score of the user
def get_score(score, result):
    if result:
        score += 1
    return score

# Ask the player if he wants to play again
def play_again():
    while True:
        play_again_input = input("\nDo you want to continue? (Y/N): ")
        play_again_input = play_again_input.lower()
        
        if play_again_input == "y":
            play = True
            break
        elif play_again_input == "n":
            play = False
            break
        else:
            print("Invalid input. Please try again.")
    return play

# Driver code
# Declare the total score and total attempts of the user 
# as well as the play variable
score, attempts = 0, 0
play = True
while play:
    attempts += 1
    binary_length = get_binary_length()
    binary_digit = get_binary_digit(binary_length)
    print("\nBinary digit:", binary_digit)

    user_answer = get_user_answer()
    result = get_result(binary_digit, user_answer)
    
    score = get_score(score, result)
    print("Score: ", score, "/", attempts)
    
    play = play_again()

# Display the final score
print("Final score:", score, "/", attempts)