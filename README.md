# ALGORAND TRANSACTION CSV EXPORTER

# What does it do?
<li>This script will export transactions for an algorand wallet to a CSV file.  </li>
<li>It is intended to assist with filing taxes.</li>
<li>It uses the v1 API from algoexplorer.io (which is free and doesn't require any special credentials)</li>

# How to use it:
<li>Simply update the wallet variable with the wallet address(es) you're interested in, and then run the script.</li>
<li>The packages used by the code are common ones, but you may need to install them if you don't already have them: pandas, pandas.io.json, requests, datetime, and numpy

# Additional Notes:
<li>The last several columns in the export that start with "z_" are fields I added to the API feed at the end.  They are the most commonly used fields, and should help you find what you're looking for more easily.</li>
<li>Optionally, you can update the timezone adjustment variable with the number of hours your timezone is from UDT (not required)</li>
<li>The datetime fields that start with "z_" are in the format that Excel uses.  Simply change the format mask in Excel for these fields to datetime to see it formatted.</li>

# Did this script help you?  Want to tip me?
I hope this helped you; It helped me too! If you feel inclined to tip, here is an Algo wallet address I set up specifically for tips (not necessary but certainly welcome!):
<p>5Q2RGRRXLC3643TFP22Y5LITE5P3SPQLZO2U4KLDALLMUMZWCOEFVEKQEQ</p>
