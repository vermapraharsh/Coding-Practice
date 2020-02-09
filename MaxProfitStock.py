#Max Profit Stock
#Cost of stock is given in array where each index is the day, and the element is the price of the stock on the given day

stockPrice = [100, 180, 260, 310, 40, 535, 695, 696, 0]
buyDate = []
sellDate = []
margin = 0
maxProfit = 0
arrayLen = len(stockPrice)
for x in range(0,arrayLen):
    for y in range(x+1,arrayLen):
        margin = stockPrice[y] - stockPrice[x]
        if margin > maxProfit:
            maxProfit = margin
            buyDate.append(x)
            sellDate.append(y)
print('Maximum profit is:' + str(maxProfit))
print('Buy on days:' + str(buyDate))
print('Sell on corresponding days:' + str(sellDate))
