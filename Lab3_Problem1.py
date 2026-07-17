def greedy_knapsack(w, n1, n2, n3):

    total_weight = 0
    total_profit = 0

    type1 = 0
    type2 = 0
    type3 = 0

    while type2 < n2 and total_weight + 2 <= w:
        type2 += 1
        total_weight += 2
        total_profit += 8

    while type1 < n1 and total_weight + 3 <= w:
        type1 += 1
        total_weight += 3
        total_profit += 7

    while type3 < n3 and total_weight + 5 <= w:
        type3 += 1
        total_weight += 5
        total_profit += 6

    print("\nSelected Items")
    print("Type 1:", type1)
    print("Type 2:", type2)
    print("Type 3:", type3)
    print("Total Weight:", total_weight)
    print("Total Profit:", total_profit)


w = int(input("Enter maximum weight: "))
n1 = int(input("Enter maximum Type 1 items: "))
n2 = int(input("Enter maximum Type 2 items: "))
n3 = int(input("Enter maximum Type 3 items: "))

greedy_knapsack(w, n1, n2, n3)