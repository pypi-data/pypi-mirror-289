import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Function to get user input for house prices data
def get_user_input():
    data = []
    print("Enter the house prices data:")
    print("Format: <Number of Rooms>,<Lot Size>,<Year Built>,<Price>")
    print("Enter 'done' when you are finished.")

    while True:
        user_input = input("Enter data: ")
        if user_input.lower() == 'done':
            break
        try:
            rooms, lot_size, year_built, price = map(float, user_input.split(','))
            data.append([rooms, lot_size, year_built, price])
        except ValueError:
            print("Invalid format. Please enter the data in the correct format.")

    return pd.DataFrame(data, columns=['Rooms', 'LotSize', 'YearBuilt', 'Price'])

# Function to train and evaluate the model
def train_and_evaluate():
    # Get house prices data from user
    df = get_user_input()

    # Define the features and target variable
    X = df[['Rooms', 'LotSize', 'YearBuilt']]
    y = df['Price']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Calculate the mean squared error
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

    return model

# Function to make predictions on new data
def predict_price(model):
    print("\nEnter new house data to predict the price:")
    while True:
        user_input = input("Enter data (<Number of Rooms>,<Lot Size>,<Year Built>) or 'done' to exit: ")
        if user_input.lower() == 'done':
            break
        try:
            rooms, lot_size, year_built = map(float, user_input.split(','))
            new_data = pd.DataFrame([[rooms, lot_size, year_built]], columns=['Rooms', 'LotSize', 'YearBuilt'])
            predicted_price = model.predict(new_data)[0]
            print(f"Predicted Price: {predicted_price}")
        except ValueError:
            print("Invalid format. Please enter the data in the correct format.")

# Function to run the entire flow
def run_model():
    model = train_and_evaluate()
    predict_price(model)
