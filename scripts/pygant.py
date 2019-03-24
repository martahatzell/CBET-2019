"""
GANTT Chart with Matplotlib
Sukhbinder
"""

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import matplotlib.dates
from matplotlib.dates import WEEKLY,MONTHLY, DateFormatter, rrulewrapper, RRuleLocator 
import numpy as np
  
 
def _create_date(datetxt):
    """Creates the date"""
    month,year=datetxt.split('-')
    day = 01
    date = dt.datetime(int(year), int(month), int(day))
    mdate = matplotlib.dates.date2num(date) 
    return mdate
 
def CreateGanttChart(fname):
    """
        Create gantt charts with matplotlib
        Give file name.
    """ 
    ylabels = []
    customDates = []
    colors = []
    try:
        textlist=open(fname).readlines()
    except:
        return
#
    for tx in textlist:
        if not tx.startswith('#'):
            ylabel,startdate,enddate,color=tx.split('\t')
            ylabels.append(ylabel.replace('\n',''))
            customDates.append([_create_date(startdate.replace('\n','')),_create_date(enddate.replace('\n',''))])
            color = color.strip()
            colors.append(color)
             
    ilen=len(ylabels)
    pos = np.arange(0.5,ilen*0.5+0.5,0.5)
    task_dates = {}
    for i,task in enumerate(ylabels):
        task_dates[task] = customDates[i]
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111)
    for i in range(len(ylabels)):
         start_date,end_date = task_dates[ylabels[i]]
         color = colors[i]
         ax.barh((i*0.5)+0.5, end_date - start_date, left=start_date, height=0.3, align='center', edgecolor='k', color=color, alpha = 0.4)
         ax.annotate(ylabels[i],(start_date,(i*0.5)+0.5),va='center',fontsize=10)
    locsy, labelsy = plt.yticks(pos,['']*len(ylabels))
    plt.setp(labelsy, fontsize = 12)
    ax.axis('tight')
    ax.set_ylim(ymin = -0.1, ymax = ilen*0.5+0.5)
    ax.xaxis.grid(color = 'k', linestyle = ':')
    ax.xaxis_date()

    #plot quarterly
    rule = rrulewrapper(MONTHLY, interval=6)
    loc = RRuleLocator(rule)
    formatter = DateFormatter("%b '%y")
    #formatter = DateFormatter("%d-%b")
  
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_major_formatter(formatter)
    labelsx = ax.get_xticklabels()
    plt.setp(labelsx, fontsize=12)
 
    font = font_manager.FontProperties(size='small')
    ax.legend(loc=1,prop=font)
 
    ax.invert_yaxis()
    fig.autofmt_xdate()
    plt.xticks(rotation=90)
    plt.savefig('../figures/gantt_raw.pdf')
 
if __name__ == '__main__':
    fname=r"timeline.txt"
    CreateGanttChart(fname)
