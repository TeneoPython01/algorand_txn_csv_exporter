# algorand_txn_csv_exporter - (Algorand transaction CSV exporter)

This script will export transactions for an algorand wallet to a CSV file.  

It is intended to assist with filing taxes.

It uses API from algoexplorer.io (v1).

Simply update the wallet variable with the wallet address(es) you're interested in, and then run the script.

# To do:
<li>Pare down columns to just the essential ones</li>
<li>Time zone support (currently the timestamp field is UDT)</li>
<li>Time format for the datetime is in unix/epoch time, which should be converted to a conventional datetime format.  To do this in Excel, the formula is:</li>
<p><p>=(((((LEFT(<b>A2</b>,10)&"."&RIGHT(<b>A2</b>,3))*1)/60)/60)/24)+DATE(1970,1,1) <i>where <b>A2</b> is the cell you want to convert</i></p></p>
<li>Change amounts to whole units (currently the API shows in millionths, so .000001 ALGO currently shows as "1" in the amount column)</li>

# DID THIS SCRIPT HELP YOU?
I hope it did. It helped me too! If you feel inclined to tip, here is an Algo wallet address I set up specifically for tips (not necessary but certainly welcome!)
5Q2RGRRXLC3643TFP22Y5LITE5P3SPQLZO2U4KLDALLMUMZWCOEFVEKQEQ
