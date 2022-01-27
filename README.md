# ALGORAND TRANSACTION CSV EXPORTER (and associated ASAs like YLDY, etc.)

<h3> What does it do?</h3>
<li>This script will export all transactions for an algorand wallet to a CSV file.  </li>
<li>It is intended to assist with filing taxes.  For example, I used it to help find Yieldly (YLDY) and other ASA defi activity that wasn't automatically imported by Koinly.io (a crypto tax web service).</li>
<li>It uses the v1 API from algoexplorer.io (which is free and doesn't require any special credentials)</li>

<h3> How to use it:</h3>
<li>Simply update the wallet variable with the wallet address(es) you're interested in, and then run the script.</li>
<li>An active internet connection is required, since the code leverages the algoexplorer.io API to read the transactions from the blockchain</li>
<li>The packages used by the code are common ones, but you may need to install them if you don't already have them: pandas, pandas.io.json, requests, datetime, and numpy

<h3> Additional Notes:</h3>
<li>The last several columns in the export that start with "z_" are fields I added to the API feed at the end.  They are the most commonly used fields, and should help you find what you're looking for more easily.</li>
<li>Optionally, you can update the timezone adjustment variable with the number of hours your timezone is from UDT (not required)</li>
<li>The datetime fields that start with "z_" are in the format that Excel uses.  Simply change the format mask in Excel for these fields to datetime to see it formatted.</li>

<h3> What other options exist to download transactions?</h3>
<li> The official algo wallet (only available via phone app at the time of this repo's creation) will allow CSV exports, if you want to put your wallet on your phone.  I didn't want to do this.</li>
<li> This other github repo does something similar but attempts to group transcations together.  I prefer raw exports instead.  Here's a link if you want to check out their approach: https://github.com/HashingSlash/AlgoCSV </li>

# Did this script help you?  Want to tip me?
I hope this helped you; It helped me too! If you feel inclined to tip, here is an Algo wallet address I set up specifically for tips (not necessary but certainly welcome!):
<p>5Q2RGRRXLC3643TFP22Y5LITE5P3SPQLZO2U4KLDALLMUMZWCOEFVEKQEQ</p>
