"""Motivational Heatmap - Samantha Song - 2025.03.06"""
# Create Heatmaps from pandas dataframe

import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# # Create new dataframe from CSV file in wrong format
# data = pd.read_csv('2025 Resolutions - Sheet4.csv')
# data = data.set_index('Unnamed: 0').T

# to_df = np.array([['Date', 'Which Heatmap', 'Min Spent', 'Other Num', 'Notes']])

# heatmaps = data.columns.values
# for _, which_hm in enumerate(heatmaps):
#     dates = data[data[which_hm]].index.values
#     for _, date in enumerate(dates):
#         to_df = np.append(to_df, np.array([[date, which_hm, 0, 0, '']]), axis=0)

# new_df = pd.DataFrame(to_df)
# new_df.columns = new_df.iloc[0]
# new_df.drop(new_df.index[0], inplace=True)

# new_df.to_csv('resolutions_db.csv', index=False)

# Get properly formated database
data = pd.read_csv('resolutions_db.csv')
starting_date = datetime.datetime.strptime("1/1/2025", "%m/%d/%Y")
num_days = 70
date_generated = pd.date_range(starting_date, periods=num_days)
date_generated = date_generated.strftime("%m/%d/%Y")

resolutions = np.array(['Grammar', 'Kanji', 'Vocab', 'Listening', 'Reading', 'Writing', 'Speaking'])

# Create Heatmap for which_heatmap
grammar_dates = data[data['Which Heatmap'] == 'Grammar']['Date'].values
kanji_dates = data[data['Which Heatmap'] == 'Kanji']['Date'].values
vocab_dates = data[data['Which Heatmap'] == 'Vocab']['Date'].values
listening_dates = data[data['Which Heatmap'] == 'Listening']['Date'].values
reading_dates = data[data['Which Heatmap'] == 'Reading']['Date'].values
writing_dates = data[data['Which Heatmap'] == 'Writing']['Date'].values
speaking_dates = data[data['Which Heatmap'] == 'Speaking']['Date'].values

hm_array = np.empty((0, 7))

for index, date in enumerate(date_generated):
    g_b = np.isin(grammar_dates, date).any()
    k_b = np.isin(kanji_dates, date).any()
    v_b = np.isin(vocab_dates, date).any()
    l_b = np.isin(listening_dates, date).any()
    r_b = np.isin(reading_dates, date).any()
    w_b = np.isin(writing_dates, date).any()
    s_b = np.isin(speaking_dates, date).any()
    hm_array = np.vstack((hm_array, np.array([[g_b, k_b, v_b, l_b, r_b, w_b, s_b]])))

hm_df = pd.DataFrame(hm_array)
hm_df.columns = resolutions

heatmap = sns.heatmap(hm_df.T, lw=1, cmap=['linen', 'yellowgreen'], cbar=False, xticklabels=False)
heatmap.tick_params(bottom=False)
heatmap = plt.tick_params(axis='y', rotation=0)
heatmap = plt.tick_params(axis='x', rotation=0)
heatmap = plt.title('2025 Resolutions Heatmap')
# plt.tight_layout()
plt.show()