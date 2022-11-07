# Remember to chmod this file for execution: X (0755)
# /etc/profile.d

# cat ~/.discord_bot_pid.txt

# Before running, Kill the bot if already running.
FILE="~/.discord_bot_pid.txt"
if test -f "$FILE"; then
	kill -9 `cat $FILE`
	rm "$FILE"
fi

nohup python3 "./bot.py" > bot.log 2>&1 &

# Sets Process ID to User Environment Variable
# export discord_bot_pid="$!"
# echo $discord_bot_pid

# Save Process ID to Text File.
echo $!
echo $! > ~/.discord_bot_pid.txt

pid=$!
sleep 3
ps --pid "$pid" >/dev/null
if [ "$?" -eq 0 ]; then
    echo "PID $pid exists and is running."
else
    echo "PID $pid does NOT exist."
	cat "./bot.log"
fi


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