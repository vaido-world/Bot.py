# List all exported Environment Variables of Current Shell 
# export -p 
# env
# printenv

# Kill the bot
FILE="~/.discord_bot_pid.txt"
if test -f "$FILE"; then
	kill -9 `cat $FILE`
	rm "$FILE"
fi

#kill -9 `cat save_pid.txt`
#rm save_pid.txt