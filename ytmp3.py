import time
import os
import random
try:
 from pytube import YouTube

 import fontstyle as f

 from colorama import Fore , init
except:
 print('Installing required packages')
 os.system('pip install -r requirements.txt') 
 print('Run the code again')


logo_design_1 = Fore.GREEN + '''                                             
  .;'                     `;,
 .;'  ,;'             `;,  `;,   {0}ytmp3
.;'  ,;'  ,;'     `;,  `;,  `;,
::   ::   :   {1}( ){0}   :   ::   ::                              
':.  ':.  ':. {1}/_\{0} ,:'  ,:'  ,:'          
 ':.  ':.    {1}/___\{0}    ,:'  ,:'     {1}by KAIF_CODEC{0}
  ':.       {1}/_____\{0}      ,:'
           {1}/       \\{0}
'''.format(Fore.GREEN, Fore.WHITE, Fore.RED)



logo_design_2 = '''
\033[92m
          +hydNNNNdyh+
        +mMMMMMMMMMMMMm+
      `dMMm\033[0m:\033[92mNMMMMMMN\033[0m:\033[92mmMMd`
      hMMMMMMMMMMMMMMMMMMh
  \033[92m..  yyyyyyyyyyyyyyyyyyyy  ..                                     
\033[92m.mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm.            \033[0m Thanks for downloading!\033[92m
\033[92m:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
      mMMMMMMMMMMMMMMMMMMm
      `/++MMMMh++hMMMM++/`
          MMMMo  oMMMM
          MMMMo  oMMMM
          oNMm-  -mMNs      KAIF_CODEC'''



logo_design_3 = Fore.RED + '''
                      ,____
                      |---.\\
              ___     |    `      KAIF_CODEC
             / .-\  ./=)
            |  |"|_/\/|
            ;  |-;| /_|         REAP THE REWARDS
           / \_| |/ \ |
          /      \/\( |
          |   /  |` ) |
          /   \ _/    |
         /--._/  \    |
         `/|)    |    /
           /     |   |
         .'      |   |
        /         \  |
       (_.-.__.__./  /

'''

logo_design_4 = Fore.GREEN + '''
    .o oOOOOOOOo                                            OOOo
    Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
    OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
    OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
    `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
    .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
    OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
   oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
 "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
    Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                 '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                      `$"  `OOOO' `O"Y ' `OOOO'  o             .
    .                  .     OP"          : o     .

         KAIF_CODEC'''



def main_title():       
 logo_list=[logo_design_1,logo_design_2,logo_design_3,logo_design_4,logo_design_4]
 title=random.choice(logo_list)
 print(title)
 




#all texts__


text1=f.apply("Enter the url of the video you want to download  ","/green/bold")
text2=f.apply("Enter the destination path where you want to save this mp3  ","/yellow/bold")
text3=f.apply("(Or leave blank to save in current directory)","/yellow/bold")
text4=f.apply("Taken time to download =", "/cyan/bold")




def main_mp3():
 main_title()
 print('''







''')
 print(text1)
 url=input(">> ")
 print("  ")
 time1=int(time.time())
 yt = YouTube(str(url))

 video= yt.streams.filter(only_audio=True).first()
 destination="/storage/emulated/0/Download/song"
 


 out_file = video.download(output_path=destination)


 base, ext = os.path.splitext(out_file)
 new_file = base + '.mp3'
 os.rename(out_file, new_file)

 ltext=f.apply(" Has been successfully downloaded.","/green/bold")
 print(yt.title ,ltext) 

 time2=int(time.time())

 

 ftime=time2-time1
 coloured_time=f.apply(ftime,"/cyan/bold")
 print(text4,coloured_time," sec")
 print("  ")

main_mp3()
exitc=f.apply("Press [ENTER] to continue downloading another content  ","/green/bold")
print(exitc)
choice=input(">>")
while (choice =="" or choice == " " ):
 main_mp3()
 
else:
 exit()


#                      ,____
#                      |---.\\
#              ___     |    `  
#             / .-\  ./=)
#            |  |"|_/\/|
#            ;  |-;| /_|         
#           / \_| |/ \ |
#          /      \/\( |
#          |   /  |` ) |
#          /   \ _/    |
#         /--._/  \    |
#         `/|)    |    /
#           /     |   |
#         .'      |   |
#        /         \  |
#       (_.-.__.__./  /

#THERE'S A DEVIL IN THE CODE. DON'T TRY TO #CHANGE THE CODE,NOW YOU ARE IN CONTROL.
#MESSAGE BY 'KAIF_CODEC'.
 






