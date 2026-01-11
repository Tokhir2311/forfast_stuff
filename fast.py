import requests

#response = requests.get("https://jsonplaceholder.typicode.com/posts")
#print(response)
#print(response.json())
#print(response.status_code)'''


#response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
#print(response.json())


#resp = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")
#print(resp.status_code)
#print(resp.json())


#resp = requests.post(
#    url = "https://jsonplaceholder.typicode.com/posts",
#    json={
#        "userID" :11,
#        "id":104,
#        "title":"this is a custom title ",
#        "body":"this is a custom body"
#    })
#print(resp.status_code)
#print(resp.json())


# resp = requests.patch(
#     url = "https://jsonplaceholder.typicode.com/posts/2",
#     json={
#         "userID" : 2,
#         "id":123,
#         "title": "that title has been changed",
#         "body":"hello, that has been changed too"
#     })

# print(resp.status_code)
# print(resp.json())


# deleted_data = requests.delete(url="https://jsonplaceholder.typicode.com/posts/2")

# print(deleted_data.json())  #xech nima qaytmaydi
# print(deleted_data.status_code)