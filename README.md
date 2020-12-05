# fanfiction-analysis-seminar
Code, tools and data used when writing the seminar paper in the "Trends in the 21th Century Literary Theory" course at BGU

##### Scraper used in order to retrieve fanfiction works from AO3 (Archive of Our Own - https://archiveofourown.org/):
Li, Jingyi et al. AO3Scraper. 21 Sep. 2020. Software. GitHub, https://github.com/radiolarian/AO3Scraper

##### The analysis was done using "MALLET: A Machine Learning for Language Toolkit." in conjunction with the TopicModelingTool interface:
McCallum, Andrew Kachites. "MALLET: A Machine Learning for Language Toolkit.". 2.0.8, 2018. Software. UMass Amherst, http://mallet.cs.umass.edu
Enderle, Jonathan Scott et al.Topic Modeling Tool. v1.0.0, 24 Nov. 2019. Software. GitHub, https://github.com/senderle/topic-modeling-tool

##### A list of significant files and their purposes:  
split_csv_to_txts.py - used to split the original AO3scraper CSV output file that contained all of the metadata along with the body of the fanfictions themselves into txt files that only contain the body of each fanfiction

replace_in_files.rb - used to remove some special characters from the individual fanfiction txt files

remove_body.py - used to remove the body column from the output of the AO3scraper tool  to create the work_ids_and_metadata.csv file
 
topicModelingToolConsoleOutput.txt - console output of the last run of the TopicModelingTool on my data

work_ids_and_links.csv - this file contains the relation of each fanfiction's work ID in AO3 to a link that leads to it on AO3

work_ids_and_metadata.csv - this file contains the metadata related to each work ID without the body (the fanfiction's actual text)

output_csv directory and its contents - the CSV files outputed by using MALLET with the TopicModelingTool interface
