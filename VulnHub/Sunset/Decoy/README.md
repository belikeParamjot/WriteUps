# Sunset: Decoy
## About
__Series__: Sunset  
__Difficulty__: Easy/Intermediate  
__VM Page__: https://www.vulnhub.com/entry/sunset-decoy,505/  
__Download__: https://mega.nz/file/9HZAASoZ#lR-be00UrSFeUBPw4Z1TOwp9DHOnjrjCf7aKOJbLV5w  

## Solution

### Enumeration
Starting with the simple nmap scan: ```nmap -A <IP>```

![Image1]()

We can see we have 2 ports open i.e. ssh and http. Let's view the web directory first...

![Image2]()

We have a zip file available here let's download it and extract the files.

### Cracking the zip

Alright we have zip protected with a password, let's crack it with fcrackzip: ```fcrackzip -D -p /usr/share/wordlists/rockyou.txt -u save.zip```.  Note: I used -u flag to verify the password by using unzip.

![Image3]()

With this password extract the files and analyze them to find some creds.

![Image4]()

### Cracking the hash

You can explore these files on your own if you want to, but for the challenge I am going to extract the user:pass of the non-root user from our shadow file... And then crack the password hash with hashcat, for that just copy the password into some file, I named the file as ```hash```: ```hashcat -a0 -m1800 hash /usr/share/wordlists/rockyout.txt --force```

![Image5]()

So the cracked password of the non-root user is ```server```. Now let's login via ssh into the machine.

### Restricted Shell (rbash)

Now when I logged in via ssh, everything looked awful i.e. I couldn't execute any commands like this... 

![Image6]()

With a quick google search it gave me the idea of ```rbash```, and I tried to bypass this restricted shell access by logging out and logging in again with bash set to ```--noprofile``` i.e. ```ssh <user>@<IP> -t "bash --noprofile"```. Also, for our convinience, set the PATH variables to default with ```export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"```, as the creator of this box have removed the PATH variables by default, to create some confusion. Now when you're done with it... Just ls and you'll see a file called user.txt, that file contains the user flag i.e. 35253d886842075b2c6390f35946e41f.

### Privilege Escalation
This part's gonna be fun, and you're again free to experiment your stuff, but atlast what I did is have a peek into the log.txt present inside the SV-502 folder. It showed me this...

![Image7]()

I searched for the file with find command but couldn't find it, guess it might be stored somewhere inside the root directory. So I did google about chkrootkit and saw there's a vulnerability in the installed version of it. I was going through the exploit on exploit-db which said me this...

![Image8]()

As said by the image... I created a file in /tmp directory named update, gave executable permissions and wrote a simple bash script into it.

![Image9]()

This simple scripts change the root password to hacked, from whatever default the creator did set. Now all we gotta do is run chkrootkit in order to run this script as root... So I went back to my homedirectory and ran ```honeypot.decoy``` elf executable. Selected option 5, so that I could start the chkrootkit installed in the root directory.

![Image10]()

At the same moment you will notice you can login into the root with the new password you used in the update script.

![Image11]()

Here we have our root flag... 1c203242ab4b4509233ca210d50d2cc5
