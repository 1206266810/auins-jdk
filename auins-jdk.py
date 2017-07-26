#!/usr/bin/env python
import os, tarfile, shutil, fileinput

# auins-jdk (c) saojeda (saojeda.github.com)
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

# URL validation heuristics
def eval_link(link):
	if "download.oracle.com" and ".tar.gz" in link: return True
	else: return False

# Error handling
def force_term(num):
	emsg = {
		1 : "Download",
		2 : "File access"	
	}
	print(esmg[num] + " error. Terminated.")
	exit()

print("Choose installation type: \n[1] Online \n[2] Offline")

resp = int(input("Enter response: "))
while resp != 1 and resp != 2:
	resp = int(input("Enter response: "))

if resp == 1:
	rlink = input("Enter JDK download link: ")
	while not eval_link(rlink): rlink = input("Enter JDK download link: ")
	
	# Extract filename from link
	i = 0
	for x in reversed(rlink): # Start from the last element
		if x == "/": break # Find the first occurence of "/" (indicates end of filename block)
		i -= 1 # Count position

	filename = rlink[i:] # Slice string starting from the obtained position	

	# Prepare wget arguments
	wget_args = "wget -c --header \"Cookie: oraclelicense=accept-securebackup-cookie\" " + rlink
	# Execute wget and check wget's exit code: terminate program if not successful, continue otherwise
	if os.system(wget_args) != 0: force_term(1)
else:	
	filename = input("Enter file name: ")
	while not ".tar.gz" in filename: filename = input("Enter file name: ")	

# Access tarball
try: tar = tarfile.open(filename)
except: force_term(2)

tar.extractall() # Extract contents
extfname = tar.getnames() # Obtain directory names (stored in a list)
tar.close()	

# Move contents to /usr/lib directory
java_home = "/usr/lib/jvm/oracle-java-8"
shutil.move(extfname[0], java_home) # extfname[0] accesses the root folder of the tarball

# Create a backup first and then iterate throughout the environment file
first = True
envpath = "/etc/environment"
for line in fileinput.FileInput(envpath, inplace=True, backup=".bak"):
	if first: 
		print(line[:-2] + ":" + java_home + "/bin\"")  # Alter first line only
		first = False
	else: print(line, end="")

# Access environment file for appending
try: pfile = open(envpath, "a")
except: force_term(2)

# Append additional variables
pfile.write("JAVA_HOME=" + java_home + "\n")
pfile.write("JRE_HOME=" + java_home + "/jre" + "\n")
pfile.close()

# Cleanup
os.remove(filename)

print("Installation successful!")
print("NOTE: Please log out/reboot for changes to apply.")
