#!/usr/bin/env python

# file_path = "/projects/bgmp/leylacuf/bioinfo/Bi623/QAA/mus_musc_files/STAR_output/both_trimmed_Aligned.out.sam"

def is_mapped(flag):
    return (flag & 4) != 4

mapped_reads = 0
unmapped_reads = 0

with open("/projects/bgmp/leylacuf/bioinfo/Bi623/QAA/mus_musc_files/STAR_output/mbnl_trimmed_Aligned.out.sam", 'r') as samfile:
    for line in samfile:
        if line.startswith('@'): 
            continue

        fields = line.strip().split('\t')
        flag = int(fields[1])
        if (flag & 256) != 256:
            if is_mapped(flag):
                mapped_reads += 1
            else:
                unmapped_reads += 1
print(f'Mapped Reads:{mapped_reads}\nUnmapped Reads:{unmapped_reads}')