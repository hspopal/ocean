# -*- coding: utf-8 -*-

"Created on Tue Oct  1 11:32:37 2024"

"@author: Dalia"

#library imported
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt


import seaborn as sns
#dfworking is the dataframe, which I copied from my file list into python here
raw_data = pd.read_csv(
    "C:/Users/dalia/OneDrive/CHARACTER TIME OC/Dalia Fixed Time Sheets.csv")


print(raw_data)

#to look at columns in my dfworking 
raw_data.columns

#look at values in the character column
print(raw_data['Character'])


#to drop the NaN column in my dfworking, kept original and made new cleaned df, need axis = 1 to identify only column being removed
raw_data = raw_data.drop('Good_clip', axis = 1)

#to check the new columns in new df
raw_data.columns

#isolate characters into their own df for manipulation
ryan_data = raw_data[raw_data["Character"] == "Ryan"]

print(raw_data)


#calculate sum total of clip length for each character

ryan_total = sum(ryan_data['Clip_length'])


# Create empty
character_seconds_df = pd.DataFrame(columns=["Character", "Seconds"])

print(character_seconds_df)

# Create list of characters
char_list = raw_data['Character'].unique()

print(char_list)

n=0
for char in char_list:
    temp_char_df = raw_data[raw_data["Character"] == char]
    
    temp_char_total = sum(temp_char_df['Clip_length'])

    # Fill in dataframe with character totals
    character_seconds_df.loc[n,"Character"] = char
    character_seconds_df.loc[n,"Seconds"] = temp_char_total
    n += 1
    
print(character_seconds_df)

#made a copy of character seconds dataframe to create bar graph of characters in 
character_seconds_bar = character_seconds_df.copy()

#make bar plot 

#sort columns in the data set before, need to create a df for the values before making bar plot 

character_seconds_bar = character_seconds_bar.sort_values(
                        by = 'Seconds', ascending = False)

print(character_seconds_bar)

character_seconds_bar = plt.bar(character_seconds_bar['Character'],
                                character_seconds_bar['Seconds'])

#adding labels to sorted bar plot

character_seconds_bar = plt.xlabel('Character')
character_seconds_bar = plt.ylabel('Seconds')
character_seconds_bar = plt.title('ScreenTime of Each Character')

print(character_seconds_bar)

#I made an attempt at for loop to sum screen time 
#for all characters using my df_bar dataset
#removed from the code bc not needed and took too long


#x= sum(character_seconds_df['Seconds'])

#for y in character_seconds_df['Character']:
#    if y == 'Ryan':
#        clip_sum = sum(character_seconds_df.iloc[:,1])
#    if y == 'Marissa':
#        clip_sum + sum(character_seconds_df.iloc[:,1])
#    if y == 'Sandy':
#        clip_sum + sum(character_seconds_df.iloc[:,1])
#    if y == 'Seth':
#        clip_sum + sum(character_seconds_df.iloc[:,1])
#    if y == 'Luke':
#        clip_sum + sum(character_seconds_df.iloc[:,1])
#    if y == 'Summer':
#        clip_sum + sum(character_seconds_df.iloc[:,1])
#    if y == 'Jimmy':
#        clip_sum + sum(character_seconds_df.iloc[:,1])
#    if y == 'Julie':
#        clip_sum + sum(character_seconds_df.iloc[:,1])
#    if y == 'Kirsten': 
#        clip_sum + sum(character_seconds_df.iloc[:,1])
        

# Make empty df
ftr = [3600,60,1]

test = raw_data['Episode_length'][0]
print(test)

total_epleng = sum([a*b for a,b in zip(ftr, map(int,test.split(':')))])

screentime_data = pd.DataFrame(columns = char_list, index = range(total_epleng))

print(screentime_data)

for n_row in raw_data.index:
    temp_char = raw_data.loc[n_row,'Character']
    temp_start_idx= raw_data.loc[n_row, 'Start_second']
    temp_end_idx = raw_data.loc[n_row, 'End_second']
    screentime_data.loc[temp_start_idx:temp_end_idx, temp_char] = 1

screentime_data.fillna(0, inplace = True)

print(screentime_data)



#make each graph a different, recommend using seaborn


#change y axis to 1.2


fig, axs = plt.subplots(8, sharex=True, sharey=True)
fig.suptitle('Dalia Screentime Character')
axs[0].plot(screentime_data['Ryan'])
axs[1].set_ylim(0, 1.2)
axs[2].plot(screentime_data['Sandy'])
axs[2].set_ylim(0, 1.2)
axs[3].plot(screentime_data['Seth'])
axs[3].set_ylim(0, 1.2)
axs[4].plot(screentime_data['Kirsten'])
axs[4].set_ylim(0, 1.2)
axs[5].plot(screentime_data['Summer'])
axs[5].set_ylim(0, 1.2)
axs[0].set_ylim(0, 1.2)
axs[1].plot(screentime_data['Marissa'])
axs[6].plot(screentime_data['Luke'])
axs[6].set_ylim(0, 1.2)
axs[7].plot(screentime_data['Jimmy'])
axs[7].set_ylim(0, 1.2)

print(fig)




#make bar plot data of data 


#Upload other datasets of episode 1 and clean and add sources for each 
zach_data = pd.read_csv(
    "C:/Users/dalia/OneDrive/CHARACTER TIME OC/ZACH- character_time_stamps.csv")
print(zach_data)

sophia_data = pd.read_csv(
    "C:/Users/dalia/OneDrive/CHARACTER TIME OC/SOPHIA -character_time_stamps.csv")
print(sophia_data)

#made a copy of my original raw dataset for manipulation
dalia_data = raw_data.copy()

dalia_data['Source'] = 'Dalia'

print(dalia_data)


#Sophia Data fixing
sophia_data = sophia_data.drop('Good_clip', axis =1)

sophia_data.drop(sophia_data.index[81:], inplace=True)

sophia_data.loc[74:80] = sophia_data.loc[74:80].fillna({'Season':1})

sophia_data['Source'] = 'Sophia'

print(sophia_data)

sophia_data_ep1 = sophia_data[sophia_data['Episode'] == 1]

print(sophia_data_ep1)


#zach data fixing
zach_data = zach_data.drop(63)

zach_data.drop(zach_data.index[154:], inplace = True)

zach_data = zach_data.drop('Good_clip', axis = 1)

zach_data['Source'] = 'Zach'

zach_data = zach_data.replace(to_replace="Marissa ", value="Marissa")

print(zach_data)

zach_data_ep1 = zach_data[zach_data['Episode'] == 1]

print(zach_data_ep1)

#merging the datasets
mergedf = pd.merge(dalia_data, zach_data, how='outer')
print(mergedf)

masterdf = pd.merge(mergedf, sophia_data, how = 'outer')
print(masterdf)


# make new df for episode 1 bar plot 

ep_1_df = masterdf[masterdf['Episode']  <2]
print(ep_1_df)



character_seconds_source_df = pd.DataFrame(columns=["Character", "Seconds","Source"])
print(character_seconds_source_df)

# Create list of characters
char_list2 = ep_1_df.drop_duplicates(subset=['Character', 'Source'])
print(char_list2)

char_list3 = char_list2[['Character','Source']]
print(char_list3)

n=0
source_list = ep_1_df['Source'].unique()
for char in char_list:
    temp_char_df = ep_1_df[ep_1_df["Character"] == char]
    for rater in source_list:
        temp_char_source = temp_char_df[temp_char_df['Source'] == rater]
        temp_char_total = sum(temp_char_source['Clip_length'])
    
        # Fill in dataframe with character totals
        character_seconds_source_df.loc[n,"Character"] = char
        character_seconds_source_df.loc[n,"Seconds"] = temp_char_total
        character_seconds_source_df.loc[n,'Source'] = rater
        n += 1
        
print(character_seconds_source_df)


source_ep1_bar = character_seconds_source_df.sort_values(by = 'Seconds', ascending = False)

print(source_ep1_bar)
#df_bar3 = plt.bar(df_bar2['Character'],df_bar2['Seconds'], group = df_bar2['Source'])

#sns.barplot(data = source_ep1_bar, x='Character', y='Seconds', hue='Source')


# Make line graphs for sophia and zach and add rater column to df 



#For zach
ftr = [3600,60,1]

test = zach_data['Episode_length'][0]
print(test)

zchar = zach_data['Character'].unique()

print(zchar)

z_total_epleng = sum([a*b for a,b in zip(ftr, map(int,test.split(':')))])

zach_data_screentime = pd.DataFrame(columns = zchar, index = range(z_total_epleng))

print(zach_data_screentime)

for n_row in zach_data.index:
    temp_char = zach_data.loc[n_row,'Character']
    temp_start_idx= zach_data.loc[n_row, 'Start_second']
    temp_end_idx = zach_data.loc[n_row, 'End_second']
    zach_data_screentime.loc[temp_start_idx:temp_end_idx, temp_char] = 1

zach_data_screentime.fillna(0, inplace = True)

print(zach_data_screentime)

#Zach DATAset for screentime data on EPISODe 1 ONLY

ftr = [3600,60,1]

test = zach_data_ep1['Episode_length'][0]
print(test)

zchar = zach_data_ep1['Character'].unique()
print(zchar)

z_total_epleng = sum([a*b for a,b in zip(ftr, map(int,test.split(':')))])

zach_screentime_ep1 = pd.DataFrame(columns = zchar, index = range(z_total_epleng))

print(zach_screentime_ep1)

for n_row in zach_data_ep1.index:
    temp_char = zach_data_ep1.loc[n_row,'Character']
    temp_start_idx= zach_data_ep1.loc[n_row, 'Start_second']
    temp_end_idx = zach_data_ep1.loc[n_row, 'End_second']
    zach_screentime_ep1.loc[temp_start_idx:temp_end_idx, temp_char] = 1

zach_screentime_ep1.fillna(0, inplace = True)

print(zach_screentime_ep1)


#zach lineplot

fig, axs = plt.subplots(8, sharex=True, sharey=True)
fig.suptitle('Zach Screentime Character')
axs[0].plot(zach_data_screentime['Ryan'])
axs[1].set_ylim(0, 1.2)
axs[2].plot(zach_data_screentime['Sandy'])
axs[2].set_ylim(0, 1.2)
axs[3].plot(zach_data_screentime['Seth'])
axs[3].set_ylim(0, 1.2)
axs[4].plot(zach_data_screentime['Kirsten'])
axs[4].set_ylim(0, 1.2)
axs[5].plot(zach_data_screentime['Summer'])
axs[5].set_ylim(0, 1.2)
axs[0].set_ylim(0, 1.2)
axs[1].plot(zach_data_screentime['Marissa'])
axs[6].plot(zach_data_screentime['Luke'])
axs[6].set_ylim(0, 1.2)
axs[7].plot(zach_data_screentime['Jimmy'])
axs[7].set_ylim(0, 1.2)

print(fig)


#Sophia Dataframe for line 

ftr = [3600,60,1]

test = sophia_data['Episode_length'][0]
print(test)

schar = sophia_data['Character'].unique()
print(schar)

s_total_epleng = sum([a*b for a,b in zip(ftr, map(int,test.split(':')))])

sophia_data_screentime = pd.DataFrame(columns = schar, index = range(s_total_epleng))
print(sophia_data_screentime)
for n_row in sophia_data.index:
    temp_char = sophia_data.loc[n_row,'Character']
    temp_start_idx= sophia_data.loc[n_row, 'Start_second']
    temp_end_idx = sophia_data.loc[n_row, 'End_second']
    sophia_data_screentime.loc[temp_start_idx:temp_end_idx, temp_char] = 1

sophia_data_screentime.fillna(0, inplace = True)
print(sophia_data_screentime)

#Sophia Dataset for screentime ONLY EPISODE 1

ftr = [3600,60,1]

test = sophia_data_ep1['Episode_length'][0]
print(test)

schar = sophia_data_ep1['Character'].unique()

print(schar)

s_total_epleng = sum([a*b for a,b in zip(ftr, map(int,test.split(':')))])

sophia_screentime_ep1 = pd.DataFrame(columns = schar, index = range(s_total_epleng))

print(sophia_screentime_ep1)

for n_row in sophia_data_ep1.index:
    temp_char = sophia_data_ep1.loc[n_row,'Character']
    temp_start_idx= sophia_data_ep1.loc[n_row, 'Start_second']
    temp_end_idx = sophia_data_ep1.loc[n_row, 'End_second']
    sophia_screentime_ep1.loc[temp_start_idx:temp_end_idx, temp_char] = 1

sophia_screentime_ep1.fillna(0, inplace = True)

sophia_screentime_ep1['Seconds'] = sophia_screentime_ep1.index

print(sophia_screentime_ep1)



#Sophia Lineplot

fig, axs = plt.subplots(8, sharex=True, sharey=True)
fig.suptitle('Sophia Screentime Character')
axs[0].plot(sophia_data_screentime['Ryan'])
axs[1].set_ylim(0, 1.2)
axs[2].plot(sophia_data_screentime['Sandy'])
axs[2].set_ylim(0, 1.2)
axs[3].plot(sophia_data_screentime['Seth'])
axs[3].set_ylim(0, 1.2)
axs[4].plot(sophia_data_screentime['Kirsten'])
axs[4].set_ylim(0, 1.2)
axs[5].plot(sophia_data_screentime['Summer'])
axs[5].set_ylim(0, 1.2)
axs[0].set_ylim(0, 1.2)
axs[1].plot(sophia_data_screentime['Marissa'])
axs[6].plot(sophia_data_screentime['Luke'])
axs[6].set_ylim(0, 1.2)
axs[7].plot(sophia_data_screentime['Jimmy'])
axs[7].set_ylim(0, 1.2)

print(fig)


#Add rater category to each df for screentime

sophia_data_screentime['Rater'] = 'Sophia'

zach_data_screentime['Rater'] = 'Zach'

screentime_data['Rater'] = 'Dalia'

screentime_data['Seconds'] = screentime_data.index

sophia_data_screentime['Seconds'] = sophia_data_screentime.index

zach_data_screentime['Seconds'] = zach_data_screentime.index


print(sophia_data_screentime)
print(zach_data_screentime)
print(screentime_data)

zach_sophia_data_screentime = pd.merge(sophia_data_screentime, zach_data_screentime, how='outer')

print(zach_sophia_data_screentime)

screentime_sum = pd.merge(zach_sophia_data_screentime, screentime_data, how = 'outer')

print(screentime_sum)




#Graph for screentime plot with all three raters

sns.set()



fig, axs = plt.subplots(9, sharex=True, sharey=True)
fig.suptitle('Screentime Character')
n=0
for char in char_list:
    sns.lineplot(data = screentime_sum, x= screentime_sum['Seconds'], y=screentime_sum[char].values, hue = 'Rater', ax = axs[n])
    plt.ylim(0, 1.2)
    axs[n].legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)
    n=n+1
print(fig)



#Inter rater between sophia and zach 
from sklearn.metrics import cohen_kappa_score
ryan_zach = zach_data_screentime['Ryan']

print(ryan_zach)

ryan_sophia = sophia_data_screentime['Ryan']

print(ryan_sophia)

output = cohen_kappa_score(ryan_zach, ryan_sophia)

print(output)

print(char_list)



# Convert the results into a DataFrame for comparison


# Display the resulting DataFrame

kappa_results = pd.DataFrame(columns = char_list)

print(kappa_results)

kappa_results['Raters'] = 'Zach and Sophia','Dalia and Sophia','Zach and Dalia'
print(kappa_results)

for char in char_list: 
    temp_rater_list_zach = zach_data_screentime[char]
    temp_rater_list_sophia = sophia_data_screentime[char]
    temp_rater_list_dalia = screentime_data[char]
    print(temp_rater_list_dalia)
    print(temp_rater_list_zach)
    print(temp_rater_list_sophia)
        
    temp_output1 = cohen_kappa_score(temp_rater_list_zach, temp_rater_list_sophia)
    print(temp_output1)
    temp_output2 = cohen_kappa_score(temp_rater_list_dalia, temp_rater_list_sophia)
    print(temp_output2)
    temp_output3 = cohen_kappa_score(temp_rater_list_zach, temp_rater_list_dalia)
    print(temp_output3)
    
    
    kappa_results.loc[kappa_results['Raters'] == 'Zach and Sophia', char] = temp_output1
    kappa_results.loc[kappa_results['Raters'] == 'Dalia and Sophia', char] = temp_output2
    kappa_results.loc[kappa_results['Raters'] == 'Zach and Dalia', char] = temp_output3
    
print(kappa_results)    

#revised kappa results for episode 1 only 

kappa_results_ep1 = pd.DataFrame(columns = char_list)

kappa_results_ep1['Raters'] = 'Zach and Sophia','Dalia and Sophia','Zach and Dalia'

print(kappa_results_ep1)

for char in char_list: 
    temp_rater_list_zach = zach_screentime_ep1[char]
    temp_rater_list_sophia = sophia_screentime_ep1[char]
    temp_rater_list_dalia = screentime_data[char]
        
    temp_output1 = cohen_kappa_score(temp_rater_list_zach, temp_rater_list_sophia)
    print(temp_output1)
    temp_output2 = cohen_kappa_score(temp_rater_list_dalia, temp_rater_list_sophia)
    print(temp_output2)
    temp_output3 = cohen_kappa_score(temp_rater_list_zach, temp_rater_list_dalia)
    print(temp_output3)
    
    
    kappa_results_ep1.loc[kappa_results_ep1['Raters'] == 'Zach and Sophia', char] = temp_output1
    kappa_results_ep1.loc[kappa_results_ep1['Raters'] == 'Dalia and Sophia', char] = temp_output2
    kappa_results_ep1.loc[kappa_results_ep1['Raters'] == 'Zach and Dalia', char] = temp_output3
    
print(kappa_results_ep1)

# bargraph add average overall 


#First thing I did here was attempt to make a 
#cohen kappa score for two zach and sophia on ryan. 

ryan_zach = zach_data_screentime['Ryan']
print(ryan_zach)
ryan_sophia = sophia_data_screentime['Ryan']
print(ryan_sophia)

ryan_zach_sophia_score = cohen_kappa_score(ryan_zach, ryan_sophia)

#this gives me the score
print(ryan_zach_sophia_score)

#this prints the length of each person
print(len(ryan_zach), len(ryan_sophia))

#this makes a new df I can use
kappa_results_bar_ep1 = kappa_results_ep1
print(kappa_results_bar_ep1)

#this is needed to make the df in which I can look at the 
#cohen kappa scores for each rater and character
kappa_results_long = kappa_results_ep1.melt(id_vars="Raters", 
                                            var_name="Character", 
                                            value_name="Kappa Score")
print(kappa_results_long)

#this is my barplot of the results
kappa_results_bar = sns.barplot(data = kappa_results_long, x='Character', 
                                y='Kappa Score', hue='Raters')

sns.move_legend(kappa_results_bar, "upper left", bbox_to_anchor=(1, 1))



#relationship dictionary in which we will keep a working directory of all 
relation_dict = {}
relation_dict['Ryan-Seth'] = []
relation_dict['Ryan-Seth'].append("752-926")



#sophia_screentime_ep1 and zach_screentime_ep1 were the 
#df I used for the relationship dictionary 
zach_screentime_ep1['Seconds'] = zach_data_screentime.index
print(zach_screentime_ep1)

#this is an example of what I was trying to do that I attempted
temp_seth_ryan_z = zach_screentime_ep1[(zach_screentime_ep1['Ryan'] == 1)
                                       & (zach_screentime_ep1['Seth'] == 1 )]
grouped = temp_seth_ryan_z.groupby('Seth').sum()


#to chunk my lists by successive, I used this 
#new definition chunk_by_successiev for my lists
def chunk_by_successive(lst):
        """Chunks a list of numbers based on successive sequences."""

        result = []
        current_chunk = []

        for num in lst:
            if not current_chunk or num == current_chunk[-1] + 1:
                current_chunk.append(num)
            else:
                result.append(current_chunk)
                current_chunk = [num]

        if current_chunk:
            result.append(current_chunk)

        return result 

#example of this
seth_ryan = chunk_by_successive(temp_seth_ryan_z['Seconds']) 
print(seth_ryan)
    


# Generate all unique combinations of pairs
import itertools
char_pairings = list(itertools.combinations(char_list, 2))    

print(char_list)


    
    
# make a new list with zach and sphia agreement data on 
#when characters are on screen (time wise)
 



#first attempt was as a df not a list, was not successful, was not getting successive
# Add the shared values to a new column in df

ryan_df = pd.DataFrame()
print(ryan_df)

for char in char_list:
    temp_df_zach = zach_screentime_ep1[zach_screentime_ep1[char] == 1 
                                       & zach_screentime_ep1['Seconds']]
    print(temp_df_zach)
    temp_df_sophia = sophia_screentime_ep1[sophia_screentime_ep1[char] == 1 
                                           & sophia_screentime_ep1['Seconds']]
    print(temp_df_sophia)
    zach_sophia_ep1 = pd.merge(temp_df_zach, temp_df_sophia, how = 'inner')
    print(zach_sophia_ep1)
    

#here is the actual successive chunking. Got it to work till the end. 
#Need to trouble shoot the last 4 lines starting from n=0

nan_check = sophia_screentime_ep1.isnull() # or df.isna()
print(nan_check)



temp_shared_list = []

for char_a in char_list: 
    for char_b in char_list:
        if char_a != char_b:
            print(f"Checking: {char_a}, {char_b}")  # Debugging print
            print(f"Columns in Sophia DF: {sophia_screentime_ep1.columns}")  # Debugging print

            # Check unique values before filtering
            print(f"Unique values in {char_a}:", sophia_screentime_ep1[char_a].unique())
            print(f"Unique values in {char_b}:", sophia_screentime_ep1[char_b].unique())

            temp_df_sophia = sophia_screentime_ep1[(sophia_screentime_ep1[char_a] == 1) &
                                                   (sophia_screentime_ep1[char_b] == 1)][['Seconds', char_a, char_b]]
            print(temp_df_sophia)  # Print output



#Troubleshoooting Sophia Temp DF to find out why not getting back any values in the loop below 
for char_a in char_list: 
    for char_b in char_list:
        if char_a != char_b:
            print(sophia_screentime_ep1[sophia_screentime_ep1[char_a] == 1])  # Check rows where char_a is 1
            print(sophia_screentime_ep1[sophia_screentime_ep1[char_b] == 1])

for char_a in char_list: 
    for char_b in char_list:
        if char_a != char_b:
            char_a == sophia_screentime_ep1['Ryan']
            char_b == sophia_screentime_ep1['Seth']

            temp_df_sophia = sophia_screentime_ep1[(sophia_screentime_ep1[char_a] == 1) &
                                    (sophia_screentime_ep1[char_b] == 1)][['Seconds', char_a, char_b]]
            print(temp_df_sophia)




temp_shared_list = []
for char_a in char_list: 
    for char_b in char_list:
        if char_a != char_b:
            temp_df_zach = zach_screentime_ep1[(zach_screentime_ep1[char_a] == 1) & 
                                (zach_screentime_ep1[char_b] == 1)][['Seconds',char_a, char_b]]
            print(temp_df_zach)
for char_a in char_list: 
    for char_b in char_list:
        if char_a != char_b:

            temp_df_sophia = sophia_screentime_ep1[(sophia_screentime_ep1[char_a] == 1) &
                            (sophia_screentime_ep1[char_b] == 1)][['Seconds', char_a, char_b]]
            print(temp_df_sophia)
#Above code gives me a temp df from sophia and 
#zach of the character pairings and their corredponding seconds
            temp_zach_list = temp_df_zach['Seconds']
            print(temp_zach_list)
            temp_list_sophia = temp_df_sophia['Seconds']
            print(temp_list_sophia)
            for x in temp_zach_list: 
                if x in temp_list_sophia:
                    temp_shared_list.append(x)
                    print(temp_shared_list)
                    chunked_list = chunk_by_successive(temp_shared_list['Seconds'])
                    print(chunked_list)



#BELOW CODE WORKS!!!!!!!!!!!!
#THE PIECE DE RESISTANCE!!!! IM DONEEEEEEE!
chunked_dict = {}
temp_shared_list = []
for char_a in char_list: 
    for char_b in char_list:
        if char_a != char_b:
            temp_df_zach = zach_screentime_ep1[(zach_screentime_ep1[char_a] == 1) & 
                                (zach_screentime_ep1[char_b] == 1)][['Seconds',char_a, char_b]]
            print(temp_df_zach)
            temp_df_sophia = sophia_screentime_ep1[(sophia_screentime_ep1[char_a] == 1) &
                            (sophia_screentime_ep1[char_b] == 1)][['Seconds', char_a, char_b]]
            print(temp_df_sophia)
            temp_zach_list = temp_df_zach['Seconds']
            print(temp_zach_list)
            temp_list_sophia = temp_df_sophia['Seconds']
            print(temp_list_sophia)
            
            temp_shared_list = [x for x in temp_zach_list if x in temp_list_sophia]
            
            chunked_list = chunk_by_successive(temp_shared_list)

            # Store in dictionary using (char_a, char_b) as key
            chunked_dict[(char_a, char_b)] = chunked_list
            print(chunked_dict)
            
            
            

#I think there are no similar valyes for sophia df



#   I think at this point, where I have the 1 to 1 get 
#            temp_zach_list = temp_df_zach['Seconds']
#            print(temp_zach_list)
#            temp_list_sophia = temp_df_sophia['Seconds']
#            print(temp_list_sophia)
#            for x in temp_zach_list:
#                if x in temp_list_sophia:
#                   temp_shared_list.append(x)
#                   chunked_list = chunk_by_successive(temp_shared_list)
#                   for sublist in chunked_list:
#                       for n in range(len(sublist)):
#                           chunked_list.append([sublist[n], sublist[-1]])
            
                  
                      
                   
        
#Dictionary Not working

#ryan_seth_df = pd.DataFrame(zach_screentime_ep1[(zach_screentime_ep1['Seth'] == 1) & 
#                    (zach_screentime_ep1['Ryan'] == 1)][['Seconds','Seth', 'Ryan']])


#print(ryan_seth_df)

#zach_ryan_seth_chunked = chunk_by_successive(ryan_seth_df['Seconds'])

#print(zach_ryan_seth_chunked)





















