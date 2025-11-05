#ALGORITHM
#Count the total number of missions
#Count the number of successful missions
#Calculate the success rate
#Generate the list of missions launched before the year 2000
#Print results to the screen

#MISSION LISTS - CREATE REFERENCE LIST VARIABLES
mission_names = ["Apollo 11", "Challenger", "Curiosity Rover", "Viking 1", "Mars Pathfinder", "Hubble Telescope", "Apollo 13"]
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

#MISSION COUNTS AND SUCCESS RATE CALCULATIONS
mission_count = len(mission_names) #count of missions
mission_success_count = int(0) #define variable for successes as integer
for x in mission_success: #for loop to count the number of successes found
    if x == True:
        mission_success_count += 1
mission_success_rate = float(mission_success_count / mission_count) #calculates the success rates
rounded_success_rate = round(mission_success_rate, 4) * 100 #converts success rate to a rounded percent

#MISSIONS PRIOR TO THE YEAR 2000
pre2k_missions = [] #define the list to populate
for n, y in zip(mission_names, mission_years): #for loop to generate a list of mission prior to 2000
    if y < 2000: 
        pre2k_missions.append(n) #save the results to the list

#OUTPUT RESULTS TO SCREEN
print("Total number of missions:", mission_count)
print("Number of successful missions:", mission_success_count)
print("Success rate:", str(rounded_success_rate) + "%")
print("Missions launched before the year 2000:")
for i in pre2k_missions: #for loop to print the list items one at a time with formatting
    print("-", i)