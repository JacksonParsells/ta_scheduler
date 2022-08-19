# takes feedback from a google form and parses the resulting csv file

# to get started, make sure you've installed the following packages using pip:
#  - tkinter

# @author Sydney Nepo
# @author Jackson Parsells

# use tkinter to make it interactive baybeee
import tkinter as tk

# for csv parsing
# csv expected format:
# Name, Minimum hours per week, Maximum hours per week, Time Availability. Please fill this out with your current schedule. If your schedule changes we'll definitely find accommodation. Keep in mind that Monday/Tuesday are the high traffic days for OH.  [9:00am-10:15am], Time Availability. Please fill this out with your current schedule. If your schedule changes we'll definitely find accommodation. Keep in mind that Monday/Tuesday are the high traffic days for OH.  [10:30am-11:45am], Time Availability. Please fill this out with your current schedule. If your schedule changes we'll definitely find accommodation. Keep in mind that Monday/Tuesday are the high traffic days for OH.  [12:00pm-1:15pm], Time Availability. Please fill this out with your current schedule. If your schedule changes we'll definitely find accommodation. Keep in mind that Monday/Tuesday are the high traffic days for OH.  [1:30pm-2:45pm], Time Availability. Please fill this out with your current schedule. If your schedule changes we'll definitely find accommodation. Keep in mind that Monday/Tuesday are the high traffic days for OH.  [3:00pm-4:15pm], Time Availability. Please fill this out with your current schedule. If your schedule changes we'll definitely find accommodation. Keep in mind that Monday/Tuesday are the high traffic days for OH.  [4:30pm-5:45pm], Time Availability. Please fill this out with your current schedule. If your schedule changes we'll definitely find accommodation. Keep in mind that Monday/Tuesday are the high traffic days for OH.  [6:00pm-7:15pm], Time Availability. Please fill this out with your current schedule. If your schedule changes we'll definitely find accommodation. Keep in mind that Monday/Tuesday are the high traffic days for OH.  [7:30pm-8:45pm], Time Availability. Please fill this out with your current schedule. If your schedule changes we'll definitely find accommodation. Keep in mind that Monday/Tuesday are the high traffic days for OH.  [9:00pm-10:15pm], How willing are you to hold virtual office hours?, Are you a first time TA? (if so, welcome!), How willing are you to lead lab? (note: if this is your first semester as a TA, you cannot be a lab leader this term), If your answer to the above was greater than 0, which labs would you want to lead (all labs are on Wednesday), Please list any other preferences (preferred times, days, people to work with, etc...), What are you most excited for in CS11 this semester? (personally I am looking forward to working in Cummings since I wasn't here last spring. yay windows!), Any other comments or questions? Any accommodations that you'd like me to try to arrange (I'll try my best 😊)
import csv

# constants for time stuff ig
OFFICE_HOUR_BLOCK_LENGTH_MIN = 75
LAB_BLOCK_LENGTH_MIN = 75

# classes for block and student
class block:
    """
    block object
    """
    def __init__(self, id):
        self.id = id
        self.committedTAs = [] # list of TAs who have committed to this block
        self.availableTAs = [] # list of TAs who are available to work on this block
        self.isFull = False # whether or not this block is full
    
    def addCommittedTA(self, ta):
        self.committedTAs.append(ta)
    
        ta.addCommittedBlock(self, OFFICE_HOUR_BLOCK_LENGTH_MIN)
        
        if len(self.committedTAs) == 2:
            self.isFull = True
    
    def removeCommittedTA(self, ta):
        self.committedTAs.remove(ta)
        
        ta.removeCommittedBlock(self, OFFICE_HOUR_BLOCK_LENGTH_MIN)
        
        if len(self.committedTAs) < 2:
            self.isFull = False
    
    def addAvailableTA(self, ta):
        self.availableTAs.append(ta)

    def removeAvailableTA(self, ta):
        self.availableTAs.remove(ta)

class student:
    """
    student object
    """
    def __init__(self, name, minHours, maxHours, timeAvailabilityMap, willingnessToLeadLab, isNewTA, isWillingToHoldVirtualOfficeHours, preferences):
        self.name = name
        self.minHours = minHours
        self.maxHours = maxHours
        self.currentHours = 0 # "accumulated" hours for each TA
        self.availableBlocks = timeAvailabilityMap # list of blocks that are available to work on
        self.committedBlocks = [] # list of blocks that this student has committed to
        self.isLabLead = False
        self.willingnessToLeadLab = willingnessToLeadLab
        self.isWillingToHoldVirtualOfficeHours = isWillingToHoldVirtualOfficeHours
        self.isNewTA = isNewTA
        self.needsShift = False
        self.canAddShift = True
        self.preferences = preferences
    
    def addCommittedBlock(self, block, hours):
        self.currentHours += hours
        self.committedBlocks.append(block)
    
    def removeCommittedBlock(self, block, hours):
        self.committedBlocks.remove(block)
        self.currentHours -= hours

# actual functions :")

def get_csv_fields(csv_file_name):
    """
    construct a student object
    """
    students = []

    with open(csv_file_name, 'r') as csvfile:
        #  read each field from the csv file and construct a student object for each row
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            # skip the header row
            if i == 0:
                continue

            # destructure row into variables
            name = row[1]
            minHours = int(row[2])
            maxHours = int(row[3])
            timeAvailability1 = row[4]
            timeAvailability2 = row[5]
            timeAvailability3 = row[6]
            timeAvailability4 = row[7]
            timeAvailability5 = row[8]
            timeAvailability6 = row[9]
            timeAvailability7 = row[10]
            timeAvailability8 = row[11]
            timeAvailability9 = row[12]
            isWillingToHoldVirtualOfficeHours = row[13]
            isNewTA = row[14]
            willingnessToLeadLab = row[15]
            preferences = row[17]

            # construct a student object
            timeAvailabilityMap = {
                "9:00am-10:15am": timeAvailability1,
                "10:30am-11:45am": timeAvailability2,
                "12:00pm-1:15pm": timeAvailability3,
                "1:30pm-2:45pm": timeAvailability4,
                "3:00pm-4:15pm": timeAvailability5,
                "4:30pm-5:45pm": timeAvailability6,
                "6:00pm-7:15pm": timeAvailability7,
                "7:30pm-8:45pm": timeAvailability8,
                "9:00pm-10:15pm": timeAvailability9
            }
            currStudent = student(name, minHours, maxHours, timeAvailabilityMap, willingnessToLeadLab, isNewTA, isWillingToHoldVirtualOfficeHours, preferences)
            
            # add the student to the list of students
            students.append(currStudent)

    return students

def load_calendar():
    pass

# main(e)

def main():
    """
    beep boop, fill in main here
    """
    get_csv_fields('TAAvailability.csv')


if __name__ == '__main__':
    main()
