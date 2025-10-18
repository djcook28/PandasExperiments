import pandas as pd
import sqlite3

if __name__ == "__main__":
    df = pd.read_excel('Carsales.xlsx', index_col=0)

    dbconnect = sqlite3.connect('carsales.db')

    df.to_sql('carsales', dbconnect, if_exists='replace')

    del df

    df = pd.read_sql("select * from carsales", dbconnect)

    #print(df)
    print(df.info())
    print(df['Tata'].info())
    print(df[['Tata']].info())

    print(type(df.loc[2, 'Tata']))
    print(type(df.iloc[2, 2]))

    print(df.dtypes)

    y = df.loc[2, "Tata"]
    print(type(int(y)))

    x = df.loc[2].tolist()

    print(x)
    print(type(x))

    x = df.Tata.tolist()

    print(x)
    print(type(x))
    for i in x:
        print(type(i))