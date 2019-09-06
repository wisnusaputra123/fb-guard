#-*- coding: utf-8 -*-
#!/bin/python2
# Instagram : @wisnu_as123 
# Facebook : Wisnu Al Vinzcara
# Author : wisnu-saputra
import requests, json, argparse

class color:
      green = '\033[92m'
      blue = '\033[94m'
      white = '\033[0m'
      yellow = '\033[93m'


class Facebook_Guard:
       active = "https://graph.facebook.com/graphql"
       On = 'true'
       Off = 'false'

       def __init__(self, user, passwd):
          self.user = user
          self.passwd = passwd


       def generate(self, facebook_user, pwd):
          self.user_name = facebook_user
          self.password = pwd
          self.token = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+self.user_name+"&locale=en_US&password="+self.password+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").text
          self.load_token = json.loads(self.token)
          self._token = self.load_token['access_token']
          Y = open('token.log', 'w')
          Y.write(str(self._token))
          Y.close
          print color.green+"[+] Generate Access Token Success [+]\n"+color.white

       def get_uid(self, token):
          self._token = token
          self.get_uid_ = requests.get("https://graph.facebook.com/me?access_token=%s" % self._token).text
          self._uid = json.loads(self.get_uid_)
          self.ID = self._uid['id']
          Y = open('uid.log', 'w')
          Y.write(str(self.ID))
          Y.close
          print color.green+"[+] Get ID success [+]\n"+color.white


       def active_(self, uid, token, ON_OFF):
          self.enable_disable = ON_OFF
          self.uid = uid
          self._token = token
          self.data = 'variables={"0":{"is_shielded":%s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (self.enable_disable, str(self.uid))
          self.headers = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % self._token}
          self.response = requests.post(Facebook_Guard.active, data=self.data, headers=self.headers)
          self.active__ = self.response.json()
          print self.active__





pars = argparse.ArgumentParser(prog='python2 Guard')
pars = argparse.ArgumentParser(description='Facebook Picture Profile Guard')
pars.add_argument("-u", '--user',  help="Email or Phone Number Facebook")
pars.add_argument("-p", '--password',  help="Facebook password")
pars.add_argument("--enable", help="Enable Profile Picture Guard", action='store_true')
pars.add_argument("--disable", help="Disable Profile Picture Guard", action='store_true')
args = pars.parse_args()

email_or_phone = args.user
password = args.password
ON = args.enable
OFF = args.disable
FB_ = Facebook_Guard(email_or_phone, password)
banner =  color.green+'''
__      _(_)___ _ __  _   _
\ \ /\ / / / __| '_ \| | | |
 \ V  V /| \__ \ | | | |_| |
  \_/\_/ |_|___/_| |_|\__,_|
 ___  __ _ _ __  _   _| |_ _ __ __ _
/ __|/ _` | '_ \| | | | __| '__/ _` |
\__ \ (_| | |_) | |_| | |_| | | (_| |
|___/\__,_| .__/ \__,_|\__|_|  \__,_|
          |_|                                                        
      [ Facebook Picture Guard ]
     __________________________
      [ youtube : DSV plankton ]
      [ whatsapp :085718945758 ]

'''+color.green

try:
   print banner
   FB_.generate(email_or_phone, password)
   input_token = open('token.log', 'r').read()
   FB_.get_uid(input_token)
   if ON:
      input_token = open('token.log', 'r').read()
      input_ID = open('uid.log', 'r').read()
      FB_.active_(input_ID, input_token, Facebook_Guard.On)
      print color.blue+"[!] Picture Guard Has been Enable [!]"+color.white
   if OFF:
      input_token = open('token.log', 'r').read()
      input_ID = open('uid.log', 'r').read()
      FB_.active_(input_ID, input_token, Facebook_Guard.Off)
      print color.yellow+"[!] Picture Guard Has been Disable [!]"+color.white
except TypeError:
   pars.print_help()
except KeyError:
   color.red+'[x] Invalid User or password [x]'+color.white


