# MiscTools
Various tools I've made to make life easier

# flask_page_generator.py
Script to easily insert pages into a flask environment.
To use:
Must have template pages for html, css, js, and python files.
Once template pages are made, insert tags for page name replacement as desired.
Update tags within this script to match those in the templates.
Update filepath placeholders in this script to match your flask environment.
Update flask blue print placeholders in the init_insert_template to match your flask environment.

# sqlchecker.py
Reads in a dict of reserved SQL keywords and scans the provided input to determine whether or not a SQL keyword is present
Useful for PCAP analysis to determine validity of SQLi security events
To use:
	Create your SQL reserved words CSV file depending on your version of SQL
	Update the file path variable in this script