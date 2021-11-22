import requests, json, getpass

def getData():

    file = open('ckan-token.txt', 'r')
    token = file.readlines().pop(0)

    test_api_url = "https://ckan.dlr.wobcom.tech/api/3/action/package_list"
    api_call_headers = {'Authorization': token}
    api_call_response = requests.get(test_api_url, headers=api_call_headers, verify=False)
    return api_call_response.text
if __name__ == '__main__':
    print(getData())