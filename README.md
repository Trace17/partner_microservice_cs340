# Communication Contract Partner Microservice

This microservice calculates the monthly amount a user will have to save to reach a target amount within a time frame (in years) specifed by the user using an expected annual interest rate as well as a current principal amount. 

## REQUEST
This microservice program recieves a request by monitoring a text file 'user_input.txt', when this text file is filled with 4 numbers seperated by commas the program begins automatically. Necessary input is:

1. An annual interest rate (adjusted to a decimal)
2. A target savings goal
3. A current principal amount
4. A time frame (specified in years)

## RECEIVE 
This microservice program outputs the necissary information for the user who requested it to a text file named 'monthly_savings_amount.txt'. The user can read this file to recieve the monthly amount a user would need to save based on their input to reach their savings goal. 

## UML Sequence Diagram
<img width="724" alt="Screen Shot 2022-10-31 at 1 18 36 PM" src="https://user-images.githubusercontent.com/91487097/199102519-aae060fb-90fb-4cc8-932f-32a9a1c5485f.png">
