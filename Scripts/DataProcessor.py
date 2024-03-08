import pandas as pd

class DataProcessor:
    """
    Class designed to process and harbor all data and inputs for the model
    
    Attributes:
        input_loc (str): filepath to data inputs
        input_filename_format (str): the format of filenames for raw data inputs - enables efficient reading of data
        relevant_years (list): list of ints representing range of years of data we want to read in
        job_code_text_corpus (list): text corpus that will be used to identify relevant job titles - we will assess each job title's similarity to the corpus
        data_all_years (pd.DataFrame): DF of concatenated data from all relevant years

    Methods:
        __init__: initializer class
        read_and_process_files: reads in raw data files and performs processing
    
    """
    def __init__(self, input_loc:str, input_filename_format:str, relevant_years:list, output_loc:str):
        """
        Initializes instance of DataManager class

        Parameters:
            input_loc (str): filepath to inputs folder
            input_filename_format (str): the format of filenames for raw data inputs - enables efficient reading of data
            relevant_years (list): list of ints representing range of years of data we want to read in
            output_loc (str): filepath to outputs folder
            
        """
        self.input_loc = input_loc
        self.input_filename_format = input_filename_format
        self.relevant_years = relevant_years
        self.output_loc = output_loc
        self.data_all_years = self.read_and_process_files(folder_loc=input_loc,
                                                          filename_format=input_filename_format,
                                                          years=relevant_years,
                                                          output_loc=output_loc)

    def read_and_process_files(self, folder_loc:str, filename_format:str, years:list, output_loc:str):
        """
        Reads in datafiles from folder_loc, processes, and concatenates them
            
        Parameters: 
            folder_loc (str): filepath for folder where data is located
            filename_format (str): format of the filenames located in folder_loc
            years (list): two-item list representing range of years we want to analyze
            output_loc (str): location to write data_all_years to

        Returns:
            data_all_years (pd.DataFrame): DF including data from all years specified in years parameter
        """
        # empty DF - DFs from each year will be concatenated here
        data_all_years = pd.DataFrame()
        for i in range(years[0], years[1]+1):
            # read in file
            filename = filename_format.format(year=i)
            df = pd.read_csv(f"{folder_loc}/{filename}")
            # process file, address column names that change between years
            # changing col names to most recent version to align w/ most recent data
            df.columns = df.columns.str.upper()
            new_col_names = {
                            'AREA_TITLE':'STATE', 'LOC_QUOTIENT':'LOC_Q',
                            'H_WPCT10':'H_PCT10', 'H_WPCT25':'H_PCT25', 'H_WPCT75':'H_PCT75', 'H_WPCT90':'H_PCT90',
                            'A_WPCT10':'A_PCT10', 'A_WPCT25':'A_PCT25', 'A_WPCT75':'A_PCT75', 'A_WPCT90':'A_PCT90',
                            'GROUP':'O_GROUP', 'OCC_GROUP':'O_GROUP',
                            'ST':'PRIM_ST'
                            }
            df = df.rename(columns=new_col_names)
            # create 'YEAR' col to identify source year in concatenated DF
            df['YEAR'] = i
            # concat this iteration's DF to data_all_years
            data_all_years = pd.concat([data_all_years, df])
        
        data_all_years.to_csv(f"{output_loc}/data_all_years.csv", index=False)
        
        return data_all_years