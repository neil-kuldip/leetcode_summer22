# 121. Best Time to Buy and Sell Stock
# Difficulty: Easy

# Prompt
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Thought Process 
# Max difference between largest and smallest value, given smallest value comes first
# Can determine for any index what is the max element value to the right of it --> Worked on another problem with this exact prompt
# Make a duplicate array but iterate backwards to get max value for each index
# Now just one iteration to get the max difference
import typing as *

def maxProfit(prices: List[int]) -> int:
    if len(prices) == 1:
        return 0
    
    maxPrices = [0]*len(prices)
    maxPrices[-1] = prices[-1]
    for itr in range(len(prices)-2, -1, -1):
        maxPrices[itr] = prices[itr] if prices[itr] > maxPrices[itr+1] else maxPrices[itr+1]
    print(maxPrices)
    
    maxDiff = 0
    for itr in range(len(prices)):
        if maxPrices[itr] - prices[itr] > maxDiff:
            maxDiff = maxPrices[itr] - prices[itr]
    
    return maxDiff

# Time complexity is O(n) since we are doing multiple iterations through the input array in making the maxPrices array and finding the max difference
# Space complexity is O(n) for the maxPrices array made to find the max difference
