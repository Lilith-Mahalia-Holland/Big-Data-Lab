
# Author: Lilith Holland
# Make sure that box drive is installed and you have editor approval on the file.
# Make sure that the variables below are all configured to your current machine.
# This script will crash sometimes, I'm working on fixing this but it's a difficult problem.






import pandas as pd
import numpy as np
import os
import sys


# ALL OF THIS NEEDS TO BE SETUP FOR YOUR CURRENT SYSTEM
# Base path to the save and load locations, above any folders that are used
# Since this script modifies and creates files make sure you change the path's, otherwise the script will not work
load_base_path = "C:/Users/jdhjr/Box/COVID-19 Raw Twitter JSONs"
save_base_path = "C:/Users/jdhjr/Box/COVID-19 Flattened Twitter CSVs"
user_base_dir = "C:/Users/jdhjr"
# The last folder will not be done due to how python works, if you want to do 12 folders put 0 and 12 in.
folder_start = 0
folder_end = 12
all_folder = False


if not os.path.isdir(user_base_dir):
    sys.exit()


# I search for all of the json data by walking the load_path location
load_folder_name = next(os.walk(load_base_path), (None, None, []))[1]
save_folder_name = load_folder_name


# Combine the full load path with each individual folder name and append these to a new list
load_folder_path = []
save_folder_path = []
for i in range(0, len(load_folder_name)):
    load_folder_path.append(load_base_path + "/" + load_folder_name[i])
    save_folder_path.append(save_base_path + "/" + save_folder_name[i])


for i in range(0, len(save_folder_path)):
    if os.path.exists(save_base_path) and not os.path.exists(save_folder_path[i]):
        os.makedirs(save_folder_path[i])


# Walk the path of each folder and create a sub list of all file names for each folder name
# This loop is only keeping the names of each folder for saving reasons
save_file_path = []
load_file_path = []
save_file_name = []
for i in range(0, len(load_folder_path)):
    # Walk the contents of folder i in the load_path_temp list
    load_file_name = next(os.walk(load_folder_path[i]), (None, None, []))[2]
    inner_save_file_path = []
    inner_load_file_path = []
    inner_save_file_name = []
    # Go through all files and only keep files that are of type .json and append these files to the inner_path list
    for j in range(0, len(load_file_name)):
        if load_file_name[j].endswith(".json"):
            # Append paths together and create a list for names, this is all done so I can dynamically name and load
            # files
            inner_save_file_path.append(save_folder_path[i] + "/" + os.path.splitext(load_file_name[j])[0])
            inner_load_file_path.append(load_folder_path[i] + "/" + load_file_name[j])
            inner_save_file_name.append(os.path.splitext(load_file_name[j])[0])
    save_file_path.append(inner_save_file_path)
    load_file_path.append(inner_load_file_path)
    save_file_name.append(inner_save_file_name)


del(i, j, inner_load_file_path, inner_save_file_name, inner_save_file_path, load_file_name, load_folder_name,
    load_folder_path, save_folder_name)


# Thee dictionaries are used to fill in missing nested values, from my understanding this is an annoying caveat of
# steaming the json file in rather than just load it as a whole.
user_dict = {'id': None,
             'id_str': None,
             'name': None,
             'screen_name': None,
             'location': None,
             'url': None,
             'description': None,
             'translator_type': None,
             'protected': None,
             'verified': None,
             'followers_count': None,
             'friends_count': None,
             'listed_count': None,
             'favourites_count': None,
             'statuses_count': None,
             'created_at': None,
             'utc_offset': None,
             'time_zone': None,
             'geo_enabled': None,
             'lang': None,
             'contributors_enabled': None,
             'is_translator': None,
             'profile_background_color': None,
             'profile_background_image_url': None,
             'profile_background_image_url_https': None,
             'profile_background_tile': None,
             'profile_link_color': None,
             'profile_sidebar_border_color': None,
             'profile_sidebar_fill_color': None,
             'profile_text_color': None,
             'profile_use_background_image': None,
             'profile_image_url': None,
             'profile_image_url_https': None,
             'profile_banner_url': None,
             'default_profile': None,
             'default_profile_image': None,
             'following': None,
             'follow_request_sent': None,
             'notifications': None}
retweet_dict = {'created_at': None,
                'id': None,
                'id_str': None,
                'text': None,
                'display_text_range': None,
                'source': None,
                'truncated': None,
                'in_reply_to_status_id': None,
                'in_reply_to_status_id_str': None,
                'in_reply_to_user_id': None,
                'in_reply_to_user_id_str': None,
                'in_reply_to_screen_name': None,
                'user': {'id': None,
                         'id_str': None,
                         'name': None,
                         'screen_name': None,
                         'location': None,
                         'url': None,
                         'description': None,
                         'translator_type': None,
                         'protected': None,
                         'verified': None,
                         'followers_count': None,
                         'friends_count': None,
                         'listed_count': None,
                         'favourites_count': None,
                         'statuses_count': None,
                         'created_at': None,
                         'utc_offset': None,
                         'time_zone': None,
                         'geo_enabled': None,
                         'lang': None,
                         'contributors_enabled': None,
                         'is_translator': None,
                         'profile_background_color': None,
                         'profile_background_image_url': None,
                         'profile_background_image_url_https': None,
                         'profile_background_tile': None,
                         'profile_link_color': None,
                         'profile_sidebar_border_color': None,
                         'profile_sidebar_fill_color': None,
                         'profile_text_color': None,
                         'profile_use_background_image': None,
                         'profile_image_url': None,
                         'profile_image_url_https': None,
                         'profile_banner_url': None,
                         'default_profile': None,
                         'default_profile_image': None,
                         'following': None,
                         'follow_request_sent': None,
                         'notifications': None},
                'geo': None,
                'coordinates': None,
                'place': None,
                'contributors': None,
                'is_quote_status': None,
                'quote_count': None,
                'reply_count': None,
                'retweet_count': None,
                'favorite_count': None,
                'entities': {'hashtags': None,
                             'urls': None,
                             'user_mentions': [{'screen_name': None,
                                                    'names': None,
                                                    'id': None,
                                                    'id_str': None,
                                                    'indicies': None}],
                             'symbols': None,
                             'media': [{'id': None,
                                        'id_str': None,
                                        'indices': None,
                                        'media_url': None,
                                        'media_url_https': None,
                                        'url': None,
                                        'display_url': None,
                                        'expanded_url': None,
                                        'type': None,
                                        'sizes': {'small': {'w': None, 'h': None, 'resize': None},
                                                  'thumb': {'w': None, 'h': None, 'resize': None},
                                                  'large': {'w': None, 'h': None, 'resize': None},
                                                  'medium': {'w': None, 'h': None, 'resize': None}}}]},
                'extended_entities': {'media': [{'id': None,
                                                 'id_str': None,
                                                 'indices': None,
                                                 'media_url': None,
                                                 'media_url_https': None,
                                                 'url': None,
                                                 'display_url': None,
                                                 'expanded_url': None,
                                                 'type': None,
                                                 'sizes': {'small': {'w': None, 'h': None, 'resize': None},
                                                           'thumb': {'w': None, 'h': None, 'resize': None},
                                                           'large': {'w': None, 'h': None, 'resize': None},
                                                           'medium': {'w': None, 'h': None, 'resize': None}}}]},
                'favorited': None,
                'retweeted': None,
                'possibly_sensitive': None,
                'filter_level': None,
                'lang': None}
retweet_user_entities_user_mentions_dict = {'screen_name': None,
                                            'names': None,
                                            'id': None,
                                            'id_str': None,
                                            'indicies': None}


# This unnest function will take away one layer of a nested dictionary at a time, the dict variable are used either
# when the NA values have not be replaced by a dict in a previous step, the empty_test variable is used when there is
# an empty list rather than a NA value, this needs a special test case due to issues with handling na values and lists.
def df_unnest (df, dict=None, column=None, empty_test=False):
    # This is a warning that pandas has where it tries to inform the user about nested data frames, I turned this off
    # as it is not an omnipotent warning and is giving a false positive in certain scenarios.
    pd.options.mode.chained_assignment = None
    # Create a dataframe of the column to be worked on and a data frame for the original - the column being worked on
    temp_df_new = df[column]
    temp_df_old = df.loc[:, df.columns != column]
    # the empty test here just makes sure that if the data frame has a row which is an empty list that row will be
    # replaced by an NA value
    if empty_test:
        temp_df_new = temp_df_new.apply(lambda x: np.nan if len(x) == 0 else x[0])
    # The NA test is simply finding and replacing any NA rows with an empty None version of the appropriate dictionary
    temp_df_new[temp_df_new.isna()] = temp_df_new.loc[temp_df_new.isna()].apply(lambda x: dict)


    # Rebuild the dataframe from a list of dictionaries composed of all rows in the previous version
    temp_df_new = pd.DataFrame(temp_df_new.values.tolist(), index=temp_df_new.index)
    # Dynamically name the columns
    temp_df_new = temp_df_new.add_prefix(column + "_")
    # Join the original and new dataframe
    temp_df = pd.concat([temp_df_old, temp_df_new], axis=1, join="inner")
    return temp_df


# This is just a long list of all column names that are required throughout the process of creating the final data frame
initial_columns = ["created_at", "id_str", "text", "in_reply_to_status_id_str", "in_reply_to_user_id_str", "in_reply_to_screen_name", "user", "retweeted_status"]
user_data_columns = ["user_id_str", "user_screen_name", "user_description", "user_followers_count", "user_friends_count", "user_statuses_count",
                     "user_favourites_count", "user_created_at", "user_verified"]
retweet_data_columns = ["retweeted_status_created_at", "retweeted_status_id_str", "retweeted_status_text", "retweeted_status_retweet_count", "retweeted_status_lang",
                        "retweeted_status_user"]
retweet_user_data_columns = ["retweeted_status_user_id_str", "retweeted_status_user_screen_name", "retweeted_status_user_description", "retweeted_status_user_verified"]
retweet_mentions_columns = ["retweeted_status_entities_user_mentions_screen_name", "retweeted_status_entities_user_mentions_id_str"]


# Simple check to load all folders if required
if all_folder:
    folder_end = len(save_folder_path)


# for i in range(0, len(load_file_path)-1):
# Run through all of the possible folders
#try:
for i in range(folder_start, folder_end):
    print("Starting folder %d\n" % (i + 1))
    # Run through all possible files in each folder
    for j in range(0, len(load_file_path[i])):
        # If a file exists make sure to not re calculate the file
        if not os.path.isfile(save_file_path[i][j] + ".zip"):
            # If the file does not exist make an empty data frame
            sdf = pd.DataFrame()
            print(" Starting file %d\n" % (j +1))
            # Read through the JSON in chunks of 10,000
            # There is some kind of bug with converting the slices into a list
            # for df in reader: lines = list(islice(self.data, self.chunksize))
            try:
                with pd.read_json(load_file_path[i][j], lines=True, chunksize=10000, orient="columns", encoding="utf-8-sig") as reader:
                    chunk = 1
                    # For each chunk run through this process
                    for df in reader:
                        print("     Starting chunk %d" % chunk)
                        # Remove all initial unnecessary columns
                        df = df[initial_columns]
                        # Unnest the user column with the user dictionary
                        df = df_unnest(df, user_dict, "user")
                        df = df_unnest(df, retweet_dict, "retweeted_status")
                        df = df_unnest(df, column="retweeted_status_user")
                        df = df_unnest(df, column="retweeted_status_entities")
                        df = df_unnest(df, retweet_user_entities_user_mentions_dict,
                                       "retweeted_status_entities_user_mentions", empty_test=True)
                        # Combine all of the column names that are kept
                        df = df[initial_columns[:-2] + user_data_columns + retweet_data_columns[:-1] +
                                retweet_user_data_columns + retweet_mentions_columns]
                        # Concatinate each chunk into the sdf data frame
                        sdf = pd.concat([sdf, df], ignore_index=True)
                        print("     Finished chunk %d\n" % chunk)
                        chunk = chunk + 1
                # create a zip file for each data frame, I would prefer to make them share but that has issues atm
                compression_opts = dict(method="zip", archive_name=save_file_name[i][j] + ".csv")
                # Save the csv into the zip file
                sdf.to_csv(save_file_path[i][j] + ".zip", index=False, compression=compression_opts)
                print(" Finished file %d\n" % (j + 1))
            except:
                print("     Error on current chunk")
        else:
            print(" File %d has already been done\n" % (j + 1))
    print("Finished folder %d\n" % (i + 1))
