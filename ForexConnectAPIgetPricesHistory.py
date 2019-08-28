#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime
 
from forexconnect import fxcorepy, ForexConnect
 
 
def session_status_changed(session: fxcorepy.O2GSession,
                           status: fxcorepy.AO2GSessionStatus.O2GSessionStatus):
    print("Trading session status: " + str(status))
 
 
def main():
 
    with ForexConnect() as fx:
        try:
            fx.login("D261153925", "384", "fxcorporate.com/Hosts.jsp",
                     "Demo", session_status_callback=session_status_changed)
 
            history = fx.get_history("EUR/USD", "H1",
                                    datetime.datetime.strptime("07.01.2019 21:21:21", '%m.%d.%Y %H:%M:%S').replace(tzinfo=datetime.timezone.utc),
                                    datetime.datetime.strptime("07.31.2019 21:21:21", '%m.%d.%Y %H:%M:%S').replace(tzinfo=datetime.timezone.utc))
 
            print("Date, BidOpen, BidHigh, BidLow, BidClose, Volume")
            for row in history:
                print("{0:s}, {1:,.5f}, {2:,.5f}, {3:,.5f}, {4:,.5f}, {5:d}".format(
                    pd.to_datetime(str(row['Date'])).strftime('%m.%d.%Y %H:%M:%S'), row['BidOpen'], row['BidHigh'],
                    row['BidLow'], row['BidClose'], row['Volume']))
 
        except Exception as e:
            print("Exception: " + str(e))
 
        try:
            fx.logout()
        except Exception as e:
            print("Exception: " + str(e))
 
 
if __name__ == "__main__":
    main()


# In[ ]:




