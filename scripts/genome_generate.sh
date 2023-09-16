#!/usr/bin/bash
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=compute               #REQUIRED: which partition to use
#SBATCH --mail-user=leylacuf@uoregon.edu     #optional: if you'd like email
#SBATCH --mail-type=ALL                   #optional: must set email first, what type of email you want
#SBATCH --cpus-per-task=8                 #optional: number of cpus, default is 1
#SBATCH --mem=32GB                        #optional: amount of memory, default is 4GB
#SBATCH --error=genome_gen.err          ### File in which to store job error messages
#SBATCH --output=genome_gen.out         ### File in which to store job output

conda activate bgmp-QAA

/usr/bin/time -v STAR \
    --runThreadN 8 \
    --runMode genomeGenerate \
    --genomeDir /projects/bgmp/leylacuf/bioinfo/Bi623/QAA/mus_musc_files/STAR_output \
    --genomeFastaFiles /projects/bgmp/leylacuf/bioinfo/Bi623/QAA/mus_musc_files/Mus_musculus.GRCm39.dna.primary_assembly.fa \
    --sjdbGTFfile /projects/bgmp/leylacuf/bioinfo/Bi623/QAA/mus_musc_files/Mus_musculus.GRCm39.110.gtf