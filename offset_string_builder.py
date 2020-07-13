# Generates a user-readable string for the UTC offset of a given timezone
# Moment.js does this in 1 line, but I couldn't find a pythonic solution that was as simple, so I decided to do it from scratch
# You'd think .utcoffset() function would get the simple offset, but it takes into account days for whatever reason, so the total_seconds returned can give a crazy result

def get_offset_string(timezone):
	import pytz, datetime
	
	tmp_now = datetime.datetime.now(pytz.timezone(timezone))
	is_dst = (tmp_now.dst() != datetime.timedelta(0))
	offset = tmp_now.utcoffset().total_seconds()/60/60
	
	# Determine the sign of the offset for string display
	if offset >= 0:
		sign = "+"
	else:
		sign = "-"
		
	# Set the DST string
	if is_dst:
		dst_str = " DST"
	else:
		dst_str = ""
		
	# If the offset is a real number, flat even or odd, take the shortcut
	if offset % 2 == 0.0 or offset % 2 == 1:
		hours = abs(int(offset))
		if hours < 10:
			hours = '0' + str(hours)
		offset_string = "UTC" + sign + str(hours) + ":00" + dst_str
	else: # Else set the hours and determine the remaining minutes
		offset = abs(offset) # abs prevents weird modulus values
		hours = int(offset - (offset % 2))
		ratio_minutes = offset % 2
		minutes = int(60 * ratio_minutes)
		
		# Have to perform this check due to how modulus math can work out with certain floats, e.g. 5.5
		# 5.5 would set hours to 4 and minutes to 90
		if minutes >= 60:
			hours += 1
			minutes = minutes - 60
		
		# Pad hours and minutes with 0 if less than 10 to get HH:MM format
		if hours < 10:
			hours = '0' + str(hours)
		if minutes < 10:
			minutes = '0' + str(minutes)
		
		offset_string = "UTC" + sign + str(hours) + ":" + str(minutes) + dst_str
	
	return offset_string
	
