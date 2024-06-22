import random
import sys
import matplotlib.pyplot as plt

args = sys.argv

def main():
    if len(args) > 2:
        print("Too many arguments, just give me one int")
    elif len(args) == 2:
        try:
            sides = int(args[1])
            roll_to_win(sides)
        except ValueError:
            print("Please provide a single int as an argument.")
    else:
        print(roll_die(20))

def roll_die(sides):
    return random.randint(1, sides)

def roll_to_win(sides):
    counter = 0
    num = 0
    stop_at = 500
    keep_count = {i: 0 for i in range(1, sides + 1)}

    while num != sides:
        num = roll_die(sides)
        counter += 1

        keep_count[num] += 1

        if num == sides:
            print(f"It took {counter} rolls to hit {sides} on a {sides}-sided die.")
            break
        if counter == stop_at:
            print(f"We stopped at {counter}, maybe next time!")
            break

    plot_results(keep_count)

def plot_results(keep_count):
    sorted_keys = sorted(keep_count.keys())
    sorted_values = [keep_count[key] for key in sorted_keys]
    plt.figure(figsize=(10, 6))
    plt.bar(sorted_keys, sorted_values, color='skyblue', width=0.8)
    plt.xlabel('Die Face', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.title('Frequency of Each Die Face Rolled', fontsize=16)
    plt.xticks(sorted_keys, rotation=45)
    plt.grid(True)
    plt.show()

main()
