# data format will be in [{"name" : "chai with python", "time" : "10 min"}]

import json


def load_data() :
    try :
        with open("youtube.txt", "r") as file :
            return  json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos) :
    with open("youtube.txt", "w") as file :
        json.dump(videos, file)

def list_all_videos(videos) :
    for index , video in  enumerate(videos, start = 1) :
        print(f"{index}. '{video['name']}' - {video['time']}")

def add_video(videos) :
    name = input("Enter the video title: ")
    time = input("Enter the video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
    print("Video added successfully")
    print("\n")

def update_video(videos) :
    pass

def delete_video(videos) :
    pass




print("\n Youtube Manager | choose an option")
print("1. List all videos")
print("2. Add a video")
print("3. Update a video details")
print("4. Delete a video")
print("5. Exit")
print("\n")
        
choice = input("Enter your choice: ")
print("\n")

match choice :
    case "1":
        videos = load_data()
        list_all_videos(videos)
        print("\n")    
    case "2":
        videos = load_data()
        add_video(videos)
        print("Your Final list of videos is : ")
        print()
        list_all_videos(videos)
        print()
    case "3":
        pass
    case "4":
        pass
    case "5":
        pass

        
