# Cricket_Live
Live Cricket Score can be obtained on Whatsapp through message from a bot

## Cric API
API used for getting live cricket updates.</br>
* An account has to be created by signing up in Cric [website](https://www.cricapi.com/)
* The account will have a unique API key which is to be used in the code as "self.apikey"

## Twilio
This is used for sending messages to whatsapp number</br>
* Install by using 'pip install twilio'
* Create an account in [Twilio](https://www.twilio.com/)
* The account will have an account sid which is to be used as "account_sid" in the code
* Also an authorisation token will be present to be used as "account_auth_token" in the code
* Type your whatsapp number after "to='whatsapp:'" present in the last line of code
* For activating message service ,click on the round icon present in top left corner,then click on Programmable SMS,then save the number displayed as contact in phone and send a whatsapp message(present in the same webpage) to the number 
