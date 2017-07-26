# auins-jdk (autoinstall-jdk)  
```              _                 _     _ _    
   __ _ _   _(_)_ __  ___      (_) __| | | __
  / _` | | | | | '_ \/ __|_____| |/ _` | |/ /
 | (_| | |_| | | | | \__ \_____| | (_| |   < 
  \__,_|\__,_|_|_| |_|___/    _/ |\__,_|_|\_\
                             |__/     
```
Installing Java Development Kit (JDK) on Ubuntu without using a third-party repository (PPA) is quite difficult. This Python tool saves time and effort by automatically installing and configuring Java Development Kit (JDK) for Ubuntu systems.

## Features
- `wget`-based downloader 
- parchive (tarball) handling
- automatic `/etc/environment` configuration
- uses only standard Python modules

## Dependencies
NOTE: Everything listed here is already included in a standard Ubuntu installation
- wget
- python 3

## Usage
`$ sudo python3 auins-jdk.py`

### Modes of installation

**For online:**

1. Go to the JDK download page (http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
2. Select your Java SE Development Kit package and copy its link.
3. Use this link by pasting it when requested by the program.

**For offline:**

Place your downloaded JDK package (in tarball) in the same directory with the program.


### Additional notes
- For safety, a backup named `environment.bak` for `/etc/environment` is created before it is modified.
- This has been used and tested on Ubuntu 16.04. It is recommended to use this on a system
without any previous attempts in JDK installation (i.e. newly-installed OS.) Doing so ensures that the
`/etc/environment` file is not yet heavily modified and the directories/files that will be moved to `/usr/lib`
will not conflict with any JDK related-files created prior to usage.
