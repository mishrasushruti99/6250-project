import subprocess
import shlex

var_1 = "training/training_vM6.py"
var_2 = "../../mimicdata/mimic3/disch_summary_readmission_labels.csv"
var_3 = "../../mimicdata/mimic3/vocab.csv"
var_4 = "conv_encoder"
var_5 = "5"
var_6 = "--desc"
var_7 = "new_vocab_02_1_wts"
var_8 = "--embed-dropout-bool"
var_9 = "True"
var_10 = "--embed-dropout-p"
var_11 = "0.3"
var_12 = "--bce-weights"
var_13 = "0.2,1"
var_14 = "--batch-size"
var_15 = "50"
var_16 = "--kernel-sizes"
var_17 = "3,5"
var_18 = "--num-filter-maps"
var_19 = "100"
var_20 = "--fc-dropout-p"
var_21 = "0.5"
var_22 = "--embed-file"
var_23 = "../../mimicdata/mimic3/processed_full.embed"
subprocess.call(shlex.split('./train_v2.sh training/training_vM7.py ../../../Data/dis_sum_train.csv ../../../Data/vocab.csv conv_encoder 5 --embed-dropout-bool True --embed-dropout-p 0.3 --bce-weights 0.2,1 --batch-size 50 --kernel-sizes 3,5 --num-filter-maps 100 --fc-dropout-p 0.5 --embed-file ../../../Data/processed_full.embed'))
