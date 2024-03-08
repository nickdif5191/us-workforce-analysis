import pandas as pd

class DataFilterer:

    """
    Class designed to filter processed data to relevant data we will analyze

    Attributes:
        relevant_states (list): list of states whose data we will analyze

    Methods:
        __init__: initializes instance of DataFilterer class
        filter_data: filters processed data to the relevant data we care about
    
    """
    def __init__(self, relevant_states:list):
        """
        Initializes instance of DataFilterer class

        Parameters:
            relevant_states (list): list of states we want to analyze 
        """
        self.relevant_states = relevant_states        
        

    def filter_data(self, data_all_years:pd.DataFrame, relevant_job_titles:list):
        """
        Filters data to relevant occupations and states 

            Parameters: 
                data_all_years (pd.DataFrame): DF with data from all years - returned from read_and_process_files
                relevant_job_titles (list): list of job titles we want to analyze
            Returns:
                relevant_data (pd.DataFrame): DF with data from all years, but only for job codes and states we care about
        """
        job_titles_mask = data_all_years["OCC_TITLE"].isin(relevant_job_titles)
        try: 
            states_mask = data_all_years["STATE"].isin(self.relevant_states)
        except TypeError: # handle case where relevant_states is None - set all rows w/ a State to TRUE
            states_mask = data_all_years["STATE"].notna()
        relevant_data = data_all_years.loc[job_titles_mask & states_mask,:]
        # relevant_row_mask = data_all_years["OCC_TITLE"].isin(relevant_job_titles) & data_all_years["STATE"].isin(self.relevant_states) 
        # relevant_data = data_all_years.loc[relevant_row_mask,:]
        return relevant_data
    
    def standardize_occ_title_format(self, relevant_data:pd.DataFrame):
        """
        Standardizes the format of all values in OCC_TITLE format to prepare for output

        Parameters:
            relevant_data (pd.DataFrame): DF of relevant data to analyze, OCC_TITLE NOT standardized
        
        Returns:
            relevant_data (pd.DataFrame): DF of relevant data to analyze, OCC_TITLE standardized
        """
        relevant_data["OCC_TITLE"] = relevant_data["OCC_TITLE"].str.title()
        relevant_data['OCC_TITLE'] = relevant_data['OCC_TITLE'].str.replace('*', '')

        return relevant_data