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
        data1=json.load(file)
        input_user=input("Enter the name of product for which you wants to search :")
        for dat in data1:
            if dat["Name"] ==input_user:
                print("Qty :",dat["Quantity"])
                print("price :",dat["Total_price"])

def Update_stock():
    with open("json.txt","r")as file:
        read2=json.load(file)
        user_input2=input("Write the name of thing which you wants to update :")
        user_input3=input("Enter the new quantity of product :")
        user_input4=int(input("Enter the new price of product :"))
        T_price=int(user_input3)*user_input4
        for read in read2:
            if read["Name"]==user_input2:
                read["Quantity"]=user_input3
                read["Price"]=user_input4
                read["Total_price"]=T_price
    with open ("json.txt","w")as file:
        json.dump(read2,file,indent=1)
