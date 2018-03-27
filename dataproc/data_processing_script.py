import sys
import datasets
from learn import models
import log_reg
from dataproc import extract_wvs
from dataproc import get_discharge_summaries
from dataproc import concat_and_split
from dataproc import build_vocab
from dataproc import vocab_index_descriptions
from dataproc import word_embeddings
from constants import MIMIC_3_DIR, DATA_DIR

import numpy as np
import pandas as pd

from collections import Counter, defaultdict
import csv
import math
import operator

sys.path.append('../')

#################################
#Order of scripts:
# 1. get_discharge_summaries
# 2. build_vocab
# 3. word_embeddings
# 4. extract_wvs

if __name__ == "__main__":

    #Defining variables
    Y = 'full' #use all available labels in the dataset for prediction
    notes_file = '%s/NOTEEVENTS_2000.csv' % MIMIC_3_DIR # raw note events downloaded from MIMIC-III
    vocab_size = 'full' #don't limit the vocab size to a specific number
    vocab_min = 3 #discard tokens appearing in fewer than this many documents

    #This reads all notes, selects only the discharge summaries, and tokenizes them, returning the output filename
    disch_full_file = get_discharge_summaries.write_discharge_summaries(out_file="%s/disch_full.csv" % MIMIC_3_DIR)

    df = pd.read_csv('%s/disch_full.csv' % MIMIC_3_DIR)

    #Let's sort by SUBJECT_ID and HADM_ID to make a correspondence with the MIMIC-3 label file
    df = df.sort_values(['SUBJECT_ID', 'HADM_ID'])

    sorted_file = '%s/disch_full.csv' % MIMIC_3_DIR
    df.to_csv(sorted_file, index=False)

    #Build vocab from training data
    vname = '%s/vocab.csv' % MIMIC_3_DIR
    infile = '%s/disch_full.csv' % MIMIC_3_DIR
    build_vocab.build_vocab(vocab_min, infile, vname)


    #Pre-train word embeddings - train word embeddings on all words
    w2v_file = word_embeddings.word_embeddings('full', '%s/disch_full.csv' % MIMIC_3_DIR, 100, 0, 5)

    #Write pre-trained word embeddings with new vocab
    extract_wvs.gensim_to_embeddings('%s/processed_full.w2v' % MIMIC_3_DIR, '%s/vocab.csv' % MIMIC_3_DIR, Y)



