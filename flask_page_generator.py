# flask_page_generator.py
# Given a page name for a new page in a flask environment, setup the necessary files in the correct directories

# Imports
from shutil import copyfile, move
import fileinput
import os

# Meta variables
setup_name = None
setup_directory = None
css_content = None
js_content = None
html_content = None
py_content = None

# Filepath vars
local_filepath = '#localPathToThisScript'
css_file = local_filepath + 'some_page.css'
js_file = local_filepath + 'some_page.js'
html_file = local_filepath + 'some_page.html'
py_file = local_filepath + 'some_page.py'
init_file = '#pathToFlaskInitFile'

# Target file vars
target_css_file = None
target_js_file = None
target_html_file = None
target_py_file = None

# Meta directory path vars
static_dir_path = '#pathToFlaskStaticDirectory'
scripts_path = '#pathToFlaskScriptsDirectory'
templates_path = '#pathToFlaskTemplatesDirectory'

# Wrap logic in KeyboardInterrupt/SystemExit try/except to exit gracefully if user exits
try:
	# Display welcome, prompt and get desired page name
	print('Welcome!')
	setup_name = raw_input('Enter desired page name:')

	# Assign vars
	setup_directory = static_dir_path + setup_name
	target_css_file = local_filepath + setup_name + .'css'
	target_js_file = local_filepath + setup_name + '.js'
	target_html_file = local_filepath + setup_name + '.html'
	target_py_file = local_filepath + setup_name + .'py'

	# Add files to list
	target_file_list = []
	target_file_list.append('target_css_file')
	target_file_list.append('target_js_file')
	target_file_list.append('target_html_file')
	target_file_list.append('target_py_file')

	# Print generated data for user confirmation
	print('Directory to create:')
	print(setup_directory)
	print('Files to create:')
	for file in target_file_list:
		print(file)

	# Copy files locally for text replacement prior to moving
	print('Copying files...')
	try:
		copyfile(css_file, target_css_file)
		copyfile(js_file, target_js_file)
		copyfile(html_file, target_html_file)
		copyfile(py_file, target_py_file)
	except IOError:
		print('Error: Destination is not writable!')
		print(IOError)
		exit(0)

	# Set up the directory in static dir for js and css files
	print('Making directory...')
	os.mkdir(setup_directory)
	confirm_list = os.listdir(static_dir_path)
	if setup_name in confirm_list:
		print('Directory successfully created at ' + static_dir_path)
	else:
		print('Error: Directory was not successfully created at ' + static_dir_path)

	# Get the contents of the files to replace tags in
	print('Reading file contents for js and css files')
	try:
		with open(target_js_file) as js_file:
			js_content = js_file.read()
			js_file.close()
		with open(target_html_file) as html_file:
			html_content = html_file.read()
			html_file.close()
		except IOError:
			print(IOError)
			exit(0)

	# Replace the contents are necessary
	print('Replacing tagged content in file contents')
	tags = [
		"#someTag",
		"#someOtherTag"
		#...
	]	
	for tag in tags:
		js_content = js_content.replace(tag, setup_name)
		html_content = html_content.replace(tag, setup_name)
	print('Tags replace successfully.')

	# Write the replaced content
	print('Writing file contents for js and css files...')
	try:
		with open(target_js_file,'w') as js_file:
			js_file.write(js_content)
			js_file.close()
		with open(target_html_file,'w') as html_file:
			html_file.write(html_content)
			html_file.close()
	except IOError:
		print(IOError)
		exit(0)
	print('Tags updated in files successfully.')

	# Move files to the correct location
	print('Moving files...')
	try:
		move(target_css_file, setup_directory)
		move(target_js_file, setup_directory)
		move(target_py_file, setup_directory)
		move(target_html_file, setup_directory)
	except Error as e:
		print(e)
		exit(0)

	# Update the init file
	init_insert_template = '''
		#########################
		# some_page ROUTES		#
		#########################

		# Render route
		@#yourBluePrint.route('/some_page')
		def some_page():
			# Import necessary packages

			# Render the page
			return render_template ('#yourBluePrint/some_page.html')

		# Data route
		@#yourBluePrint.route('/some_page/data',methods=[#desiredMethods])
		def some_page_data():
			# Import necessary packages
			import #yourBluePrint.scripts.some_page as some_page
			
			return some_page.some_page_function()

		#########################
		# END some_page ROUTES	#
		#########################

		#$_ROUTE_INSERT$#
	'''

	# Update the template
	init_insert_template = init_insert_template.replace('some_page',setup_name)

	# Update the init file
	try:
		with open(init_file, 'r') as init_file_open:
			init_contents = init_file_open.read()
			init_file_open.close()
	except IOError:
			print(IOError)
			exit(0)
	init_tag = '#$_ROUTE_INSERT$#'
	init_contents = init_contents.replace(init_tag,init_insert_template)
	try:
		with open(init_file, 'w') as init_file_write:
			init_file_write.write(init_contents)
			init_file_write.close()
	except IOError:
		print(IOError)
		exit(0)
	print('Init file updated successfully')
except (KeyboardInterrupt, SystemExit):
	print('\nManual exit triggered. Goodbye!')