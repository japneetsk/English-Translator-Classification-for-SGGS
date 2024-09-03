import os.path
from os import path
import pandas as pd
import math

########################################################################################################################################
# Function to read CSV file, obtain relevant columns, convert to dataframe and save back as 1 CSV file

def readcsvtodf(fullpath, directory, csvfilenum):
    
    # provide list of headers in data
    header_list = ['id', 
                   'sttm_id', 
                   'writer', 
                   'section', 
                   'subsection', 
                   'lines_id',
                   'lines_source_page', 
                   'lines_source_line', 
                   'lines_pronunciation',
                   'lines_pronunciation_information', 
                   'lines_type',
                   'lines_gurmukhi_SGPC', 
                   'lines_translations_language',
                   'lines_translations_english_writer', 
                   'lines_translations_english',
                   'lines_translations_punjabi_Bhai_Manmohan_Singh', #Bhai Manmohan Singh Translation
                   'lines_translations_punjabi_Fareedkot_Teeka', # Fareedkot Teeka Translation
                   'lines_translations_punjabi_Fareedkot_Teeka_additional_information_reference',
                   'lines_translations_punjabi_Prof_Sahib_Singh', # Prof. Sahib Singh Translation in Punjabi
                   'lines_translations_punjabi_Prof_Sahib_Singh_additional_information__arth',
                   'lines_translations_punjabi_Prof_Sahib_Singh_additional_information__note',
                   'lines_translations_spanish_SikhNet']
        
    # read csv file to pandas dataframe
    data = pd.read_csv(fullpath,names=header_list, sep=',', dtype=object, error_bad_lines=True)
    
    # keep only those rows where the english translations/strings are found
    search_values = ['Dr. Sant Singh Khalsa','Bhai Manmohan Singh']
    newdata = data[data.lines_translations_english_writer.str.contains('|'.join(search_values), na=False)]
    
    # subset for following columns: writer, lines_translations_english_writer, lines_translations_english, lines_type
    column_names = ["writer","lines_translations_english_writer","lines_translations_english","lines_type"]
    subsetdata = newdata[column_names]
    
    # Fill NaN values with previous values for all rows
    subsetdata.fillna(method='ffill', inplace=True)
    
    # Assign path for where data file will be saved
    dfpath = directory + "\\" + 'datadf.csv'
    
    # create empty dataframe with only headers
    column_names = ["writer","lines_translations_english_writer","lines_translations_english","lines_type"]
    emptydf = pd.DataFrame(columns = column_names)
    
    # if file doesn't exist, then first create an empty csv file with only headers. then, append the data to the csv file
    if path.exists(dfpath) == False:
        emptydf.to_csv(dfpath, mode='w', header=True)
        print("Created data.df.csv with headers only.")
        subsetdata.to_csv(dfpath, mode='a', header=False)
        print('Appended %s.csv successfully.' % csvfilenum)
    else:
        subsetdata.to_csv(dfpath, mode='a', header=False)
        print('Appended %s.csv successfully.' % csvfilenum)



########################################################################################################################################

# Read Files from directory and process them into refined dataset saved in 1 single file 

directory = r'csv_output_files'
cnt = 1
while cnt < 1431 :
    strcnt = str(cnt)
    csvfilenum = strcnt.rjust(4,"0")
    fullpath = directory + "\\" + csvfilenum +'.csv'
    if path.exists(fullpath) == False:
        print("Does not exist: "+ strcnt)
    else:
        readcsvtodf(fullpath, directory, csvfilenum)
    cnt += 1

############################


