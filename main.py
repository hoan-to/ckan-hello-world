import requests, json, getpass

def getData():

    test_api_url = "https://ckan.dlr.wobcom.tech/api/3/action/package_list"
    api_call_headers = {'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2Mzc1ODYzMTIsImp0aSI6IlJMYUY1UUVvYVFKLXEtQWttZTF3bEJHNE9Sa0RMeXlmY2FMWTJ0NVR5dDB2ZmN1TjV6ejRjRHRCSkNrUWdDeEhkVVJ0cWNVUWhicHYtMFRPIn0.pimCCGBm9bkRCQ6qG96dAqGZyU8jKORu8vBwOJY3VmM'}
    api_call_response = requests.get(test_api_url, headers=api_call_headers, verify=False)
    return api_call_response.text

if __name__ == '__main__':
    print(getData())