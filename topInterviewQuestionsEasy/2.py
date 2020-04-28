def maxProfit(prices):
    maxprofit = 0
    for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                maxprofit += prices[i] - prices[i-1]
    return maxprofit


foo = [1,7,2,3,6,7,6,7]

print(maxProfit(foo))

