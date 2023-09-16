#!/usr/bin/bash
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=compute               #REQUIRED: which partition to use
#SBATCH --mail-user=leylacuf@uoregon.edu     #optional: if you'd like email
#SBATCH --mail-type=ALL                   #optional: must set email first, what type of email you want
#SBATCH --cpus-per-task=8                 #optional: number of cpus, default is 1
#SBATCH --mem=32GB                        #optional: amount of memory, default is 4GB
#SBATCH --error=align.err          ### File in which to store job error messages
#SBATCH --output=align.out         ### File in which to store job output


#Be sure to use the queuing system and request 8 cores on 1 node

conda activate bgmp-QAA

/usr/bin/time -v STAR --runThreadN 8 --runMode alignReads \
    --outFilterMultimapNmax 3 \
    --outSAMunmapped Within KeepPairs \
    --alignIntronMax 1000000 --alignMatesGapMax 1000000 \
    --readFilesCommand zcat \
    --readFilesIn /projects/bgmp/leylacuf/bioinfo/Bi623/QAA/trimmomatic_output/mbnl_R1.trimmed.fastq.gz /projects/bgmp/leylacuf/bioinfo/Bi623/QAA/trimmomatic_output/mbnl_R2.trimmed.fastq.gz \
    --genomeDir /projects/bgmp/leylacuf/bioinfo/Bi623/QAA/mus_musc_files/STAR_output \
    --outFileNamePrefix mbnl_trimmed_