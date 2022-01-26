# algorand_txn_csv_exporter - (Algorand transaction CSV exporter)

This script will export transactions for an algorand wallet to a CSV file.  

It is intended to assist with filing taxes.

It uses API from algoexplorer.io (v1).

Simply update the wallet variable with the wallet address(es) you're interested in, and then run the script.

# To do:
<li>Pare down columns to just the essential ones</li>
<li>Time zone support (currently the timestamp field is UDT)</li>
<li>Change amounts to whole units (currently the API shows in millionths, so .000001 ALGO currently shows as "1" in the amount column)</li>

# DID THIS SCRIPT HELP YOU?
I hope it did. It helped me too! If you feel inclined to tip, here is an Algo wallet address I set up specifically for tips (not necessary but certainly welcome!)
5Q2RGRRXLC3643TFP22Y5LITE5P3SPQLZO2U4KLDALLMUMZWCOEFVEKQEQ
