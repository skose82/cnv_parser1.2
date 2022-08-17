CNV_Parser_v1.2_raw_code

#Pandas dataframe script to search for CNVs in any gene. Can now concatenate and search through 200 samples at a time.

import numpy as np
#import pyranges as pr
import os
import pandas as pd
import glob

path = r'/Users/adminskose/Desktop/CNV_COHORT/Intersected/200'

all_files = glob.glob(os.path.join(path , "*.bed"))
list = []
for filename in all_files:
   df = pd.read_csv(filename, encoding='ISO-8859-1', sep='\t', header=None)
   list.append(df)

concat_df = pd.concat(list, axis=0, ignore_index=True)

# If you want to check index positions / 0 is row and , next is column. 
print(str(concat_df.iloc[0, 16]) + " " + str(concat_df.iloc[0, 4],) + " " + str(concat_df.iloc[0,15]) + " " + str(concat_df.iloc[0,9]))

DIS3L2_df = concat_df[concat_df.eq("DIS3L2").any(1)]

DIS3L2_df.to_csv('200_DIS3L2_w_sanity_cnv_parser_check.csv', index=False)
