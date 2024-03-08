import pandas as pd
import numpy as np
from gensim.models import KeyedVectors
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords   

class JobCodeIdentifier:
    """
    Class designed to identify relevant job codes in our dataset

    Attributes:
        data_all_years (pd.DataFrame): DF containing read and processed data from all relevant years
        job_code_text_corpus (list): text corpus used to identify relevant job titles - we will assess each job title's similarity to the corpus
        model_loc (str): location of Word2Vec model that will calculate similarity btwn job titles and text corpus

    Methods:
        tokenize_text_corpus: tokenizes the text corpus, allowing for comparison to occupation titles
        identify_relevant_job_codes: uses Word2Vec model to compare occupation titles to text corpus and identify most relevant titles
        calculate_similarity: calculates similarity of an individual occupation title to the text corpus

    """
    def __init__(self, data_all_years:pd.DataFrame, job_code_text_corpus:list, model_loc:str, relevance_threshold:float) :
        """
        Initializes instance of JobCodeIdentifier class

        Parameters:
            data_all_years (pd.DataFrame): DF containing read and processed data from all relevant years
            job_code_text_corpus (list): text corpus that will be used to identify relevant job titles - we will assess each job title's similarity to the corpus
            model_loc (str): location of Word2Vec model that will calculate similarity btwn job titles and text corpus
            relevance_threshold (float): threshold to identify relevant job codes - those with similarity rating higher than this are deemed relevant
        """
        self.data_all_years = data_all_years
        self.job_code_text_corpus = job_code_text_corpus
        self.model_loc = model_loc
        self.relevance_threshold = relevance_threshold
        
    def tokenize_text_corpus(self, text_corpus):
        """
        Tokenizes text corpus, makes lowercase, removes stopwords and non-alphanumerics

        Parameters:
            self
        Returns:
            tokenized_text_corpus (list): tokenized version of the text corpus
        """
        # load stop words
        stop_words = set(stopwords.words('english'))

        tokenized_text_corpus = [word for word in word_tokenize(text_corpus.lower()) if word.isalpha() and word not in stop_words] 
        return tokenized_text_corpus
    
    def identify_relevant_job_codes(self, data_all_years:pd.DataFrame, text_corpus:str, model_loc:str, relevance_threshold:float):
        """
        Given a list of keywords describing occupations we're interested in, identifies relevant occupation titles in the data
        
        Parameters:
            data_all_years (pd.DataFrame): DF with data from all years - returned from read_and_process_files
            text_corpus (list): tokenized list of keywords describing occupations we're interested in
            model_loc (str): filepath of pre-trained Word2Vec model
            relevance_threshold (float): threshold to identify relevant job codes - those with similarity rating higher than this are deemed relevant
        Returns:
            relevant_titles (list): list of occupation titles relevant to the analysis
        """
        # load Word2Vec model
        model = KeyedVectors.load_word2vec_format(model_loc, binary=True)

        occupation_titles = data_all_years["OCC_TITLE"].unique().tolist()

        # load stop words
        stop_words = set(stopwords.words('english'))
        # tokenize occupation titles and remove stop words
        tokenized_titles = [
            [word for word in word_tokenize(title.lower()) if word.isalnum() and word not in stop_words] 
            for title in occupation_titles
            ]
        
        tokenized_text_corpus = self.tokenize_text_corpus(text_corpus=text_corpus)

        # calculate similarity to keywords for each occupation title  
        similarities = [self.calculate_similarity(model=model, occupation_title=title, text_corpus=tokenized_text_corpus) for title in tokenized_titles]
        
        similarities_to_compare = [np.max(similarity) for similarity in similarities]

        # select titles with similarities above the threshold
        relevant_titles = [title for title, similarity in zip(occupation_titles, similarities_to_compare) if similarity > relevance_threshold]
        return relevant_titles

    def calculate_similarity(self, model, occupation_title:str, text_corpus:list):
        """
        Uses Word2Vec model to calculate the similarity of an individual occupation title to the text corpus
        
            Parameters: 
                model (model): Word2Vec model
                occupation_title (str): title of an individual occupation
                text_corpus (list): list of keywords describing occupations we're interested in
            Returns:
                similarity_metric (float): measurement of similarity of the occupation title to the text corpus
        """

        try:
            # calculate the similarity between each word in the occupation title and every word in the corpus
            similarities = [model.similarity(occupation_title, keyword.lower()) for keyword in text_corpus]
            # calculate HOW similar (quantified) is each word in the occupation title to its most similar word in the corpus?
            similarity_metric = np.max(similarities)
        except KeyError:
            similarity_metric = 0 # Handle the case where a word is not in the vocabulary

        return similarity_metric