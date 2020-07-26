# Sunset: 1
## About
__Series__: Sunset  
__Difficulty__: Easy/Intermediate  
__VM Page__: https://www.vulnhub.com/entry/sunset-1,339/  
__Download__:  https://mega.nz/#!AGZU1C6J!y_Pc0BEJ2EsAFiBeUY91s4e9mgrlo8sN4aT3wKVen6s  

## Solution

### Enumeration

A simple nmap scan gave me these results:

![Image1]()

### Login with FTP
As we can we see this vm has 2 open ports, ftp and ssh respectively. Also, the result here shows that ftp has anonymous login enabled. I logged into ftp via credential anonymous:anonymous, and found it has one file named backup stored in its directory...

![Image2]()

After I downloaded the file, it gave me a list of user, with their passwords encrypted in sha512crypt (How did I identify that? The starting of sha512 hashes are with $6$). I extracted the password hashes into another file.

![Image3]()

### Cracking the hashes

With the help of hashcat, I bruteforced the passwords in the ```hashes``` file, which cracked 1 hash for me...

![Image4]()

### Logging with SSH

I then used the user,pass sunset:cherry14 and logged into the target vm using ssh.

![Image5]()

Here we got our user flag.

### Privilege Escalation
Tried running sudo -l which gave me the binary ```/usr/bin/ed``` that I can run using root.

![Image6]()

So I went to this [site](https://gtfobins.github.io/) and searched the binary named ed. I found that there is a simple way I can use this binary to gain root access.

![Image7]()

KABOOM!! The root flag is ours.
