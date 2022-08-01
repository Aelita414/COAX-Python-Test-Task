#task 1 - There is string s = "Python Bootcamp". Write the code that hashes string.
s = "Python Bootcamp"
hash_string = hash(s)
print("Hash string: %s" % hash_string)

#task 2 - You are working on a project for TikTok. The future project will be a web-site of all public GIF images. You need to write a function that converts TikTok video to GIF. The input parameter is url address of TikTok video, i.e. "TikTok example". The output parameter is path to GIF image, i.e. "/home/user/TikTok-example-1.gif".

import requests
import os

video_url = input('URL: ')


def downloading_gif(url=''):
    try:
        response = requests.get(url=url)
        with open('video.gif', 'wb') as file:
            file.write(response.content)
        return os.path.abspath('video.gif')
    except Exception as _ex:
        return 'Ooops!'


def main():
    print(downloading_gif(url=video_url))


if __name__ == '__main__':
    main()
