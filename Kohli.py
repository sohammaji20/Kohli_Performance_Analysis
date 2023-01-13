import pandas as pd
df = pd.read_csv("dataset.csv")
# print(df.head(10))
# df.info()
# print(df.shape)
# print(df.describe())

# print(df["Opposition"].describe())

# print(df["Runs"].value_counts())

# new_df=df[["Runs", "4s", "6s","Opposition"]]

# print(new_df)

# print(new_df.describe())

# print(new_df.iloc[2:5]["Runs"])

# vs_aussies = df[df["Opposition"] == "v Australia"]
# print(vs_aussies.head(10))

# print(vs_aussies["6s"].sum())

Aus_centuries = df[(df["Opposition"] == "v Australia") & (df["Runs"] >= 100)]
print(Aus_centuries)

def find_centuries(x):
    if x >= 100:
        return "OG"
    else:
        return "NOOB"

df["Centuries"] = df["Runs"].apply(find_centuries)
print(df)