//Max Profit Stock
//Cost of stock is given in array where each index is the day, and the element is the price of the stock on the given day
#include <iostream>
#include <array>

int main()
{
  int stockPrice = {100, 180, 260, 310, 40, 535, 695};
  int margin = 0;
  int maxProfit = 0;
  int arrayLen = stockPrice.size();
  for(int x = 0; x <= stockPrice.size(); x++)
  {
    for(int y = x+1; y <= stockPrice.size(); y++)
    {
      margin = stockPrice[y] - stockPrice[x];
      if(margin > maxProfit)
      {
        maxProfit = margin;
      }
    }
  }
  std::cout << maxProfit;
  std::cout << "Hello";
  return 0;
}
