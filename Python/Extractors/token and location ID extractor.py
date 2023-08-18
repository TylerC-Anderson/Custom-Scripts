# Token and Location ID extractor

"""
PURPOSE: This program accepts a text file with a list of names and marketing sources.
The names and marketing sources are provided as a URL, and extracting them 
manually via copy-paste is tedious and time consuming. Essentially is a more
robust version of the Marketing Source Extractor, as it needed to extract
based on 2 symbols instead of just one.

USAGE: Currently accepts .txt only.
"""

from pathlib import Path

# accepts filepath as input to open .txt file for processing
print("Welcome! I'm happy to be here to extract a file for you.")
print("Please ensure input.txt has the correct input AND that any")
print("past results in output.txt have been saved elsewhere.")
input("Then hit enter to continue.")

#TODO Add file handling for multiple file extensions. Perhaps make it extension-
#     agnostic for ease of use
path_to_input = Path(__file__).parent.parents[0].resolve() / 'Inputs' / 'input.txt'

# intializing empty variables to be used later
locationid = ''
token = ''
results_list = []

desired_props = []

def main():

    print("Please enter in the property names you would like to search, or hit enter to search all in document. Type a 0 to end the list of properties.")

    props_prompt = input()

    if len(props_prompt) == 0:
        pass
    else:
        props_prompt = props_prompt.title().strip()
        desired_props.append(props_prompt)
        while props_prompt != '0':
            props_prompt = input().title().strip()
            desired_props.append(props_prompt)

    with path_to_input.open(mode='r', encoding='utf-8') as props_file:
        print('Thank you. Processing...')

        results_list.extend(word_sep(props_file, desired_props))

        ## for testing
        # print(results_list)

        # prep for output file path
        path_to_output = Path(__file__).parent.parents[0].resolve() /  'Outputs' / 'output.txt'

        # then write the results to the designated output path in the following format:
        #     Property Name: [name]
        #     LocationID: [ID]
        #     Token: [Token]

        with path_to_output.open(mode='w', encoding='utf-8') as outputs:
            for result in results_list:
                outputs.write(f"Property name: {result[0]}\nLocationID: {result[1]}\nToken: {result[2]}\n\n")

    # print exit message and end program after user input
    input("Done. Hope I did well! Press Enter key to exit :)")


def word_sep(file_to_search, props_list=[]):
    
    results = []
    if props_list:
        props_list.remove('0')

    # # for testing
    # print(props_list)

    if props_list:
        
        for lines in file_to_search:
            
            for prop in props_list:

                if prop.lower() in lines.lower():

                    ## for testing
                    print(prop)
                    print(lines)

                # first split the line we are reading into individual words
                    line_as_list = lines.split()

                    # initializing the prop name to empty
                    prop_name = ''
                    
                    # for each of the words in the line
                    for word in line_as_list:
                        
                        # if the word has http in it, we are going to split the URL at the
                        # equal signs first
                        if 'http'in word:
                            no_equals = word.split('=')

                            # now go through each substring in the result of the split and where
                            # we find the &, split again and get the first result after the split
                            # which will be the location ID
                            for substring in no_equals:
                                if '&' in substring:
                                    locationid = substring.split('&')[0]
                            
                            # finally, we know the token is the last thing in the list resulting from
                            # the split at the ='s so we store that as the token
                            token = no_equals[-1]
                        else:

                            #if the word does not have http then it is the prop name and
                            # we can store that as such
                            prop_name += f'{word} '
                    # put the results of the above into the results_list and repeat until done
                    prop_name.title()
                    results.append([prop_name, locationid, token])
    else:
        for lines in file_to_search:
            # first split the line we are reading into individual words
            line_as_list = lines.split()

            # initializing the prop name to empty
            prop_name = ''

            #TODO Perhaps turn the below into a module that the script can call.
            #     Would help with allowing the user to input arbitrary symbols
            #     they need the script to separate by.

            # for each of the words in the line
            for word in line_as_list:
                
                # if the word has http in it, we are going to split the URL at the
                # equal signs first
                if 'http'in word:
                    no_equals = word.split('=')

                    # now go through each substring in the result of the split and where
                    # we find the &, split again and get the first result after the split
                    # which will be the location ID
                    for substring in no_equals:
                        if '&' in substring:
                            locationid = substring.split('&')[0]
                    
                    # finally, we know the token is the last thing in the list resulting from
                    # the split at the ='s so we store that as the token
                    token = no_equals[-1]
                else:

                    #if the word does not have http then it is the prop name and
                    # we can store that as such
                    prop_name += f'{word} '
            
            # put the results of the above into the results_list and repeat until done
            prop_name.title()
            results.append([prop_name, locationid, token])
    
    return results
    

main()
