def get_filename_strings(ts_fn):
    return {
        "metadata_unique_session_ids": f"m2c2kit_metadata_unique-session-ids_{ts_fn}.csv",
        "metadata_unique_participant_ids": f"m2c2kit_metadata_unique-participant-ids_{ts_fn}.csv",
    }
    
def get_m2c2kit_access_token(username=None, password=None):

    if username is None or password is None:
        # specify parameters for M2C2kit backend
        username = input('Enter username for M2C2kit backend...') # you will be prompted for a username
        password = getpass('Enter password for M2C2kit backend...') # you will be prompted for a password

    # specify login endpoint URL
    login_url = "https://prod.m2c2kit.com/auth/token"
    payload = f"=grant_type%3D&=scope%3D&=client_id%3D&=client_secret%3D&username={username}&password={password}"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # attempt login
    login_response = requests.request("POST", login_url, data=payload, headers=headers)
    access_token = login_response.json().get("access_token")


    # specify filename from current run time for filenames
    ts_fn = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # query range of data for a given study
    print("Token granted at: ", ts_fn)

    return access_token, ts_fn

def get_m2c2kit_trial_level_data(access_token=None, study_id=None, start_date=None, end_date=None, activity_name=None, skip=0):

    # check if required fields present
    if access_token is None:
        raise ValueError("access_token is required")
    if study_id is None:
        raise ValueError("study_id is required")
    if start_date is None:
        raise ValueError("start_date is required")
    if end_date is None:
        raise ValueError("end_date is required")
    if activity_name is None:
        raise ValueError("activity_name is required")

    # specify query endpoint URL
    query_url = "https://prod.m2c2kit.com/query/"

    # specify query parameters ----
    querystring = {"fields":"study_uid,uid,session_uid,activity_name,event_type,content,metadata",
                "activity_name":activity_name,
                "format":"json",
                "study_uid":study_id,
                "start_date":start_date,
                "end_date":end_date,
                "skip":skip,
                "limit":"1000"}

    payload = ""
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {access_token}"
    }

    # TODO: check for total and run with new limit and skip if reached limit ----
    data_response = requests.request("GET", query_url, data=payload, headers=headers, params=querystring)
    data_json = data_response.json()
    data_records = data_json.get("results")
    data_total = data_json.get("total")
    data_limit = data_json.get("limit")
    data_df = pd.DataFrame(data_records)

    # iterate over the dataset to get all trials ----
    all_trials = []
    for index, row in data_df.iterrows():
        json_data = row['content'].get("trials", [])
        all_trials.extend(json_data)

    # convert all trials to dataframe ----
    df_all = pd.DataFrame(all_trials)
    return df_all, data_total, data_limit

def get_m2c2kit_metadata(access_token=None, study_id=None, resource="session-counts"):

    # check if required fields present
    if access_token is None:
        raise ValueError("access_token is required")
    if study_id is None:
        raise ValueError("study_id is required")
    
    # specify query endpoint URL
    query_url = f"https://prod.m2c2kit.com/metadata/{resource}"

    # specify query parameters ----
    querystring = {"study_uid":study_id}

    payload = ""
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {access_token}"
    }

    # TODO: check for total and run with new limit and skip if reached limit ----
    data_response = requests.request("GET", query_url, data=payload, headers=headers, params=querystring)
    data_json = data_response.json()
    data_df = pd.DataFrame(data_json)

    return data_df, data_json

def summary_symbol_search(x, trials_expected=20):
    d = {}
    d["flag_is_invalid_n_trials"] = x["session_uuid"].count() != trials_expected
    d["n_trials"] = x["session_uuid"].count()
    d["n_trials_lure"] = (x["trial_type"] == "lure").sum()
    d["n_trials_responsetime_lt250ms"] = (x["response_time_duration_ms"] < 250).sum()
    d["n_trials_responsetime_gt10000ms"] = (
        x["response_time_duration_ms"] > 10000
    ).sum()
    d["n_correct_trials"] = (
        x["user_response_index"] == x["correct_response_index"]
    ).sum()
    d["n_incorrect_trials"] = (
        x["user_response_index"] != x["correct_response_index"]
    ).sum()
    d["mean_response_time_overall"] = x["response_time_duration_ms"].mean()
    d["mean_response_time_correct"] = x.loc[
        (x["user_response_index"] == x["correct_response_index"]),
        "response_time_duration_ms",
    ].mean()
    d["mean_response_time_incorrect"] = x.loc[
        (x["user_response_index"] != x["correct_response_index"]),
        "response_time_duration_ms",
    ].mean()
    d["median_response_time_overall"] = x["response_time_duration_ms"].median()
    d["median_response_time_correct"] = x.loc[
        (x["user_response_index"] == x["correct_response_index"]),
        "response_time_duration_ms",
    ].median()
    d["median_response_time_incorrect"] = x.loc[
        (x["user_response_index"] != x["correct_response_index"]),
        "response_time_duration_ms",
    ].median()
    d["sd_response_time_overall"] = x["response_time_duration_ms"].std()
    d["sd_response_time_correct"] = x.loc[
        (x["user_response_index"] == x["correct_response_index"]),
        "response_time_duration_ms",
    ].std()
    d["sd_response_time_incorrect"] = x.loc[
        (x["user_response_index"] != x["correct_response_index"]),
        "response_time_duration_ms",
    ].std()
    return pd.Series(
        d,
        index=[
            "flag_is_invalid_n_trials",
            # 'flag_is_potentially_invalid_rt',
            "n_trials",
            "n_trials_lure",
            "n_correct_trials",
            "n_incorrect_trials",
            "n_trials_responsetime_lt250ms",
            "n_trials_responsetime_gt10000ms",
            "mean_response_time_overall",
            "mean_response_time_correct",
            "mean_response_time_incorrect",
            "median_response_time_overall",
            "median_response_time_correct",
            "median_response_time_incorrect",
            "sd_response_time_overall",
            "sd_response_time_correct",
            "sd_response_time_incorrect",
        ],
    )


def summary_grid_memory(x, trials_expected=4):
    d = {}
    d["flag_is_invalid_n_trials"] = x["session_uuid"].count() != trials_expected
    d["n_trials"] = x["session_uuid"].count()
    d["n_perfect_trials"] = (x["number_of_correct_dots"] == 3.0).sum()
    d["mean_correct_dots"] = (x["number_of_correct_dots"]).mean()
    d["min_correct_dots"] = (x["number_of_correct_dots"]).min()
    d["sum_correct_dots"] = (x["number_of_correct_dots"]).sum()
    return pd.Series(
        d,
        index=[
            "flag_is_invalid_n_trials",
            "n_trials",
            "n_perfect_trials",
            "mean_correct_dots",
            "min_correct_dots",
            "sum_correct_dots",
        ],
    )
    
def summarise_m2c2kit_data(df = None, activity_name=None, group_by=["participant_id", "session_uuid", "session_id"], trials_expected = -999, ts_fn = None):
    if activity_name == "symbol-search" or activity_name == "symbolsearch" or activity_name == "symbol_search" or activity_name == "Symbol Search" or activity_name == "Symbol Match":
        activity_name_fn = activity_name.replace(" ", "_").lower()
        df_session_summary = df.groupby(group_by).apply(summary_symbol_search, trials_expected=trials_expected)
        df_session_summary.reset_index().to_csv(f"m2c2kit_scored_activity-{activity_name_fn}_{ts_fn}.csv", index=False)
        valid_scoring = True
    if activity_name == "grid-memory" or activity_name == "Dot Memory" or activity_name == "Grid Memory":
        activity_name_fn = activity_name.replace(" ", "_").lower()
        df_session_summary = df.groupby(group_by).apply(summary_grid_memory, trials_expected=trials_expected)
        valid_scoring = True

    if valid_scoring:
        df_session_summary.reset_index().to_csv(f"m2c2kit_scored_activity-{activity_name_fn}_{ts_fn}.csv", index=False)
        return df_session_summary
    else:
        print("Activity not supported yet. Please contact M2C2 for further coordination.")
        df_session_summary = None
        
        
# query Symbol Search activity data
df_symbolsearch, total_symbolsearch, limit_symbolsearch = get_m2c2kit_trial_level_data(access_token=access_token, 
                                                             study_id=study_id, 
                                                             start_date=start_date, 
                                                             end_date=end_date, 
                                                             skip=0,
                                                             activity_name="Symbol Search")

# query Symbol Search activity data
df_gridmemory, total_gridmemory, limit_gridmemory = get_m2c2kit_trial_level_data(access_token=access_token, 
                                                           study_id=study_id, 
                                                           start_date=start_date, 
                                                           end_date=end_date, 
                                                           skip=0,
                                                           activity_name="Grid Memory")

df_symbolsearch_dedup = df_symbolsearch.drop_duplicates(subset=['activity_uuid', 'session_uuid', 'trial_begin_iso8601_timestamp'])
df_gridmemory_dedup = df_gridmemory.drop_duplicates(subset=['activity_uuid', 'session_uuid', 'trial_begin_iso8601_timestamp'])

# confirm deduplication
print(f"Symbol Search: {df_symbolsearch.shape} to {df_symbolsearch_dedup.shape}")
print(f"Grid Memory: {df_gridmemory.shape} to {df_gridmemory_dedup.shape}")

# save data

# with duplicates (i.e., all downloaded data)
df_symbolsearch.to_csv(f"m2c2kit_raw_symbolsearch_{ts_fn}.csv")
df_gridmemory.to_csv(f"m2c2kit_raw_gridmemory_{ts_fn}.csv")

# without duplicates (i.e., deduplicated data)
df_symbolsearch_dedup.to_csv(f"m2c2kit_dedup_symbolsearch_{ts_fn}.csv")
df_gridmemory_dedup.to_csv(f"m2c2kit_dedup_gridmemory_{ts_fn}.csv")

session_counts = get_m2c2kit_metadata(access_token=access_token, study_id=study_id, resource="session-counts")
session_counts_df = session_counts[0]
session_counts_df.to_csv(f"m2c2kit_metadata_session-counts_{ts_fn}.csv", index=False)
display(session_counts_df)


session_counts_by_activity = get_m2c2kit_metadata(access_token=access_token, study_id=study_id, resource="session-counts-by-activity")
session_counts_by_activity_df = session_counts_by_activity[0]
session_counts_by_activity_df.to_csv(f"m2c2kit_metadata_session-counts-by-activity_{ts_fn}.csv", index=False)
display(session_counts_by_activity_df)

# note, this function writes files for you! 
df_symbolsearch_summary = summarise_m2c2kit_data(df = df_symbolsearch_dedup, activity_name="Symbol Search", group_by=["participant_id", "session_uuid", "activity_uuid", "session_id"], trials_expected = -999, ts_fn = ts_fn)
df_gridmemory_summary = summarise_m2c2kit_data(df = df_gridmemory_dedup, activity_name="Grid Memory", group_by=["participant_id", "session_uuid", "activity_uuid", "session_id"], trials_expected = -999, ts_fn = ts_fn)