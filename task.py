import pandas as pd


df = pd.DataFrame(pd.read_csv("../dataset/archive/IPL Player Stat.csv"))


print(df.head(10).to_string())


print(df.isnull().count())
#find top players , based on runs , wickets , strike rate and overall contribution

print("\n\n")
print("Players ranking based on Runs: ")
print("-" * 50)
print("\n\n")


output_list = ["player", "runs"]
top_runs =  df.sort_values(by="runs", ascending=False)
top_runs_names = top_runs[output_list]
print(top_runs_names.head(10).to_string())

print("\n\n")
print("Players ranking based on Wickets: ")

print("-" * 50)
print("\n\n")



output_list = ["player", "wickets"]
top_wickets =  df.sort_values(by="wickets", ascending=False)
top_wicket_taker_names = top_wickets[output_list]
print(top_wicket_taker_names.head(10).to_string())


print("\n\n")
print("Players ranking based on Strike rate: ")

print("-" * 50)
print("\n\n")
output_list = ["player", "batting_strike_rate"]
top_sr =  df.sort_values(by="batting_strike_rate", ascending=False)
top_sr_names = top_sr[output_list]
print(top_sr_names.head(10).to_string())


print("\n\n")
print("Players ranking based on Overall Score (Custom Calculation): ")

print("-" * 50)
print("\n\n")


W1, W2, W3, W4 = 0.4, 0.2, 0.2, 0.2
W5, W6, W7, W8 = 0.5, 0.2, 0.15, 0.15
W9, W10 = 0.1, 0.1
epsilon = 1e-3

df["normalized_bowling_sr"] = df["bowling_strike_rate"].replace(0, epsilon).max() / (df["bowling_strike_rate"] + epsilon)
df["normalized_bowling_econ"] = df["bowling_economy"].replace(0, epsilon).max() / (df["bowling_economy"] + epsilon)
df["normalized_bowling_avg"] = df["bowling_avg"].replace(0, epsilon).max() / (df["bowling_avg"] + epsilon)

df["Batting_Score"] = (df["runs"] * W1) + (df["batting_strike_rate"] * W2) + \
                      (df["batting_avg"] * W3) + (df["boundaries_percent"] * W4)



df["Bowling_Score"] = (df["wickets"] * W5) + \
                      (df["normalized_bowling_sr"] * W6) + \
                      (df["normalized_bowling_econ"] * W7) + \
                      (df["normalized_bowling_avg"] * W8)

df["Fielding_Score"] = (df["catches"] * W9) + (df["stumpings"] * W10)


df["Overall_Score"] = df["Batting_Score"] + df["Bowling_Score"] + df["Fielding_Score"]



output_list = ["player", "Overall_Score"]
df_sorted = df.sort_values(by="Overall_Score", ascending=False)
df_overall_score = df_sorted[output_list]

print(df_overall_score.head(10))








