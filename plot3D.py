#import librarie for loading and plotting the data
import pandas as pd
import matplotlib.pyplot as plt

# import the data from the data directory and name the dataframe after the charcteristic particle diameter in the file
df_1 = pd.read_csv('data/1x50bin_0.021m 1.csv')

# rename all columns, except for the first and last, to the corresponding particle position
# the second column should be named h2o_mf_bin1, the third h2o_mf_bin2, and so on
column_names = ['time'] + [f'h2o_mf_bin{i}' for i in range(1, df_1.shape[1] - 1)] + ['Temp']
df_1.columns = column_names

#z = h2o_mf
#x = time
#y = position



# plot the h2o_mf for each position as a function of time in a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(1, df_1.shape[1] - 1):
    ax.plot(df_1['time'], df_1[f'h2o_mf_bin{i}'], zs=i, zdir='y')
plt.show()
