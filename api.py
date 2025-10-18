import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# prevents warnings about future implementations from appearing
import warnings
warnings.filterwarnings('ignore', 'use_inf_as_na')

iris = sns.load_dataset('iris')
print(iris)

plt.boxplot(iris['sepal_length'], showmeans=True, meanline=True,)