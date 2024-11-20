
# python 3.13 version 11/20/24 

import pickle
import pandas as pd
from datetime import datetime

# Assuming `session_data` is a dictionary with user-specific data during the session
# and `training_data` is a DataFrame or a list of data that has been used for training.
# You can adapt this structure based on how your chatbot is designed.

def save_data(session_data, training_data, session_filename="session_data.pkl", training_filename="training_data.csv"):
    """
    Saves session data to a pickle file and training data to a CSV file.
    
    Args:
    - session_data (dict): Data for the current user session
    - training_data (pd.DataFrame or list): Training data to be saved
    - session_filename (str): Path to the pickle file for session data
    - training_filename (str): Path to the CSV file for training data
    """
    
    # Save session data to a pickle file
    with open(session_filename, 'wb') as session_file:
        pickle.dump(session_data, session_file)
        print(f"Session data saved to {session_filename}")

    # Save training data to a CSV file
    if isinstance(training_data, pd.DataFrame):
        training_data.to_csv(training_filename, index=False)
        print(f"Training data saved to {training_filename}")
    else:
        # If it's not a DataFrame, convert it to one before saving to CSV
        df = pd.DataFrame(training_data)
        df.to_csv(training_filename, index=False)
        print(f"Training data saved to {training_filename}")


# Example usage: 
session_data = {
    'user_id': 12345,
    'messages_exchanged': 50,
    'last_interaction': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'user_preferences': {'theme': 'dark', 'language': 'English'}
}

# Example: Your training data could be a DataFrame or any other format you store it in
training_data = pd.DataFrame({
    'user_id': [12345, 67890],
    'interaction_count': [50, 40],
    'last_interaction': ['2024-11-05 14:35:00', '2024-11-05 15:00:00']
})





# Call the function when the user signs off
save_data(session_data, training_data)

with open('session_data.pkl', 'rb') as handle:
     unserialized_data = pickle.load(handle)
     print('unserialized data: ', unserialized_data)

pd.to_pickle(training_data,'saved_pkl.pkl' )