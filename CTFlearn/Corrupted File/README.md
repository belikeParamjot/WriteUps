# Corrupted File
## About

### General Information

__Challenge Description__: Help! I can't open this file. Something to do with the file header… Whatever that is.

__Challege Category__: FORENSICS

__Challenge Difficulty__: HARD

__Skills__: Observational

__Tools__: hexedit, vim

Download the file [here.](https://mega.nz/file/aKwGFARR#rS60DdUh8-jHMac572TSsdsANClqEsl9PD2sGl-SyDk)

## Solution

Now tbh, whenever I see such challenges with name corrupted file... My eyes go to the meta header of the file... So when I downloaded the file... I saw the extension ```.gif```. So I went to this [site](https://en.wikipedia.org/wiki/List_of_file_signatures), and searched for GIFs.

![Image1](https://github.com/iParamjotSingh/WriteUps/blob/master/CTFlearn/Corrupted%20File/1.png)

Then I viewed the header of the file to check how much of the header is included. I found out that the header was completed with the bytes that were not similar i.e. GIF8 _9a_. So our only work to add the rest of the bytes of the gif header i.e. ___GIF8___

So I opened the file in vim with ```vim unopenable.gif```(or you can use any text editor to edit it) and added __GIF8__ in the beginning, which made it look like this.

![Image2](https://github.com/iParamjotSingh/WriteUps/blob/master/CTFlearn/Corrupted%20File/2.png)

Then save the file. When I opened it... It gave me the gif with the flag in base64 format. I then used this [site] where I uploaded the gif to reduce it's speed. Change the speed according to your convenience, and write the flag manually in your notepad which is displayed at a reduced speed. 

![Image3](https://github.com/iParamjotSingh/WriteUps/blob/master/CTFlearn/Corrupted%20File/3.png)

Then decode the flag with the command ```echo "<string>" | base64 -d``` which gives you your flag. 

![Image4](https://github.com/iParamjotSingh/WriteUps/blob/master/CTFlearn/Corrupted%20File/4.png)

__Flag__: flag{g1f_or_j1f}
