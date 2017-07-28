# auins-jdk (autoinstall-jdk)  
```           _                 _     _ _    
   __ _ _   _(_)_ __  ___      (_) __| | | __
  / _` | | | | | '_ \/ __|_____| |/ _` | |/ /
 | (_| | |_| | | | | \__ \_____| | (_| |   < 
  \__,_|\__,_|_|_| |_|___/    _/ |\__,_|_|\_\
                             |__/     
```
Installing and updating Java Development Kit (JDK) on Ubuntu without using a third-party repository (PPA) is quite difficult. This Python tool saves time and effort by automatically installing/updating and configuring Java Development Kit (JDK) for Ubuntu systems.

## Usage
`$ sudo python3 auins-jdk.py <mode> "<path_to_file>"`

### Modes
`--install`: Install JDK for the first time

`--update`: Update previously installed JDK

`<path_to_file>`: Location of the JDK tarball

### Example:
`$ sudo python3 auins-jdk.py --install "jdk-8u141-linux-x64.tar.gz"`

## Notes
- This has been used and tested on Ubuntu 16.04. Although untested, this might be compatible for Debian-based systems and other distributions. 
- `--update` mode can only be used if you previously installed JDK using this tool.
