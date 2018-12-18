from easygui import *


msg = "Enter logon information"
title = "Demo of multpasswordbox"
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
