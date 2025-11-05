#ALGORITHM
#Count the total number of missions
#Count the number of successful missions
#Calculate the success rate
#Generate the list of missions launched before the year 2000
#Print results to the screen

#MISSION LISTS
mission_names = ["Apollo 11", "Challenger", "Curiosity Rover", "Viking 1", "Mars Pathfinder", "Hubble Telescope", "Apollo 13"]
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

#MISSION COUNTS AND SUCCESS RATE CALCULATIONS
mission_count = len(mission_names)
mission_success_count = int(0)
for x in mission_success:
    if x == True:
        mission_success_count += 1
mission_success_rate = float(mission_success_count / mission_count)
rounded_success_rate = round(mission_success_rate, 4) * 100

#MISSIONS PRIOR TO THE YEAR 2000
pre2k_missions = []
for x in mission_years:
    if x > 2000: 
        pre2k_missions.extend(mission_names)

#OUTPUT RESULTS TO SCREEN
print("Total number of missions:", mission_count)
print("Number of successful missions:", mission_success_count)
print("Success rate:", str(rounded_success_rate) + "%")
print("Missions launched before the year 2000:")
for i in pre2k_missions: 
    print("-", i)

#print(pre2k_missions)