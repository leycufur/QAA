#!/usr/bin/env python

# dir = "/projects/bgmp/shared/2017_sequencing/"

##### LOOK AT PS4 PART1 #####
import bioinfo
import argparse
import gzip
import matplotlib.pyplot as plt


# from tabulate import tabulate
# read1 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz"
# read2 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz"
# index1 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz"
# index2 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz"

# table = [['File name', 'Label'], 
#          [read1, 'read1'], 
#          [read2, 'read2'], 
#          [index1, 'index1'],
#          [index2, 'index2']]

# print(tabulate(table))
parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, help="Your file name", required=True)
parser.add_argument('-l', type=int, help="Read length of base pairs in your file", required=True) #length can be determined on the command line using zcat filename | head -2 | grep -v "^@" | wc -L
parser.add_argument('-o', type=str, help="Your outfile name", required=True) #length can be determined on the command line using zcat filename | head -2 | grep -v "^@" | wc -L

args = parser.parse_args()

filename = args.f
read_length = args.l
outfile = args.o

# This was taken from ps4; we are still working with 101 bps so I can leave the value of 101 in there for the reads but will need to update for indexes
def init_list(lst: list, value: float=0.0) -> list:
    '''This function takes an empty list and will populate it with
    the value passed in "value". If no value is passed, initializes list
    with 101 values of 0.0.'''
    i = 0
    while i <=read_length:
        lst.append(value)
        i+=1
    return lst
my_list: list = []
my_list = init_list(my_list)


# This was taken from ps4
file = filename     #do NOT change this path - move your file to this location
#file = "test.fastq"            #when testing, uncomment this line to use the smaller test file
                                 #BE SURE TO SWITCH BACK BEFORE RUNNING JUST BEFORE SUBMISSION

def populate_list(file:str) -> tuple[list, int]:
    '''Creates and empty list using init_list(), opens Fastq file, loops through every individual sequence record
    and converts the phred score to a number, then adds the qual scores to an cumulative sum in the list, keeps track of
    total number of lines in the file, and returns the list and number of lines as a tuple.'''
    
    num_lines = 0 #Initialize line counter
    # my_list: list = []
    # my_list = init_list(my_list)
    
    with gzip.open(file, "rt") as fastq: #open fastq file
        for line in fastq: #iterate over each line in the file
            num_lines += 1 #increment the line counter
            
            if num_lines%4==0: #use only the 4th line of the record that contains quality scores
                phred_scores = line.strip() #strip whitespaces,  new lines, etc.
                for i, phred in enumerate(phred_scores): #iterate over each quality score character
                    my_list[i] += bioinfo.convert_phred(phred) #convert quality scores to phred scores and add the quality scores to my_list
                    
    return my_list, num_lines # return list of quality scores (my_list) and line count (num_lines)

my_list, num_lines = populate_list(file)
# print(my_list)
# print(num_lines)


for i, value in enumerate(my_list):
    mean_list = value/(num_lines/4)
    my_list[i]=mean_list

# def mean_quality_scores(my_list, num_lines):
#     "This function"
#     for mean_score, value in enumerate(my_list):
#         my_list[mean_score] = value/num_lines
#     return my_list
print(my_list)



plt.bar(range(len(my_list)),my_list)
plt.ylabel("Mean quality score per position")
plt.xlabel("Base position")
plt.title("Mean Quality Scores")
plt.savefig(f'{outfile}')
