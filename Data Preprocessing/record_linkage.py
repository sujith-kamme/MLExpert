from functools import reduce
import numpy as np

def preprocessing(df_youtube, df_spotify):
    for dataframe in [df_youtube, df_spotify]:
        dataframe["account_holder"] = (
            dataframe[["first_name", "last_name"]]
            .agg(" ".join, axis=1)
            .str.lower()
        )
        
        dataframe["ip_prefix"] = dataframe["non_mfa_ip_addresses"].apply(
            lambda addresses: [
                ".".join(addr.split(".")[:3]) 
                for addr in addresses
            ]
        )
    return df_youtube, df_spotify

def link_records(df_youtube, df_spotify):
    processed_yt, processed_sp = preprocessing(df_youtube, df_spotify)
    
    contact_indices = find_matching_contacts(processed_yt, processed_sp)
    digit_matches, ip_matches = find_composite_matches(processed_yt, processed_sp)
    
    combined_indices = reduce(
        np.union1d, 
        [contact_indices, digit_matches, ip_matches]
    )
    return processed_yt.iloc[combined_indices]

def find_matching_contacts(df1, df2):
    return np.nonzero(
        np.isin(df2["preferred_contact"], df1["preferred_contact"])
    )[0]

def find_composite_matches(df1, df2):
    """Find matches based on composite criteria"""
    name_indices = np.nonzero(
        np.isin(df2["account_holder"], df1["account_holder"])
    )[0]
    
    postal_indices = np.nonzero(
        np.isin(df2["billing_zip_code"], df1["billing_zip_code"])
    )[0]
    
    card_indices = np.nonzero(
        np.isin(df2["last_four_digits"], df1["last_four_digits"])
    )[0]
    
    ip_indices = np.nonzero(
        np.any(
            np.isin(
                df2["ip_prefix"].tolist(),
                df1["ip_prefix"].tolist()
            ),
            axis=1
        )
    )[0]
    
    name_zip_card = reduce(
        np.union1d,
        [name_indices, postal_indices, card_indices]
    )
    
    name_zip_network = reduce(
        np.union1d,
        [name_indices, postal_indices, ip_indices]
    )
    
    return name_zip_card, name_zip_network
