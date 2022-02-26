# New-Discord-Message-Alerter
This python script monitors a specific Discord channel that you specify and alerts you to new messages in that Discord channel.
OK, so 'Monitors' may not be the best term - the script is currently set to just check the Discord channel one time, then quit. You could definitely modify the code, however, so that it runs in a loop at a time interval that you specify.
This would allow you launch the script just once and you're good to go.


## Quick Overview
The way it works is that you launch the Python script and it downloads all messages in the Discord channel (that you specify) into a .txt (text) file that you specify (in the code).
It compares the contents of that .txt file to the contents of the 'old' text file. If they match, then there's no new messages and doesn't really do anything. If the 2 files are different, then there's a new message.
In this case, you can have the script do whatever you want - play a sound, send an email, launch a program, visit a web page, etc. The way I have it currently, it just visits a web page. 
The reason I have it this way is I have an Arduino on my network acting as a web server, and whenever someone accesses it, the Arduino turns a lamp on and off several times to get my attention. 
In the code that I have provided, it just visits my YouTube channel. If I get enough interest in doing what I do with the Arduino, I'll share all of that stuff here.




## Pre-requisites
There are some things you'll need before this software will work:
- A working copy of Python of course, which can be found at: https://www.python.org/downloads/ (Download and install it)
- You'll need the 'requests' package: `pip install requests`
- If when you run the script, it complains about anything else missing, you may need to install it the same way (I can't remember): `pip install packagename`
- Your Discord authorization code/key. It's a little too lengthy/involved to explain here, so let me refer you to the following YouTube video (not me, and I am not affiliated with him): https://www.youtube.com/watch?v=xh28F6f-Cds
- The channel ID of the Discord channel you want to check for new messages in. 
 (To get the Channel ID of the channel you want to check, right-click on the Discord channel name in Discord and choose 'Copy ID' in Discord, then paste it below as the value.
       If 'Copy ID' is not an option, you need to enable 'Developer Mode' under 'Advanced' in your 'User Settings' of Discord)


## Instructions

### The Python script
1. Download the `monitordiscordalerter.py` file located in the `Python` folder in this repository. Place it into a folder of your choosing on your computer's hard drive.
2. Open the `monitordiscordalerter.py` file in a text (i.e. Notepad) or code (i.e. Sublime) editor
3. Look for the following 5 lines of code:
   - `new_file = r"C:\\MyStuff\\DiscordChannelContentsNew.txt"`
   - `old_file = r"C:\\MyStuff\\DiscordChannelContentsOld.txt"`
   - `url_to_visit = 'https://www.youtube.com/user/domiflichi'`
   - `the_channel_id_to_check = 'channelidofdiscordchannelyouwantomonitor'`
   - `discord_authorization_code = 'yourdiscordauthorizationcode'`
4. Change the 'values' of all of those variables to match your needs
5. Save the file, close the editor

Of course if you want your script to do something other than calling a web page, you'll need to update the appropriate area of the code. 



### Make it run!
Depending on how frequently you want it to run, you can just use Window's built-in 'Task Scheduler' to launch your script. If you want it to run more frequently than 
once every 5 minutes, you'll have to find a different task scheduler program.\
\
Additionally, if your computer locks (either manually or automatically...ie after interrupting your screensaver), 'Task Scheduler' probably won't work for you (it didn't for me anyway). 
In this case, I would recommend using a different task scheduler program. I personally use RoboIntern: https://robointern.tech/. It allows you to run something as
frequently as every minute. Also, it successfully runs this script even when the computer is locked.
