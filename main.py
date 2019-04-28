from instagram_web_api import Client, ClientCompatPatch, ClientError, ClientLoginError
import os
from os import sys

web_api = Client(auto_patch=True, drop_incompat_keys=False)

def main():

  blank = '\n' * 999

  print(blank + '''
 _____           _         _____                      
|_   _|         | |       / ____|                     
  | |  _ __  ___| |_ __ _| (___   ___ _ __ __ _ _ __  
  | | | '_ \/ __| __/ _` |\___ \ / __| '__/ _` | '_ \ 
  | |_| | | \__ \ || (_| |____) | (__| | | (_| | |_) |
|_____|_| |_|___/\__\__,_|_____/ \___|_|  \__,_| .__/ 
                                               | |    
  by mm4rk3t                                   |_|    
''')

  try:
      username = input('Select username: ')
      profilepicURL = web_api.user_info2(username)['profile_pic_url_hd']
      os.system('wget -q -O ~/Pictures/InstaScrap/%s.jpeg %s' %(username, profilepicURL))
      print("\nImage downloaded to '~/Pictures/InstaScrap/%s.jpeg'\n" %username)
      
      display = input('Do you wish to display the image? [y/n]: ')
      
      if display == 'y':
        os.system('mupdf ~/Pictures/InstaScrap/%s.jpeg' %username)
      else:
        pass
      print('----------------------------------------------------------------------------')

  except ClientError:
      print(blank + "User '%s' not found!" %(username))
      choice = input('\nDo you wish to quit? [y/n]: ').lower()
      if choice == 'y':
        print('----------------------------------------------------------------------------')
        os.system('exit')
      else:
        main()
main()