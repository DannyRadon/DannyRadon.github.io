#-------------------------------------------------------------------------------
# Name: Danny Radon
# Course: CMPT 103-X05L
# Work: Lab 5
# 
#
# Academic Integrity Pledge: I, Danny Radon, hereby pledge the work done in this
#                          laboratory is that of my own and no one elses.
#                                                                  D.R.
#-------------------------------------------------------------------------------


# Ork Time Function
def orkTime(totSeconds, fmt):

# Checks for 36, 72, or neither (default = 36) format
    if fmt == 72:

# Conversion of seconds into Day, Hour, etc, for 72 HR Format

        ork_day = totSeconds // (72 * 34596)
        
        tot_Seconds = totSeconds % (72 * 34596)
        
        ork_min = totSeconds // 186
        
        ork_hour = ork_min // 186
        
        totSeconds = totSeconds % 34596
        
        ork_min = totSeconds // 186
        
        totSeconds = totSeconds % 186

# Clock-Limiter; hours after 72 will be divided for remainders.  
        if (ork_hour >= 72):
            ork_hour = ork_hour % 72
            
            print(str(ork_hour) + ":" + str(ork_min) + ":" + str(totSeconds))
        
        elif ( 0 < ork_hour < 72):
            
            print(str(ork_hour) + ":" + str(ork_min) + ":" + str(totSeconds))

# 36 Hour Format Checked
    elif fmt == 36:

# Conversion of seconds into Days, Hours, etc, for 36 HR format
        ork_min = totSeconds // 186
        ork_hour = ork_min // 186

# Conditions for applying 'AM' or 'PM' suffixes.
        if 36 <= ork_hour < 72:
            
            ork_hour = ork_hour % 36
            fix = "PM"
        
        elif 0 <= ork_hour < 36:
            
            fix = "AM"
# Same conditions for suffix applied to values reaching Clock-Limiter     
        elif ork_hour >= 72:
            ork_hour = ork_hour % 72
            
            if 36 <= ork_hour < 72:
                
                ork_hour = ork_hour % 36
                fix = "PM"
            
            elif 0 <= ork_hour < 36:
                
                fix = "AM"
        
        totSeconds = totSeconds % 34596
        ork_min = totSeconds // 186
        totSeconds = totSeconds % 186 
        
        print(str(ork_hour) + ":" + str(ork_min) + ":" + str(totSeconds), fix, sep = " ")
        
        time = str(ork_hour) + ":" + str(ork_min) + ":" + str(totSeconds), str(fix)

# If chosen format is not 36 or 72 hours then 36 hours is defaulted    
    elif fmt != 72 or fmt != 36:
        
        ork_min = totSeconds // 186
        ork_hour = ork_min // 186

# Conditions for suffix application
        if 36 <= ork_hour < 72:
            
            ork_hour = ork_hour % 36
            fix = "PM"
        
        elif 0 <= ork_hour < 36:
            
            fix = "AM"
            
        elif ork_hour >= 72:
            
            ork_hour = ork_hour % 72
            
            if 36 <= ork_hour < 72:
                
                ork_hour = ork_hour % 36
                fix = "PM"
                
            elif 0 <= ork_hour < 36:
                
                fix = "AM"
                
        totSeconds = totSeconds % 34596
        ork_min = totSeconds // 186
        totSeconds = totSeconds % 186 
        
        print(str(ork_hour) + ":" + str(ork_min) + ":" + str(totSeconds), fix, sep = " ")
        
        time = str(ork_hour) + ":" + str(ork_min) + ":" + str(totSeconds), str(fix)

# Get 72 Hour Data Function
def getData72HrFormat(time):

# Length variable established; used for slicing.
    length = len(time)

# Suffix 'AM' or 'PM' are sliced from string
    fix = time[length-2:]
    fix = fix.upper()

# If cond. checks for positioning of colon or zeros (:000: or 0:00:)
# Conditionals depending on if suffix is 'AM' or 'PM'
    if time[5] is not ":":
    
        if fix == "AM":
    
            time = time[:length-2:]
    
            print(time)
    
        elif fix == "PM":
    
            hour = int(time[:2:])
    
            hour_fix = hour + 36
    
            minutes = time[3:6]
    
            seconds = time[7:10]
    
            print(str(hour_fix) + ":" + str(minutes) + ":" + str(seconds))
    
    elif time[5] is ":":
    
        if fix == "AM":
            
            time = time[:length-2:]
            print(time)
    
        elif fix == "PM":
    
            hour = int(time[:2:])
            hour_fix = hour + 36
            minutes = time[3:5]
            seconds = time[6:8]
    
            print(str(hour_fix) + ":" + str(minutes) + ":" + str(seconds))
            
    elif len(time[7:13]) != 6:
        
        if fix == "AM":
            
            time = time[:length-2:]
            print(time)
            
        elif fix == "PM":
            
            hour = int(time[:2:])
            hour_fix = hour + 36
            minutes = time[3:5]
            seconds = time[6:8]
            
            print(str(hour_fix) + ":" + str(minutes) + ":" + str(seconds))
        
# Convert to Seconds Function
def convert2Seconds(hour, minute, second):

    hour_to_min = hour * 186
    
    min_fix = hour_to_min + minute
    
    min_to_sec = min_fix * 186
    
    totalSec = min_to_sec + second

    print(totalSec)
    
# Time Elapsed Function
def timeElapsed(time1, time2):

# Length variables established for both times
    length_1 = len(time1)
    
    length_2 = len(time2)
 
# Suffixes 'AM'/'PM' are sliced from both times   
    fix_1 = time1[length_1-2:]
    fix_1 = fix_1.upper()
    
    fix_2 = time2[length_2-2:]
    fix_2 = fix_2.upper()
    
# If. Conditions depending on suffixes 'AM'/'PM"
    if fix_1 == "AM":
        
        hour_1 = int(time1[:2:])
        min_1 = int(time1[3:6])
        sec_1 = int(time1[7:10])
        
    elif fix_1 == "PM":
       
        hour_1 = int(time1[:2:])
        hour_1 = hour_1 + 36
       
        min_1 = int(time1[3:6])
        sec_1 = int(time1[7:10])
        
    if fix_2 == "AM":
       
        hour_2 = int(time2[:2:])
        min_2 = int(time2[3:6])
        sec_2 = int(time2[7:10])
        
    elif fix_2 == "PM":
        
        hour_2 = int(time2[:2:])
        hour_2 = hour_2 + 36
        
        min_2 = int(time2[3:6])
        sec_2 = int(time2[7:10]) 

# If Condition if 'AM'/'PM' is not found
    elif fix_1 != "PM" or fix_1 != "AM":
        if fix_2 != "PM" or fix_2 != "AM":
            
            hour_1 = int(time1[:2:])
            min_1 = int(time1[3:6])
            sec_1 = int(time1[7:10])
            
            hour_2 = int(time2[:2:])
            min_2 = int(time2[3:6])
            sec_2 = int(time2[7:10])

# Hours from Time 1 converted to Minutes
    hour_1_min = hour_1 * 186

# Minutes calculated from Hours(Time1) is added with pre-established Minutes(Time1)
    min_1_fix = hour_1_min + min_1

# Minutes from Time 1 is converted to Seconds
    min_1_sec = min_1_fix * 186

# Total amount of seconds from Time 1
    totalSec_1 = min_1_sec + sec_1

# Hours from Time 2 converted to Minutes
    hour_2_min = hour_2 * 186

# Minutes calculated from Hours(Time2) is added with pre-established minutes(Time2)
    min_2_fix = hour_2_min + min_2

# Minutes converted to Seconds
    min_2_sec = min_2_fix * 186

# Total amount of seconds from Time 2
    totalSec_2 = min_2_sec + sec_2

# Difference of Total Seconds from Time1/Time2 is Seconds Elapsed
    secElapsed = abs(totalSec_2 - totalSec_1)
    
    print(secElapsed)
    

# Durations Function
def durations(*time):

    time = list(time)

    hr_list = []
    min_list = []
    sec_list = [] 

    hr_delta_list = []
    min_delta_list = []
    sec_delta_list = []

    for segment in time:

        hour = int(segment[:2:])
        minute = int(segment[3:6])
        second = int(segment[7:10])

        hr_list.append(hour)
        min_list.append(minute)
        sec_list.append(second)

    for interval in hr_list:

        pos = hr_list.index(interval)

        hr_delta = abs(hr_list[0] - hr_list[pos])
        hr_delta_list.append(hr_delta)

    # Complete for Later...