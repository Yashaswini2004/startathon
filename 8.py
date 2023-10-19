import os
import requests
base_url="https://xkcd.com"
save_directory="xkcd_comics"
if os.path.exists(save_directory):
    os.makedirs(save_directory)
comic_number=1
for i in range(15):
    comic_url=f'{base_url}/{comic_number}/info.O.json'
    response=requests.get(comic_url)
    if response.status_code==200:
        comic_data=response.json()
        image_url=comic_data['img']
        response=requests.get[image_url]
        image_path=os.path.join(save_directory,f'xkcd_{comic_number}.png')
        with open(image_path,"wb") as image_file:
            image_file.write(response.content)
        print(f"Downloaded comic#{comic_number}")
        comic_number+=1
    else:
        break
        print("15 xkcd comic downloaded successfully")

