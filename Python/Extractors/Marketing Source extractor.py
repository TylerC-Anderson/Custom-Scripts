# Marketing Source Extractor

"""
PURPOSE: This program accepts a text file with a list of names and marketing sources.
The names and marketing sources are provided as a URL, and extracting them 
manually via copy-paste is tedious and time consuming.

USAGE: Currently accepts .txt only.
"""

from pathlib import Path

# Prints welcome message and accepts filepath to open input.txt file for
# processing

print("Welcome! I'm happy to be here to extract a file for you.")
print("Please ensure input.txt has the correct input AND that any")
print("past results in output.txt have been saved elsewhere.")
input("Then hit enter to continue.")

#TODO Add file handling for multiple file extensions. Perhaps make it extension-
#     agnostic for ease of use
path_to_input = Path(__file__).parent.resolve() / 'input.txt'

# intializing empty variables to be used later
results_list = []

with path_to_input.open(mode='r', encoding='utf-8') as sources_file:
    print('Thank you. Processing...')

    #TODO Add a way to accept user-input for an arbitrary number of symbols to
    #     separate from
    # with the filepath open we begin going line by line through the file
    for lines in sources_file:
        # first split the line we are reading into individual words
        line_as_list = lines.split(':')
        results_list.append(line_as_list[0])

    # prep for output file path
    path_to_output = Path(__file__).parent.resolve() / 'output.txt'

    with path_to_output.open(mode='w', encoding='utf-8') as outputs:
        outputs.write("Sources:\n\n")
        for result in results_list:
            outputs.write(f"{result}\n")

# print exit message and end program after enter key input
input("Done. Hope I did well! Press Enter key to exit :)")
