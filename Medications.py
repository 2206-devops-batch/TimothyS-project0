# Data Structures containing prescribed medications and their day and time to be taken (Time to take medication: Medications prescribed)
# Moved To Clients.SampleMedList -->
#       from Clients.SampleClientMedList import MedList
#       from Clients.TimothyMedList import MedList

from Clients.TimothyMedList import MedList


# Function that returns the prescribed medications on the given day and time
def get_meds(medlist, day, time):
    # Returning prescribed medications to take on given time (fitting in time range of two hours before and after) and day
    return medlist[day][time]
