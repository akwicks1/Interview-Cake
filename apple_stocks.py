def get_max_profit(stock_prices_yesterday):
	"""Get the maximum profit from stocks."""

#input list #output int 
	highest = stock_prices_yesterday[0] 
	lowest = stock_prices_yesterday[0]
	profit = 0
	for num in stock_prices_yesterday: 
		if num < lowest:
			lowest = num 
		elif num > highest:
			highest = num
	profit = highest - lowest 
	return profit


print get_max_profit([10, 7, 5, 8, 11, 9])


# No shorting you must buy before you sell.
# You may not buy and sell in the same time step (at least 1 minute must pass).

def get_max_profit(stock_prices_yesterday):
	"""Return the maximum profit from stocks."""
 
	highest = stock_prices_yesterday[0] 
	lowest = stock_prices_yesterday[0]
	profit = 0
	for num in stock_prices_yesterday: 
		if num < lowest:
			lowest = num 
		elif num > highest:
			highest = num
	profit = highest - lowest 
	return profit


print get_max_profit([10, 7, 5, 8, 11, 9])
