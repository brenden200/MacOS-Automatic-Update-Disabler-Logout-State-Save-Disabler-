#Displays current update settings
#Disables automatic update features
#Refreshes preference caches
#Displays the updated settings afterward

#
import os

os.system('defaults read /Library/Preferences/com.apple.SoftwareUpdate')
os.system('defaults read /Library/Preferences/com.apple.commerce')
os.system('sudo defaults write /Library/Preferences/com.apple.SoftwareUpdate AutomaticCheckEnabled -bool false')
os.system('sudo defaults write /Library/Preferences/com.apple.SoftwareUpdate AutomaticDownload -bool false')
os.system('sudo defaults write /Library/Preferences/com.apple.SoftwareUpdate ConfigDataInstall -bool false')
os.system('sudo defaults write /Library/Preferences/com.apple.SoftwareUpdate CriticalUpdateInstall -bool false')
os.system('sudo defaults write /Library/Preferences/com.apple.commerce AutoUpdate -bool false')
os.system('sudo defaults write /Library/Preferences/com.apple.commerce AutoUpdateRestartRequired -bool false')
os.system('killall cfprefsd')
os.system('defaults read /Library/Preferences/com.apple.SoftwareUpdate')
os.system('defaults read /Library/Preferences/com.apple.commerce')
input('Automatic Updates Disabled. Press ENTER to exit...  ')
###########