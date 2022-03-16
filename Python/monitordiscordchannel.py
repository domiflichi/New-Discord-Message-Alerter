import requests, json, filecmp, os, shutil, urllib.request

#
# Found out how to read from a Discord channel in Python from this YouTube video:
#   It contains important info such as how to get your authorization code/key that you need for this script to work
#   https://www.youtube.com/watch?v=xh28F6f-Cds
# 
# 
# Self note - it appears that this code shows the newest message first and works it way backwards
# 
#
# I thought about just comparing the last message (instead of the whole thread/channel), but what if the last 2 messages were the same? (Not likely, but possible I suppose)
# But then again, downloading/comparing the whole thread/room could get big. Or does it only download so many days with? If this happens, we may get false positives.
# Maybe try just the last 5 messages instead?
# (Just something to keep in mind for the future)
#


new_file = r"C:\\MyStuff\\DiscordChannelContentsNew.txt" # our text file that we dump all messages from the Discord channel to
old_file = r"C:\\MyStuff\\DiscordChannelContentsOld.txt" # our text file that contains the previous contents

url_to_visit = 'https://www.youtube.com/user/domiflichi' # Can be any web page you want. This is just a test/example

# This is the Discord channel ID of the channel that you want to monitor and alert you of new messages in
#   To get the Channel ID of the channel you want to check, right-click on the Discord channel name in Discord and choose 'Copy ID' in Discord, then paste it below as the value
#       (If 'Copy ID' is not an option, you need to enable 'Developer Mode' under 'Advanced' in your 'User Settings' of Discord)
the_channel_id_to_check = 'channelidofdiscordchannelyouwantomonitor' 

# To learn how to retrive your authorization code/key (this is a bit more involved/tricky), please watch the YouTube video linked at the top of this script
#   Disclaimer - I have no affiliation with the person that created that video.
discord_authorization_code = 'yourdiscordauthorizationcode'



# this is the function that actually reads the Discord channel
def retrieve_messages(channelid):
    headers = {
        'authorization': discord_authorization_code
    }
    r = requests.get(f'https://discord.com/api/v8/channels/{channelid}/messages', headers=headers)
    jsonn = json.loads(r.text)

    with open(new_file, 'w', encoding="utf-8") as f: # Open up our 'new_file' for writing
        for value in jsonn: # loop through the contents of each json message entry
            #print(value, '\n') # this shows the entire json content for each json message - we don't want to see the whole raw json message
            #print(value['content'], '\n') #this one shows just the 'content' value for each json message
            f.writelines(value['content'] + '\n') # write the value of the 'content' key, and also a line break (\n) at the end


# Call the above function to retrieve the messages from the Discord channel, passing it the channel id we want to read from
retrieve_messages(the_channel_id_to_check)


if os.path.isfile(old_file): # Check to see if the 'old_file' exists. If it does, then continue
    # 'old_file' exists!
    result = filecmp.cmp(new_file, old_file, shallow=False) # Compare the 2 files in 'deep mode'

    if result: # 'result' = True
        print("Match - no new messages :(") # If the contents of 'new_file' and 'old_file' are the same, that means no new Discord messages have come in
        # Nothing really to do here
    else: # 'result' = False. | If the contents are different, then we know a new message came in!
        # ****************** THIS BLOCK IS WHERE ALL THE ACTION IS!!! PLACE WHATEVER YOU WANT TO DO AFTER A NEW DISCORD MESSAGE ARRIVES IN HERE!!! *******************
        # ****************** You can do whatever you want in this block. i.e. play a sound, launch a program, create a file, etc. Get creative! **********************
        print("No match = new message!") # Print to the console that we have a new message
        webUrl = urllib.request.urlopen(url_to_visit) # open a connection to a URL using urllib
        # get the result code and print it
        print("result code: " + str(webUrl.getcode())) # A successful call to a webpage/site will result in code 200 - so that's what we want to see!
        shutil.copyfile(new_file, old_file) # Now we want to duplicate the contents of 'new_file' to 'old_file' file by copying the file
        # Nothing left to do now!
        # ******************* END ACTION BLOCK ************************************************************************************************************************
else: # 'old_file' doesn't exist, so we're gonna create one!
    print("'DiscordChannelContentsOld.txt' does not exist! First time run?") # Print to the console that 'old_file' doesn't exist yet and it could be because this is the first time this script has been run
    print("Creating 'DiscordChannelContentsOld.txt' (duplicating 'DiscordChannelContentsNew.txt' to 'DiscordChannelContentsOld.txt')...") # Tell the user we're going to create an 'old_file' now
    shutil.copyfile(new_file, old_file) # This was probably the first time this script was ran, so we need to create the 'DiscordChannelContentsOld.txt' file by copying the 'DiscordChannelContentsNew.txt'
    print("'DiscordChannelContentsOld.txt' created from 'DiscordChannelContentsNew.txt' - ready to go!") # Tell the user that we created the 'old_file' now

print() # Print a blank line to the console for better visual
print("All done. Goodbye!") # End of script, see you later!