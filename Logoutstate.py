#First read shows the current value (or missing key)
#write sets the preference
#killall cfprefsd refreshes the preference cache
#Second read confirms it changed to 0

#
import os

os.system('defaults read com.apple.loginwindow TALLogoutSavesState')
os.system('defaults write com.apple.loginwindow TALLogoutSavesState -bool false')
os.system('killall cfprefsd')
os.system('defaults read com.apple.loginwindow TALLogoutSavesState')

input('Logout state saving disabled. Press ENTER to exit...  ')
#####

