# Imports
import os,copy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import date, timedelta as td
import matplotlib.dates as mdates
from matplotlib.dates import HOURLY, DateFormatter, rrulewrapper, RRuleLocator, drange
from apscheduler.schedulers.blocking import BlockingScheduler
#import nice_plots as nplt
#import datetime
#from datetime import timedelta
def prj12():
previous = datetime.now()-td(1)
now = datetime.now()


# Function to cheak if leap year
def checkleap(year):
	return ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)))

# Date of the year Conversion
def convert_date(day,month,year):
	if checkleap(year)==True:
		days = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
		if month == 1:
			return day
		else:
			return day+days[month-2]
	else:
		days = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
		if month == 1:
			return day
		else:
			return day+days[month-2]

#Function to check presence of Nan
def checknonan(df):
	for i in df:
		if np.isnan(i):
			return False
	return True

#Function to count number of Nan
def countnan(df):
	count = 0
	for i in df:
		if np.isnan(i):
			count = count+1
	return count

#Function to convet time of week in seconds to hours
def gettime(times):
	hours = 0.0
	minutes = 0.0
	t = -1
	tm = []
	for each in times:
		if t!=each:
			minutes = minutes+1
			if minutes>60:
				hours = hours+1
				minutes = minutes%60
			t = each
		#print 'hr: ',hours,'mins: ',minutes
		tm1 = float((hours)+(float((minutes)/60)))
		tm.append(tm1)
	return tm

def getalttime(times,start):
	hours = 0.0
	minutes = 0.0
	t = -1
	tm = []
	for each in times:
		if t!=each:
			minutes = minutes+1
			if minutes>60:
				hours = hours+1
				minutes = minutes%60
			t = each
		#print 'hr: ',hours,'mins: ',minutes
		tm1 = float((hours+5)+(float((minutes+30)/60)))
		tm2 = start+td(hours=tm1)
		tm.append(tm2)
	return tm


#Function to check validity of dates
def validdt(start_date,start_month,start_year,end_date,end_month,end_year,date_from,date_upto):
    if start_year>end_year or (start_year<date_from.year or end_year>date_upto.year) :
        return False
    elif start_year==end_year and (start_year==date_from.year and end_year==date_upto.year) and (start_month>end_month or start_month<date_from.month or end_month>date_upto.month):
        return False
    elif start_year==end_year and (start_year==date_from.year and end_year==date_upto.year) and start_month==end_month and (start_month==date_from.month and end_month==date_upto.month) and (start_date>end_date or start_date<date_from.day or end_date>date_upto.day):
        return False
    return True

#Function to obtain range of dates
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + td(n)

#Function to convert folder name into human readable format date
def conv_readdate(dt):
	dt_year = 2000+int(dt/1000)
	dt_doy = dt%1000
	t = date.fromordinal(date(dt_year, 1, 1).toordinal() + dt_doy - 1)
	return t

def main():
	#nplt.nplts(fs=18)
	#Check latest date of the data available
	os.chdir('/media/sumanjit/Bela/2018')
	sub = [x for x in os.listdir('.') if os.path.isdir(x)]
	dt = max(sub)
	date_upto = conv_readdate(int(dt))
	os.chdir('/Users/prajawal/Desktop/prajawal_data/')
	#Check oldest date of the data available
	os.chdir('/Users/prajawal/Desktop/prajawal_data/')
	sub = [x for x in os.listdir('.') if os.path.isdir(x)]
	dt = min(sub)
	date_from = conv_readdate(int(dt))
	os.chdir('/Users/prajawal/Desktop/prajawal_data/')
	print ("\nData available from %s to %s\n" %(date_from,date_upto))

	alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
	#alpha=['A','B','C','D','E','F','G','H']

	#Taking valid start and end dates as input from user
alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']#,'U','V','W','X']
start_date = int(previous.day)
start_month = int(previous.month)
start_year = int(previous.year)
end_date=int(now.day)
end_month=int(now.month)
end_year=int(now.year)
d1 = date(start_year,start_month,start_date)
d2 = date(end_year,end_month,end_date)

	#Conversion into datetime format
d1 = date(start_year,start_month,start_date)
d2 = date(end_year,end_month,end_date)
#d3 = date(end_year,end_month,end_date)
#elev = float(input('Enter the minimum elevation angle = '))

#Reading and storing data from different files
frames = []
for single_date in daterange(d1,d2):
    curr_date = str(convert_date(int(single_date.day),int(single_date.month),int(single_date.year)))
    curr_date = curr_date.zfill(3)
    curr_folder = str(str(int(single_date.year)%2000)+str(curr_date))
alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']#,'U','V','W','X']
for letter in alpha:
	    try:
		filename = str('SEPT'+curr_date+letter+'.'+'18_.ismr')
		with open('/Users/prajawal/Desktop/prajawal_data/%s/%s' %(curr_folder,filename)) as f:
					df = pd.read_csv(f,usecols=[1,2,22],names=['time','svid','TEC'])
					#df = df[df['elevation']>=elev]
					frames.append(df)
	    except (IOError):
				df1 = copy.deepcopy(frames[len(frames)])
				df1['time']=df['time']+3600
				tec = ['nan' for each in df1['time']]
				df1['TEC'] = tec
				frames.append(df1)

result =pd.concat(frames)
result[['TEC']] = result[['TEC']].apply(pd.to_numeric,errors='coerce')
#Replace NaN and negative values with zero
result.loc[~(result['TEC'] > 0), 'TEC'] = np.nan
dttime = datetime(start_year,start_month,start_date)
result['t-ddmm'] = getalttime(result['time'],dttime)
result['t-time'] = gettime(result['time'])
#mxtime = max(result['t-time'])
#mntime = min(result['t-time'])
# result['t-hrs'] = gettime(result['time'])
result = result.drop('time',1)
#print result['t-time']
dfm = result.groupby('svid')
	# gb = dfm.groups
	# for key, values in gb.iteritems():
	# 	print df.ix[values], "\n\n"
svid = set()
for elements in result['svid']:
			svid.add(elements)
svid1 = sorted(svid)

cnt = 0
while(cnt!=1):
    for each in svid1:
             if each>37:
                        svid.remove(each)
    svid2 = sorted(svid)
    n = 37
    constl = 'gps'
    cnt=1

fig,ax = plt.subplots()
clr = iter(plt.cm.rainbow(np.linspace(0,1,len(svid2))))

	#maxtecdf = []
	#maxtm    = []
for each in svid2:
		dftemp = dfm.get_group(each)
		timedf = np.array(dftemp['t-time'])
		tecdf = np.array(dftemp['TEC'],dtype=float)
		cl = next(clr)
		ax.scatter(timedf,tecdf,label='%d' %each,c=cl,edgecolor=cl)
		#maxtecdf.append(np.max(tecdf))
		#ineed = np.where(tecdf == np.max(tecdf))
		#maxtm.append(timedf[ineed])
		xmin = 0.0
		xmax = 24.0
		ymin = 0.0
		ymax = 150.0
		axes = plt.gca()
		axes.set_xlim([xmin,xmax])
		axes.set_ylim([ymin,ymax])

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(linestyle='--')

	#mtec = max(maxtecdf)
	#jneed = maxtecdf.index(mtec)
	#mtm = maxtm[jneed]

	#ft1 = plt.figtext(0.6, 0.8, r'Max Value : %.2f'%mtec)
	#ft2 = plt.figtext(0.6, 0.75,r'Max Time : %.2f'%mtm)
plt.xlabel('UT(h)',fontsize=16)
plt.ylabel(r'Value of TEC(in TECU x $\frac{10^{16}}{m^2}$)',fontsize=16)
plt.title('TEC plot of %s  \n' %(d1))
plt.legend(bbox_to_anchor=(1, 1), loc='upper left',prop={'size':12}, borderaxespad=0.,frameon=False,title='svid no.',scatterpoints=1 )
plt.savefig('prajawal.png')
#format = "png"
#sio = cStringIO.StringIO()
#plt.savefig(sio, format=format)
#print "Content-Type: image/%s\n" % format
#sys.stdout.write(sio.getvalue())
#plt.savefig('img_test.png',dpi=100)
#print "Content-Type: text/html\n"
#print """<html><body>
#<h1>prajawal </h1>
#<img src="data:image/png;base64,%s"/>
#</body></html>""" % sio.getvalue().encode("base64").strip()
scheduler = BlockingScheduler()
scheduler.add_job(prj12, 'interval', hours=1)
scheduler.start()
if __name__=="__main__":
	main()
