import requests
import json

acc_token = input("Please insert your access token :")
print("\n Menu Option")
print("*-" * 78 )
print("Test server connection [0]")
print("Display user info [1]")
print("Display rooms info [2]")
print("Create a room [3]")
print("Send message to a room [4]")


option=input("\n Enter your option here: ")
headers = {

            'Authorization' : 'Bearer {}'. format(acc_token),
            'Content-Type' : 'application/json'
}
url='https://webexapis.com/v1/people/me'
res=requests.get(url, headers=headers)

if option== "0":
    if res.status_code == 200:
        print("Connection Successful!")
    else:
        print("Connection Failed!")
    
elif option== "1":
        
        userInfo = res.json()
        print("User Info")
        print(f"Displayed Name: {userInfo['displayName']}")
        print(f"Nickname: {userInfo['nickName']}")
        print(f"Email: {', '.join(userInfo['emails'])}")

elif option=="2":
    url='https://webexapis.com/v1/rooms'
    params={'max':'5'}
    res=requests.get(url,headers=headers, params=params)
    roomInfo = res.json()

    if res.status_code == 200:
         
         if'items' in roomInfo:
              print("Room Info")
              for item in roomInfo['items']:
                
                print("*-"* 78)
                print(f"Room Id: {item['id']}")
                print(f"Room Name: {item['title']}")
                print(f"Date Created: {item['created']}")
                print(f"Last Activity: {', '.join(item['lastActivity'])}")
                print("*-"* 78)

elif option=="3":
    url='https://webexapis.com/v1/rooms'
    roomName=input("Create Room Name :")
    params={'title': roomName}

    res=requests.post(url, headers=headers, json=params)
    if res.status_code == 200:
        print(f"room:{roomName} has been created")
    else:
        print(f"an error {res.status_code} found!")

elif option=="4":
    url='https://webexapis.com/v1/rooms'
    params={'max':'5'}
    res=requests.get(url,headers=headers, params=params)
    roomInfo = res.json()

    if res.status_code == 200:
        print("\t ROOM")
        print("-"* 100)
        for i,item in enumerate ( roomInfo['items']):
            print(f" ({i + 1}) {item['title']}")
            

            print("-"*100)
            roomChoice=int(input("Choose a room for the message to be send:"))-1

            if 0 <= roomChoice <len( roomInfo['items']):
                roomIDselected=roomInfo['items'] [roomChoice]['id']
                roomNameSelected=roomInfo['items'] [roomChoice]['title']
                messageToRoom=input("Enter your message:")
                params={'roomId':roomIDselected, 'markdown' :messageToRoom}
                url='https://webexapis.com/v1/messages'
                res=requests.post(url, headers=headers,json=params)

                if res.status_code == 200:
                    print(f"Message :{messageToRoom} has been sent")

                else:
                    print(f"Failed to sent message {res.status_code}")

else:
    print("Choose only 1 - 4!")
userInput=input("Press enter to go to Exit >>>")