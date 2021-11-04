#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv ('HSR Metro SG_exit (Pin Chi) - Copy of THSR_exit.csv')
if df['Stationname En'][0] == 'Nangang' :
    print(df['Stationname En'][0])
len(df['Stationname En'])
df.head()


# In[5]:


class exitprint:
    def __init__(self, station_inf):
        self.short_name = station_inf[0]
        self.lon = station_inf[1]
        self.lat = station_inf[2]
        self.exitid = station_inf[3]
    def printGroovyCode(self):
        for i in range(len(self.exitid)):
            groovyCode = "exit \"" + self.exitid[i] + "\" with {\n" +                          "    short_name \"" + self.short_name[i] + "\"\n" +                          "    coords { lat " + str(self.lon[i]) + "; lon " + str(self.lat[0]) + " }\n" +                          "    layer 0\n}"
            print(groovyCode)


# In[6]:


# input the station name and output the results
stationName = input('Enter the station👍 :')
station_inf = [[],[],[],[]] # shortname,lon,lat,exitid
for i in range(len(df['Stationname En'])) :
    if df['Stationname En'][i] == stationName :
        station_inf[0].append(df['short name'][i])
        station_inf[1].append(df['Exitposition Positionlon'][i])
        station_inf[2].append(df['Exitposition Positionlat'][i])
        station_inf[3].append(df['exitid'][i])


# In[7]:


# Example output format:
# exit "TaiwanStation_NanGangNangang_E42781" with {
#    short_name "1"
#    coords { lat 25.051816; lon 121.606523 }
#    layer 0
# }
test = exitprint(station_inf)
test.printGroovyCode()


# In[ ]:





# In[ ]:




