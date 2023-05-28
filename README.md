# fraud_detection (Overview)
In the modern world, where the majority of transactions are conducted electronically, fraud is becoming more prevalent. As a result, systems must be created to detect and stop such activities. This report outlines the creation of Python modules that forecast fraudulent activity in transaction files using statistical functions. 
Statistical functions that can be used to determine whether a transaction is fraudulent or not based on the transaction details of a user were used in this report's set of Python modules. A "Transacation.txt" file containing the transactional information of numerous users at various locations served as the dataset for this project. The attributes in the file are separated by a ':' on each line. The attributes include the user id, transaction id, the transaction description, the transaction amount, the x and y coordinates of each transaction, and a Boolean label that indicates whether the transaction is fraudulent or not. 
Transaction_file, user_id, x_location, y_location, and amount are among the parameters that the function that forecasts the fraudulent attribute accepts. Together with the three functions, these parameters are used to forecast the fraudulent attribute for a given transaction detail.  
To interact with the functions, a menu-driven user interface has been developed. This report gives a thorough explanation of the methodology used to develop the functions and the user interface, as well as the degree of success in foreseeing fraudulent transactions. 

# Problem Analysis 
Fraudulent transactions can cause insignificant losses and damage to the reputation of individuals and organizations. Traditional approaches to fraud detection, such as manual reviews and rule-based systems, are often time-consuming and error-prone. Therefore, there is a need for more efficient and accurate fraud detection methods that can process large volumes of transaction data in real-time.
The main challenge in fraud detection is distinguishing legitimate transactions from fraudulent ones, which can be difficult as fraudsters often try to conceal their activities by using sophisticated techniques. Therefore, fraud detection systems must be able to identify patters and anomalies in transaction data that indicate fraudulent behaviour. 
In this project, the aim is to develop a fraud detection system that utilizes statistical methods such as z-score and interquartile range, which are commonly used in fraud detection. These statistical methods allow the system to identify outliers and unusual patterns in transaction data, which can indicate potential fraud.

# Solution Requirements
a. dataset_module: This module has a function that pulls the Transaction.txt file's attributes and features and returns a dictionary. 

b. distance_module: module includes two functions.
•	A function that determines how far apart any two transactions of a user is, given in any order. 
•	A function that determines the distance between transactions of any two users.

c. statistics_module: This module contains 12 functions 
•	A function that returns the average number of transactions made by each user and by everyone.  
•	a function that displays the transactional mode of each user and all users. 
•	a formula that calculates the median of each user's transactions and those of all users.  
•	the function that gives the interquartile range for all users and for any user's transactions.  
•	a function that calculates any user's location centroid based on the locations of their transactions.  
•	the function that determines the transaction's standard deviation for any particular user.  
•	a mechanism that determines the legitimacy of a transaction, and includes information on such transactions.  
•	a function that, for any specific user, returns an abnormal transaction.  
•	a method for calculating the Z-score for each user's transaction as well as for all user transactions.  
•	A formula that determines the transactional frequencies at a specific location.   
•	A function that returns the nth percentiles of transactions for any user and for all users.
•	A function that returns the outlier of any location and of any user.

d.	test_module: This module implements the UI that the user will use to interact with the above functions. 

# Implementation of Solution

Data Extraction and Pre-processing 
 To make the 'Transaction.txt' file useful in the project, the transaction information was extracted and pre-processed. The necessary attributes, including user_id, transaction_id, description, amount, x_coordinate, and y_coordinate, as well as fraudulent, were extracted as dictionaries during the pre-processing step by making use of the colon separator on each line.   
Fraudulent Transaction Prediction
To predict whether a transaction is fraudulent, the following steps were taken: 
	The parameters, transaction_file, user_id, amount, x_coordinate, y_coordinate, were passed to the function for predicting the fraudulent attribute. 
	Three functions were used in the function that predicts the fraudulent attribute: transaction_amount_zscore, transaction_location_centroid, and transaction_interquartile_range. 
 
	Transaction_amount_zscore calculates the transaction amount's z-score for a specific user. A data point's z-score indicates how far away from the mean a multiple of its standard deviation is. It may be a sign of a fraudulent transaction if the transaction amount is excessively high or low in comparison to the user's typical transaction amount. The transaction is marked as possibly fraudulent if the z-score of the transaction amount exceeds a specific threshold value, which for this project is assumed to be + or - 3. 
	Transaction_location_centroid determines the centroid of every location where a given user has made a transaction. The centroid represents the average location of all user transactions. It may be a sign of a fraudulent transaction if a transaction is made from a location that is too far from the user's usual transaction locations. The transaction is marked as potentially fraudulent if the transaction location exceeds a specific threshold value. 
	Transaction_interquartile_range identifies the user and determines the interquartile range of all transaction amounts. The difference between the data's 75th and 25th percentiles is used to calculate the interquartile range, which is a measurement of the data's spread. It may be a sign of a fraudulent transaction if a transaction amount is outside the Interquartile range upper and lower bounds. The transaction is marked as possibly fraudulent if the transaction amount exceeds a predetermined threshold. The boundary used in this project is from the upper bound: (third quartile+1.5*interquartile range) and the lower bound: (first quartile-1.5*interquartile range)
Using the user_id provided in the parameter, the transaction information for a specific user, including the transaction amount and transaction coordinates, was first collected in order to predict the fraudulent attribute. The z-score of the transaction amount, the distance between the transaction location and the centroid of all the transaction locations, and the interquartile range of all the transaction amounts are then computed using the three aforementioned functions. 
We mark the transaction as fraudulent if any one of the three calculated values is higher than a predetermined threshold. The accuracy of our prediction is then assessed by comparing the predicted fraudulent attribute with the actual fraudulent attribute in the transaction file. By contrasting the predicted results with the actual results in the datasets, the accuracy of the fraudulent transaction prediction was calculated, but in this project, more precedence was given to the location outlier function, when the results of the prediction were compared to the actual fraudulent parameter for the transaction, the result of the location outlier had a greater accuracy compared to the other two functions. The accuracy was determined in this way. The average measurement accuracy was discovered to be roughly 80%, which is a commendable outcome for a straightforward prediction model not utilising machine learning algorithms. 


In sum, the combination of these three operations offers a straightforward yet efficient method of anticipating potentially fraudulent transactions without the need for more intricate machine learning models. 

# Program Execution
By developing a "test_module" where a "User" class was created, a menu-driven user interface was created to make the fraud detection system more approachable and user-friendly. Four attributes are accepted by the class: "user_id," "transaction_file," "transaction," and "get_all." The 'get_all' parameter, which has a Boolean type, specifies whether the statistics of all users or just the specific user with the specified user_id should be computed. Since the User class is only for users, and we only need the statistics of the user that has been instantiated, so the “get_all” is initialised to False. 
Other methods in the User class also return the statistics_module and distance_module functions. The Distance_Module and Statistics_Module functions can be efficiently interacted with by the User class. The following are the features that the test_module provides: 
1.	Enter Transaction Data 
2.	Predict Fraudulent Activity 
3.	View Transaction Statistics 
4.	Exit  
Enter Transaction Data:  
The user is given the choice of providing the path to the transaction file where the dictionary of transaction attributes will be obtained when they run the 'view_user_transaction_statistics' function cell in the Jupyter test_module file, or using the default file path, which is assumed to be in the same directory as the module and is named 'Transaction.txt'.   
Depending on what function(s) the user decides to access, the user will be prompted to input the following fields: 
•	User Id 
•	Transaction Amount 
•	X Coordinate and Y Coordinate 
•	Z-score Threshold
•	Transaction (a dictionary describing a transaction) 
With the exception of Transaction, all fields will generally require user input. The end result is shown as a dictionary once the user has entered all the required information.
Predict Fraudulent Activity: 
•	The user is prompted to enter the necessary parameters for the fraud detection function when attempting to access the 'is_fraudulent' function. The following fields must be filled out by the user: 
•	User Id 
•	Amount 
•	X Coordinate 
•	Y Coordinate 
•	Threshold (Optional)
The system will use its fraud detection feature to determine whether or not the transaction is fraudulent once the user has entered all the required information.  A normal distribution curve describing the user’s transaction amount gets displayed, giving an extra overview of the what the threshold for the z-score should look like.
View Transaction Statistics: 
Showing various transaction data statistics, the statistics include: 
•	the average amount spent per transaction, 
•	the median amount spent per transaction,
•	the mode amount spent per transaction, 
•	the interquartile range of the transaction, 
•	the percentiles of the transaction amount, 
•	the standard deviation of the transaction amount,
•	the z-score of the transaction amount,
•	the centroid of the transaction locations, 
•	the distance between the transaction locations. 
The user will have a thorough understanding of the transaction data thanks to these statistics, which can also be used to spot any potential patterns or outliers. 
 
Exit: 
Users are given choices during prompts that will end the programme that is currently running.  
