import pymongo
from bson import ObjectId
client = pymongo.MongoClient("mongodb+srv://Youtubepy:Youtubepy@cluster0.549mvqo.mongodb.net/")
db=client["Fav_manager"]
video_collection=db["videos"]
print(video_collection)


def add_video(name,link):
    video_collection.insert_one({"name":name,"link":link})


def list_videos():
    for video in video_collection.find():
        print(f"ID:{video['_id']},name:{video['name']} and link:{video['link']}")


def update_video(video_id,new_name,new_link):
    video_collection.update_one({'_id':ObjectId(video_id)},{"$set":{"name":new_name,"link":new_link}})


def delete_video(video_id):
    video_collection.delete_one({"_id":ObjectId(video_id)})    
    
    

def main():
    while(True):
        print("1:List all favourites ")
        print("2:Add a video ")
        print("3:Update a video ")
        print("4:Delete a video ")
        print("5:Exit")
        choice=input("Enter your choice:  ")
        
        if(choice=='1'):
            list_videos()
        elif(choice=='2'):
            name=input("Enter the video name:  ")
            link=input("Enter video link:  ")
            add_video(name,link)
        elif(choice=='3'):
            video_id=input("Enter the video ID to update:  ")
            name=input("Enter the updated video name:  ")
            link=input("Enter updated video link:  ")
            update_video(video_id,name,link)
        elif(choice=='4'):
            video_id=input("Enter video ID to delete:  ")
            delete_video(video_id)
        elif(choice=='5'):
            break
        else:
            print("Enter a valid choice: ")
            
        
        
        

if __name__=="__main__":
    main()
