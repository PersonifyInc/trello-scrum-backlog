import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.interpolate import spline

def PlotBurndown(date_labels,completed_on,churn_on,mrd_backlog,post_mrd_backlog,defect_backlog,design_backlog):
	N = len(date_labels)

	# Commands to format and place labels
	def format_label(x, pos=None):
		thisind = np.clip(int(x+0.5),0,N-1)
		return date_labels[thisind]
	
	# Get data series for rows
	# Adapted from http://stackoverflow.com/questions/2225995/how-can-i-create-stacked-line-graph-with-matplotlib 
	y = np.row_stack((np.array(mrd_backlog), np.array(design_backlog), np.array(post_mrd_backlog), np.array(defect_backlog) ))   	
	y_stack = np.cumsum(y, axis=0)   # a 3x10 array
	
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ind = np.arange(N)

	colors = ["#1f8181", "#f2bc79", "#f28972", "#bf1b39", "#000000"]
	
	ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(format_label)) 
	ax.xaxis.set_major_locator(matplotlib.ticker.LinearLocator(N/2)) # Sets up N labeled ticks, no more, no less
	fig.autofmt_xdate() # Have angled labels
	ax.set_ylabel('Backlog [Cards]')
	ax.grid(True)

    # Line plot of churn (separate y-axis)
	ax2 = ax.twinx()
	ax2.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(format_label)) 
	ax2.xaxis.set_major_locator(matplotlib.ticker.LinearLocator(N/2)) # Sets up N labeled ticks, no more, no less
	ax2.set_ylabel('Churn [LOC]')
	
	# Ref: http://stackoverflow.com/questions/5283649/plot-smooth-line-with-pyplot
	xnew = np.linspace(ind[0], ind[-1], 300)
	power_smooth = spline(ind,churn_on,xnew)
	
	churn_plot = ax2.plot(ind, churn_on, '-', color=colors[4], alpha=0.7)
	#ax2.plot(xnew, power_smooth, '-', color=colors[4], alpha=0.7)
	
	# Plot the stacked bars
	ax.fill_between(ind, 0, y_stack[0,:], facecolor=colors[0], alpha=0.7)
	ax.fill_between(ind, y_stack[0,:], y_stack[1,:], facecolor=colors[1], alpha=0.7)
	ax.fill_between(ind, y_stack[1,:], y_stack[2,:], facecolor=colors[2], alpha=0.7)
	ax.fill_between(ind, y_stack[2,:], y_stack[3,:], facecolor=colors[3], alpha=0.7)
	
	# Bar chart for cards completed
	ax.bar(ind, completed_on, color=colors[4], alpha=0.7)
	
	plt.title("Personify Live Burndown")

	proxy = [plt.Rectangle((0,0),1,1,facecolor=fc,alpha=0.7) for fc in colors]
	proxy.append(churn_plot)
	plt.legend(proxy, ["MRD", "Design", "Post-MRD", "Defects", "Completed", "Churn"])

	plt.grid(b=True,axis='x')

	plt.show()
