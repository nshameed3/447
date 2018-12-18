from easygui import *
import test


msg = "Enter logon information"
title = "LOGIN"
fieldNames = ["User ID", "Password"]
fieldValues = []  # we start with blanks for the values
fieldValues = multpasswordbox(msg,title, fieldNames)

# make sure that none of the fields was left blank
while 1:
	if fieldValues == None: break
	errmsg = ""
	for i in range(len(fieldNames)):
		if fieldValues[i].strip() == "":
			errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
	
	check = test.checkUserPass(fieldValues[0], fieldValues[1])
	if check is None:
		errmsg="Not a valid userName or Password"
	else:
		errmsg=""
	if errmsg == "": break # no problems found
	fieldValues = multpasswordbox(errmsg, title, fieldNames, fieldValues)
switch = test.checkIfCall(check[0])


#SELECTION FOR THE MISSION CHIEF
if switch is None:
	msg = "Choose from the following"
	title = "MISSION CHIEF"
	choices = ["Create Mission", "Create Team", "Update Mission", "Update Team", "View Event Map", "Delete Mission"]
	choice = choicebox(msg, title, choices)


	if(choice == "Create Mission"):
		msg = "Enter mission information"
		title = "CREATE MISSION"
		fieldNames = ["First Name","Last Name","Phone Number","Street Address","City","State","ZipCode", "Availability"]
		fieldValues = []  # we start with blanks for the values
		fieldValues = multenterbox(msg,title, fieldNames)

		# make sure that none of the fields was left blank
		while 1:
			if fieldValues == None: break
			errmsg = ""
			for i in range(len(fieldNames)):
				if fieldValues[i].strip() == "":
					errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
			if errmsg == "": break # no problems found
			fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
		print("Reply was:", fieldValues)
	
else: #SELECTION FOR THE CALL STAFF
	msg = "Choose from the following"
	title = "CALL STAFF"
	choices = ["Create Event Report", "Create Equipment Report", "Create Volunteer Report", "Delete Event", "Delete Equipment", "Delete Volunteer"]
	choice = choicebox(msg, title, choices)
	
	if choice == "Create Event Report":
		msg = "Enter event information"
		title = "EVENT REPORT"
		fieldNames = ["Description","Street Address","City","State","ZipCode", "Phone Number", "Reccomended Equipment", "Priority"]
		fieldValues = []  # we start with blanks for the values
		fieldValues = multenterbox(msg,title, fieldNames)
	
		# make sure that none of the fields was left blank
		while 1:
			if fieldValues == None: break
			errmsg = ""
			for i in range(len(fieldNames)):
				if fieldValues[i].strip() == "":
					errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
			if errmsg == "": break # no problems found
			fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
		print ("Reply was:", fieldValues)
		if fieldValues != "None":
			temploc = (fieldValues[1]+", "+fieldValues[2]+", "+fieldValues[3]+", "+fieldValues[4])
			test.addEvent(loc = temploc, desc = fieldValues[0], prio= fieldValues[7], equip= fieldValues[6] )

	#CREAT EQUIPMENT REPORT BLOCK
	elif choice == "Create Equipment Report":	
		#call staf selection
		msg = "Enter equipment information"
		title = "EQUIPMENT REPORT"
		fieldNames = ["Owner Name","Owner Phone Number","Type", "Description", "Condition", "Location"]
		fieldValues = []  # we start with blanks for the values
		fieldValues = multenterbox(msg,title, fieldNames)
	
		# make sure that none of the fields was left blank
		while 1:
			if fieldValues == None: break
			errmsg = ""
			for i in range(len(fieldNames)):
				if fieldValues[i].strip() == "":
					errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
			if errmsg == "": break # no problems found
			fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
		print ("Reply was:", fieldValues)
		if fieldValues != "None":
			test.addEquipment(desc = fieldValues[3], loc = fieldValues[5], owner = fieldValues[0]+", "+fieldValues[1], cond = fieldValues[4])
	
	#CREATE VOLUNTEER REPORT
	elif choice == "Create Volunteer Report":
		msg = "Enter volunteer information"
		title = "VOLUNTEER REPORT"
		fieldNames = ["First Name","Last Name","Phone Number","Street Address","City","State","ZipCode", "Availability"]
		fieldValues = []  # we start with blanks for the values
		fieldValues = multenterbox(msg,title, fieldNames)
	
		# make sure that none of the fields was left blank
		while 1:
			if fieldValues == None: break
			errmsg = ""
			for i in range(len(fieldNames)):
				if fieldValues[i].strip() == "":
					errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
			if errmsg == "": break # no problems found
			fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
		print ("Reply was:", fieldValues)
