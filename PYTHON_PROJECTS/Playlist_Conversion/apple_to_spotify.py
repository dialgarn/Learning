import pandas as pd

# create universal pathing so it doesnt matter where people install program
# make it user friendly with nice UI

data = pd.read_csv('my greatest work of art.txt', sep="   ", header=None, engine='python')

print(data)
