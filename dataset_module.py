#!/usr/bin/env python
# coding: utf-8

# In[4]:


#initializing file name
transaction_file = 'Transaction.txt'
#transaction file length
transaction_length = 7

#This function retrieves the transactions data from the transaction file in form of a dictionary.
def get_all_transactions(transaction_file):    
    #initializing the array variable that collates the dictonary that contains the transaction details. 
    dataset = []        
    try:
        
        #using the open function to collect the transactions from the transaction file, and storing it in the 'file' variable as a list.
        with open(transaction_file) as file:
            # the for loop is used to access the transactions in the 'file' variable, one line at a time.
            for line in file:
                striped = line.strip('\n') #eliminates any unwanted string like '\n' that could be present due to the line separations
                user_list = striped.split(':') # splits the data in each transaction and store in a list.
                
                if len(user_list)==transaction_length: # makes sure the attributes of the transaction is not less than or greater than 7.
                    
                    # the varibles in the tupple below collate the transaction data from the list ('user_list') and store them.
                                        
                    (
                        user_id,
                        transaction_id,
                        description, 
                        amount,
                        x_coordinate,
                        y_coordinate,
                        fraudulent
                    ) =  user_list
                    
                    # the dictionary 'dicts' is used to represent the transaction in each line.
                    dicts = {
                        'user_id': user_id,
                        'transaction_id': transaction_id,
                        'description': description,
                        'amount': amount,
                        'x': x_coordinate,
                        'y': y_coordinate,
                        'fraudulent': fraudulent
                    }
                    
                   
                    # the dictionaries are then added to the 'dataset' list as the loop runs over the lines, as shown below.                    
                    dataset += [dicts]                
                
    except IOError as err:  #this except block catches any error that could occur while accessing the transactions from the transaction file given.
        
        # An empty array is returned and an error message is displayed so as to prevent program crash and provide information on why it is empty.
        print(err)                
        return []
    
    finally:
        #The dataset collated is then returned if no error is encoutered in the try block above.
        return dataset
        
# print(get_all_transactions(transaction_file))
# This fucntion returns a list of the transactions of a user using the user's id, by making use of the 'get_all_transactions' fucntion above.        


def get_user_transactions(transaction_file, user_id):
    all_transactions = get_all_transactions(transaction_file) #Stores all transaction in the all_transactions variable.
    
    user_transactions = [] #initilizing a variable that stores the transactions of the specified user.
    
    for transaction in all_transactions:
        
        if transaction['user_id'] == str(user_id): #A condition that only allows transactions whose 'user_id' attribute 
                                                #is the same as the one specified in the parameter.
            user_transactions += [transaction]            
    
    return user_transactions
# print(get_user_transactions(transaction_file, 22))
#This function returns a list of user ids present in the transaction file.


def get_user_ids(transaction_file):
    all_transactions = get_all_transactions(transaction_file)     #Stores all transaction in the all_transactions variable.
    user_ids = [] #initilizing a variable that stores all user_ids
    for transaction in all_transactions:
        if transaction['user_id'] not in user_ids: #If the attribute 'user_id' of a transaction is not equal to user_ids variable
            user_ids += [transaction['user_id']] #the 'user_id' attribute of the transaction is added to the user_ids list.
    return user_ids

#print(get_user_transactions(transaction_file, "22"))

