print("30 Days Down - What did you think")
print()
for i in range(1,30):
    day = input(f"How was your day{i}? ")
    response = f"You thought day{i} was {day}"
    print(f"\033[34m{response:^35}\033[0m")
    print()
    


