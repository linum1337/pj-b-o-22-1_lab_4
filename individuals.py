def solve_cart():
    sugar_cost = int(input("Введите стоймость 1кг конфет\n"))
    sugar = int(input("Введите кол-во конфет\n"))
    cookies_cost = int(input("Введите стоймость 1кг печенья\n"))
    cookies = int(input("Введите кол-во печенья\n"))
    apples_cost = int(input("Введите стоймость 1кг яблок\n"))
    apples = int(input("Введите кол-во яблок\n"))
    cart = [sugar, cookies, apples, ]
    costs = [sugar_cost, cookies_cost, apples_cost]
    full_count = 0
    for i in range(len(cart)):
        full_count += (cart[i] * costs[i])
    print(full_count)


if __name__ == '__main__':
    solve_cart()
