#!/usr/bin/env python
# coding: utf-8

# In[2]:



from math import sqrt

# This function computes the distance between any two given transactions of a user.
# It accepts two parameters, 'transaction1' and 'transaction2', which are the transaction details of the user.
def user_transaction_distance(transaction1, transaction2):
    
    # the x,y location of 'transaction1' is stored in the variables below.
    transX1 = transaction1['x']
    transY1 = transaction1['y']
    
    # the x,y location of 'transaction2' is stored in the variables below.
    transX2 = transaction2['x']
    transY2 = transaction2['y']
    
    # the location varibles above are stored in the 'trans_list' varible to form a list, for further examination.
    trans_list = list(transX1)+list(transY1)+list(transX2)+list(transY2)
    
    # the varible below stores a boolean that determines if the location variables are numbers or not.
    is_alpha = False
    
    # the for loop is used to set the 'is_alpha' variable to True if any of the string in the 'trans_list' is not a number.
    for string in trans_list:
        if string!='.' and string.isalpha():
            is_alpha = True
    
    # if the 'is_alpha' variable remains False, the code below runs.
    # The reason for doing this is to prevent any calculation error or program crash due to wrong input of parameters.
    if not is_alpha:
        
        x1 = float(transX1)
        y1 = float(transY1)
        
        x2 = float(transX2)
        y2 = float(transY2)
        
        diff_x = x2 - x1
        diff_y = y2 - y1
        distance = sqrt(pow(diff_x, 2) + pow(diff_y, 2))
        
        # The distance is then returned as a float type after the successful calculations above.
        return distance
# print(user_transaction_distance({'x':'322','y':'429'},{'x':'372','y':'229'}))
def transaction_distance(transaction1, transaction2):
    
    transX1 = transaction1['x']
    transY1 = transaction1['y']
    
    transX2 = transaction2['x']
    transY2 = transaction2['y']
    trans_list = list(transX1)+list(transY1)+list(transX2)+list(transY2)
    is_alpha = False
        
    for string in trans_list:
        if string!='.' and string.isalpha():
            is_alpha = True
            
    if not is_alpha:
        
        x1 = float(transX1)
        y1 = float(transY1)
        
        x2 = float(transX2)
        y2 = float(transY2)
        
        diff_x = x2 - x1
        diff_y = y2 - y1
        distance = sqrt(pow(diff_x, 2) + pow(diff_y, 2))
            
        return distance

#(transaction1,transaction2) = [{'user_id': '30', 'transaction_id': '501096', 'description': 'HOTEL PLEASURE', 'amount': '760.18', 'x': '620.0', 'y': '561.0', 'fraudulent': 'true'}, {'user_id': '30', 'transaction_id': '501097', 'description': 'SCTY XXX', 'amount': '815.35', 'x': '535.0', 'y': '649.0', 'fraudulent': 'true'}]


# In[ ]:




