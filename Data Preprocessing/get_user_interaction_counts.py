from datetime import datetime, timedelta

def get_user_interaction_counts(search_interaction_df):
    # Get the most recent date from the dataframe
    max_date = search_interaction_df.select("date").orderBy("date", ascending=False).first()[0]
    reference_date = datetime.strptime(max_date, "%Y-%m-%d")
    
    # Calculate interaction periods
    time_periods = {
        "month": {"days": 30, "suffix": "month_interaction_count"},
        "week": {"days": 7, "suffix": "week_interaction_count"},
        "day": {"days": 1, "suffix": "day_interaction_count"}
    }
    
    # Initialize with monthly data
    result_df = None
    
    # Build the combined dataframe
    for period, config in time_periods.items():
        period_counts = get_df_counts_from_date_by_user_id(
            search_interaction_df, 
            reference_date, 
            config["days"]
        ).withColumnRenamed("interaction_count", config["suffix"])
        
        if result_df is None:
            result_df = period_counts
        else:
            result_df = result_df.join(period_counts, on="user_id", how="left")
    
    # Replace null values with zeros
    return result_df.fillna(0)

def get_df_counts_from_date_by_user_id(df, reference_date, interval):
    interval_start = reference_date - timedelta(days=interval)
    
    filtered_df = (
        df.filter((df.date >= interval_start) & (df.date <= reference_date))
        .groupBy("user_id")
        .agg({"*": "count"})
        .withColumnRenamed("count(1)", "interaction_count")
    )
    
    return filtered_df