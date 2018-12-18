import pymysql
from geopy.geocoders import Nominatim

def getConnection():
	return pymysql.connect(host='localhost',
	user='root',
	password='bigButts',
	db='test')

conn = getConnection()
cursor = conn.cursor()

#inserts a person into the database
def addPerson(commit = False):	
	try:
		#first_name = input("Input new first_name: ")
		first_name = "FName 1"
		#last_name = input("Input new last_name: ")
		last_name = "LName 1"
		#phone = input("Input new PhoneNumber: ")
		phone = "111222333"
			
		#Create a new record
		query = "INSERT INTO `Person` (`FirstName`,`LastName`, `PhoneNumber`)  VALUES ('" + first_name + "', '" + last_name + "','" + phone + "');"
		
		cursor.execute(query)
		newPersId = conn.insert_id()
		
		if(commit == True):
			conn.commit()
			
		return  newPersId
		
	except Exception:
		print("Error in addPerson")
#updates a person's information
def updatePerson(passedId, fn = "null", ln = "null", pn = "null"):
	try:
		if fn != "null":
			query = "update person set firstName = '"+fn+"' where Person_ID = +'"+str(passedId)+"';"
			cursor.execute(query)
		if ln != "null":
			query = "update person set lastName = '"+ln+"' where Person_ID = +'"+str(passedId)+"';"
			cursor.execute(query)
		if pn != "null":
			query = "update person set phoneNumber = '"+pn+"' where Person_ID = +'"+str(passedId)+"';"
			cursor.execute(query)
		conn.commit()
	except Exception:
		print("Error in updatePerson")
#inserts an employee into the database
def addEmp(passedId, commit = False):
	#check if using an existing person or a new person is to be created
	if passedId <= 0:
		newPersId = addPerson()
	else:
		newPersId = passedId
		
	try:
		#username = input("Input new username: ")
		username = "test1"
		#password = input("Input new password: ")
		password = "pass1"
		
		# Create a new record
		query = "INSERT INTO `Employee` (`Person_ID`, `username`,`password`)  VALUES ( "+ str(newPersId) +", '" + username + "', '" + password + "');"
	
		cursor.execute(query)
		newEmpId = conn.insert_id()
		if(commit == True):
			conn.commit()
		return newEmpId

	except Exception:
		print("Error in addEmp")
#updates an employee's information
def updatePerson(passedId, un = "null", pw = "null"):
	try:
		if un != "null":
			query = "update employee set username = '"+un+"' where Employee_ID = +'"+str(passedId)+"';"
			cursor.execute(query)
		if pw != "null":
			query = "update employee set password = '"+pw+"' where Employee_ID = +'"+str(passedId)+"';"
			cursor.execute(query)
		conn.commit()
	except Exception:
		print("Error in updatePerson")
		
#inserts a call staff employee into the database
def addCallStaff(passedId):
	#check if using an existing employee or a new employee is to be created
	if passedId <= 0:
		newEmpId = addEmp()
	else:
		newEmpId = passedId
	
	try:
		newEmpId = addEmp()
		query = "INSERT INTO `CallStaff` (`Employee_ID`)  VALUES ( "+ str(newEmpId) +");"
		cursor.execute(query)
		newStaffId = conn.insert_id()
		conn.commit()
		
		return  newStaffId
		
	except Exception:
		print("Error in addCallStaff")	

#inserts a missionchief into the database
def addMissionChief(passedId):
	#check if using an existing employee or a new employee is to be created
	if passedId <= 0:
		newEmpId = addEmp()
	else:
		newEmpId = passedId
	
	try:
		newEmpId = addEmp()
		query = "INSERT INTO `MissionChief` (`Employee_ID`)  VALUES ( "+ str(newEmpId) +");"
		cursor.execute(query)
		newChiefId = conn.insert_id()
		conn.commit()
		
		return  newChiefId
		
	except Exception:
		print("Error in addMissionChief")	

#inserts a volunteer into the database
def addVolunteer(passedId):
	
	if passedId <= 0:
		newPersId = addPerson()
	else:
		newPersId = passedId
	
	#avail = input("Input availability: ")
	avail = "10am to 5pm"
	
	try:
		query = "INSERT INTO `Volunteer` (`availability`, `Person_ID`, Team_ID)  VALUES ( '"+avail+"', "+ str(newPersId)+", null);"
		cursor.execute(query)
		newVolId = conn.insert_id()
		conn.commit()
		
		return  newVolId
		
	except Exception:
		print("Error in addVolunteer")
#removes an volunteer from the database
def removeVolunteer(passedId):
	try:
		query = "Delete From `Volunteer` Where Volunteer_ID = "+str(passedId)+";"
		cursor.execute(query)
		conn.commit()
		
	except Exception:
		print("Error in removeVolunteer")

#inserts a new equipment into the database
def addEquipment():
	#desc = input("Input description: ")
	desc = "Boat"
	#loc = input("Input current location: ")
	loc = "8475 West Hill Street, Baltimore"
	#owner = input("Input Contact information for the Owner: ")
	owner = "Michael James, 443-444-7786"
	#cond = input("Input current condition of the item: ")
	cond = "Fully functioning, a few scratches"
	
	try:
		query = "INSERT INTO `Equipment` (`description`, `location`, `ownerInfo`, `condition`)  VALUES ( '"+desc+"', '"+loc+"', '"+owner+"', '"+cond+"');"
		cursor.execute(query)
		newEquipId = conn.insert_id()
		conn.commit()
		
		return  newEquipId
		
	except Exception:
		print("Error in addEquipment")		
#removes an equipment from the database
def removeEquipment(passedId):
	try:
		query = "Delete From `Equipment` Where Equipment_ID = "+str(passedId)+";"
		cursor.execute(query)
		conn.commit()
		
	except Exception:
		print("Error in removeEquipment")

#inserts a new event into the database
def addEvent():
	#loc = input("Input location as an address: ")
	loc = "4700 Gateway Terrace, Arbutus Md"
	geolocator = Nominatim(user_agent="software_proj")
	location = geolocator.geocode(loc)
	
	#print(location.address)
	#print((location.latitude, location.longitude))
	#print(location.raw)
	
	#desc = input("Input description of the event: ")
	desc = "Ive fallen and I cant get up"
	#prio = input("Input Priority of the event: ")
	prio = "medium"
	status = "new"
	#equip = input("List special equipment that might be needed:")
	equip = "Ambulance"
	
	try:
		query = "INSERT INTO `Event` (`location`, `description`, `priority`, `status`, `equipNeeded`, `lat`, `long`)  VALUES ( '"+location.address+"', '"+desc+"', '"+prio+"', '"+status+"', '"+equip+"', "+str(location.latitude)+", "+str(location.longitude)+");"
		cursor.execute(query)
		newEventId = conn.insert_id()
		conn.commit()
		
		return  newEventId
		
	except Exception:
		print("Error in addEvent. Make sure you are using a valid address")		
#removes an event from the database
def removeEvent(passedId):
	try:
		query = "Delete From `Event` Where Event_ID = "+str(passedId)+";"
		cursor.execute(query)
		conn.commit()
		
	except Exception:
		print("Error in removeEvent")

#inserts a new team into the database
def addTeam():
	try:
		query = "INSERT INTO `Team` VALUES ();"
		cursor.execute(query)
		newTeamId = conn.insert_id()
		conn.commit()
		
		return  newTeamId
		
	except Exception:
		print("Error in addTeam")	
#removes a team from the database
def removeTeam(passedId):
	try:
		query = "Delete From `Team` Where Team_ID = "+str(passedId)+";"
		cursor.execute(query)
		conn.commit()
		
	except Exception:
		print("Error in removeTeam")

#adds a team to a mission
def addTeamAssignment(volId, teamId):
	try:
		query = "INSERT INTO `TeamAssignments` (`Volunteer_ID`, `Team_ID`) VALUES ("+str(volId)+", "+str(teamId)+");"
		cursor.execute(query)
		conn.commit()
		
	except Exception:
		print("Error in addTeamAssignment")
#removes a team from a mission
def removeTeamAssignment(volId, teamId):
	try:
		query = "Delete From `TeamAssignments` Where Team_ID = "+str(teamId)+" And Volunteer_ID = "+str(volId)+";"
		cursor.execute(query)
		conn.commit()
		
	except Exception:
		print("Error in removeTeamAssignment")

#adds a mission into the database
def addMission():
	try:
		query = "INSERT INTO `Mission` (`timeSinceAssigned`, `timeCreated`, `priority`, `status`) VALUES ( null, current_timestamp(), null, 'new');"
		cursor.execute(query)
		newMissionId = conn.insert_id()
		conn.commit()
		
		return  newMissionId
		
	except Exception:
		print("Error in addMission")
#removes a mission from the database
def removeMission(passedId):
	try:
		query = "Delete From `Mission` Where Mission_ID = "+str(passedId)+";"
		cursor.execute(query)
		conn.commit()
		
	except Exception:
		print("Error in removeMission")

#assigns a team to a mission
def addIsOn(teamId, missId):
	try:
		query = "INSERT INTO `is_on` (`Team_ID`, `Mission_ID`) VALUES ("+str(teamId)+", "+str(missId)+");"
		cursor.execute(query)
		conn.commit()
		
	except Exception:
		print("Error in addIsOn")
#removes a team from a mission
def removeIsOn(teamId, missId):
	try:
		query = "Delete From `is_on` Where Team_ID = "+str(teamId)+" And Mission_ID = "+str(missId)+";"
		cursor.execute(query)
		conn.commit()
		
	except Exception:
		print("Error in removeIsOn")

#add an event into the mission's list of events
def addEventList(eventId, missId):
	try:
		query = "INSERT INTO `EventList` (`Event_ID`, `Mission_ID`) VALUES ("+str(eventId)+", "+str(missId)+");"
		cursor.execute(query)
		conn.commit()
		
	except Exception:
		print("Error in addEventList")
#removes an event from a mission
def removeEventList(eventId, missId):
	try:
		query = "Delete From `EventList` Where Event_ID = "+str(eventId)+" And Mission_ID = "+str(missId)+";"
		cursor.execute(query)
		conn.commit()
		
	except Exception:
		print("Error in removeEventList")


#add a new equipment to the mission's list of equipment
def addEquipmentList(equipId, missId):
	try:
		query = "INSERT INTO `EquipmentList` (`Equipment_ID`, `Mission_ID`) VALUES ("+str(equipId)+", "+str(missId)+");"
		cursor.execute(query)
		conn.commit()
		
	except Exception:
		print("Error in addEventList")
#removes equipment from a mission
def removeEquipmentList(equipId, missId):
	try:
		query = "Delete From `EquipmentList` Where Equipment_ID = "+str(equipId)+" And Mission_ID = "+str(missId)+";"
		cursor.execute(query)
		conn.commit()
		
	except Exception:
		print("Error in removeEquipmentList")

updatePerson(1, pn = "")


