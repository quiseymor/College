def exchange_coins(amount, coins):
    if amount == 0:
        yield []
    elif not coins:
        return
    else:
        coin = coins[0]
        max_count = amount // coin
        for count in range(max_count + 1):
            for remainder in exchange_coins(amount - coin * count, coins[1:]):
                yield [coin] * count + remainder


amount = 10
coins = [1, 2, 5]

for variant in exchange_coins(amount, coins):
    print(variant)
