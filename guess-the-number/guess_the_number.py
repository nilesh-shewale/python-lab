import sys, os
from random import randint

def get_limits():
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        if start >= end:
            print(f"Error: start limit ({start}) must be smaller than the end limit ({end})")
            sys.exit(1)
    except IndexError as err:
        print(f"Error: {err}")
        print(f"Usage: python {os.path.basename(sys.argv[0])} <int:start> <int:end>")
        sys.exit(1)
    except ValueError as err:
        print(f"Error: {err}")
        print(f"Usage: python {os.path.basename(sys.argv[0])} <int:start> <int:end>")
        sys.exit(1)
    return start, end

def process_guess(key, guess):
    if guess == key:
        return 0
    elif guess < key:
        return -1
    else:
        return 1

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    start, end = get_limits()
    key = randint(start, end)
    guesses = 0
    while True:
        try:
            guess = int(input(f"Guess a number ({start}~{end}): "))
        except ValueError:
            print(f"Oops! Guess must be a number.", end='\n\n')
            continue
        else:
            if not (start <= guess <= end):
                print(f"Oops! Guess is out of range.", end='\n\n')
                continue
        guesses += 1
        result = process_guess(key, guess)
        if result == 0:
            if guesses == 1:
                print(f"Habibi, you're a genius! You've guessed the correct number in 1st attempt only.", end='\n\n')
                sys.exit(0)
            else:
                print(f"Wallah, you've the guessed the correct number in {guesses} attempts.", end='\n\n')
                sys.exit(0)
        elif result == -1:
            print("Uff! Raise the bar, try again.", end='\n\n')
        else:
            print("Uff! Lower the bar, try again.", end='\n\n')

if __name__ == "__main__":
    main()