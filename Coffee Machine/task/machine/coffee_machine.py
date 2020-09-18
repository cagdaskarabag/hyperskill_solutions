avail_water = int(input("Write how many ml of water the coffee machine has: "))
avail_milk = int(input("Write how many ml of milk the coffee machine has: "))
avail_beans = int(input("Write how many grams of coffee beans the coffee machine has: "))
cups = int(input("Write how many cups of coffee you will need: "))

needed_water = 200 * cups  # How much is needed for cups wanted.
needed_milk = 50 * cups
needed_beans = 15 * cups

cup_water = avail_water // 200  # How many cups could be made from each ingredient
cup_milk = avail_milk // 50
cup_beans = avail_beans // 15

if needed_water <= avail_water and needed_milk <= avail_milk and needed_beans <= avail_beans:  # We have enough ingredients
    if cup_water * 200 - needed_water >= 200 and cup_milk * 50 - needed_milk >= 50 and cup_beans * 15 - needed_beans >= 15:  # At least 1 more cup
        extra_water = (cup_water * 200 - needed_water) // 200
        extra_milk = (cup_milk * 50 - needed_milk) // 50
        extra_beans = (cup_beans * 15 - needed_beans) // 15
        extra_cups = min(extra_water, extra_milk, extra_beans)  # The most extra that can be made
        print(f"Yes, I can make that amount of coffee (and even {extra_cups} more than that)")
    else:
        print("Yes, I can make that amount of coffee")  # Can't make more
else:
    if cup_water * 200 < needed_water or cup_milk * 50 < needed_milk or cup_beans * 15 < needed_beans:
        max_cups = min(cup_water, cup_milk, cup_beans)
        print(
            f"No, I can make only {max_cups} cups of coffee")  # Can't make enough cups. Have beans for 5 cups but only water for 1? Only 1 cup.
