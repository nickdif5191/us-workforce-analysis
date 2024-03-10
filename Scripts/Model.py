import pandas as pd
import os
from DataProcessor import DataProcessor
from JobCodeIdentifier import JobCodeIdentifier
from DataFilterer import DataFilterer

class Model:
    """
    Class designed to read, process, and filter occupational data to data specific to an industry

    Attributes:
        job_code_text_corpus (list): text corpus used to identify relevant job titles - we will assess each job title's similarity to the corpus
        relevant_states (list): list of states we want to analyze 
        relevance_threshold (float): threshold to identify relevant job codes - those with similarity rating higher than this are deemed relevant
        
    Methods:
        __init__: Initializes instance of DataModel class
        get_output_loc: returns output location of DataProcessor object
        run_model: performs reading, processing, filtering processes, returning data we will analyze
    """
    def __init__(self, job_code_text_corpus, relevant_states, relevance_threshold):
        """
        Initializes instance of DataModel class
            
            Parameters:
                job_code_text_corpus (list): text corpus used to identify relevant job titles - we will assess each job title's similarity to the corpus
                relevant_states (list): list of states we want to analyze 
                relevance_threshold (float): threshold to identify relevant job codes - those with similarity rating higher than this are deemed relevant
            
            Returns:
                data_to_analyze (pd.DataFrame): data relevant to the specified states (via relevant_states0) and industry (via job_code_text_corpus and relevance_threshold)
        """
        self.job_code_text_corpus = job_code_text_corpus
        self.relevant_states = relevant_states
        self.relevance_threshold = relevance_threshold

        self.data_to_analyze = self.run()

    def get_output_loc(self):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), "../Outputs"))
    
    def run(self):
        
        data_processor = DataProcessor(input_loc=os.path.abspath(os.path.join(os.path.dirname(__file__), "../Data")),
                            input_filename_format="state_M{year}_dl.csv",
                            relevant_years=[2001,2022], 
                            output_loc=os.path.abspath(os.path.join(os.path.dirname(__file__), "../Outputs")))
        
        job_code_identifier = JobCodeIdentifier(data_all_years=data_processor.data_all_years, 
                        job_code_text_corpus=self.job_code_text_corpus,
                        model_loc=os.path.abspath(os.path.join(os.path.dirname(__file__), "../Scripts/GoogleNews-vectors-negative300.bin")),
                        relevance_threshold=self.relevance_threshold)
        
        data_filterer = DataFilterer(relevant_states=self.relevant_states)

        relevant_job_titles = job_code_identifier.identify_relevant_job_codes(data_all_years=data_processor.data_all_years,
                                                                              text_corpus=self.job_code_text_corpus,
                                                                              model_loc=job_code_identifier.model_loc,
                                                                              relevance_threshold=self.relevance_threshold)

        data_to_analyze = data_filterer.filter_data(data_all_years=data_processor.data_all_years, 
                                                    relevant_job_titles=relevant_job_titles)
        
        data_to_analyze = data_filterer.standardize_occ_title_format(relevant_data=data_to_analyze)
        
        return data_to_analyze
    



