import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Read the csv file
df = pd.read_csv("dataset.csv")
print(df.head())

#Find total number of runs Kohli has scored
total_runs = df["Runs"].sum()
no_of_matches = len(df["Runs"])
print(f"Total number of runs Kohli has Scored in {no_of_matches} matches: ", total_runs)

#Average of the the number of runs he has scored
avg_runs = df["Runs"].mean()
print(f"Average runs scored by Kohli in {no_of_matches} matches: ",int(avg_runs))

#No of mathches he has played in different position
positions = df["Pos"].unique()
print(positions)

df["Pos"] = df["Pos"].map({
    3.0: "Batting at 3",
    4.0: "Batting at 4",
    2.0: "Batting at 2",
    1.0: "Batting at 1",
    7.0: "BAtting at 7",
    5.0: "Batting at 5",
    6.0: "Batting at 6"
})
# print(df[["Runs","Pos","Opposition"]].head())
def show_pie_plot(df,key):
    count = df[key].value_counts()
    count_values = count.values
    # print(count_values)
    count_labels = count.index
    # print(count_labels)
    fig = plt.figure(figsize = (10,7))
    plt.pie(count_values, labels=count_labels)
    plt.show()

# pos_count = df["Pos"].value_counts()
# print(pos_count)
# print(type(pos_count))  #"""it is series class object type"""

# pos_values = pos_count.values
# print(pos_values)
# pos_labels = pos_count.index
# print(pos_labels)
# fig = plt.figure(figsize = (10,7))
# plt.pie(pos_values, labels=pos_labels)
# plt.show()

#for oppositions
# opponents = df["Opposition"].unique()
# print(opponents)

# df["Pos"] = df["Pos"].map({
#     3.0: "Batting at 3",
#     4.0: "Batting at 4",
#     2.0: "Batting at 2",
#     1.0: "Batting at 1",
#     7.0: "BAtting at 7",
#     5.0: "Batting at 5",
#     6.0: "Batting at 6"
# })
# print(df[["Runs","Pos","Opposition"]].head())

# opponent_count = df["Opposition"].value_counts()
# print(opponent_count)
# # print(type(pos_count))  #"""it is series class object type"""

# opponent_values = opponent_count.values
# print(opponent_values)
# opponent_labels = opponent_count.index
# print(opponent_labels)
# fig = plt.figure(figsize = (10,7))
# plt.pie(opponent_values, labels=opponent_labels)
# plt.show()
show_pie_plot(df,"Pos")
show_pie_plot(df,"Opposition")
show_pie_plot(df,"Ground")




#Total runs scored in different position
total_runs_at_pos = df.groupby("Pos")["Runs"].sum()
runs_at_pos_values = total_runs_at_pos.values
runs_at_pos_labels = total_runs_at_pos.index

fig = plt.figure(figsize=(10,7))
plt.pie(runs_at_pos_values, labels = runs_at_pos_labels)
plt.show()

#Total sixes eith different position
sixes_with_ops = df.groupby("Opposition")["6s"].sum()
sixes_with_ops_values = sixes_with_ops.values
sixes_with_ops_labels = sixes_with_ops.index
fig = plt.figure(figsize=(10,7))
plt.pie(sixes_with_ops_values, labels = sixes_with_ops_labels)
plt.show()

#No of Century Scored by Kohli in the first and seccond innings
centuries = df.query("Runs >= 100")
print(centuries)

innings = centuries["Inns"]
tons = centuries["Runs"]
print(innings)
print(tons)
fig = plt.figure(figsize=(10,7))
plt.bar(innings,tons,color = 'blue',width=0.2)
plt.show()

#Calculate the dismissials of Kohli
dismissals = df["Dismissal"].value_counts()
print(dismissals)

dismissals_count = dismissals.values
dismissals_labels = dismissals.index
show_pie_plot(df,"Dismissal")



#Agains which teams Kohli has scored most centuries
fig = plt.figure(figsize=(10,7))
plt.bar(centuries["Opposition"], centuries["Runs"], color = 'Red', width=0.2)
plt.show()


