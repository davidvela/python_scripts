import requests,json,urllib
from requests_ntlm import HttpNtlmAuth


# ------- http_call() ---------

root_url = "https://sharepoint.mycompany.com"
headers = {'accept': "application/json;odata=verbose","content-type": "application/json;odata=verbose"}
##"DOMAIN\username",password 
auth = HttpNtlmAuth("MYCOMPANY"+"\\"+"UserName",'Password')

def getToken():
    contextinfo_api = root_url+"/_api/contextinfo"
    response = requests.post(contextinfo_api, auth=auth,headers=headers)
    response =  json.loads(response.text)
    digest_value = response['d']['GetContextWebInformation']['FormDigestValue']
    return digest_value

def createSite(title,url,desc):
    create_api = root_url+"/_api/web/webinfos/add"
    payload = {'parameters': {
            '__metadata':  {'type': 'SP.WebInfoCreationInformation' },
            'Url': url,
            'Title': title,
            'Description': desc,
            'Language':1033,
            'WebTemplate':'STS#0',
            'UseUniquePermissions':True}
        }
    response = requests.post(create_api, auth=auth,headers=headers,data=json.dumps(payload))
    return json.loads(response.text)


def main_HTTP_Calls_UserPassw():
    print("Hello, World!")
    
    headers['X-RequestDigest']=getToken()
    print( createSite("Human Resources","hr","Sample Description") )

def main_HTTP_Calls_AppID():
    print("Hello, World!")


def main_ShLib():
    print("Hello, World!")


if __name__== "__main__" :
    main_HTTP_Calls()