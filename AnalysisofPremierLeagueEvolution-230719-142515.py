#!/usr/bin/env python
# coding: utf-8

# <center><img src="https://gitlab.com/accredian/insaid-data/-/raw/main/Logo-Accredian/Case-Study-Cropped.png" width= 30% /></center> <br> <center><b>Prepared By - Subhasish Sinha</b></center>

# ---
# # **Table of Contents**
# ---
# 
# 1. [**Introduction**](#Section1)<br>
# 2. [**Problem Statement**](#Section2)<br>
# 3. [**Installing & Importing Libraries**](#Section3)<br>
#   3.1 [**Installing Libraries**](#Section31)<br>
#   3.2 [**Upgrading Libraries**](#Section32)<br>
#   3.3 [**Importing Libraries**](#Section33)<br>
# 4. [**Data Acquisition & Description**](#Section4)<br>
# 5. [**Data Pre-Profiling**](#Section5)<br>
# 6. [**Data Pre-Processing**](#Section6)<br>
# 7. [**Data Post-Profiling**](#Section7)<br>
# 8. [**Exploratory Data Analysis**](#Section8)<br>
# 9. [**Summarization**](#Section9)</br>
#   9.1 [**Conclusion**](#Section91)</br>
#   9.2 [**Actionable Insights**](#Section91)</br>
# 
# ---

# ---
# <a name = Section1></a>
# # **1. Introduction**
# ---
# 
# The Premier League is the most-watched sports league in the world, with an estimated cumulative global audience of 3.2 billion people in the 2019/20 season1. The league consists of 20 clubs that compete for the title of the champion of English football, as well as for qualification to European and international tournaments. The Premier League is also a lucrative business, generating revenues of 4.8 billion pounds in the 2019/20 season, despite the impact of the COVID-19 pandemic.

# ---
# <a name = Section2></a>
# # **2. Problem Statement**
# ---   
#   
# <p align="center"><img src="https://upload.wikimedia.org/wikipedia/en/thumb/f/f2/Premier_League_Logo.svg/1200px-Premier_League_Logo.svg.png"></p>
# 
# 
# 
# - **Scenario:**
#   - English Premier League is the top level of the English football league system.
# 
#   - It is contested by 20 clubs, it operates on a system of promotion and relegation with the English Football League.
# 
#   - They have accumulated the data of all the matches that has happened betweeen 1993-2018 inclusively.
# 
#   - The company is trying to find the pattern of evolution of different teams over the years.
# 
#   - But their traditional systems are not up to the mark to find out deeper patterns.
# 
#   - To tackle this problem they hired a genius team of data scientists. Considering me as one of them...

# ---
# <a id = Section3></a>
# # **3. Installing & Importing Libraries**
# ---
# 
# - This section is emphasised on installing and importing the necessary libraries that will be required.

# ### **Installing Libraries**

# In[ ]:


get_ipython().system('pip install -q datascience                                         # Package that is required by pandas profiling')
get_ipython().system('pip install -q pandas-profiling                                    # Library to generate basic statistics about data')
# To install more libraries insert your code here..


# ### **Upgrading Libraries**
# 
# - **After upgrading** the libraries, you need to **restart the runtime** to make the libraries in sync.
# 
# - Make sure not to execute the cell under Installing Libraries and Upgrading Libraries again after restarting the runtime.

# In[ ]:


get_ipython().system('pip install -q --upgrade pandas-profiling                          # Upgrading pandas profiling to the latest version')


# ### **Importing Libraries**
# 
# - You can headstart with the basic libraries as imported inside the cell below.
# 
# - If you want to import some additional libraries, feel free to do so.
# 

# In[2]:


#-------------------------------------------------------------------------------------------------------------------------------
import pandas as pd                                                 # Importing package pandas (For Panel Data Analysis)
from ydata_profiling import ProfileReport                          # Import Pandas Profiling (To generate Univariate Analysis)
#-------------------------------------------------------------------------------------------------------------------------------
import numpy as np                                                  # Importing package numpys (For Numerical Python)
#-------------------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt                                     # Importing pyplot interface to use matplotlib
import seaborn as sns                                               # Importing seaborn library for interactive visualization
get_ipython().run_line_magic('matplotlib', 'inline')
#-------------------------------------------------------------------------------------------------------------------------------
import scipy as sp                                                  # Importing library for scientific calculations
#-------------------------------------------------------------------------------------------------------------------------------


# ---
# <a name = Section4></a>
# # **4. Data Acquisition & Description**
# ---
# 
# |Id|Feature|Description|
# |:--|:--|:--|
# |01|Div| The division the match was played in.| 
# |02|Date| The date the match was played.| 
# |03|HomeTeam| The name of the home team.| 
# |04|AwayTeam| The name of the away team.|
# |05|FTHG| The total number of goals scored by the home team during the match at full time.|
# |06| FTAG| The total number of goals scored by the away team during the match at full time.|
# |07|FTR| The full time result ('H' for home team win, 'A' for away team win, or 'D' for draw).|
# |08|HTHG| The total number of goals scored by the home team at half time.|
# |09|HTAG| The total number of goals scored by the away team at half time.|
# |10|HTR| The half time result ('H' for home team advantage, 'A' for away team advantage, or 'D' for draw).|
# |11|Season| The season in which the match was played.|
# 

# In[3]:


data = pd.read_csv(filepath_or_buffer = 'https://raw.githubusercontent.com/insaid2018/Term-1/master/Data/Projects/English_Premier_League.csv')
print('Data Shape:', data.shape)
data.head()


# In[19]:


data['Date']= pd.to_datetime(data['Date'], dayfirst=True)


# ### **Data Description**
# 
# - To get some quick description out of the data you can use describe method defined in pandas library.

# In[20]:


data.describe()


# ***KEY OBSERVATIONS***
# 
# 1. The average number of goals scored by the home team during the match at full time (FTHG) is higher than the average number of goals scored by the away team during the match at full time (FTAG). This suggests that the home team has an advantage over the away team in general.
# 
# 2. The standard deviation of FTHG and FTAG are both around 1.12, which means that the variation of goals scored by both teams is similar. This implies that the matches are relatively competitive and unpredictable.
# 
# 3. The minimum and maximum values of FTHG and FTAG are 0 and 9, and 0 and 8, respectively. This indicates that there are some matches with no goals scored by either team, and some matches with very high scores by one or both teams. These could be outliers or anomalies in the data.
# 
# 4. The median values of FTHG and FTAG are both 1, which means that half of the matches have one goal scored by each team. This shows that the matches are often close and balanced.
# 
# 5. The average number of goals scored by the home team at half time (HTHG) is lower than the average number of goals scored by the home team at full time (FTHG). This suggests that the home team tends to score more goals in the second half of the match than in the first half.
# 
# 6. The average number of goals scored by the away team at half time (HTAG) is lower than the average number of goals scored by the away team at full time (FTAG). This suggests that the away team also tends to score more goals in the second half of the match than in the first half.
# 
# 7. The median values of HTHG and HTAG are both 0, which means that half of the matches have no goals scored by either team at half time. This shows that the matches are often goalless or tied at half time.

# ### **Data Information**

# In[21]:


data.info()


# ---
# <a name = Section5></a>
# # **5. Data Pre-Profiling**
# ---

# In[22]:


# Profile Report of Premier League dataset

profile = ProfileReport(df=data)
profile.to_file(output_file='PremierL_Pre_Pandas_Report.html')
print('Accomplished!')

profile.to_notebook_iframe()


# ---
# <a name = Section6></a>
# # **6. Data Pre-Processing**
# ---

# In[25]:


# Check for missing values
missing_data = data.isnull().sum()

# Since 'HTHG', 'HTAG', and 'HTR' are missing in a significant number of rows,
# we will check how many rows are affected and consider options for handling them.
missing_data_counts = missing_data[missing_data > 0]

missing_data_counts


# **Note : Given the focus of our analysis is on understanding the evolution of teams over the years, the full-time results and goals might be more relevant than half-time scores.So we leave them as it is, depending on whether we'll need them later.**

# In[37]:


# Aggregating data by team and season

# Creating a function to compute wins, draws, and losses for each team per season
def compute_team_stats(df, team_name):
    # Home and away games
    home_games = df[df['HomeTeam'] == team_name]
    away_games = df[df['AwayTeam'] == team_name]

    # Wins, draws, losses
    home_wins = home_games[home_games['FTR'] == 'H'].shape[0]
    away_wins = away_games[away_games['FTR'] == 'A'].shape[0]
    draws = home_games[home_games['FTR'] == 'D'].shape[0] + away_games[away_games['FTR'] == 'D'].shape[0]
    losses = home_games.shape[0] - home_wins - draws/2 + away_games.shape[0] - away_wins - draws/2

    # Goals scored and conceded
    goals_scored = home_games['FTHG'].sum() + away_games['FTAG'].sum()
    goals_conceded = home_games['FTAG'].sum() + away_games['FTHG'].sum()

    return {
        'Wins': home_wins + away_wins,
        'Draws': draws,
        'Losses': losses,
        'Goals Scored': goals_scored,
        'Goals Conceded': goals_conceded
    }

# Getting unique teams and seasons
teams = data['HomeTeam'].unique()
seasons = data['Season'].unique()

# Creating a DataFrame to hold the aggregated data
team_stats = pd.DataFrame(columns=['Season', 'Team', 'Wins', 'Draws', 'Losses', 'Goals Scored', 'Goals Conceded'])

# Populating the DataFrame
for season in seasons:
    season_data = data[data['Season'] == season]
    for team in teams:
        stats = compute_team_stats(season_data, team)
        new_stats = pd.DataFrame({
            'Season': [season],
            'Team': [team],
            'Wins': [stats['Wins']],
            'Draws': [stats['Draws']],
            'Losses': [stats['Losses']],
            'Goals Scored': [stats['Goals Scored']],
            'Goals Conceded': [stats['Goals Conceded']],
            })
        team_stats = pd.concat([team_stats, new_stats], ignore_index=True)

# Displaying the first few rows of the aggregated data
team_stats.head(10)


# ---
# <a name = Section7></a>
# # **7. Data Post-Profiling**
# ---

# In[39]:


# Profile Report of Premier League dataset

profile = ProfileReport(df=team_stats)
profile.to_file(output_file='PremierL_Post_Pandas_Report.html')
print('Accomplished!')

profile.to_notebook_iframe()


# ---
# <a name = Section8></a>
# # **8. Exploratory Data Analysis**
# ---

# In[40]:


## Trend Analysis: Identify if certain teams have shown consistent improvement, decline, or fluctuation in their performance.

import matplotlib.pyplot as plt
import seaborn as sns

# Setting up the visual style
sns.set_style("whitegrid")

# For trend analysis, let's select a few prominent teams to focus on.
selected_teams = ['Arsenal', 'Chelsea', 'Liverpool', 'Manchester United', 'Manchester City', 'Tottenham']

# Filtering the dataset for these teams
filtered_team_stats = team_stats[team_stats['Team'].isin(selected_teams)]

# Pivot the data for better visualization
pivot_wins = filtered_team_stats.pivot(index='Season', columns='Team', values='Wins').fillna(0)
pivot_goals_scored = filtered_team_stats.pivot(index='Season', columns='Team', values='Goals Scored').fillna(0)

# Plotting the trends for Wins and Goals Scored
plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)
sns.lineplot(data=pivot_wins)
plt.title('Number of Wins Over Seasons')
plt.xlabel('Season')
plt.ylabel('Wins')
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
sns.lineplot(data=pivot_goals_scored)
plt.title('Goals Scored Over Seasons')
plt.xlabel('Season')
plt.ylabel('Goals Scored')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# Number of Wins Over Seasons: This chart illustrates the fluctuating fortunes of the teams in terms of wins per season. It provides a clear view of periods of dominance, consistency, or decline for each team.
# 
# Goals Scored Over Seasons: This chart reflects the offensive capabilities of the teams across different seasons. It can be indicative of changes in playing style, management, or player roster.
# 
# These visualizations offer a snapshot of how these teams have evolved in terms of performance and playing style over the years. Further analysis could delve into specific periods of change, like managerial shifts or key player transfers, to understand the underlying factors driving these trends.

# In[41]:


## Comparative Analysis: Compare the performance of teams against each other and against the league average.
# Ensuring that all relevant columns are in numeric format
team_stats['Wins'] = pd.to_numeric(team_stats['Wins'], errors='coerce')
team_stats['Losses'] = pd.to_numeric(team_stats['Losses'], errors='coerce')
team_stats['Goals Scored'] = pd.to_numeric(team_stats['Goals Scored'], errors='coerce')
team_stats['Goals Conceded'] = pd.to_numeric(team_stats['Goals Conceded'], errors='coerce')

# Recalculate the win-loss ratio with the numeric data
team_stats['Win-Loss Ratio'] = team_stats['Wins'] / (team_stats['Losses'] + 1)  # Adding 1 to avoid division by zero

# Re-filter the data for selected teams
filtered_team_stats_comparative = team_stats[team_stats['Team'].isin(selected_teams)]

# Recreate the pivot tables
pivot_win_loss_ratio = filtered_team_stats_comparative.pivot(index='Season', columns='Team', values='Win-Loss Ratio')
pivot_goals_scored = filtered_team_stats_comparative.pivot(index='Season', columns='Team', values='Goals Scored')
pivot_goals_conceded = filtered_team_stats_comparative.pivot(index='Season', columns='Team', values='Goals Conceded')

# Attempting the visualizations again
plt.figure(figsize=(18, 12))

# Plot for Win-Loss Ratio
plt.subplot(2, 1, 1)
sns.heatmap(pivot_win_loss_ratio, annot=True, cmap="coolwarm", center=0, fmt=".2f")
plt.title('Win-Loss Ratio per Season', fontsize=16)
plt.xlabel('Team', fontsize=14)
plt.ylabel('Season', fontsize=14)

# Plot for Goals Scored vs. Goals Conceded
plt.subplot(2, 1, 2)
sns.heatmap(pivot_goals_scored - pivot_goals_conceded, annot=True, cmap="coolwarm", center=0, fmt=".0f")
plt.title('Goals Scored vs. Goals Conceded per Season', fontsize=16)
plt.xlabel('Team', fontsize=14)
plt.ylabel('Season', fontsize=14)

plt.tight_layout()
plt.show()


# Win-Loss Ratio per Season: This heatmap shows the win-loss ratio for each team across different seasons. Higher values indicate a greater number of wins compared to losses. This visualization helps in understanding which seasons were particularly successful or challenging for each team.
# 
# Goals Scored vs. Goals Conceded per Season: This heatmap compares the goals scored and goals conceded for each team per season. Positive values (warmer colors) indicate seasons where the team scored more goals than they conceded, suggesting stronger offensive performance. Conversely, negative values (cooler colors) suggest a stronger defensive focus or challenges in scoring.
# 
# These heatmaps provide a clear and concise way to compare the performance of Arsenal, Chelsea, Liverpool, and Tottenham over the years, highlighting their strengths and weaknesses in different seasons.

# ---
# <a name = Section9></a>
# # **9. Summarization**
# ---

# <a name = Section91></a>
# ### **9.1 Conclusion**
# 
# - --

# **Overall Performance Trends:**
# 
# Teams like Arsenal and Chelsea have shown consistent high performance in many seasons, as indicated by their win-loss ratios and goals scored.
# Liverpool, while having fluctuating win-loss ratios, often maintained a positive goal difference, indicating strong offensive capabilities.
# Tottenham, compared to the others, had more variability in their performance across seasons.
# 
# **Offensive and Defensive Capabilities:**
# 
# Chelsea and Arsenal often had higher goals scored compared to goals conceded, suggesting effective offensive strategies and robust defense.
# Liverpool consistently scored high numbers of goals, underlining their offensive strength, even in seasons with lower win-loss ratios.
# Tottenham's goal difference varied significantly, indicating fluctuations in their offensive and defensive balance.
# 
# **Seasonal Consistency and Evolution:**
# 
# Arsenal and Chelsea demonstrated remarkable consistency in maintaining a positive win-loss ratio, suggesting steady team management and player performance.
# Liverpool's performance, particularly in terms of wins and goals scored, improved notably in later seasons, hinting at successful strategic changes.
# Tottenham's evolution is marked by a gradual improvement, with more recent seasons showing better performance compared to the early years of the dataset.
# 
# **Comparative Performance:**
# 
# When compared head-to-head, these teams showed different strengths; for instance, Arsenal and Chelsea generally outperformed Tottenham in both wins and goal differences.
# Liverpool, while having competitive matches with Arsenal and Chelsea, often had an edge in goal scoring.

# <a name = Section92></a>
# ### **9.2 Actionable Insights**
# ---

# **The analysis highlights the importance of consistent team management and player development in achieving sustained success in the league.
# Offensive capabilities, while crucial, need to be balanced with strong defensive strategies to ensure overall team success.
# Teams’ performance can be significantly influenced by strategic changes, management decisions, and key player acquisitions or losses.**
