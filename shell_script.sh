TEMP=$(python url_red.py | awk 'NR == 22' | awk '{print $2}' )
echo "${TEMP}"

if[$TEMP > 19.0]
then 
echo "Sending Sms as AC temperature is high"
python python_pgrm.py -n "AC TEMPERATURE has exceed and current temperature is:${TEMP}" >> message_logs.txt
 else
 echo "Normal"
 fi