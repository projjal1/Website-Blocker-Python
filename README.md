# Website-Blocker-Python
A script to block certain website access from Computer. The scripting is done in Python, and is compatible with Windows and Linux.

## Description
IT administrators always want to restrict internet access in a work environment to certain URLs. Although they use advance DNS and Directory services to accomplish this, many don't.

Also in a multiwork environment like a cyber-cafe this is very much needed. I have written a Python script to emulate this scenario.

Running the Python script will add redirect entries or loopback entries to dns file against such website URLs specified in block_websites file. 

Again I have included a way to block certain websites at particular time interval (called work hour) and not block at certain time(called fun hour). When the script gets out of work hours, it will delete those new entries added to dns config file. Thus enable access.

## Motivation or Improvement 
The enthusiasts are advised to develop on this. What can be done is we can create an executable that run as a process rather than execution as a script from Command Line.

## Instructions 
Make necessary changes to <b>block_hours.txt</b> as needed. 

<b>Note "work hours" refer to start time of blocking sites, and "free" refers to end of blocking URLs.</b>

The sites that need to be blocked can be added as an entry in seperate lines in <b>block_sites.txt</b>

## Dependencies
<ul>
  <li>Python 3.5+</li>
  <li>Windows Host, Linux Host</li>
  <li>Terminal to execute script from</li>
</ul>

## OS Compatibility
Linux and Windows Host 

## Execution Instructions 
Run the script from directory using command:
<pre>python script.py</pre>
