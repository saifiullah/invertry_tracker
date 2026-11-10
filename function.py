import json
class shop:
    def __init__(self,n,c,w,p):
        self.Name=n
        self.Catagory=c
        self.Quantity=w
        self.Price=p
        self.Total_price=int(w)*p
def add_stock():
    
    try:
        with open("json.txt","r")as file:
            file_open=json.load(file)
            if not isinstance(file_open,list):
                file_open=[file_open]
    except:
        file_open=[]
    count=int(input("How much product do you have"))
    for i in range(count):
        first=input(f"Write the name of product No {i+1} :")
        second=input("Write the catagorie of product :")
        third=input("Write the quantity of the product :")
        fourth=int(input("Write the price of unit :"))
        a=shop(first,second,third,fourth)
        shop_data=a.__dict__
        file_open.append(shop_data)
    with open ("json.txt","w")as file:
        json.dump(file_open,file,indent=1)
def stock_inventry():
    with open ("json.txt","r")as file:
        data=json.load(file)
        input_user=input("Enter the name of product for which you wants to search :")
        for dat in data:
            if dat["Name"] ==input_user:
                print("Qty :",dat["Quantity"])
                print("price :",dat["Total_price"])

