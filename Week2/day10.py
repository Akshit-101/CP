# ------------------------------- Coke Problem ------------------------------------
change_owned = -50
amount_due = 50
while amount_due > 0:
    insert_coin = int(input("Insert Coin: "))
    if insert_coin in [50, 25, 10, 5]:
        amount_due = amount_due - insert_coin
        if amount_due >0:
            print(f"Amount Due: {amount_due}")
        change_owned = change_owned + insert_coin
        if change_owned >= 0:
            print(f"Change Owed: {change_owned}")
    else:
        print(f"Amount Due: {amount_due}")

# --------------------------------- Happy Number ------------------------------------

def isHappy(n: int) -> bool:
    def get_next(number):
        return sum(int(digit) ** 2 for digit in str(number))
    
    seen = set()
    
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    
    return n == 1
