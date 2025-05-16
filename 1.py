#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load datasets
matches_df = pd.read_csv('matches.csv')
deliveries_df = pd.read_csv('deliveries.csv')

# Display first few rows
print("Matches Data:")
print(matches_df.head())
print("\nDeliveries Data:")
print(deliveries_df.head())

# MODULE 1: Match & Team Performance Analysis
def team_performance_analysis():
    team_wins = matches_df['winner'].value_counts()
    plt.figure(figsize=(12,6))
    sns.barplot(x=team_wins.index, y=team_wins.values, palette='viridis')
    plt.xticks(rotation=90)
    plt.xlabel("Teams")
    plt.ylabel("Number of Wins")
    plt.title("Overall Team Performance in IPL")
    plt.show()

team_performance_analysis()

# MODULE 2: Player Statistics & Rankings
def player_statistics():
    top_scorers = deliveries_df.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12,6))
    sns.barplot(x=top_scorers.index, y=top_scorers.values, palette='coolwarm')
    plt.xlabel("Players")
    plt.ylabel("Total Runs")
    plt.title("Top 10 Highest Run Scorers in IPL")
    plt.xticks(rotation=45)
    plt.show()

player_statistics()

# MODULE 3: Venue & Toss Study
def venue_toss_study():
    toss_wins = matches_df.groupby('venue')['toss_winner'].count().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12,6))
    sns.barplot(x=toss_wins.index, y=toss_wins.values, palette='magma')
    plt.xticks(rotation=90)
    plt.xlabel("Venues")
    plt.ylabel("Number of Toss Wins")
    plt.title("Top 10 Venues with Most Toss Wins")
    plt.show()

venue_toss_study()

# MODULE 4: Head-to-Head Comparisons
def head_to_head(team1, team2):
    head_to_head_df = matches_df[(matches_df['team1'].isin([team1, team2])) & (matches_df['team2'].isin([team1, team2]))]
    head_to_head_wins = head_to_head_df['winner'].value_counts()
    plt.figure(figsize=(8,4))
    sns.barplot(x=head_to_head_wins.index, y=head_to_head_wins.values, palette='Set2')
    plt.xlabel("Teams")
    plt.ylabel("Number of Wins")
    plt.title(f"{team1} vs {team2} Head-to-Head Wins")
    plt.show()

head_to_head("Mumbai Indians", "Chennai Super Kings")

# MODULE 5: Win Prediction & Trend Analysis
def win_trend_analysis():
    yearly_wins = matches_df.groupby('season')['winner'].value_counts().unstack().fillna(0)
    yearly_wins.T.plot(kind='bar', stacked=True, figsize=(15,7), colormap='Paired')
    plt.xlabel("Seasons")
    plt.ylabel("Wins")
    plt.title("Win Trends Across IPL Seasons")
    plt.legend(title='Teams', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

win_trend_analysis()

# MODULE 6: Interactive Visualizations & Dashboards
def interactive_dashboard():
    fig = px.bar(matches_df, x='season', y='id', color='winner', title='IPL Winners Over the Years', labels={'id':'Matches Played'})
    fig.show()

interactive_dashboard()


# In[3]:


# Load datasets
matches_df = pd.read_csv('matches.csv')
deliveries_df = pd.read_csv('deliveries.csv')


# In[4]:


# Display first few rows
print("Matches Data:")
print(matches_df.head())
print("\nDeliveries Data:")
print(deliveries_df.head())


# In[6]:


# MODULE 1: Match & Team Performance Analysis
def team_performance_analysis():
    team_wins = matches_df['winner'].value_counts()
    plt.figure(figsize=(12,6))
    sns.barplot(x=team_wins.index, y=team_wins.values, palette='viridis')
    plt.xticks(rotation=90)
    plt.xlabel("Teams")
    plt.ylabel("Number of Wins")
    plt.title("Overall Team Performance in IPL")
    plt.show()

team_performance_analysis()


# In[7]:


# MODULE 2: Player Statistics & Rankings
def player_statistics():
    top_scorers = deliveries_df.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12,6))
    sns.barplot(x=top_scorers.index, y=top_scorers.values, palette='coolwarm')
    plt.xlabel("Players")
    plt.ylabel("Total Runs")
    plt.title("Top 10 Highest Run Scorers in IPL")
    plt.xticks(rotation=45)
    plt.show()

player_statistics()


# In[8]:


# MODULE 3: Venue & Toss Study
def venue_toss_study():
    toss_wins = matches_df.groupby('venue')['toss_winner'].count().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12,6))
    sns.barplot(x=toss_wins.index, y=toss_wins.values, palette='magma')
    plt.xticks(rotation=90)
    plt.xlabel("Venues")
    plt.ylabel("Number of Toss Wins")
    plt.title("Top 10 Venues with Most Toss Wins")
    plt.show()

venue_toss_study()


# In[9]:


# MODULE 4: Head-to-Head Comparisons
def head_to_head(team1, team2):
    head_to_head_df = matches_df[(matches_df['team1'].isin([team1, team2])) & (matches_df['team2'].isin([team1, team2]))]
    head_to_head_wins = head_to_head_df['winner'].value_counts()
    plt.figure(figsize=(8,4))
    sns.barplot(x=head_to_head_wins.index, y=head_to_head_wins.values, palette='Set2')
    plt.xlabel("Teams")
    plt.ylabel("Number of Wins")
    plt.title(f"{team1} vs {team2} Head-to-Head Wins")
    plt.show()

head_to_head("Mumbai Indians", "Chennai Super Kings")


# In[10]:


# MODULE 5: Win Prediction & Trend Analysis
def win_trend_analysis():
    yearly_wins = matches_df.groupby('season')['winner'].value_counts().unstack().fillna(0)
    yearly_wins.T.plot(kind='bar', stacked=True, figsize=(15,7), colormap='Paired')
    plt.xlabel("Seasons")
    plt.ylabel("Wins")
    plt.title("Win Trends Across IPL Seasons")
    plt.legend(title='Teams', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

win_trend_analysis()


# In[11]:


# MODULE 6: Interactive Visualizations & Dashboards
def interactive_dashboard():
    fig = px.bar(matches_df, x='season', y='id', color='winner', title='IPL Winners Over the Years', labels={'id':'Matches Played'})
    fig.show()

interactive_dashboard()


# In[ ]:




