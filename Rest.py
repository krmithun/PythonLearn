import requests
import json

# header = {'Content-type': 'application/json',
#           'RBM-Authorization': self.config.rbm_auth_token}
# # json.dumps encodes the python object into json
# resp = requests.post(url, data=json.dumps(request_body),
#                      headers=header)
#

# data = {"suite_id": suite_id, "name": run_name}
# header = {"Content-Type": "application/json"}
# url = \
#     "https://testrail.lab.nbttech.com/core/index.php?/api/v2/add_run/" + \
#     str(project_id)
# res = requests.post(
#     url,
#     data=json.dumps(data),
#     headers=header,
#     auth=(
#         'icebox-users@riverbed.com',
#         '2top90!'))
# print(res.json()["id"])

headers = {'content-type': 'application/json'}

url = "https://reqres.in/api/users/2"
# url = 'http://{0}:{1}/api/st_mgmt/1.0/'.format(controller_ip,controller_port)
# response = requests.request("GET", url, headers=headers)
response = requests.get(url, headers=headers)

print("\n" + response.text)
if response.status_code == 200:
    print("response.status_code {}".format(response.status_code))
    print("response.reason {}".format(response.reason))
    print("response.text {}".format(json.loads(response.text)))
    # print("response.headers {}".format(response.headers))

    d_res = json.loads(response.text)
    print("email {}".format(d_res['data']['email']))

url = "https://jsonplaceholder.typicode.com/posts"
# payload = {"email":"krmithun@gmail.com", "first_name":"Mithun", "last_name":"Rajarama"}
response = requests.request("GET", url, headers=headers)
print("response.status_code {}".format(response.status_code))
print("response.reason {}".format(response.reason))
print("response.text {}".format(json.loads(response.text)))

url = "https://fakerestapi.azurewebsites.net/api/v1/Users"
# payload = "{\"id\":100,\"userName\":\"Mithun\",\"password\":\"Rajarama\"}"
# payload = json.dumps({
#   "id": 20,
#   "userName": "string1",
#   "password": "string1"
# })
payload = {
  "id": 20,
  "userName": "string1",
  "password": "string1"
}
# response = requests.request("POST", url, data=payload, headers=headers)
response = requests.post(url, data=json.dumps(payload), headers=headers)
print("response.status_code {}".format(response.status_code))
print("response.reason {}".format(response.reason))
print("response.text {}".format(json.loads(response.text)))
print("response.text {}".format(response.text))
print("response.text {}".format(str(response.json())))