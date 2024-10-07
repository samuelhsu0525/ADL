import pandas as pd
import sys
# Read data from the source CSV file
submit_file = "predict.csv"
data = pd.read_csv(submit_file)

dest_file = sys.argv[1]
data.to_csv(dest_file, index=False)