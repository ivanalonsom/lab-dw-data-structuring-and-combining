import pandas as pd

def ini_dataframe_csv(url):

    df = pd.read_csv(url)
    return df

def change_cols_names(df):

    df.columns = ["Customer", 'ST', 'GENDER', 'Education', 'Customer Lifetime Value', 'Income', 'Monthly Premium Auto', 'Number of Open Complaints', 'Policy Type', 'Vehicle Class', 'Total Claim Amount']

    for x in df.columns:
        df.rename(columns={x: x.lower().replace(" ", "_")}, inplace=True)

    df.rename(columns={'st': 'state'}, inplace=True)

    return df



def fix_gender(x):
    if x == "Male":
        return "M"
    elif x == "Femal":
        return "F"
    elif x == "female":
        return "F"
    else:
        return x


def fix_state(df, map_states):
    
    df = df.replace(map_states)
    return df

def fix_education(df):
    df = df.str.replace("Bachelors", "Bachelor")
    return df

def fix_lifetime_value(df):
    df = df.str.replace("%", "")
    return df


def fix_vehicle_class(df, map_vehicles):
    
    df = df.replace(map_vehicles)
    return df


def change_object_to_float(df):
    df = df.str.replace('[a-zA-Z]', '0.0', regex=True)
    df = df.astype(float)
    return df


def fix_open_complaints(x):
    if type(x) != int:
        if pd.isnull(x) or '/' not in x:
            return x
        elif '/' in x:
            x_splitted = x.split("/")
            return x_splitted[1]


def drop_null_values(df):

    df.dropna(inplace=True)         
    return df


def keep_last_duplicate(df):
    
    df.drop_duplicates(subset=["state", "income"], keep='last', inplace=True) 
    return df


def new_index_reseted(df):
    df.reset_index(drop=True, inplace=True)     # drop True elimina el índice original y se reemplaza con uno nuevo que empieza de 0. Con False (por defecto) crea una nueva col con los índices nuevos
    return df


def create_csv(df):
    df.to_csv('ex5_file.csv', index=True) 



def main_cleaning(df, map_states, map_vehicles):

    df = change_cols_names(df)

    df["gender"] = df["gender"].apply(fix_gender)

    df["state"] = fix_state(df["state"], map_states)

    df["education"] = fix_education(df["education"])

    df["customer_lifetime_value"] = fix_lifetime_value(df["customer_lifetime_value"]) 

    
    df["vehicle_class"] = fix_vehicle_class(df["vehicle_class"], map_vehicles)

    df["customer_lifetime_value"] = change_object_to_float(df["customer_lifetime_value"])

    df["number_of_open_complaints"] = df["number_of_open_complaints"].apply(fix_open_complaints)

    df = drop_null_values(df)

    df = keep_last_duplicate(df)

    df = new_index_reseted(df)

    return df
