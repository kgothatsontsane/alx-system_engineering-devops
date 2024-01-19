# Command Line For The Win

[CMDCHALLENGE](https://cmdchallenge.com/) is an awesome game that challenges your Command Line skills.
Everything is done via the command line and the questions are becoming increasingly complicated.
It’s a good training to improve your command line skills!

I have provided the screenshots of my progress in the [CMDCHALLENGE](https:cmdchallenge.com/)
and the the tasks 0-9, 10-18 19-27 in .png format.

The steps I have taken to use the SFTP command-line tool so that I can
perform the file transfer using SFTP are as follows:

## 1.
Established a connection to the sandbox environment using the SFTP command-line tool with the following command:
sftp 8c60a240e4fb@8c60a240e4fb.9b220f8f.alx-cod.online
which uses the host name and username.
I was asked for a password and used the one provided to me for the sandbox environment.

## 2.
Once connected, I navigate to the directory where I want to upload the screenshots.
Which is /root/alx-system_engineering-devops/command_line_for_the_win/ directory.

I use the command:
cd /root/alx-system_engineering-devops/command_line_for_the_win/
to navigate to the directory used the command:
pwd
to confirm that I am indeed in the correct directory.

## 3.
Use the SFTP put command to upload the screenshots from my local machine to my sandbox environment.

Before I upload the screenshots to my sandbox environment I have to locate them on my local machine first.
I use the following command to navigate to the folder on my local machine that has the screenshots:
lcd /Users/kgothatsontsane/Desktop/command_line_for_the_win/

The I confirm that I am in the correct directory using the command:
lpwd

I then proceed to upload the screenshots using the command:
put *.png

and I get the output:
ploading 0-first_9_tasks.png to /root/alx-system_engineering-devops/command_line_for_the_win/0-first_9_tasks.png
0-first_9_tasks.png                                              100%  313KB 127.4KB/s   00:02    
Uploading 1-next_9_tasks.png to /root/alx-system_engineering-devops/command_line_for_the_win/1-next_9_tasks.png
1-next_9_tasks.png                                               100%  322KB 215.7KB/s   00:01    
Uploading 2-next_9_tasks.png to /root/alx-system_engineering-devops/command_line_for_the_win/2-next_9_tasks.png
2-next_9_tasks.png                                               100%  410KB 438.3KB/s   00:00    


## 4.
I then confirm that the screenshots have been successfully transferred by checking the sandbox directory
by listing the files of the directory in the SFTP command line tool using the command:
ls

## 5.
The files are present in the directory and I will now push the screenshots to GitHub as mentioned in the initial requirements.

### END
