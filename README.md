# fanfiction-analysis-seminar
Code, tools and data used when writing the seminar paper in the "Trends in the 21th Century Literary Theory" course at BGU

##### A list of significant files and their purposes:  
split_csv_to_txts.py - used to split the original AO3scraper CSV output file that contained all of the metadata along with the body of the fanfictions themselves into txt files that only contain the body of each fanfiction

replace_in_files.rb - used to remove some special characters from the individual fanfiction txt files

remove_body.py - used to remove the body column from the output of the AO3scraper tool  to create the work_ids_and_metadata.csv file
 
topicModelingToolConsoleOutput.txt - console output of the last run of the TopicModelingTool on my data

work_ids_and_links.csv - this file contains the relation of each fanfiction's work ID in AO3 to a link that leads to it on AO3

work_ids_and_metadata.csv - this file contains the metadata related to each work ID without the body (the fanfiction's actual text)

the output_csv directory and its contents - the CSV output of the TopicModelingTool tool
