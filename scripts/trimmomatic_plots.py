#!/usr/bin/env python


import matplotlib.pyplot as plt

both_dict_R1 = {}
mbnl_dict_R1 = {}

both_dict_R2 = {}
mbnl_dict_R2 = {}


# with open("/projects/bgmp/leylacuf/bioinfo/Bi623/QAA/trimmomatic_output/new_distribution_both_R1.trimmed.tsv", 'r') as fh1:
#     for line in fh1:
#         line = line.strip("\n").split('\t')
#         counts_R1 = int(line[0])
#         length_R1 = int(line[1])
#         both_dict_R1[length_R1] = counts_R1

# # for key, value in both_dict_R1.items():
# #     print(type(key), type(value))
# # for keys, values in both_dict_R1.items():
# #     print(keys, values)

# with open("/projects/bgmp/leylacuf/bioinfo/Bi623/QAA/trimmomatic_output/new_distribution_mbnl_R2.trimmed.tsv", 'r') as fh2:
#     for line in fh2:
#         line = line.strip("\n").split('\t')
        
#         counts_R2 = int(line[0])
#         length_R2 = int(line[1])
#         both_dict_R2[length_R2] = counts_R2


with open("/projects/bgmp/leylacuf/bioinfo/Bi623/QAA/trimmomatic_output/new_distribution_mbnl_R1.trimmed.tsv", 'r') as fh1:
    for line in fh1:
        line = line.strip("\n").split('\t')
        counts_R1 = int(line[0])
        length_R1 = int(line[1])
        mbnl_dict_R1[length_R1] = counts_R1


with open("/projects/bgmp/leylacuf/bioinfo/Bi623/QAA/trimmomatic_output/new_distribution_mbnl_R2.trimmed.tsv", 'r') as fh2:
    for line in fh2:
        line = line.strip("\n").split('\t')
        
        counts_R2 = int(line[0])
        length_R2 = int(line[1])
        mbnl_dict_R2[length_R2] = counts_R2



# plt.bar(both_dict_R1.keys(), both_dict_R1.values(), alpha = 1, label = 'Forward Read (R1)', color = "#D35400")
# plt.bar(both_dict_R2.keys(), both_dict_R2.values(), alpha = 0.6, label = 'Reverse Read (R2)', color = "#6C3483")
# plt.yscale('log')
# plt.title("both")
# plt.xlabel("Read Length in bps")
# plt.ylabel("log10 of Read Counts")
# plt.legend(loc='upper left')
# plt.savefig("read_len_dist_both")


plt.bar(mbnl_dict_R1.keys(), mbnl_dict_R1.values(), alpha = 0.7, label = 'Forward Read (R1)', color = "#D35400")
plt.bar(mbnl_dict_R2.keys(), mbnl_dict_R2.values(), alpha = 0.6, label = 'Reverse Read (R2)', color = "#6C3483")
plt.yscale('log')
plt.title("mbnl")
plt.xlabel("Read Length in bps")
plt.ylabel("log10 of Read Counts")
plt.legend(loc='upper left')
plt.savefig("read_len_dist_mbnl")