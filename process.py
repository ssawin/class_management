import csv
import re


comment_character = '%'
python_character='#'
escape_character='\\'
file='/Users/ssawin/Documents/python/class_management/test.csv'


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



def build_data(file):
    """reads a csv file and produces data, a list of dictionaries and globals, a dictionary"""
    with open(file,'rU') as csvfile:
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

    


class Field:

    def __init__(self):
        self.errors = []


    def pass_through_dquotes(self,text,i):
        """i is the index with the string text, and is currently pointing at an open double quote.
        This cycles through to the next occurence of an unescaped double quote, returning the index of
        that point.  If none is reached returns appropriate syntax error."""
        j=i+1
        while j<len(text) and text[j]!='"':
            if text[j] == escape_character:
                j=j+2
            else:
                j=j+1
        if j == len(text):
            return (j,"No matching double quote for quote at index "+repr(i)+" of '"+text+"'")
        else: 
            return (j,None)

    def pass_through_squotes(self,text,i):
        """i is the index with the string text, and is currently pointing at an open double quote.
        This cycles through to the next occurence of an unescaped double quote, returning the index of
        that point.  If none is reached returns appropriate syntax error."""
        j=i+1
        while j<len(text) and text[j]!='"':
            if text[j] == escape_character:
                j=j+2
            else:
                j=j+1
        if j == len(text):
            return (j,"No matching single quote for quote at index "+repr(i)+" of '"+text+"'")
        else: 
            return (j,None)


    def pass_through_python(self,text,i):
        """i is the index with the string text, and is currently pointing at a python character.
        This cycles through to the next occurence of an unescaped python character, skipping all text inside double or single quotes,
        returning the index of that point.  If none is reached returns appropriate syntax error."""
        j=i+1
        error=None
        while j<len(text) and text[j]!=python_character:
            if text[j] == escape_character:
                j=j+1
            elif text[j] == '"':
                (j,error)=pass_through_dquotes(text,j)
            elif text[j] == '"':
                (j,error)=pass_through_squotes(text,j)
            j=j+1
        if j == len(text):
            if error:
                return (j,error)
            else:
                return (j,"No ending for python code begun at index "+repr(i)+" of '"+text+"'")
        else: 
            return (j,None)


    def process_list_entry(self,text):
        """ breaks text up by semicolons.  semicolons which are between unescaped " or ' or
        unescaped python characters not inside quotes are ignored.  returns list of text
        pieces followed by error message unless text is entirely python code.  In that case returns
        text and error message."""
        temp=text.strip()
        if temp[0] == python_character and pass_through_python(temp,0)==(len(temp)-1,None):
            return (temp,None)
        else:
            list=[ ]
            while temp:
                j=0
                error = None
                while j<len(temp) and temp[j] != ';' and not(error):   # travel through looking for a semicolon
                    if temp[j]=='"':    #ignore all text from opening quote to closing quote
                        (j,error)=pass_through_dquotes(temp,j)
                    elif temp[j] == python_character:  #ignore all text from opening python character to closing python character
                        (j,error)=pass_through_python(temp,j)
                    j=j+1
                list.append(temp[:j])
                if j<len(temp)-1:
                    temp=temp[j+1:]
                else:
                    temp = None
        return (list,error)




