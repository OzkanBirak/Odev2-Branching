import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    
    return pd.read_csv(filepath)

def basic_analysis(df):
    
    print("Veri setinin ilk 5 satırı:")
    print(df.head())
    print("\nVeri setinin sütun bilgileri:")
    print(df.info())
    print("\nTemel istatistikler:")
    print(df.describe())

def visualize_data(df, column1, column2):
    
    plt.figure(figsize=(8,5))
    sns.scatterplot(x=df[column1], y=df[column2])
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.title(f'{column1} vs {column2}')
    plt.show()

if __name__ == "__main__":
    
    filepath = "data/sample_data.csv"
    df = load_data(filepath)
    basic_analysis(df)
    visualize_data(df, df.columns[0], df.columns[1])
