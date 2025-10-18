import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel('Carsales.xlsx', index_col=0)
    df.index.rename('Sales Place', inplace=True)

    print(df)

    with pd.ExcelWriter('Carsales2.xlsx') as writer:
        for columns in df.columns:
            df[columns].to_excel(writer, sheet_name=columns)

    df2 = pd.read_excel('Carsales2.xlsx', index_col=0)
    print(df2)

    df3 = pd.read_excel('Carsales2.xlsx', index_col=0, sheet_name=['Mercedes', 'Ford', 'Tata', 'Renault'])
    print(df3)

    df4 = pd.DataFrame()
    for dict in df3.values():
        df4 = pd.concat([df4, pd.DataFrame.from_dict(dict)], axis=1)

    print(df4)