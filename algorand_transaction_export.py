import pandas as pd
from pandas.io.json import json_normalize
import requests
from datetime import datetime
import numpy as np

#enter one or more wallet addresses, then run the code.  CSVs will export to the working directory of the code.
#the wallets below are some wallet addresses I found by searching google.  they are here to demo the code only.
my_wallets = [
    'Y76M3MSY6DKBRHBL7C3NNDXGS5IIMQVQVUAB6MP4XEMMGVF2QWNPL226CA',
    'WLWWUUU2HNSYE7L5MY5CH5PMEU2IDC32UMREY363YMJU5JGILTW3WE3UFI'
    ]

#enter how many hours your local time is from UDT
adjust_hours = -5 #this example would be eastern US time

#NOTE, when the export is complete, the last several columns that start with "z_" are
#the most commonly needed fields

#loop through the wallets
for my_wallet in my_wallets:

    try:
        del df_full
    except:
        pass

    df_full = pd.DataFrame()

    looper = 1
    iteration = 0

    #loop through all of the transcations in the wallet, 100 at a time.  (the API has a limit of 100 txns per pull)
    while looper == 1:

        range_start = 100 * iteration
        range_increment = 100
        range_end = range_start + range_increment - 1

        print('get wallet', my_wallet, 'txn in range', range_start, 'to', range_end)

        my_range = str(range_start) + '/to/' + str(range_end)

        #this is the API:
        my_url = 'https://api.algoexplorer.io/v1/account/'+my_wallet+'/transactions/from/'+my_range

        r = requests.get(my_url)
        df_iteration = json_normalize(r.json())

        #when the API call results in zero records, then end the loop.
        if len(df_iteration) == 0:
            looper = 0
            print(str(len(df_full)), ' total txns found in this wallet.')

        df_iteration['z_scanned_wallet'] = my_wallet
        df_full = pd.concat([df_full, df_iteration], sort=True)

        iteration = iteration + 1

    #create columns at the end of the data set with the most important data elements
    df_full['z_excel_datetime_udt'] = ((((df_full['timestamp']/60)/60)/24)+25569) # convert unix format and keep in UDT timezone
    df_full['z_excel_datetime_local'] = df_full['z_excel_datetime_udt'] + (adjust_hours/24) # adjust the datetime to local time using the adjust_hours variable at the start of the script
    df_full['z_amt_whole'] = df_full['amount']/1000000.000000 #convert amount to whole units instead of how the API displays millionths without decimals
    df_full['z_from'] = df_full['from']
    df_full['z_to'] = df_full['to']
    try:
        df_full['z_symbol'] = df_full['unitName']
    except:
        pass
    df_full['z_txid'] = df_full['txid']
    df_full['z_fee_whole'] = df_full['fee']/1000000.000000
    df_full['z_type'] = np.where(df_full['z_scanned_wallet']==df_full['from'],'send',np.where(df_full['z_scanned_wallet']==df_full['to'],'receive','other'))

    df_smaller = df_full[df_full.columns[:-7]]

    #create variables for date and time in yyyymmdd and hhmmss format to use in the exported CSV filename
    my_date = datetime.now().year*10000+datetime.now().month*100+datetime.now().day
    my_time = datetime.now().hour*10000+datetime.now().minute*100+datetime.now().second
    
    #filename syntax is "algo_export_[first 6 chars of wallet address]_[date]_[time].csv"
    filename = './algo_export_'+my_wallet[0:6]+'_'+str(my_date)+'_'+str(my_time)+'.csv'
    df_full.to_csv(filename)
    print('export complete: ' + filename + '\n\n')

