#!/usr/bin/env python
# coding: utf-8

# In[46]:


from math import sqrt
from dataset_module import get_user_transactions, get_user_ids
import statistics
transaction_file = 'Transaction.txt'
#calculates the average of the amount of the user's transaction
def get_average_user_transaction(transaction_file,get_all,user_id=''):    
    
    # To maintain consistency and prevent errors, the user_id variable is casted as a string.
    user_id = str(user_id)
    
    # The condition below checks that the user_id is empty. The 'not get_all' is a boolean checking if the get_all is False.
    if user_id=='' and not get_all:
       print('Enter user_id as the third parameter') 
    
    # This fetches all the user ids and stores it in the all_user_ids variable.
    all_user_ids = get_user_ids(transaction_file)
    
    users_average_transactions = []
    
    # The variable initialized below is used to check if the user_id provided exists in the transaction file.
    total_transactions=0
    
    # The for loop below iterates through all the user's ids present in the all_user_ids list.
    for i_d in all_user_ids:
        
        # if the get_all variable is false and the i_d variable in the for loop above is not equal to the user_id provided
        # in the parameter, the 'continue' code below skips the loop for i_d.
        if not get_all and i_d!=user_id:
            continue
        
        # The code below fetches the amount in each transaction, adds them together, and devides by the total number of transactions
        average_transaction=0
        
        user_transactions = get_user_transactions(transaction_file, i_d)
        amount = 0
        count=0
        for transaction in user_transactions:
            if transaction['fraudulent']!= 'true':
                amount += float(transaction['amount'])
                count += 1
        # the total_transactions variable below is not updated if the i_d in the for loop above is not equal to user_id variable.
        total_transactions = len(user_transactions)          
        if total_transactions!=0:                
            average_transaction = amount/count
        
        users_average_transactions += [{'user_id':i_d, 
            'average_transaction':average_transaction}]                
    # this condition checks if the total_transaction variable is still zero or not.
    if total_transactions==0:
        if user_id!='':
            print('No Transaction with user_id of',f"'{user_id}'", 'exists in', transaction_file)             
    
    return users_average_transactions

# print(get_average_user_transaction(transaction_file, False, '31'))


# In[7]:


#calculates the mode of the amount of the user's transaction
def get_user_transactions_mode(transaction_file, get_all, user_id=''):
    
    # To maintain consistency and prevent errors, the user_id variable is casted as a string.
    user_id = str(user_id)
    
     # The condition below checks that the user_id is empty. The 'not get_all' is a boolean checking if the get_all is False.
    if user_id=='' and not get_all:
       print('Enter user_id as the third parameter') 
    
    # This fetches all the user ids and stores it in the all_user_ids variable.
    all_user_ids = get_user_ids(transaction_file)
    users_transaction_mode = []
    
    # The variable initialized below is used to check if the user_id provided exists in the transaction file.
    user_amounts_mode=0
    
    # The for loop below iterates through all the user's ids present in the all_user_ids list. 
    for i_d in all_user_ids:
         
        # if the get_all variable is false and the i_d variable in the for loop above is not equal to the user_id provided
        # in the parameter, the 'continue' code below skips the loop for i_d.
        if not get_all and i_d!=user_id:
            continue    
        
        # The code below fetches the amount in each transaction,counts the total number of times an amount was spent
        user_transactions = get_user_transactions(transaction_file, i_d)
        user_amounts = []        
        for transaction in user_transactions:
            if transaction['fraudulent']!= 'true':
                user_amounts += [float(transaction['amount'])]        
        user_amounts_mode_list = []
        for curr_amount in sorted(user_amounts):
            count=0
            for amount in user_amounts:
                if curr_amount==amount:
                    count += 1
            user_amounts_mode_list += [{'amount':curr_amount, 'frequency':count}]       
        # the user_amounts_mode variable below is not updated if the i_d in the for loop above is not equal to user_id variable.
        user_amounts_mode_count = 0
        user_amounts_mode = 0
        for data in user_amounts_mode_list:            
            if int(data['frequency']) >= user_amounts_mode_count:
                user_amounts_mode = data                        
                user_amounts_mode_count = data['frequency']                
        users_transaction_mode += [{'user_id':i_d, 
            'transaction_mode':user_amounts_mode['amount'],
            'frequency':user_amounts_mode['frequency']}]                
    
    # this condition checks if the user_amounts_mode variable is zero or not.
    if user_amounts_mode==0:
        if user_id!='':
            print('No Transaction with user_id of',f"'{user_id}'", 'exists in', transaction_file)             
    
    return users_transaction_mode
    
# print(get_user_transactions_mode(transaction_file, False, 22))


# In[9]:


#calculates the median of the amount of the user's transaction
def get_user_transactions_median(transaction_file, get_all, user_id=''):
    
    # To maintain consistency and prevent errors, the user_id variable is casted as a string.
    user_id = str(user_id)
    
    # The condition below checks that the user_id is empty. The 'not get_all' is a boolean checking if the get_all is False.
    if user_id=='' and not get_all:
       print('Enter user_id as the third parameter') 
    
    # This fetches all the user ids and stores it in the all_user_ids variable.
    all_user_ids = get_user_ids(transaction_file)
    users_transaction_median = []
    
    # The variable initialized below is used to check if the user_id provided exists in the transaction file.
    user_amounts_median=[]
    
    # The for loop below iterates through all the user's ids present in the all_user_ids list. 
    for i_d in all_user_ids:
        
        # if the get_all variable is false and the i_d variable in the for loop above is not equal to the user_id provided
        # in the parameter, the 'continue' code below skips the loop for i_d.
        if not get_all and i_d!=user_id:
            continue    
        # The code below fetches the amount in each transaction and sorts them in an ascending order,
        # the amount present at the center of the sorted list is determined to be the median,
        # if the lenght of the list is a odd number. If the length is found to be a even number, two amounts will be present
        # at the center, and the median is calculated by adding the two amounts and dividing the result by two.
        
        # the user_amounts_median variable code below is not updated if the i_d in the for loop above is not equal to user_id variable.
        user_transactions = get_user_transactions(transaction_file, i_d)
        user_amounts = []        
        for transaction in user_transactions:
            if transaction['fraudulent']!= 'true':
                user_amounts += [float(transaction['amount'])]        
        user_amounts_median_list = []
        for curr_amount in sorted(user_amounts):            
            user_amounts_median_list += [{'amount':curr_amount}]        
        list_length = len(user_amounts_median_list)
        
        if list_length%2==1:
            midIndex = int(list_length//2)
            user_amounts_median = [user_amounts_median_list[midIndex]]
        else:
            user_amounts_median = [user_amounts_median_list[int(list_length/2)],
                                   user_amounts_median_list[int((list_length/2)-1)]]        
        if len(user_amounts_median)<2:
            users_transaction_median += [{'user_id':i_d, 
                'transaction_median':user_amounts_median[0]['amount']}]
        else:
            users_transaction_median += [{'user_id':i_d, 
                'transaction_median':(user_amounts_median[0]['amount'] + 
                                      user_amounts_median[1]['amount'])/2}]        
    # this condition checks if the user_amounts_median variable is zero or not.
    if len(user_amounts_median)==0:
        if user_id!='':
            print('No Transaction with user_id of',f"'{user_id}'", 'exists in', transaction_file)             
    
    return users_transaction_median
    
# print(get_user_transactions_median(transaction_file, False, '24'))


# In[10]:


# computes the interquartile range of the user's transaction amounts
def get_user_transactions_interquartile_range(transaction_file, get_all, user_id=''):
    
    # To maintain consistency and prevent errors, the user_id variable is casted as a string.
    user_id = str(user_id)
    
    # The condition below checks that the user_id is empty. The 'not get_all' is a boolean checking if the get_all is False.
    if user_id=='' and not get_all:
       print('Enter user_id as the third parameter') 
    
    # This fetches all the user ids and stores it in the all_user_ids variable.
    all_user_ids = get_user_ids(transaction_file)
    
    # The variable initialized below is used to check if the user_id provided exists in the transaction file.
    users_transaction_quartile_range = []
    global user_amounts_median
    
    # The function defined below calculates the median of a list of transaction amounts. The median_list parameter takes 
    # the the list of upper_half and lower_half of the sorted user's transaction amounts respectively.
    def quartile_median (median_list):            
        global user_amounts_median
        user_amounts_median=[]
        list_length = len(median_list)
        transaction_median=[]        
        if list_length%2==1:
            midIndex = int(list_length//2)                            
            user_amounts_median = [median_list[midIndex]]
        else:
            midIndex = int(list_length//2)                
            user_amounts_median = [median_list[int(list_length/2)],
                                   median_list[int((list_length/2)-1)]]        
        if len(user_amounts_median)<2:
            transaction_median += [{'user_id':i_d, 
                'transaction_median':user_amounts_median[0]['amount']}]
        else:
            transaction_median += [{'user_id':i_d, 
                'transaction_median':(user_amounts_median[0]['amount'] + 
                                      user_amounts_median[1]['amount'])/2}]        
        return transaction_median
    
    # The for loop below iterates through all the user's ids present in the all_user_ids list. 
    for i_d in all_user_ids:
        
        # if the get_all variable is false and the i_d variable in the for loop above is not equal to the user_id provided
        # in the parameter, the 'continue' code below skips the loop for i_d.
        if not get_all and i_d!=user_id:
            continue    
        
        
        # the user_transaction_quartile_range variable in the code below is not updated if the i_d in the for loop above is not equal to user_id variable.
        
        # The code below computes the interquartile range by computing the median of the upper_half and median of the lower half
        # of the sorted user's transaction amounts, using the 'quartile_median' function defined above. The difference between the 
        # first quartile and the third quartile calculated results in the interquartile range.
        user_transactions = get_user_transactions(transaction_file, i_d)
        user_amounts = []        
        for transaction in user_transactions:
            if transaction['fraudulent']!= 'true':
                user_amounts += [float(transaction['amount'])]        
        user_amounts_median_list = []
        for curr_amount in sorted(user_amounts):            
            user_amounts_median_list += [{'amount':curr_amount}]                
                        
        list_len = len(user_amounts_median_list)        
        if list_len%2==1:
            midIndex = int(list_len//2)
            lower_half = user_amounts_median_list[0:midIndex]                
            upper_half = user_amounts_median_list[midIndex+1:]                            
        else:
            midIndex = int(list_len//2)
            lower_half = user_amounts_median_list[0:midIndex]
            upper_half = user_amounts_median_list[midIndex:]
          
        first_quartile = quartile_median(lower_half)
        third_quartile = quartile_median(upper_half)
        interquartile_range = third_quartile[0]['transaction_median'] - first_quartile[0]['transaction_median']
        
        users_transaction_quartile_range += [{'user_id':i_d, 'interquartile_range':interquartile_range}]        
        
    # this condition checks if the length of the users_transaction_quartile_range variable is zero or not.
    if len(users_transaction_quartile_range)==0:
        if user_id!='':
            print('No Transaction with user_id of',f"'{user_id}'", 'exists in', transaction_file)             
    
    return users_transaction_quartile_range
    
# print(get_user_transactions_interquartile_range(transaction_file, False, 25))


# In[11]:


# calculates the geometric center of the locations of the user's transactions
def get_location_centroid(transaction_file, get_all, user_id=''):
    
    # To maintain consistency and prevent errors, the user_id variable is casted as a string.
    user_id = str(user_id)
    
    # The condition below checks that the user_id is empty. The 'not get_all' is a boolean checking if the get_all is False.
    if user_id=='' and not get_all:
       print('Enter user_id as the third parameter') 
    
    # This fetches all the user ids and stores it in the all_user_ids variable.
    all_user_ids = get_user_ids(transaction_file)    
    
    # The variable initialized below is used to check if the user_id provided exists in the transaction file.
    user_location_centroid=[]
    
    # The for loop below iterates through all the user's ids present in the all_user_ids list. 
    for i_d in all_user_ids:
        
        # if the get_all variable is false and the i_d variable in the for loop above is not equal to the user_id provided
        # in the parameter, the 'continue' code below skips the loop for i_d.
        if not get_all and i_d!=user_id:
            continue    
        
        # to calculate the centroid of the locations, the x_coordinate and y_coordinate attributes of the user's transaction
        # are fetched from the transaction file. The x_centroid and y_centroid is calculated by suming the x_coordinates and y_coordiantes
        # and dividing the result of the sumations respectively by the total number of locations.
        user_transactions = get_user_transactions(transaction_file, i_d)
        x_sum=0
        y_sum=0
        no_of_locations=0
        for transaction in user_transactions:      
            if transaction['fraudulent']!= 'true':
                x_sum+=float(transaction['x'])
                y_sum+=float(transaction['y'])
                no_of_locations += 1
            
        x_centroid = x_sum/no_of_locations
        y_centroid = y_sum/no_of_locations        
        
        # the user_location_centroid variable below is not updated if the i_d in the for loop above is not equal to user_id variable.
        user_location_centroid += [{'user_id':i_d, 'x':x_centroid, 'y':y_centroid}]
        
    # this condition checks if the length of the user_location_centroid variable is zero or not.
    if len(user_location_centroid)==0:
        if user_id!='':
            print('No Transaction with user_id of',f"'{user_id}'", 'exists in', transaction_file)             
    
    return user_location_centroid        

# print(get_location_centroid(transaction_file,False, 21))


# In[12]:


# calculates the standard deviation(s) of the user(s)'s transaction amounts.
def get_transaction_standard_deviation(transaction_file, get_all, user_id=''):
    
    # To maintain consistency and prevent errors, the user_id variable is casted as a string.
    user_id = str(user_id)
    
    # The condition below checks that the user_id is empty. The 'not get_all' is a boolean checking if the get_all is False.
    if user_id=='' and not get_all:
       print('Enter user_id as the third parameter') 
       
    # This fetches all the user ids and stores it in the all_user_ids variable.
    all_user_ids = get_user_ids(transaction_file)    
    
    # The variable initialized below is used to check if the user_id provided exists in the transaction file.
    users_standard_deviation=[]
    
    # The for loop below iterates through all the user's ids present in the all_user_ids list. 
    for i_d in all_user_ids:
        
        # if the get_all variable is false and the i_d variable in the for loop above is not equal to the user_id provided
        # in the parameter, the 'continue' code below skips the loop for i_d.
        if not get_all and i_d!=user_id:
            continue    
        
        # the code below gets the transaction mean of the user with user_id, i_d, of the current loop. 
        transaction_mean = get_average_user_transaction(transaction_file, False, i_d)[0]['average_transaction']
        
        # The standard deviation is calculated by summing the difference between the transaction mean and each of the transaction amount,
        # the square of which is then divided by one less the number of transactions made by each user (n-1). The square root of the result
        # is taken to be the standard deviation of each user's tranaction amounts respectively.
        user_transactions = get_user_transactions(transaction_file, i_d)        
        diff_square_sum = 0   
        frequency_sum = 0            
        amount_list = []                
        for transaction in user_transactions:                                    
            if transaction['fraudulent']!= 'true':
                amount_list = sorted(amount_list + [float(transaction['amount'])])                                    
                diff = float(transaction['amount'])-transaction_mean                
                diff_square = pow(diff,2)
                diff_square_sum += diff_square
                frequency_sum += 1        
                      
        standard_deviation = sqrt(diff_square_sum/(frequency_sum-1))        
        # the users_standard_deviation variable below is not updated if the i_d in the for loop above is not equal to user_id variable.
        users_standard_deviation += [{'user_id':i_d, 'standard_deviation':standard_deviation}]
    
    # this condition checks if the length of the users_standard_deviation variable is zero or not.
    if len(users_standard_deviation)==0:
        if user_id!='':
            print('No Transaction with user_id of',f"'{user_id}'", 'exists in', transaction_file)             
    
    return users_standard_deviation 

# print(get_transaction_standard_deviation(transaction_file, False, 25))       


# In[17]:


# calculates the z-score of the user's transaction amounts
def get_user_transaction_zscore(transaction_file, get_all, user_id='', test_amount=''):
    
    # To maintain consistency and prevent errors, the user_id variable is casted as a string.
    user_id = str(user_id)
    
    # The condition below checks that the user_id is empty. The 'not get_all' is a boolean checking if the get_all is False.
    if user_id=='' and not get_all:
       print('Enter user_id as the third parameter') 
       
    # This fetches all the user ids and stores it in the all_user_ids variable.
    all_user_ids = get_user_ids(transaction_file)    
    
    # The variable initialized below is used to check if the user_id provided exists in the transaction file.
    users_zscore_list=[]
    
    # The for loop below iterates through all the user's ids present in the all_user_ids list. 
    for i_d in all_user_ids:
        
        # if the get_all variable is false and the i_d variable in the for loop above is not equal to the user_id provided
        # in the parameter, the 'continue' code below skips the loop for i_d.
        if not get_all and i_d!=user_id:
            continue    
        
        # The transaction mean and standard deviation of the user with the specified id, i_d, is fetched, using the code below.
        transaction_mean = get_average_user_transaction(transaction_file, False, i_d)[0]['average_transaction']
             
        transaction_stdev = get_transaction_standard_deviation(transaction_file, False, i_d)[0]['standard_deviation']
        
        # To calculate the z-score, we first calculate the difference between the values of the transaction mean gotten above and
        # the transaction amount of the user. The result is then divided by the standard deviation, 'transaction_stdev', above.
        # The end results of the calculation gives the z-score of the user's transaction amounts.
        user_transactions = get_user_transactions(transaction_file, i_d)                                
        zscore_list = []
        # In the case where the test_amount parameter is empty, the calculations indicated above are used to get the z-score using the 
        # transaction amount of the user in the transaction file.
        if test_amount=='':
            for transaction in user_transactions:                                              
                mean_diff = float(transaction['amount'])-transaction_mean                
                zscore = (mean_diff)/transaction_stdev        
                zscore_list += [{'amount':transaction['amount'], 'zscore':zscore, 'fraudulent': transaction['fraudulent']}]
            users_zscore_list += [{'user_id':i_d, 'zscore_list':zscore_list}]
        # Otherwise, that is, if the test_amount is provided in the parameter, the following happens.
        else:            
        # the z-score is calulated by computing the difference between the values of the transaction mean gotten above and
        # the test_amount of the user. The result is then divided by the standard deviation, 'transaction_stdev', above.
        # The end results of the calculations give the z-score of the user's transaction amounts.
            amount_list = list(str(test_amount))
            catch_error = False
            for val in amount_list:
                if not val.isdigit() and val!='.':
                    catch_error = True
            if not catch_error:
                mean_diff = float(test_amount)-transaction_mean            
                zscore = (mean_diff)/transaction_stdev                    
                users_zscore_list += [{'user_id':i_d, 'zscore':zscore, 'amount':test_amount}]
            else:
                users_zscore_list+=[{'error':True}]
    # this condition checks if the length of the users_zscore_list variable is zero or not.
    if len(users_zscore_list)==0:
        if user_id!='':
            print('No Transaction with user_id of',f"'{user_id}'", 'exists in', transaction_file)             
    
    return users_zscore_list
# print(get_user_transaction_zscore(transaction_file, False, 25, test_amount='10ew]')) 


# In[55]:


# calculates the location outliers of the user's transaction locations.
def get_outliers(transaction_file, get_all, user_id='', test_x='', test_y=''):
    
    # To maintain consistency and prevent errors, the user_id variable is casted as a string.
    user_id = str(user_id)
    
    # The condition below checks that the user_id is empty. The 'not get_all' is a boolean checking if the get_all is False.
    if user_id=='' and not get_all:
       print('Enter user_id as the third parameter') 
    
    # This fetches all the user ids and stores it in the all_user_ids variable.
    all_user_ids = get_user_ids(transaction_file)    
    
    # The variable initialized below is used to check if the user_id provided exists in the transaction file.
    user_location_outliers=[]
    
    # The for loop below iterates through all the user's ids present in the all_user_ids list. 
    for i_d in all_user_ids:
        
        # if the get_all variable is false and the i_d variable in the for loop above is not equal to the user_id provided
        # in the parameter, the 'continue' code below skips the loop for i_d.
        if not get_all and i_d!=user_id:
            continue    
        
        # To determine if a transaction's location is an outlier, the distance between each user's transaction's location and the 
        # corresponding user's transaction centroid is stored in a list. The list is then use to compute the mean of the distance,
        # distance_mean, and the standard deviation of the distance, distance_stdev. A transaction's location is determined to be
        # an oulier if it's distance from the centroid is greater than 2 + the distance mean * distance standard deviation, that is,
        # 2+distance_mean * distance_stdev.
        
        user_transactions = get_user_transactions(transaction_file, i_d)        
        user_location_centroid = get_location_centroid(transaction_file, False, i_d)                
        x_centroid = user_location_centroid[0]['x']
        y_centroid = user_location_centroid[0]['y']        
        
        centroid = sqrt(pow(x_centroid,2)+pow(y_centroid,2))
        distance_list = []
        for transaction in user_transactions:
            if transaction['fraudulent']!= 'true':
                x = float(transaction['x'])
                y = float(transaction['y'])
                r = sqrt(pow(x,2)+pow(y,2))
                distance = abs(centroid - r)
                distance_list = sorted(distance_list + [distance])
        
        distance_mean = sum(distance_list)/len(distance_list)
        mean_diff_square_sum=0
        for dist in distance_list:
            mean_diff = dist - distance_mean            
            mean_diff_square = pow(mean_diff,2)
            mean_diff_square_sum+=mean_diff_square
        
        distance_stdev = sqrt(mean_diff_square_sum/len(distance_list) - 1)       
        is_outlier = 'false'
        if test_x=='' and test_y=='':
            location_info = []
            for transaction in user_transactions:
                is_outlier = 'false'
                x = float(transaction['x'])
                y = float(transaction['y'])
                r = sqrt(pow(x,2)+pow(y,2))
                distance = abs(centroid - r)
                if distance > (distance_mean + 2 * distance_stdev):
                    is_outlier = 'true'
                location_info += [{'x':x,'y':y,'distance_from_centroid':distance, 'outlier':is_outlier, 'fraudulent':transaction['fraudulent']}] 
            user_location_outliers += [{'user_id':i_d, 'location_info':location_info}]
        else:
            loc_list = list(str(test_x))+list(str(test_y))            
            catch_error = False
            for val in loc_list:
                if not val.isdigit() and val!='.':
                    catch_error = True
            if not catch_error:
                is_outlier = 'false'
                x = float(test_x)
                y = float(test_y)
                r = sqrt(pow(x,2)+pow(y,2))
                distance = abs(centroid - r)
                if distance > (distance_mean + 2 * distance_stdev):
                    is_outlier = 'true'
                user_location_outliers += [{'user_id': i_d, 'x':x, 'y':y, 'outlier':is_outlier}]
            else:
                user_location_outliers += [{'error':True}]
    # this condition checks if the length of the user_location_outliers variable remains at zero or not.
    if len(user_location_outliers)==0:
        if user_id!='':
            print('No Transaction with user_id of',f"'{user_id}'", 'exists in', transaction_file)             
    
    return user_location_outliers
# print(get_outliers(transaction_file, False,22,test_x='232',test_y='433'))


# In[20]:


# determines whether a user's transaction amount is abnormal.
def get_user_abnormal_transactions(transaction_file, get_all, user_id='', test_amount=''):
    
    # To maintain consistency and prevent errors, the user_id variable is casted as a string.
    user_id = str(user_id)
    
    # The condition below checks that the user_id is empty. The 'not get_all' is a boolean checking if the get_all is False.
    if user_id=='' and not get_all:
       print('Enter user_id as the third parameter') 
    
    # This fetches all the user ids and stores it in the all_user_ids variable.
    all_user_ids = get_user_ids(transaction_file)
    
    # The variable initialized below is used to check if the user_id provided exists in the transaction file.
    abnormal_transaction_list = []
    
    global user_amounts_median
    
    # The function defined below calculates the median of a list of transaction amounts. The median_list parameter takes 
    # the the list of upper_half and lower_half of the sorted user's transaction amounts respectively.
    def quartile_median (median_list):            
        global user_amounts_median
        user_amounts_median=[]
        list_length = len(median_list)
        transaction_median=[]        
        if list_length%2==1:
            midIndex = int(list_length//2)                            
            user_amounts_median = [median_list[midIndex]]
        else:
            midIndex = int(list_length//2)                
            user_amounts_median = [median_list[int(list_length/2)],
                                   median_list[int((list_length/2)-1)]]        
        if len(user_amounts_median)<2:
            transaction_median += [{'user_id':i_d, 
                'transaction_median':user_amounts_median[0]['amount']}]
        else:
            transaction_median += [{'user_id':i_d, 
                'transaction_median':(user_amounts_median[0]['amount'] + 
                                      user_amounts_median[1]['amount'])/2}]        
        return transaction_median
    
    # The for loop below iterates through all the user's ids present in the all_user_ids list. 
    for i_d in all_user_ids:
        
        # if the get_all variable is false and the i_d variable in the for loop above is not equal to the user_id provided
        # in the parameter, the 'continue' code below skips the loop for i_d.
        if not get_all and i_d!=user_id:
            continue    
        
        # The code below computes the interquartile range by computing the median of the upper_half and median of the lower half
        # of the sorted user's transaction amounts, using the 'quartile_median' function defined above. The difference between the 
        # first quartile and the third quartile calculated results in the interquartile range.
        user_transactions = get_user_transactions(transaction_file, i_d)
        user_amounts = []        
        for transaction in user_transactions:
            if transaction['fraudulent']!= 'true':
                user_amounts += [float(transaction['amount'])]        
        user_amounts_median_list = []
        for curr_amount in sorted(user_amounts):            
            user_amounts_median_list += [{'amount':curr_amount}]                
                        
        list_len = len(user_amounts_median_list)        
        if list_len%2==1:
            midIndex = int(list_len//2)
            lower_half = user_amounts_median_list[0:midIndex]                
            upper_half = user_amounts_median_list[midIndex+1:]                            
        else:
            midIndex = int(list_len//2)
            lower_half = user_amounts_median_list[0:midIndex]
            upper_half = user_amounts_median_list[midIndex:]
          
        first_quartile = quartile_median(lower_half)
        third_quartile = quartile_median(upper_half)
        interquartile_range = third_quartile[0]['transaction_median'] - first_quartile[0]['transaction_median']
        
        # After computing the interquartile range, to detect if a transaction amount is abnormal, two bounds are created, 
        # the upper_bound and lower_bound. The upper_bound is calculated as 1.5 * the interquartile range + the third quartile and 
        # the lower_bound is calculated as first quartile - 1.5 * the interquartile range. A transaction amount becomes an abnormal 
        # distribution if the value does not fall within the range of the upper and lower bound.
        
        upper_bound = third_quartile[0]['transaction_median'] + 1.5 * interquartile_range
        lower_bound = first_quartile[0]['transaction_median'] - 1.5 * interquartile_range
        lst= []
        if test_amount == '':
            for transaction in user_transactions:
                is_outlier = 'false'
                amount = float(transaction['amount'])
                if amount > upper_bound or amount < lower_bound:
                    is_outlier = 'true'
                lst += [{'amount':amount,'outlier':is_outlier, 'fraudulent': transaction['fraudulent']}] 
            abnormal_transaction_list += [{'user_id':i_d, 'abnormal_transactions':lst}]        
        else:
            amount_list = list(str(test_amount))
            catch_error = False
            for val in amount_list:
                if not val.isdigit() and val!='.':
                    catch_error = True
            if not catch_error:
                is_outlier = 'false'
                amount = float(test_amount)
                if amount > upper_bound or amount < lower_bound:
                    is_outlier = 'true'            
                abnormal_transaction_list += [{'user_id':i_d, 'amount':test_amount, 'outlier':is_outlier}]        
            else:
                abnormal_transaction_list += [{'error':True}]
    # this condition checks if the length of the abnormal_transaction_list variable remains at zero or not.
    if len(abnormal_transaction_list)==0:
        if user_id!='':
            print('No Transaction with user_id of',f"'{user_id}'", 'exists in', transaction_file)             
    
    return abnormal_transaction_list
# print(get_user_abnormal_transactions(transaction_file, False, 29, '6-=9'))


# In[36]:


# predicts if a user's transaction is fraudulent by taking the trasansaction amount, x_coordinate and y_coordiate as parameters.
def is_fraudulent (transaction_file, user_id, transaction='', amount='', x='', y='', threshold=''):
    
    # If the transaction parameter remains empty, the code below assigns the amount, x, y parameters to amount_val, 
    # x_val and y_val respectively. Otherwise, the amount, x_coordiante, y_coordinate attributes of the transaction parameter
    # are assinged to the amount_val, x_val and y_val respectively.
    
    threshold_val = str(threshold)
    catch_error = False
    if threshold_val!='':
        threshold_list =list(str(threshold_val))
        for val in threshold_list:
            if not val.isdigit() and val!='.':
                catch_error = True
    else:
        threshold_val = 3
    
    amount_val = amount    
    if amount!= '':
        amount_list = list(str(amount_val))        
        for val in amount_list:
            if not val.isdigit() and val!='.':
                catch_error = True
        amount_val = amount
    else:
        amount_val = transaction['amount']    
    if not catch_error:
        user_transactions_zscore = get_user_transaction_zscore(transaction_file, False, user_id, amount_val)
        user_abnormal_transaction = get_user_abnormal_transactions(transaction_file, False, user_id, amount_val)
    
    x_val = x
    y_val = y
    
    if x!='' and y!='':
        loc_list = list(str(x))+list(str(y))        
        for val in loc_list:
            if not val.isdigit() and val!='.':
                catch_error = True
        x_val = x
        y_val = y
    else:
        x_val = transaction['x']
        y_val = transaction['y']
    
    if not catch_error:
        # To determine if a transaction is fraudulent, three functions were taken into account. They are the get_outliers function initialized below,
        # the get_user_abnormal_transactions and get_user_transaction_zscore functions initialized above. 
        user_location_outliers = get_outliers(transaction_file, False, user_id, x_val, y_val)
    
        # The is_fraudulent variable is initialized to be false.
        is_fraudulent='false'
        z_score=user_transactions_zscore[0]
        
        # To determine if an amount is a zscore outlier. We first initialize a threshold.
        # the threshold is assumed to be 3 for this project. Although this may not always be true for some users. It is
        # expected to be applicable to perfectly bell shaped normal distributions.
        
        # the is_outlier variable is initialized to be false.
        is_outlier = 'false'
        if abs(float(z_score['zscore']))>float(threshold_val):
            # the is_outlier variable for the z-score beocmes true if the absolute value of a transaction's amount is greater than
            # the threshold vlaue specified above.
            is_outlier = 'true'
        z_score['outlier']=is_outlier

        abnormal_transaction= user_abnormal_transaction[0]
        location_outlier = user_location_outliers[0]
        
        # Here, what contributes to the is_fraudulent variable value the most is the location_outlier. The other variables,
        # abnormal_transaction and z_score, only contribute to the is_fraudulent attribute when the location_outlier value is false.
        if location_outlier['outlier'] == 'false':
            if abnormal_transaction['outlier'] == 'true' and z_score['outlier'] == 'true':
                is_fraudulent='true' 
            else:
                is_fraudulent='false'
        elif location_outlier['outlier'] == 'true':
            is_fraudulent = 'true'
        
        #This function returns a dictionary of the predicted fraudulent transaction status, is_fraudulent, along with other information that back the prediction.
        return {'user_id':user_id,'amount':z_score['amount'],'x':location_outlier['x'],'y':location_outlier['y'],'z_score':z_score['zscore'],'z_score_outlier':z_score['outlier'],'abnormal_transaction':abnormal_transaction['outlier'],'location_outlier':location_outlier['outlier'],'is_fraudulent': is_fraudulent}
    else:
        return {'error':True}


# print(is_fraudulent(transaction_file, 29,amount=3000, x=800, y='8108',threshold='4.54'))


# In[35]:


# calculates the number of times (frequency) that transactions take place at a specified location.
def get_location_transaction_frequency(transaction_file, user_id, transaction='', x='', y=''):
    
    catch_error = False
    user_id = str(user_id)               
    # If the transaction parameter remains empty, the code below assigns the x, y parameters to x_val and y_val respectively. 
    # Otherwise, the x_coordiante, y_coordinate attributes of the transaction parameter
    # are assinged to the x_val and y_val respectively.
    user_transactions = get_user_transactions(transaction_file,user_id)
    x_val=x
    y_val=y
    if x!='' and y!='':
        loc_list = list(str(x))+list(str(y))        
        for val in loc_list:
            if not val.isdigit() and val!='.':
                catch_error = True
        x_val = x
        y_val = y
    else:
        x_val=transaction['x']
        y_val=transaction['y']
    
    # The number of transactions done in the specified location, x_val and y_val is then used in the code below, by comparing
    # their values to the x and y coordianates of the transactions of the user.
    if not catch_error:
        location_no=0
        for transaction in user_transactions:      
            if float(transaction['x']) == float(x_val) and float(transaction['y']) == float(y_val):
                location_no += 1                    

        return {'x':x_val, 'y':y_val, 'location_frequency':location_no}        
    else:
        return {'error':True}

# print(get_location_transaction_frequency(transaction_file, 24,x=567,y='677#]'))


# In[100]:


def get_transaction_nth_percentile(transaction_file, get_all, n=100 ,user_id=''):
    
    # To maintain consistency and prevent errors, the user_id variable is casted as a string.
    user_id = str(user_id)
    
    # The condition below checks that the user_id is empty. The 'not get_all' is a boolean checking if the get_all is False.
    if user_id=='' and not get_all:
       print('Enter user_id as the fourth parameter') 
       
    # This fetches all the user ids and stores it in the all_user_ids variable.
    all_user_ids = get_user_ids(transaction_file)    
    
    # The variable initialized below is used to check if the user_id provided exists in the transaction file.
    users_nth_percentile=[]
    
    # The for loop below iterates through all the user's ids present in the all_user_ids list. 
    for i_d in all_user_ids:
        
        # if the get_all variable is false and the i_d variable in the for loop above is not equal to the user_id provided
        # in the parameter, the 'continue' code below skips the loop for i_d.
        if not get_all and i_d!=user_id:
            continue                    
        
        user_transactions = get_user_transactions(transaction_file, i_d)                   
        frequency_sum = 0            
        amount_list = []                
        for transaction in user_transactions:                                    
            if transaction['fraudulent']!= 'true':
                amount_list = sorted(amount_list + [float(transaction['amount'])])                                                    
                frequency_sum += 1
        n_list = list(str(n))
        catch_error = False
        for val in n_list:
            if not val.isdigit() and val!='.':
                catch_error = True
                
        # To caculate the nth pecentile of the user's transactions, the rank is first calculated as shown below, 
        # rank = the rounded value of ((the nth pecentile specified in the parameter / 100) * (number of user's transactions +1))
        # if the rank is < 1, the rank is defualted to be equal to 1, if the rank > the user's transactions length, the rank is
        # defaulted to be equal to the user's transactions length. The nth percentile is then calculated by getting the amount
        # in the ascending sorted list, amount_list, that is in the position, rank-1.
        if not catch_error:
            n = round(float(n))
            rank = round((n/100)*(frequency_sum + 1))
            if rank < 1:
                rank = 1
            if rank > frequency_sum:
                rank = frequency_sum

            nth_percentile = amount_list[rank-1]              
            pos = 'th'
            if n==1:
                pos='st'
            elif n==2:
                pos = 'nd'
            elif n==3:
                pos = 'rd'
            nth_description = 'transaction_amount_'+str(n)+pos+'_percentile'                  
            users_nth_percentile += [{'user_id':i_d, f'{nth_description}':nth_percentile}]
        else:
            users_nth_percentile += [{'error':True}]
    
    # this condition checks if the length of the users_nth_percentile variable remains at zero or not.
    if len(users_nth_percentile)==0:
        if user_id!='':
            print('No Transaction with user_id of',f"'{user_id}'", 'exists in', transaction_file)             
    
    return users_nth_percentile
# print(get_transaction_nth_percentile(transaction_file,False,'12.39?', '23'))

