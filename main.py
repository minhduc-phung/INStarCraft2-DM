import numpy as np
import pandas as pd

import os
for dirname, _, filenames in os.walk('.\data'):
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        print(filename)
        largest_column_count = 0

        with open(filepath, 'r') as temp_f:
            # Read the lines
            lines = temp_f.readlines()

            for l in lines:
                # Count the column count for the current line
                column_count = len(l.split(',')) + 1

                # Set the new most column count
                largest_column_count = column_count if largest_column_count < column_count else largest_column_count

        # Generate column names (will be 0, 1, 2, ..., largest_column_count - 1)
        column_names = [i for i in range(0, largest_column_count)]

        df = pd.read_csv(os.path.join(dirname, filename), header=None, names=column_names)
        # Print the first 5 rows of the dataframe.
        print(df.head(5))
