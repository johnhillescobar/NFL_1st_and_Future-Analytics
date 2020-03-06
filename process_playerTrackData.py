import csv
import time
import datetime

# #############################################
# METHOD TO CEATE A FILE WITH ALL THE INJURY PLAYS

# ARRAY WITH THE ID OF PLAYS NEEDED
PlayKey = ['39873-4-32','46074-7-26','36557-1-70','46646-3-30','43532-5-69','41145-2-60','46014-10-22','44860-5-52','44806-7-61','45962-8-40','46331-4-44','36621-13-58','44492-3-23','43505-2-49','41094-1-55','40474-1-8','39656-2-38','46587-2-13','46119-3-16','38364-5-23','45966-4-27','35611-7-42','44434-10-31','44489-11-32','44511-5-41','43826-7-12','43518-6-25','34347-5-9','41943-1-12','41209-9-9','44900-7-10','31070-3-7','38228-1-4','39956-2-14','45950-8-18','43540-3-14','44440-6-18','44449-6-13','42406-6-13','42637-3-6','46430-8-6','38192-8-8','39678-2-1','39850-9-2','43540-7-2','42600-3-1','42456-20-76','46038-30-58','41113-15-63','47235-7-55','47382-3-34','44421-12-41','42348-23-53','42398-15-33','36559-12-65','47220-4-16','47813-8-19','35570-15-35','44482-20-21','44449-28-35','38876-29-14','46098-17-27','36607-16-19','44542-13-20','45983-18-21','33474-19-7','47287-4-16','33337-8-15','47307-10-18','47307-10-18','43672-8-9','46316-5-4','42418-19-15','46394-18-3','45187-9-4','42448-14-3','47334-8-1']

# OPEN THE FILE FOR WRITING - RESULTING FILE
with open('injuryPlay.csv', 'w', newline='') as csvfile:
    # DECLARE THE WRITER
    writer = csv.writer(csvfile, delimiter=',')

    # OPEN THE FILE CONTAININ THE DATA (BIG MF FILE)
    with open('data/PlayerTrackData.csv','r') as csv_file:
        # DECLARE THE READER
        reader = csv.reader(csv_file)

        # INIT A TIMER TO RECORD THE TIME TAKEN TO PROCESS THE FILE
        started = time.time()
        print("Training started at {}".format(datetime.datetime.now()))
        
        # INIT A LINE COUNTER
        lines = 0

        # FOR EACH ROW IN READER OBJECT -> ROW IS AN ARRAY OF EACH OF THE COLUMNS ->
        for row in reader:
            # IF ITS FIRST LINE WRITE IT 
            if(lines == 0): 
                # - WRITE THE COLUMN HEADERS 
                writer.writerow(row)
            # IF FIRST ITEM OF THE LINE ARRAY IS IN THE PlayKey ARRAY WE PRINT ON THE SCREEN AND WRITE IN THE FILE
            elif(row[0] in PlayKey):
                print(row)
                writer.writerow(row)

            # KEEP COUNTING LINES
            lines = lines + 1

# SET THE EN TIMER
ended = time.time()

# PRINT THE RESULTS
print("Lines: " + str(lines))
print("Training ended at {}".format(datetime.datetime.now()))
elapsed_time = ended - started
print("Training completed in {:.0f}m {:.0f}s".format(elapsed_time // 60, elapsed_time % 60))
