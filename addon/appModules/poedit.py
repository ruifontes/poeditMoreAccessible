# -*- coding: utf-8 -*-
# addon/appModules/poedit.py
# written by Rui Fontes <rui.fontes@tiflotecnia.com>, Ângelo Abrantes <ampa4374@gmail.com> and Abel Passos do Nascimento Jr. <abel.passos@gmail.com> 
# Based on the work of  Him Prasad Gautam <drishtibachak@gmail.com>
#A part of NonVisual Desktop Access (NVDA)
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
"""
App module to enhance Poedit accessibility.
"""

import addonHandler
import appModuleHandler
import scriptHandler
from scriptHandler import script
import api
import controlTypes
import tones
import ui
import gui
import wx
from keyboardHandler import KeyboardInputGesture
from NVDAObjects.IAccessible import sysListView32
import windowUtils
import NVDAObjects.IAccessible
import winUser

addonHandler.initTranslation()

doBeep = True
sharpTone = True

# Gets the value of a object with the given controlID
def getPoeditWindow(index, visible=True):
	try:
		obj = NVDAObjects.IAccessible.getNVDAObjectFromEvent(
			windowUtils.findDescendantWindow(api.getForegroundObject().windowHandle, visible,
			controlID=index), winUser.OBJID_CLIENT, 0)
	except LookupError:
		return None
	else:
		objText = obj.value
		return objText if objText else False

# Gets the name of a object with the given controlID
def getPoeditWindow1(index, visible=True):
	try:
		obj = NVDAObjects.IAccessible.getNVDAObjectFromEvent(
			windowUtils.findDescendantWindow(api.getForegroundObject().windowHandle, visible,
			controlID=index), winUser.OBJID_CLIENT, 0)
	except LookupError:
		return None	
	else:
		objText = obj.name
		return objText if objText else False


class AppModule(appModuleHandler.AppModule):
	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)

	def getIDCodes(self):
		global transList, originID, sourcePluralID, translatedID, translatedSingularID, translatedPluralID, tradID, errorsID, translationNotesID, commentaryID, fuzzyID
		# Gets the translation list ID code, since all other are calculated in function of it...
		obj = api.getFocusObject()
		transList = obj.windowControlID
		originID = transList+12
		sourcePluralID = transList+14
		translatedID = transList+23
		translatedSingularID = transList+69
		translatedPluralID = transList+71
		tradID = transList+15
		errorsID = transList+17
		translationNotesID = transList+64
		commentaryID = transList+67
		fuzzyID = transList+60

	def checkError(self, sourceText, transText):
		# Check the number of parameters of source and translated text
		parameter = {'{': _("brace"), '}': _("brace"), '[': _("bracket"), ']': _("bracket"),
			'%s': "%s ", '%d': "%d ", '%u': "%u ", '%g': "%g ",
			'&': _("ampersand"), '\n': _("paragraph"), chr(13): _("paragraph")}
		for k in list(parameter.keys()):
			if sourceText.count(k) != transText.count(k):
				return parameter[k]
		return True if sourceText == transText else None

	@script(
		# Translators: Message to be announced during Keyboard Help 
		description = _("Reports about the copying act in poedit."), 
		# Translators: Name of the section in "Input gestures" dialog. 
		category = _("POEdit"), 
		gesture = "kb:control+b",)
	def script_copySourceText(self, gesture):
		gesture.send()
		# Translators: The copying of source text to translation pressing control+b in poedit.
		ui.message(_("copied original text."))

	@script(
		# Translators: Message to be announced during Keyboard Help 
		description = _("Reports about the deletion act in poedit."), 
		# Translators: Name of the section in "Input gestures" dialog. 
		category = _("POEdit"), 
		gesture = "kb:control+k")
	def script_deleteTranslation(self, gesture):
		self.getIDCodes()
		if getPoeditWindow(translatedID) or getPoeditWindow(translatedPluralID) or getPoeditWindow(translatedSingularID):
			gesture.send()
			# Translators: The deletion of translation pressing control+k in poedit.
			ui.message(_("translation deleted."))
		else:
			# Translators: Report that No translation text available to delete.
			ui.message(_("No text in translation."))

	@script(
		# Translators: Message to be announced during Keyboard Help 
		description = _("Reports while saving the po file."), 
		# Translators: Name of the section in "Input gestures" dialog. 
		category = _("POEdit"), 
		gesture = "kb:control+s")
	def script_savePoFile(self, gesture):
		gesture.send()
		# Translators: The saving  of currently focused  po file by  pressing control+s.
		ui.message(_("saving the po file..."))

	@script( 
		# Translators: Message to be announced during Keyboard Help 
		description = _("Reports the source text in poedit. In case of plural form of messages, pressing twice says the plural form of the source text"), 
		# Translators: Name of the section in "Input gestures" dialog. 
		category = _("POEdit"), 
		gesture = "kb:control+shift+r")
	def script_saySourceText(self, gesture):
		self.getIDCodes()
		# Translators: The announcement of the absence of source text on pressing ctrl+shift+r.
		text = _("No source text.")
		if getPoeditWindow(originID) and getPoeditWindow(sourcePluralID):
			if scriptHandler.getLastScriptRepeatCount()==0:
				text = _("singular") + ": " + getPoeditWindow(originID)
			else:
				text = _("plural") + ": " + getPoeditWindow(sourcePluralID)
		else:
			if getPoeditWindow(originID):
				if scriptHandler.getLastScriptRepeatCount()==0:
					text = getPoeditWindow(originID)
				else:
					# Translators: Announcing the absence of plural form
					text = _("Has no plural form.")
		ui.message(text)

	@script( 
		# Translators: Message to be announced during Keyboard Help 
		description = _("Reports the translated string in poedit. In case of plural form of messages, pressing twice says the another form of the translated string"), 
		# Translators: Name of the section in "Input gestures" dialog. 
		category = _("POEdit"), 
		gesture = "kb:control+shift+t")
	def script_sayTranslation(self, gesture):
		self.getIDCodes()
		# Translators: The announcement of the absence of translated text on pressing ctrl+shift+t.
		text = _("No text in translation.")
		if getPoeditWindow(translatedID):
			if scriptHandler.getLastScriptRepeatCount()==0:
				text = getPoeditWindow(translatedID)
			else:
				# Translators: Announcing the absence of plural form
				text = _("Has no plural form.")
		elif getPoeditWindow(translatedSingularID):
			if scriptHandler.getLastScriptRepeatCount()==0:
				text = _("singular") + ": " + getPoeditWindow(translatedSingularID)
			else:
				text = _("plural") + ": "
				if getPoeditWindow(translatedPluralID, False):
					text = text+getPoeditWindow(translatedPluralID, False)
				else:
					# Translators: Announcing the absence of plural form
					text = text+_("No text in translation.")
		elif getPoeditWindow(translatedPluralID):
			if scriptHandler.getLastScriptRepeatCount()==0:
				text = _("plural") + ": " + getPoeditWindow(translatedPluralID)
			else:
				text = _("singular") + ": "
				if getPoeditWindow(translatedSingularID, False):
					text = text+getPoeditWindow(translatedSingularID, False)
				else:
					# Translators: Announcing the absence of plural form
					text = text+_("No text in translation.")
		ui.message(text)

	@script( 
		# Translators: Message to be announced during Keyboard Help 
		description = _("Describes the cause of error."), 
		# Translators: Name of the section in "Input gestures" dialog. 
		category = _("POEdit"), 
		gesture = "kb:control+shift+e")
	def script_reportError(self, gesture):
		self.getIDCodes()
		if getPoeditWindow(originID) and getPoeditWindow(translatedID) :
			caseType = ""
			unequalItem = self.checkError(getPoeditWindow(originID), getPoeditWindow(translatedID))
		elif getPoeditWindow(originID) and getPoeditWindow(translatedSingularID):
			caseType = _("singular")
			unequalItem = self.checkError(getPoeditWindow(originID), getPoeditWindow(translatedSingularID))
			if not unequalItem:
				caseType = _("plural")
				unequalItem = self.checkError(getPoeditWindow(sourcePluralID), getPoeditWindow(translatedPluralID, False))
		elif getPoeditWindow(sourcePluralID) and getPoeditWindow(translatedPluralID):
			caseType = _("plural")
			unequalItem = self.checkError(getPoeditWindow(sourcePluralID), getPoeditWindow(translatedPluralID))
			if not unequalItem:
				caseType = _("singular")
				unequalItem = self.checkError(getPoeditWindow(originID), getPoeditWindow(translatedSingularID), False)
		else:
			return
		text = ""
		if unequalItem is True:
			# Translators: Announcing the fact of source and translated text are equals.
			text = _("{caseType} message contains same text in source and translation.").format(caseType = caseType)
		elif unequalItem:
			# Translators: Announcing the fact of source and translated text having different number of constants
			text += _("{caseType} message has different  number of {unequalItem} in source and translation.").format(caseType = caseType, unequalItem = unequalItem)
		if getPoeditWindow1(errorsID):
			objText = getPoeditWindow1(errorsID)
			text += objText + text
		else:
			if len(text) == 0:
				# Translators: Announcing translation without syntax errors
				text = _("no syntax error.")
			else:
				# Translators: Announcing translation without no more syntax errors
				text += _("no other syntax error.")
		ui.message(text)

	@script( 
		# Translators: Message to be announced during Keyboard Help 
		description = _("Reports any notes for translators"), 
		# Translators: Name of the section in "Input gestures" dialog. 
		category = _("POEdit"), 
		gesture = "kb:control+shift+a")
	def script_reportAutoCommentWindow(self,gesture, visible=True):
		self.getIDCodes()
		objText = getPoeditWindow1(translationNotesID)
		if objText is False:
			# Translators: Reported when the translators notes window does not contain any texts.
			objText = _("No notes for translators.")
		ui.message(objText)

	@script( 
		# Translators: Message to be announced during Keyboard Help 
		description = _("Reports any comments in the comments window"),
		# Translators: Name of the section in "Input gestures" dialog.
		category = _("POEdit"), 
		gesture = "kb:control+shift+c")
	def script_reportCommentWindow(self,gesture):
		self.getIDCodes()
		objText = getPoeditWindow(commentaryID)
		if objText is False:
			# Translators: Reported when the comment window does not contain any texts.
			objText = _("Comment window has no text.")
		elif objText is None:
			# Translators: Reported when the comments window could not be found.
			objText = _("Could not find comment window.")
		ui.message(objText)

	@script( 
		# Translators: Message to be announced during Keyboard Help 
		description = _("Toggles the beep mode and informs the new state."), 
		# Translators: Name of the section in "Input gestures" dialog. 
		category = _("POEdit"), 
		gesture = "kb:control+shift+b")
	def script_toggleBeep(self, gesture):
		global doBeep
		if doBeep:
			doBeep = False
			# Translators: Announcing the state of beeps
			ui.message(_("Beep off"))
		else:
			doBeep = True
			# Translators: Announcing the state of beeps
			ui.message(_("Beep on"))

	@script( 
		# Translators: Message to be announced during Keyboard Help 
		description = _("sets the beep volume in mild and sharp level in poedit."),
		# Translators: Name of the section in "Input gestures" dialog. 
		category = _("POEdit"), 
		gesture = "kb:control+shift+v")
	def script_setToneLevel(self, gesture):
		global sharpTone
		if sharpTone:
			sharpTone = False
			# Translators: Announcing the level of tone
			ui.message(_("set to mild tone"))
		else:
			sharpTone = True
			# Translators: Announcing the level of tone
			ui.message(_("set to high tone"))

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if "wxWindowNR" in obj.windowClassName and obj.role==controlTypes.Role.LISTITEM:
			clsList.insert(0,PoeditListItem)

	def event_NVDAObject_init(self, obj):
		if obj.role == controlTypes.Role.EDITABLETEXT and controlTypes.State.MULTILINE in obj.states and obj.isInForeground:
			left, top, width, height = obj.location
			try:
				obj.name = NVDAObjects.NVDAObject.objectFromPoint(left + 10, top - 10).name
			except AttributeError:
				pass
			return


class PoeditListItem(sysListView32.ListItem):

	def category(self):
		AppModule.getIDCodes(AppModule)
		# category: 0: untranslated; 1: fuzzy; 2: unsure; 3: normal; 4: Errorneous. 
		global msgType2
		if getPoeditWindow(translatedID):
			transID = translatedID
			sourceID = originID
		elif getPoeditWindow(translatedPluralID):
			transID = translatedPluralID
			sourceID = sourcePluralID
		elif getPoeditWindow(translatedSingularID):
			transID = translatedSingularID
			sourceID = originID
		else:
			return 0 # No text in translation.
		sourceText = getPoeditWindow(sourceID)
		translatedText = getPoeditWindow(transID)
		msgType2 = ""
		#Checking  of the equality in quantity of % variables, brackets and paragraph in source and translation. Unequal means error!
		unequalItem = AppModule.checkError(AppModule, getPoeditWindow(originID), getPoeditWindow(translatedID))
		if unequalItem == _("ampersand"):
			pass
		if unequalItem is True:
			pass
		elif unequalItem:
			# Translators: Announcing different number of paramenters in both fields
			msgType2 = _("message has different  number of {unequalItem} in source and translation.").format(unequalItem = unequalItem)
			return 4	#Either bold ornot, Error from perspective of translation rule.
		if getPoeditWindow1(fuzzyID):
			return 1	# Error from language perspective (fuzzy).
		elif getPoeditWindow1(errorsID):
			return 4	#Either bold ornot, Error from perspective of translation rule.
		elif sourceText == translatedText:
			# Translators: Announcing the same text in both fields...
			msgType2 = _("Message contains same text in source and translation.")
			return 2	# It may or may not be an error. 
		elif sourceText.count("&") != translatedText.count("&"):
			# Translators: Announcing different number of & in both fields
			msgType2 += _("Message contains different number of '&'.")
			return 2	# It may or may not be an error. 
		return 3	# normal translation.

	def _get_name(self):
		AppModule.getIDCodes(AppModule)
		type = self.category()
		global doBeep
		noticeText = " | "
		if getPoeditWindow(sourcePluralID):
			noticeText = _("Has plural form.")
		if getPoeditWindow1(errorsID):
			objText = getPoeditWindow1(errorsID)
			noticeText = objText + noticeText
		else:
			noticeText =""
		if type == 0:
			# Translators: Announcing absence of text in translation field
			focusedMessage = super(PoeditListItem,self).name + _("No text in translation.")
			return focusedMessage
		else:
			try:
				focusedMessage = super(PoeditListItem,self).name + " | " + getPoeditWindow1(tradID) + " | " + getPoeditWindow(translatedID) + noticeText
			except:
				focusedMessage = super(PoeditListItem,self).name + " | " + getPoeditWindow1(tradID) + " | " + getPoeditWindow(translatedSingularID) + noticeText
			if doBeep:
				return ("* Fuzzy" + focusedMessage if type == 1 # Fuzzy
					else focusedMessage if type == 3 # Normal translation
					else "** " + focusedMessage if type == 2 # Unsure translation
					else "*** " + focusedMessage) # type 4 # Translation with errors
			else:
				return ("* Fuzzy" +focusedMessage if type == 1 # Fuzzy
					else "** " + focusedMessage + msgType2 if type ==2 # Unsure translation
					else "*** "+focusedMessage + msgType2 if type ==4 # Translation with errors
					else focusedMessage) # Type 3 normal translation

	def event_gainFocus(self):
		super(sysListView32.ListItem, self).event_gainFocus()
		type = self.category()
		global doBeep, sharpTone
		if type < 3 and doBeep: 
			pitch = 100*(2+(sharpTone+1)*(2-type))
			tones.beep(pitch, 50)
		elif type ==4 and doBeep:
			pitch = 200*(2+sharpTone+doBeep)
			tones.beep(pitch, 75)
		pass


	@script(
		# Translators: Message to be announced during Keyboard Help
		description = _("Reports the status of message set by toggling in poedit."),
		# Translators: Name of the section in "Input gestures" dialog. 
		category = _("POEdit"), 
		gesture = "kb:control+u")
	def script_toggleTranslation(self, gesture):
		gesture.send()
		type = self.category()
		reporting =[_("No text in translation."), _("erased Fuzzy label."), _("labelled as fuzzy."), _("labelled as fuzzy."), _("Error in translation")]
		# Translators: The toggle action performed by pressing control+u in poedit.
		ui.message(reporting[type])

	@script( 
		# Translators: Message to be announced during Keyboard Help 
		description = _("Shows the  firsts suggestions, untill the maximum of 5"), 
		# Translators: Name of the section in "Input gestures" dialog. 
		category = _("POEdit"), 
		gesture = "kb:control+shift+s")
	def script_suggestions(self, gesture): 
		global sugList
		sugList = []
		# Adding the suggestions to a dictionary. The two first characters are removed since they are not printable...
		# The first part is the suggestion, the second is the keystroke...
		if getPoeditWindow1(transList+75):
			sugList.append(str(getPoeditWindow1(transList+75))[2:] + ";" + getPoeditWindow1(transList+76))
		if getPoeditWindow1(transList+83):
			sugList.append(str(getPoeditWindow1(transList+83))[2:] + ";" + getPoeditWindow1(transList+84))
		if getPoeditWindow1(transList+90):
			sugList.append(str(getPoeditWindow1(transList+90))[2:] + ";" + getPoeditWindow1(transList+91))
		if getPoeditWindow(transList+97):
			sugList.append(str(getPoeditWindow1(transList+97))[2:] + ";" + getPoeditWindow1(transList+98))
		if getPoeditWindow1(transList+104):
			sugList.append(str(getPoeditWindow1(transList+104))[2:] + ";" + getPoeditWindow1(transList+105))
		gui.mainFrame._popupSettingsDialog(SuggestionsDialog)


class SuggestionsDialog(wx.Dialog):
	def __init__(self, *args, **kwds):
		kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
		wx.Dialog.__init__(self, *args, **kwds)

		# Translators: Name of dialog with the suggestions of POEdit
		self.SetTitle(_("POEdit suggestions"))

		sizer_1 = wx.BoxSizer(wx.VERTICAL)

		self.choice_1 = wx.Choice(self, wx.ID_ANY, choices = sugList)
		self.choice_1.SetFocus()
		self.choice_1.SetSelection(0)
		sizer_1.Add(self.choice_1, 0, 0, 0)

		sizer_2 = wx.StdDialogButtonSizer()
		sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

		# Translator: Name of button to accept the selected suggestion
		self.button_1 = wx.Button(self, wx.ID_ANY, _("Accept"))
		self.button_1.SetDefault()
		sizer_2.Add(self.button_1, 0, 0, 0)

		self.button_CANCEL = wx.Button(self, wx.ID_CANCEL, "")
		sizer_2.AddButton(self.button_CANCEL)

		sizer_2.Realize()
		self.SetSizer(sizer_1)
		sizer_1.Fit(self)

		self.SetEscapeId(self.button_CANCEL.GetId())
		self.Bind(wx.EVT_BUTTON, self.onAccept, self.button_1)

		self.Layout()
		self.CentreOnScreen()

	def onAccept(self, evt):
		self.Hide()
		evt.Skip()
		choice = self.choice_1.GetStringSelection().split(";")[1][:6]
		choice = choice.replace("Ctrl", "control")
		KeyboardInputGesture.fromName(choice).send()
