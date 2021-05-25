import argparse
import csv
from os import path

# Defining optional arguments for number of audio channels, a list of sources, etc. --help will display all of these.
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--channels", type=int, choices=[2, 4, 8, 16], default=16, help="Number of audio channels. Choose 2, 4, 8, or 16.")
parser.add_argument("-l", "--list", default="sources.txt", help="Path or filename with list of sources.")
parser.add_argument("-o", "--output", default="shuffled_audio.csv", help="Path or filename of output CSV file.")
args = parser.parse_args()

# Pulls the desired number of audio channels from the added argument. If nothing is provided, it defaults to 16 channels.
channels = args.channels

# Initialize output list
output = []

# Function that runs if input file is detected as a list instead of a csv.
# It recurses through the sources list and appends the channel number to it.
def run_as_list(sources):
    for i in sources:
        for j in range(1, channels + 1):
            output.append([i + " " + "CH" + f"{j:02d}"])
    
    write_list(get_filename(), output)

# Function that runs if input file is detected as a csv instead of a list.
# Generates a list of dictionaries that will match the Ultrix database when output to a csv.
def run_as_dict(sources):
    fields = ["Name","Description","Video"]
    for f in range(1,channels+1):
        fields.append("Audio " + str(f))

    for i in sources:
        for j in range(1, channels + 1):
            temp = [i + " " + "CH" + f"{j:02d}"]
            temp.extend(["",""])
            for k in range(1,17):
                temp.append(sources[i] + ".audio.ch" + str(j))
            tempDict = dict(zip(fields,temp))
            output.append(tempDict)
    
    write_dict(get_filename(),output, fields)

# Function designed to output the list to a file.
def write_list(filename, list):
    with open(filename, 'w', newline='') as out:
        writer = csv.writer(out)
        writer.writerows(list)
    print("Output audio breakout list to '" + filename + "'")

# Function designed to generate csv that matches Ultrix database layout.
def write_dict(out_file, out_dict, fields):
    with open(out_file, 'w', newline='') as out:
        writer = csv.DictWriter(out, fieldnames = fields)
        writer.writeheader()
        writer.writerows(out_dict)
    print("Output audio breakout list to '" + out_file + "'")

# Function that checks if an output path or filename was provided. If not, uses default 'shuffled_audio.csv'.
def get_filename():
    out_file = args.output
    if out_file.split(".")[-1] != "csv":
            out_file += ".csv"
    
    return out_file


# Main function that attempts to parse an input list or csv.
# If it finds a path or filename, it uses it and attempts to process it.
# If it doesn't find a path or filename, it will attempt to use 'sources.txt', but will fail if it cannot find it.
try:
    sourceFile = args.list
    sources = {}
    with open(sourceFile, mode='r') as src:
        read = csv.reader(src)
        sources = {rows[0]:rows[1] for rows in read}
    run_as_dict(sources)

except:
    try:
        sources = []
        sourceFile = open(args.list, 'r')
        while True:
            line = sourceFile.readline()

            if not line:
                break
            sources.append(line.strip())
        sourceFile.close()
        run_as_list(sources)
    except:
        print("No input file specified and 'sources.txt' cannot be found.")
        quit()