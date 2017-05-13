## ============================== ##
#
# This is the original code from Miguel, but it doesn't work with the new
# Microsoft Translation API
#
## ============================== ##
#
# try:
#     import httplib  # Python 2
# except ImportError:
#     import http.client as httplib  # Python 3
# try:
#     from urllib import urlencode  # Python 2
# except ImportError:
#     from urllib.parse import urlencode  # Python 3
# import json
# from flask_babel import gettext
# from config import MS_TRANSLATOR_CLIENT_ID, MS_TRANSLATOR_CLIENT_SECRET

# def microsoft_translate(text, sourceLang, destLang):
#     if MS_TRANSLATOR_CLIENT_ID == "" or MS_TRANSLATOR_CLIENT_SECRET == "":
#         return gettext('Error: translation service not configured.')
#     try:
#         # get access token
#         params = urlencode({
#             'client_id': MS_TRANSLATOR_CLIENT_ID,
#             'client_secret': MS_TRANSLATOR_CLIENT_SECRET,
#             'scope': 'http://api.microsofttranslator.com',
#             'grant_type': 'client_credentials'})
#         conn = httplib.HTTPSConnection("datamarket.accesscontrol.windows.net")
#         conn.request("POST", "/v2/OAuth2-13", params)
#         response = json.loads (conn.getresponse().read())
#         token = response[u'access_token']
        
#         # translate
#         conn = httplib.HTTPSConnection('api.microsofttranslator.com')
#         params = {  'appId': 'Bearer ' + token,
#                     'from': sourceLang,
#                     'to': destLang,
#                     'text': text.encode("utf-8")}
#         conn.request("GET", '/V2/Ajax.svc/Translate?' + urlencode(params))
#         response = json.loads("{\"response\":" + conn.getresponse().read().decode('utf-8') + "}")
#         return response["response"]
#     except:
#         return gettext('Error: Unexpected error.')

## ============================== ##
#
##  Also tried this one from Payam, but can't get it to work on cloud9
#
## ============================== ##
#
# import json
# from flask_babel import gettext
# import requests
# from xml.etree import ElementTree
# from config import MS_TRANSLATOR_KEY


# def microsoft_translate(text, sourceLang, destLang):

#     # get access token
#     token_parameter = {
#         'Subscription-Key': MS_TRANSLATOR_KEY #Here go to the Keys section of your app in Azure and copy one of the two keys
#     }
#     r = requests.post("https://api.cognitive.microsoft.com/sts/v1.0/issueToken", params=token_parameter)


#     # translate
#     params = {'appid': 'Bearer ' + r.text,
#               'from': sourceLang,
#               'to': destLang,
#               'text': text.encode("utf-8")}
#     t = requests.get("https://api.microsofttranslator.com/v2/http.svc/Translate", params=params)
#     tree = ElementTree.fromstring(t.content)
#     translated_text = tree.text
#     response = json.dumps("{\"response\":" + translated_text +"}")
#     return response