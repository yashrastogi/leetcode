function maxProfit(prices: number[]): number {
  let minPrice = Infinity;
  let maxProfit = 0;
  for (let i = 0; i < prices.length; i++) {
    let profit = prices[i] - minPrice;
    if (prices[i] < minPrice) minPrice = prices[i];
    else if (profit > maxProfit) maxProfit = profit;
  }
  return maxProfit;
}
