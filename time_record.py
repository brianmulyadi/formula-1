# Script to record screen time of drivers during broadcast
# test uplink to github

# importing libraries
import time
import pandas as pd

# Timer starts
starttime = time.time()
# laptime = starttime
# lapnum=1

timestamp = []
driver = []

print("Enter driver codes to take timestamps.\nPress CTRL+C to stop")

# alonso - a | bottas - b | charles - c | daniel - d |
# latifi - f | gasly - g | hamilton - h | kimi - k |
# stroll - l | mazepin - m | norris - n | ocon - o |
# perez - p | schumacher - r | sainz - s | tsunoda - t |
# russell - u | vettel - v | max - x | giovinazzi - z |

pause_duration = 0

try:
    while True:
        # Input for the ENTER key press
        driver_input = input()

        if driver_input == "pause":
            pause_time = time.time()
            print("*** PAUSED ***")

        elif driver_input == "resume":
            resume_time = time.time()
            pause_duration = pause_duration + resume_time - pause_time

        else:
            # The current lap-time
            # laptime=round((time.time() - lasttime), 0)

            # Total time elapsed
            # since the timer started
            totaltime=round((time.time() - pause_duration - starttime), 0)

            timestamp.append(str(totaltime))
            driver.append(driver_input)

            # Printing the lap number,
            # lap-time and total time
            # print("Lap No. "+str(lapnum))
            print(f"Drivers: {driver_input}")
            print("Timestamp: "+str(totaltime))
            # print("Lap Time: "+str(laptime))

            print("*"*20)

            # Updating the previous total time
            # and lap number
            # lasttime=time.time()
            # lapnum+=1

# Stopping when CTRL+C is pressed
except KeyboardInterrupt:
    df = pd.DataFrame({'timestamp': timestamp, 'driver': driver})
    df.to_csv('timestamp_styrian2.csv')
    print("Done")
