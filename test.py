import pandas as pd
data={
    "apples": [3,4,6,9],
    "oranges": [1,5,6,8]
}

index = ['Aron','Lee','Steve','tony']
purchases = pd.DataFrame(data, index=index)
print(purchases)
print(type(purchases))

# print(purchases["apples"])

print(purchases.loc["Aron"])
