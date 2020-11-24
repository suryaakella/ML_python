import pandas as pd
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/molecular-biology/promoter-gene-sequences/promoters.data'
names = ['class','id','sequence']
df = pd.read_csv(url, names = names)
print(df.shape)
