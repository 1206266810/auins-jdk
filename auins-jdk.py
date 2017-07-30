#!/usr/bin/env python
import sys, tarfile, shutil, fileinput

# auins-jdk (c) saojeda (github.com/saojeda)
# Licensed under MIT license

splash = '''
              _                 _     _ _    
   __ _ _   _(_)_ __  ___      (_) __| | | __
  / _` | | | | | '_ \/ __|_____| |/ _` | |/ /
 | (_| | |_| | | | | \__ \_____| | (_| |   < 
  \__,_|\__,_|_|_| |_|___/    _/ |\__,_|_|\_\\
                             |__/            
'''
print(splash)

if not (sys.argv[1] == "--install" or sys.argv[1] == "--update"): 
    print("- ERROR: No valid installation mode specified!")
    quit()

# Access and extract tarball
try: tar = tarfile.open(sys.argv[2])
except:
    print("- ERROR: Failed to access \"{}\"!".format(sys.argv[2]))
    quit()

print("+ Extracting \"{}\"...".format(sys.argv[2]))
tar.extractall()  
extfname = tar.getnames() # Obtain directory names (stored in a list)
tar.close()	

java_home = "/usr/lib/jvm/oracle-java-8"

# If in update mode, remove existing java directory 
if sys.argv[1] == "--update":
    print("+ Removing \"{}\"...".format(java_home))
    shutil.rmtree(java_home, ignore_errors=True)

# Move contents to /usr/lib directory
print("+ Moving \"{}\" to \"{}\"...".format(extfname[0],java_home))
shutil.move(extfname[0],java_home) # extfname[0] accesses the root folder of the tarball

# If in install mode, add environment variables to /etc/environment
#Create a backup first and then iterate throughout the environment file
if sys.argv[1] == "--install":
    envpath = "/etc/environment"
    print("+ Creating backup \"{}.bak\"...".format(envpath))
    print("+ Appending environment variables to \"{}\"...".format(envpath)) 
    first = True
    for line in fileinput.FileInput(envpath, inplace=True, backup=".bak"):
	    if first:
                    print("{}:{}/bin\"".format(line[:-2],java_home)) # Modify first line only
                    first = False
	    else: print(line, end="")

    # Access environment file for appending
    envf = open(envpath, "a")

    # Append additional variables
    envf.write("JAVA_HOME=\"{}\"\n".format(java_home))
    envf.write("JRE_HOME=\"{}/jre\"\n".format(java_home))
    envf.close()
    print("+ Installation successful!")
else:
    print("+ Update successful!")

print("+ NOTE: Please log out/reboot for changes to apply.")
