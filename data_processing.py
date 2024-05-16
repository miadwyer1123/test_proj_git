import pandas as pd


# create a simple dataframe
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.Dataframe(data)

# add a new column 'country'
df['country'] = ['USA', 'USA', 'USA']
print(df)
