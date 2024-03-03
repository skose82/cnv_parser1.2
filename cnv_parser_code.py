CNV_Parser_v1.2_raw_code

#Pandas dataframe script to search for CNVs in any gene. Can now concatenate and search through 200 samples at a time.

import numpy as np
#import pyranges as pr
import os
import pandas as pd
import glob

path = r'/path/'

all_files = glob.glob(os.path.join(path , "*.bed"))
list = []
for filename in all_files:
   df = pd.read_csv(filename, encoding='ISO-8859-1', sep='\t', header=None)
   list.append(df)

concat_df = pd.concat(list, axis=0, ignore_index=True)

# If you want to check index positions / 0 is row and , next is column. 
print(str(concat_df.iloc[0, 16]) + " " + str(concat_df.iloc[0, 4],) + " " + str(concat_df.iloc[0,15]) + " " + str(concat_df.iloc[0,9]))

gene_df = concat_df[concat_df.eq("gene").any(1)]

gene_df.to_csv('200_gene.csv', index=False)
