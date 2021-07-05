import csv, pandas

dataframe = pandas.read_csv("final-data.csv")
del dataframe["Luminosity"]

dataframe.drop(dataframe.columns[[0]], axis=1, inplace=True)

dataframe.to_csv("final.csv")