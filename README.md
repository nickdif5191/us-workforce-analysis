# us-workforce-analysis
PROJECT DESCRIPTION:
This tool is designed to enable industry/company level analysis of occupational employment and wage statistics released each year by the Bureau of Labor Statistics.

The raw data, dating back to 2001 in its current format, included stats for over 850 occupation titles in 2022, ranging from Floral Designers to Astronomers to Rail Car Repairers. Due to its comprehensive nature, performing analysis on trends that are relevant for a specific industry and/or company can be quite challenging. 

Rather than manually selecting relevant occupation titles, this model uses Natural Language Processing (NLP) methods to automatically identify jobs that are relevant to an industry, and returns all relevant data. Users simply input a text corpus that describes the industry and/or company they are interested in (along with an optional list of states they are interested in), and the model (using NLP methods from a previously-trained Word2Vec model) outputs a filtered dataset with employment and wage statistics from 2001-2022. 

While there are many potential use cases, company HR/Recruiting departments may find the tool particularly useful. Inputting a specifically-crafted text corpus that describes the positions, requirements, and characteristics of ideal candidates would enable analysis of trends in labor pools they may be looking to pull from. Even more easily, departments could simply paste in the whole of text from their company's website or Wiki page, assuming this text is representative of company operations and job functions. 

IMPORTANT FUNCTIONALITY NOTE: 
The Word2Vec model used in this model is too large to be uploaded to GitHub. Users can download the model at https://www.kaggle.com/datasets/leadbest/googlenewsvectorsnegative300 (~3.6 GB) and move to 'Scripts' folder to be able to properly use the tool.

ANALYSIS WITH TABLEAU:
The model as posted here is currently configured to perform analysis on the "Light Industrial Manufacturing" industry. An associated packaged Tableau workbook with results is posted. If you would like to run the model for your own industry and examine results in Tableau, use the "Results.twb" file and use the output specific to your industry.
