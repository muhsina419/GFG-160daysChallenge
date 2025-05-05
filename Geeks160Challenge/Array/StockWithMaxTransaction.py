def max_profit(prices):
    profit=0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            profit += prices[i]-prices[i-1]
    return profit

if __name__ == "__main__":
    arr = list(map(int, input("Enter the prices day by day separated by spaces : ").split()))
    result = max_profit(arr)
    print("maximum profit = ", result)
