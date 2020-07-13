# MiscTools
Various tools I've made to make life easier

## paratrooper.sh
Handy network enumeration script. Stores output of ifconfig, ip route, iwlist wlan0 scanning, and netstat -lanp to a zip, then uses scp to copy this data back to a listening host. Designed to be placed on a raspberry pi dropper running Kali that has the script on a crontab, so that when you drop it on a network, it'll run the script every X minutes and get the data back to you for your use and remoting back into it :).

## flask_page_generator.py
Script to easily insert pages into a flask environment.
To use:
Must have template pages for html, css, js, and python files.
Once template pages are made, insert tags for page name replacement as desired.
Update tags within this script to match those in the templates.
Update filepath placeholders in this script to match your flask environment.
Update flask blue print placeholders in the init_insert_template to match your flask environment.

## sqlchecker.py
Reads in a dict of reserved SQL keywords and scans the provided input to determine whether or not a SQL keyword is present
Useful for PCAP analysis to determine validity of SQLi security events
To use:
	Create your SQL reserved words CSV file depending on your version of SQL
	Update the file path variable in this script
	
## opt_enum.py
Quick and dirty allowed HTTP verbs enumerator, takes a file of urls (1 per line) and runs OPTIONS against each. Could use a help message and input validation, but it works# so....

## htb_init.py
Simple script to create working directories when starting a new machine on HTB, just provide the name of the machine when running the script , e.g. 'python htb_init.py ellingson'  Saves approx 30 seconds of creating directories manually! 

## offset_string_builder.py
Easily generate UTC offset strings in Python. Couldn't find a simpler / prebuilt solution elsewhere, so I made this (possibly very redundant if my Google-fu was just weak)
