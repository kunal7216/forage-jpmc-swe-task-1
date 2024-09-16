################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import unittest
from client3 import getDataPoint, getRatio

class TestClient(unittest.TestCase):
    def test_getDataPoint(self):
        quotes = [
            {'stock': 'AAPL', 'top_bid': {'price': 100.0}, 'top_ask': {'price': 110.0}},
            {'stock': 'GOOG', 'top_bid': {'price': 500.0}, 'top_ask': {'price': 520.0}},
            {'stock': 'MSFT', 'top_bid': {'price': 200.0}, 'top_ask': {'price': 210.0}},
        ]
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            self.assertEqual(stock, quote['stock'])
            self.assertAlmostEqual(bid_price, float(quote['top_bid']['price']))
            self.assertAlmostEqual(ask_price, float(quote['top_ask']['price']))
            self.assertAlmostEqual(price, (bid_price + ask_price) / 2)

    def test_getRatio(self):
        self.assertAlmostEqual(getRatio(10, 20), 0.5)
        self.assertAlmostEqual(getRatio(20, 10), 2)
        self.assertAlmostEqual(getRatio(10, 0), float('inf'))
        self.assertAlmostEqual(getRatio(0, 10), 0)

    def test_getDataPoint_missing_top_bid(self):
        quote = {'stock': 'AAPL', 'top_ask': {'price': 110.0}}
        with self.assertRaises(KeyError):
            getDataPoint(quote)

    def test_getDataPoint_missing_top_ask(self):
        quote = {'stock': 'AAPL', 'top_bid': {'price': 100.0}}
        with self.assertRaises(KeyError):
            getDataPoint(quote)

    def test_getRatio_negative_prices(self):
        self.assertAlmostEqual(getRatio(-10, 20), -0.5)
        self.assertAlmostEqual(getRatio(20, -10), -2)

    def test_getRatio_large_prices(self):
        self.assertAlmostEqual(getRatio(1000000, 2000000), 0.5)
        self.assertAlmostEqual(getRatio(2000000, 1000000), 2)

    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109), 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '6.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            self.assertEqual(stock, quote['stock'])
            self.assertAlmostEqual(bid_price, float(quote['top_bid']['price']))
            self.assertAlmostEqual(ask_price, float(quote['top_ask']['price']))
            self.assertAlmostEqual(price, (bid_price + ask_price) / 2)

    def test_getDataPoint_calculatePriceBidGreater ThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109), 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            self.assertEqual(stock, quote['stock'])
            self.assertAlmostEqual(bid_price, float(quote['top_bid']['price']))
            self.assertAlmostEqual(ask_price, float(quote['top_ask']['price']))
            self.assertAlmostEqual(price, (bid_price + ask_price) / 2)

if __name__ == '__main__':
    unittest.main()
