# Imports
import os,copy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import date, timedelta as td
import matplotlib.dates as mdates
from matplotlib.dates import HOURLY, DateFormatter, rrulewrapper, RRuleLocator, drange
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import Dense

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
	os.chdir('/Users/prajawal/Desktop/2018')
	sub = [x for x in os.listdir('.') if os.path.isdir(x)]
	dt = max(sub)
	date_upto = conv_readdate(int(dt))
	os.chdir('/Users/prajawal/Desktop/2018')
	#Check oldest date of the data available
	os.chdir('/Users/prajawal/Desktop/2018')
	sub = [x for x in os.listdir('.') if os.path.isdir(x)]
	dt = min(sub)
	date_from = conv_readdate(int(dt))
	os.chdir('/Users/prajawal/Desktop/2018')
	print ("\nData available from %s to %s\n" %(date_from,date_upto))

	alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
	#alpha=['A','B','C','D','E','F','G','H']

	#Taking valid start and end dates as input from user
	#validity = False
	#while(validity!=True):
	#	start_date = int(input("Enter Start Date(dd):"))
	#	start_month = int(input("Enter Start Month(mm):"))
	#	start_year = int(input("Enter Start Year(yyyy):"))
	#	print ("\n")
	#	end_date = int(input("Enter End Date(dd):"))
	#	end_month = int(input("Enter End Month(mm):"))
	#	end_year = int(input("Enter End Year(yyyy):"))
	#	print ("\n")
	#	validity = validdt(start_date,start_month,start_year,end_date,end_month,end_year,date_from,date_upto)
	#	if validity == False:
	#		print ("\nPlease enter valid start and end dates\n")

	#Conversion into datetime format
	#d1 = date(start_year,start_month,start_date)
	#d2 = date(end_year,end_month,end_date)
	#d3 = date(end_year,end_month,end_date)
	#elev = float(input('Enter the minimum elevation angle = '))

	#Reading and storing data from different files
	frames = []
	for single_date in daterange(date_from,date_upto):
		curr_date = str(convert_date(int(single_date.day),int(single_date.month),int(single_date.year)))
		curr_date = curr_date.zfill(3)
		curr_folder = str(str(int(single_date.year)%2000)+str(curr_date))
		for letter in alpha:
			#try:
				filename = str('SEPT'+curr_date+letter+'.'+'18_.ismr')
				with open('/Users/prajawal/Desktop/2018/%s/%s' %(curr_folder,filename)) as f:
					df = pd.read_csv(f,usecols=[1,2,22],names=['time','svid','TEC'])
					#df = df[df['elevation']>=elev]
					frames.append(df)
			#except (IOError):
				#df1 = copy.deepcopy(frames)
				#df1.iloc('time')=df.iloc('time')+3600
				#tec = ['nan' for each in df1['time']]
				#df1['TEC'] = tec
				#frames.append(df1)

	result =pd.concat(frames)
	result[['TEC']] = result[['TEC']].apply(pd.to_numeric,errors='coerce')
	#Replace NaN and negative values with zero
	result.loc[~(result['TEC'] > 0), 'TEC'] = np.nan

	dttime = date_from
	result['t-ddmm'] = getalttime(result['time'],dttime)
	result['t-time'] = gettime(result['time'])
	#mxtime = max(result['t-time'])
	#mntime = min(result['t-time'])
	# result['t-hrs'] = gettime(result['time'])
	result = result.drop('time',1)
	dfm = result.groupby('svid')
		# gb = dfm.groups
		# for key, values in gb.iteritems():
		# 	print df.ix[values], "\n\n"
	svid = set()
	for elements in result['svid']:
				svid.add(elements)
	svid1 = sorted(svid)
	for each in svid1:
		if each>37:
			svid.remove(each)
	svid2 = sorted(svid)


	for each in svid2:
			dftemp = dfm.get_group(each)
			timedf = np.array(dftemp['t-time'])
			tecdf = np.array(dftemp['TEC'],dtype=float)

	#pd.DataFrame.from_records(tecdf)
	#training_set =tecdf
	#training_set=training_set.fillna(training_set.mean())
	pdtec=tecdf.reshape((-1,1))
	pdtec1=pd.DataFrame({'':pdtec[:,0]})
	print (pdtec1)

	#retrieving test set

	os.chdir('/Users/prajawal/Desktop/2018_1')
	sub = [x for x in os.listdir('.') if os.path.isdir(x)]
	dt = max(sub)
	date_upto_1 = conv_readdate(int(dt))
	os.chdir('/Users/prajawal/Desktop/2018_1')
	#Check oldest date of the data available
	os.chdir('/Users/prajawal/Desktop/2018_1')
	sub = [x for x in os.listdir('.') if os.path.isdir(x)]
	dt = min(sub)
	date_from_1 = conv_readdate(int(dt))
	os.chdir('/Users/prajawal/Desktop/2018_1')
	print ("\nData available from %s to %s\n" %(date_from_1,date_upto_1))

	alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
	#alpha=['A','B','C','D','E','F','G','H']

	#Taking valid start and end dates as input from user
	#validity = False
	#while(validity!=True):
	#	start_date = int(input("Enter Start Date(dd):"))
	#	start_month = int(input("Enter Start Month(mm):"))
	#	start_year = int(input("Enter Start Year(yyyy):"))
	#	print ("\n")
	#	end_date = int(input("Enter End Date(dd):"))
	#	end_month = int(input("Enter End Month(mm):"))
	#	end_year = int(input("Enter End Year(yyyy):"))
	#	print ("\n")
	#	validity = validdt(start_date,start_month,start_year,end_date,end_month,end_year,date_from,date_upto)
	#	if validity == False:
	#		print ("\nPlease enter valid start and end dates\n")

	#Conversion into datetime format
	#d1 = date(start_year,start_month,start_date)
	#d2 = date(end_year,end_month,end_date)
	#d3 = date(end_year,end_month,end_date)
	#elev = float(input('Enter the minimum elevation angle = '))

	#Reading and storing data from different files
	frames_1 = []
	for single_date in daterange(date_from_1,date_upto_1):
		curr_date_1 = str(convert_date(int(single_date.day),int(single_date.month),int(single_date.year)))
		curr_date_1 = curr_date_1.zfill(3)
		curr_folder_1 = str(str(int(single_date.year)%2000)+str(curr_date_1))
		for letter in alpha:
			#try:
				filename_1 = str('SEPT'+curr_date_1+letter+'.'+'18_.ismr')
				with open('/Users/prajawal/Desktop/2018_1/%s/%s' %(curr_folder_1,filename_1)) as f:
					df_1 = pd.read_csv(f,usecols=[1,2,22],names=['time','svid','TEC'])
					#df_1 = df_1[df_1['elevation']>=elev]
					frames_1.append(df_1)
			#except (IOError):
				#df12 = copy.deepcopy(frames)
				#df12.iloc('time')=df.iloc('time')+3600
				#tec = ['nan' for each in df12['time']]
				#df12['TEC'] = tec
				#frames.append(df12)

	result_1 =pd.concat(frames_1)
	result_1[['TEC']] = result_1[['TEC']].apply(pd.to_numeric,errors='coerce')
	#Replace NaN and negative values with zero
	result_1.loc[~(result_1['TEC'] > 0), 'TEC'] = np.nan

	dttime_1 = date_from_1
	result_1['t-ddmm'] = getalttime(result_1['time'],dttime_1)
	result_1['t-time'] = gettime(result_1['time'])
	#mxtime = max(result['t-time'])
	#mntime = min(result['t-time'])
	# result['t-hrs'] = gettime(result['time'])
	result_1 = result_1.drop('time',1)
	dfm = result_1.groupby('svid')
	svid = set()
	for elements in result_1['svid']:
		svid.add(elements)
	svid1 = sorted(svid)
	for each in svid1:
		if each>37:
			svid.remove(each)
	svid2 = sorted(svid)
	for each in svid2:
				dftemp = dfm.get_group(each)
				timedf = np.array(dftemp['t-time'])
				tecdf = np.array(dftemp['TEC'],dtype=float)


	pdtect=tecdf.reshape((-1,1))
	pdtect1=pd.DataFrame({'':pdtect[:,0]})
	print (pdtect1)
	#training_set =result.iloc[:, 2:3]
	training_set=pdtec1.fillna(pdtec1.mean())
	#test_set =result_1.iloc[:, 2:3]
	test_set=pdtect1.fillna(pdtect1.mean())
	#training_set=training_set.values
	print (training_set)
	print('testing data')
	sc = MinMaxScaler(feature_range=(0, 1))
	training_set_scaled=sc.fit_transform(training_set)
	#print(training_set_scaled)
	X_train=[]
	y_train=[]
	for i in range(60,len(training_set.index)):
		X_train.append(training_set_scaled[i-60:i , 0])
		y_train.append(training_set_scaled[i,0])
	X_train=np.array(X_train)
	y_train=np.array(y_train)
	X_train=np.reshape(X_train,(X_train.shape[0],X_train.shape[1],1))
	regressor = Sequential()
#adding lstm layers
	regressor.add(LSTM(units =50,return_sequences=True,input_shape=(X_train.shape[1],1)))
	regressor.add(Dropout(0.2))
	regressor.add(LSTM(units =50,return_sequences=True))
	regressor.add(Dropout(0.2))
	regressor.add(LSTM(units =50,return_sequences=True))
	regressor.add(Dropout(0.2))
	regressor.add(LSTM(units =50))
	regressor.add(Dropout(0.2))
	regressor.add(Dense(units = 1))
	#compiling rnn
	regressor.compile(optimizer='adam',loss='mean_squared_error')
	#fitting RNN to dataset
	regressor.fit(X_train,y_train,epochs = 5,batch_size=32)
	#test_set =result.iloc[:, 2:3].values
	#test_set=test_set.fillna(test_set.mean())
	dataset_total=pd.concat((training_set,test_set), axis = 0)
	inputs = dataset_total[len(dataset_total)-len(test_set)-10:].values
	inputs=inputs.reshape(-1,1)
	inputs=sc.transform(inputs)
	X_test=[]
	for i in range(60,len(test_set.index)):
		X_test.append(inputs[i-60:i , 0])
	X_test=np.array(X_test)
	X_test=np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))
	predicted=regressor.predict(X_test)
	predicted=sc.inverse_transform(predicted)

	#X_train=sc.inverse_transform(X_train)
	print('prediction')
	print(predicted)
	prj=np.array(test_set)
	prj1=np.array(test_set[:850])

	#plt.plot(prj,label='total data',color='blue')
	plt.plot(prj1,label='test data',color='green')
	plt.plot(predicted,label='predictions',color='red')
	plt.legend()
	plt.show()


	print(test_set)
if __name__=="__main__":
	main()
