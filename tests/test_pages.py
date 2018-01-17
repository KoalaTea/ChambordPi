     def test_order_page(self):
         self.test_app.post('/login', data={'username':'koalatea',
                                            'password':'temporary2017koalatea'})
         order = self.test_app.get('/review_order/Rum and Coke')
         print(order)
         order = self.test_app.post('/order_drink', data={'drink':'Rum and Coke',
                                                  'instructions':'test'})
         print('TEST')
         for order in orders.Order.objects():
             print(order)
         order = orders.Order.objects.get(username='koalatea')
         self.assertEqual(order.name, 'Rum and Coke')
