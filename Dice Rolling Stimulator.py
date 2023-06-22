import random

def main():
    print("=== Dice Rolling Simulator ===")
    while True:
        input("Enter")
        dice_result = random.randint(1, 6)
        print("You rolled:", dice_result)
        play_again = input("Roll again? (y/n): ")
        if play_again.lower() != 'y':
            break

if __name__ == '__main__':
    main()

