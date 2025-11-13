import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def preprocess(df):
    df = df.dropna()
    
    df = df[['MONTH', 'DAY_OF_MONTH', 'DAY_OF_WEEK', 'OP_UNIQUE_CARRIER',
             'ORIGIN', 'DEST', 'DEP_TIME', 'DEP_DELAY', 'ARR_DELAY']]
    
    df = pd.get_dummies(df, columns=['OP_UNIQUE_CARRIER', 'ORIGIN', 'DEST'])
    
    df['delay'] = (df['ARR_DELAY'] > 15).astype(int)

    X = df.drop('delay', axis=1)
    y = df['delay']

    return train_test_split(X, y, test_size=0.2, random_state=42)