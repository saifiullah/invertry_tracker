import function1
while True:
    print("1.Add stock\n2.Stock inventry\n3.Update Stock\n4.Highlighted product")
    user_will=int(input("Please select the catagories from given above"))
    if user_will== 1:
        from function1 import add_stock
        add_stock()
    if user_will==2:
        from function1 import stock_inventry
        stock_inventry()

