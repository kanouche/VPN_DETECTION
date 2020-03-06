import keras
import pandas as pd

def rename_dataframe_column(dataframe_rename_columns):
    for column in dataframe_rename_columns.columns:
        new_column_name = column.replace(" ", "_").replace('/', '_').lower()
        dataframe_rename_columns.rename(index=str, columns={column: new_column_name}, inplace=True)


def clean_dataset(dataset_to_clean):
    
    non_vpns = [ "give the data here.."]

    # iterate through dataframe and set value
    for row in dataset_to_clean.itertuples():
        if ((dataset_to_clean.at[row.Index, 'src_ip'] in non_vpns) or (
                dataset_to_clean.at[row.Index, 'dst_ip'] in non_vpns)):
            dataset_to_clean.at[row.Index, 'label'] = 1
        else:
            dataset_to_clean.at[row.Index, 'label'] = 0

        if ((dataset_to_clean.at[row.Index, 'src_ip'] in non_vpns) or (
                dataset_to_clean.at[row.Index, 'dst_ip'] in non_vpns)):
            dataset_to_clean.at[row.Index, 'label'] = 1
        else:
            dataset_to_clean.at[row.Index, 'label'] = 0

    # Drop row with infinity string value
    dataset_to_clean.drop(dataset_to_clean.loc[dataset_to_clean['flow_byts_s'] == "Infinity"].index, inplace=True)
    dataset_to_clean.drop(dataset_to_clean.loc[dataset_to_clean['flow_pkts_s'] == "Infinity"].index, inplace=True)


def main():

    dataset_training = pd.read_csv('unb-Training.csv', encoding='utf-8', low_memory=False)
    dataset_testing = pd.read_csv('unb-testing.csv', encoding='utf-8', low_memory=False)

    clean_dataset2(dataset_testing)
    clean_dataset2(dataset_training)

if __name__ == "__main__":
    main()