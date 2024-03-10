# us-workforce-analysis

This model is designed to enable industry/company level analysis of occupational employment and wage statistics released each year by the Bureau of Labor Statistics.

The raw data, dating back to 2001 in its current format, tracked employment and wage statistics for over 850 occupation titles in 2022. Due to its comprehensive nature, performing analysis on employment trends for a specific industry and/or company can be quite challenging. 

Rather than manually selecting relevant occupation titles, this model enables immediate identification of relevant jobs. Users simply input a text corpus that describes the industry and/or company they are interested in (along with an optional list of states they are interested in), and the model (using NLP techniques from a Word2Vec model) outputs a filtered dataset including employment and wage statistics from 2001-2022. 

While there are many potential use cases, one that sticks out is for company HR/Recruiting departments. Inputting a text corpus that describes the positions, requirements, and characteristics of ideal candidates would enable analysis of trends in labor pools they are looking to pull from. Even more simplistically, departments could simply paste in the whole of text from their company's website or Wiki page, assuming this text is representative of company operations and job functions. 

IMPORTANT FUNCTIONALITY NOTE: The Word2Vec model used in this model is too large to be uploaded to GitHub. Users can download the model (~3.6 GB) and move to 'Scripts' folder to be able to properly run the model.