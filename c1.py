from datetime import datetime
from operator import index
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("https://raw.githubusercontent.com/KAIR-ISZ/public_lectures/master/Data%20Analytics%202022/Lab%201%20-%20Python%20review/Data1.csv")#, index_col="Unnamed: 0")
data['Unnamed: 0'] = pd.to_datetime(data['Unnamed: 0'], format='%Y-%m-%d')
data.set_index('Unnamed: 0',inplace=True)

plt.figure()
fig1=plt
ax = plt.gca()
fig1.plot(data, label = 'Time series', linewidth = 0.75)
fig1.legend(['theta_1','theta_2','theta_3','theta_4','theta_5','theta_6'])
fig1.grid(True)
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
fig1.title('Time series')

plt.figure()
fig2=plt
fig2.hist(data, bins=50, linewidth = 0.75)
fig2.title('Histogram. Bins=50')
fig2.grid(True)

fig3=plt
fig3=data.plot.kde()
fig3.linewidth=0.75
fig3.title.set_text('KDE')
fig3.grid(True)

plt.figure()
fig4=plt
ax2 = plt.gca()
plt.plot(data.loc['2018-01-01':'2018-12-31'], label = 'Time series for 2018', linewidth = 0.75)
fig4.legend(['theta_1','theta_2','theta_3','theta_4','theta_5','theta_6'])
fig4.grid(True)
ax2.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax2.xaxis.get_major_locator()))
fig4.title('Time series for 2018')

plt.figure()
fig5=plt
fig5.hist(data.loc['2018-01-01':'2018-12-31'], bins=50)
fig5.title('Histogram for 2018. Bins=50')
fig5.grid(True)

fig6=plt
fig6=data.loc['2018-01-01':'2018-12-31'].plot.kde()
fig6.title.set_text('KDE for 2018')
fig6.grid(True)


plt.show()
