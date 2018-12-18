from easygui import *


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
  if errmsg == "": break # no problems found
  fieldValues = multpasswordbox(errmsg, title, fieldNames, fieldValues)
print "Reply was:", fieldValues




msg = "Choose from the following"
title = "CALL STAFF"
choices = ["Create Event Report", "Create Equipment Report", "Create Volunteer Report", "Delete Event", "Delete Equipment", "Delete Volunteer"]
choice = choicebox(msg, title, choices)




msg = "Enter event information"
title = "EVENT REPORT"
fieldNames = ["Name","Street Address","City","State","ZipCode", "Phone Number" "Description", "Priority"]
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
print "Reply was:", fieldValues


msg = "Enter equipment information"
title = "EQUIPMENT REPORT"
fieldNames = ["Owner Name","Owner Phone Number","Type", "Description", "Condition"]
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
print "Reply was:", fieldValues


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
print "Reply was:", fieldValues


msg = "Choose from the following"
title = "MISSION CHIEF"
choices = ["Create Mission", "Create Team", "Update Mission", "Update Team", "View Event Map", "Delete Mission"]
choice = choicebox(msg, title, choices)



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
print "Reply was:", fieldValues