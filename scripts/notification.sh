while :
do
	termux-notification -c "$(mpc)" --button1 "Prev" --button1-action "mpc prev" --button2 "Toggle" --button2-action "mpc toggle" --button3 "Next" --button3-action "mpc next" --on-delete "./notification.sh" -i 1337
done