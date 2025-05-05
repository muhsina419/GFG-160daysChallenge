def max_profit(prices):
    profit=0
    if not prices:
        return 0
    
    max_profit=0
    min_price=prices[0]
    
    for i in range(1,len(prices)):
        if prices[i]<min_price:
            min_price=prices[i]
        else:
            profit = prices[i]- min_price
        
        if profit > max_profit:
            max_profit=profit
    return max_profit

if __name__ == "__main__":
    arr = list(map(int, input("Enter the prices day by day separated by spaces : ").split()))
    result = max_profit(arr)
    print("maximum profit = ", result)
