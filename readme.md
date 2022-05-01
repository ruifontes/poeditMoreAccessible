# poeditMoreAccessible

## Informations
* Authors: Abel Passos, Ângelo Abrantes and Rui Fontes, based on work of Him Prasad Gautam
* Updated: April , 26 2022
* Download [stable version][1]
* Compatibility: NVDA version 2019.3 and later


## Presentation
This Add- on makes poedit more accessible and informative in many aspect of the shortcut command of poedit.
It also indicates the different category of messages by either a beep or a preceded asterisk announcement. The  indicating sound  will help to identify the spots of possible  error and help in correction. It is also possible to issue a command to announce the error.
Now, you can know the   source text and the translation texts separately. Further more, the plural formed messages (if any)can now be distinctly recognized. This will help you to judge the translation accuracy more easily. It avoids the round trip of TAB and shift+TAB if desired to know these messages individually.


## Features
- Announcement of the action made on pressing poedit shortcut commands;
- Specific  indication of Message  category  by a distinct  beep and/or asterick;
- Within current nvda session, the Beep can be toggled between 'on' or 'off';
- In 'beep off' mode, alternate way of indication of message category;
- Announcement of plural form;
- Commands for announcement of:
	- Translation text;
	- Ssource text;
	- Poedit translation syntax error;
	- Different numbers of parameters or '&' marks;
	- Text of comment window;
	- Text 'Note for Translators' window;
	- First suggestions, untill the maximum of 5.


## Indication for Message type
### In 'beep on' mode
- High pitched tone: No translation;
- Median pitched tone: Fuzzy translation;
- Low pitch tone:
	- the source and the translation is same;
	- The number of parameters or ampersand  sign in source and translation differs;
- No beep: Translation is normal.


### In 'beep off' mode
- Message followed by "No text in translation.": No translation;
- Message preceded by single asterisk and Fuzzy (* Fuzzy): Fuzzy translation;
- Message preceded by double asterisk (**):
	- the source and the translation text is same;
	- The number of parameters ampersand  sign in source and translation is not equal;
- Message preceded by triple asterisk (***): Error due to violation of translation Rule;
- Message without preceeding asterisk: Normal translation.


### In both beep mode
- extra sharp beep: Error due to violation of translation Rule.


## Keyboard commands
- control+b: Copies the source text to the translation box and reports;
- control+k: Deletes the translation and reports. Informs if no text available;
- control+s: saves the file by notifying the action being performed;
- control+u: Toggled the message type to fuzzy or normal and reports. Informs if no text available;
- control+shift+r:
	- Announces the source message text.
	- In case of plural form, pressing twice  reports the plural    source text;
- control+shift+t:
	- Announces the translation message text.
	- In case of plural form, pressing twice  reports the next form of translation;
- control+shift+a: Announcement about the 'Note for Translators' window;
- control+shift+c: Announcement about the comment window;
- control+shift+e: Describes the cause of error;
- control+shift+s: Announce the first suggestions untill a maximum of 5;
- control+shift+b: Temporarily toggles the beep mode to ON or OFF mode and reports;
- control+shift+v: Toggles the level of beep tone into sharp or mild.


[1]: https://github.com/ruifontes/poeditMoreAccessible/releases/download/2022.04/poeditMoreAccessible-2022.04.nvda-addon
