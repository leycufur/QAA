#!/usr/bin/bash
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=compute               #REQUIRED: which partition to use
#SBATCH --mail-user=leylacuf@uoregon.edu     #optional: if you'd like email
#SBATCH --mail-type=ALL                   #optional: must set email first, what type of email you want
#SBATCH --cpus-per-task=8                 #optional: number of cpus, default is 1
#SBATCH --mem=32GB                        #optional: amount of memory, default is 4GB
#SBATCH --error=htseq.err          ### File in which to store job error messages
#SBATCH --output=htseq.out         ### File in which to store job output


#Be sure to use the queuing system and request 8 cores on 1 node

conda activate bgmp-QAA
/usr/bin/time -v htseq-count \
    --stranded=reverse \
    /projects/bgmp/leylacuf/bioinfo/Bi623/QAA/mus_musc_files/STAR_output/both_trimmed_Aligned.out.sam \
    /projects/bgmp/leylacuf/bioinfo/Bi623/QAA/mus_musc_files/Mus_musculus.GRCm39.110.gtf > htseq_both_reverse.txt
