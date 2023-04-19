import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    
    for quote in quotes:
      
      bid_price = float(quote['top_bid']['price'])
      ask_price = float(quote['top_ask']['price'])
      price, stock = (bid_price + ask_price) / 2,  quote['stock']

      self.assertEqual(getDataPoint(quote), (stock, bid_price, ask_price, price))
      
      
      
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    
    for quote in quotes:
      
      bid_price = float(quote['top_bid']['price'])
      ask_price = float(quote['top_ask']['price'])
      price, stock = (bid_price + ask_price) / 2,  quote['stock']
      
      result = getDataPoint(quote)
      expected_result = (stock, bid_price, ask_price, price)

      self.assertEqual((result[1]>result[2]), expected_result[1]>expected_result[2])
    
    
    for i in range(len(quotes)):
      res = getDataPoint(quotes[i])
      exp = expected[i]
      assert ( res[1] > res[2] ) == (exp[1] > exp[2] )




  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
