'''
availability --> yes it available 
area_pincode --> pincode is matching than the product is available

avail;ablity --> the Stock is availble or not (user input)
area_pincode --> whether the product is available uin that area (user input)

availability = yes
area_pipcode = yes

a product is available and also in the area  whe order is got placed

if both conditions are true than 
the product is available 

if one of the condition is False 
than the product is not available 

we want both of the conditions to be true

---> availability = yes
     area_picode = yes
     
     condition1 == 'yes'
     product is available in the stock? ---> yes
     condition2 == 'yes'
     product is available in the given pincode area --> yes
     
     Product is available
     
===> availability = no
    area_pincode =yes
    
    condition1 == 'yes'
    product is available in the stock? --> condition1 == 'no'  Condition will fail
    
    condition2 == 'yes'
    product is available at th given area? --> condition2 = 'yes condition is satified
    
    product is not available in the stock.
        
'''

stock_available = input("The product is available? (Yes/No):").strip().lower()
area_pincode = input("The product is available in that area?: (Yes/No)").strip().lower()

if stock_available == 'yes' and area_pincode == 'yes':
    print("The product is available")
else:
    print("The product is not available")


