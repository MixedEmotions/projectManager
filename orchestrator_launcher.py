#!/usr/bin/python
import glob, os
import subprocess
from datetime import date, timedelta,datetime
JAR_FILE = "MixedEmotionsExampleOrchestrator-assembly-0.15.jar"
MAIN_FILE = "orchestrator.ListFutureOrchestrator"
CONF_FILE = "conf/examplePipeline.conf"
INPUTS_FOLDER  = "/var/data/inputs/projects/"

def main():
    output = open("log/log_small_orchestrator.log", "a")
    print "Starting small orchestrator"
    output.write("[%s]: Starting small orchestrator\n" % now())
    projects = [1,2,3,4,5,8,9,10]
    today = date.today()
    yesterday = today - timedelta(1)
    datestr = yesterday.strftime("%Y-%m-%d")
    for project in projects:
        directory = "%s%s/%s/twitter/" % (INPUTS_FOLDER, datestr, project)
        input_files = get_input_files(directory)
        for input_file in input_files:
            command = "java -cp %s %s %s %s" % (JAR_FILE, MAIN_FILE, CONF_FILE, input_file)
            print "Executing '%s'" % command
            output.write("[%s]: Execution '%s'\n" % (now(), command))
            code = subprocess.call(command.split(" "))
            if code == 0:
                output.write("[%s]: Success!\n"% now())
            else:
                output.write("[%s]: Error!!!!!\n"% now())
    print "----small orchestrator finished"
    output.write("[%s]: Finished\n"% now())

def get_input_files(directory):
    filenames_array = [ filenames for root, dirnames, filenames in os.walk(directory)]
    files  = [val for sublist in filenames_array for val in sublist]
    return ["%s%s" %(directory, file) for file in files if file.endswith(".txt")]

def now():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    

if __name__ == "__main__":
    main()
