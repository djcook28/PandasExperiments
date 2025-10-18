import pandas as pd
from IPython.display import display

if __name__ == '__main__':
    df = pd.read_csv('Carsales.csv', index_col=0)
    df2 = pd.read_csv('Carsales.csv', index_col=0)
    df.index.rename('Sales Place', inplace=True)
    for i in range(5000):
        df = pd.concat([df, df2], ignore_index=True)
    print(df)

    print(df.head(10))
    print(df.tail())

    print(df.iloc[2000:2011])

    # slow and combursome, converts each row into a tuple
    #for row in df.itertuples():
    #    print(row)

    # turn off pandas safety feature that tries to prevent crashes
    pd.set_option('display.max_rows', None)
    display(df)
    # turns safety feature back on
    pd.set_option('display.max_rows', 5000)