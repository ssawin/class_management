import csv
import re


comment_character = '%'



def is_comment(row):
    """Checks if a line of the csv-file is a comment line"""
    match_comment = re.compile('^'+comment_character)
    if match_comment.match(row[0].strip()):
        return True
    else:
        return False
 
def is_immediate(row):
    """Checks if a line of the csv file is an immediate preamble line"""
    return row[1].strip()=='=='

def is_preamble(row):
    """Checks of a line of the csv file is a non-immediate preamble line"""
    return row[1].strip()=='=' 


with open('test.csv','rU') as csvfile:
    reader  = csv.reader(csvfile)  # reads the csv file into a list line by line
    header = [] 
    # the preamble processing will end by producing the header list
    for  row in reader:
        if is_comment(row):
            print("there is a comment on line "+repr(int(reader.line_num)))
        elif is_immediate(row):
            print("there is an immediate assignment line "+repr(int(reader.line_num)))
        elif is_preamble(row):
            print("there is a regular preamble assignment line "+repr(int(reader.line_num)))
        else:
            header=row
            break
    if header:
        print("the header is on  line "+repr(int(reader.line_num)))
    else:
        print("funny, there is no header!")

    
        
            
