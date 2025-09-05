# Writes a list of dummy variables into a txt; calculates avg & plots all values
# The vlaues are hard-coded for now
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
import os
random.seed(123)

pyfile_path = os.path.dirname(os.path.abspath(__file__))
txtfile_path = os.path.join(pyfile_path,"values.txt")

# Write 10 random numeric values into a txt file
with open(txtfile_path, 'w') as f:
    vals = [round(random.uniform(20,38),2) for _ in range(10)]
    f.writelines([(str(val)+"\n") for val in vals])
    
# Read txt file & convert each value into float dtype
with open(txtfile_path, 'r') as f:
    value_list = [(x.strip("\n")) for x in f.readlines() ]
    value_list = [float(x) for x in value_list ]

# Display the value list:
print(f"The txt file contains below values:\n {value_list}")

# Average calculation
avg = round(sum(value_list)/len(value_list),2)

print(f"Average is: {avg}")

sns.lineplot(value_list, marker="o")
plt.axhline(y=avg, linestyle='--', label=f'average:{avg}', color='orange')
plt.legend()
plt.show()
