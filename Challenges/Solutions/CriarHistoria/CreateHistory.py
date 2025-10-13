print("Welcome to the hero's journey!")
print("In this adventure you must enter a castle to defeat the dragon that has been destroying all the nearby villages, and thus, save the world.")
print("Are you ready? If yes, grab your sword!")

userChoice = input().capitalize()

if userChoice == "Yes":
    print("You are heading to your next adventure!")
    print(r"""            
            /<
           /<
 |\_______{o}----------------------------------------------------------_
[\\\\\\\\\\\{*}:::<=============================================-       >
 |/~~~~~~~{o}----------------------------------------------------------~
           \<
            \<
             \>""")
    
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Will you walk north or south to reach the castle?")
    northOrSouth = input().capitalize()
    if northOrSouth == "North":
        print("You walk through a strange path, barely seeing where you step. After 5 days walking, a group of spiders falls upon you!")
        print(r"""     /      \         __      _\( )/_
    \  \  ,,  /  /   | /  \ |    /(O)\ 
     '-.`\()/`.-'   \_\\  //_/    _.._   _\(o)/_  //  \\
    .--_'(  )'_--.   .'/()\'.   .'    '.  /(_)\  _\\()//_
   / /` /`""`\ `\ \   \\  //   /   __   \       / //  \\ \
    |  |  ><  |  |          ,  |   ><   |  ,     | \__/ |
    \  \      /  /         . \  \      /  / .              _
   _    '.__.'    _\(O)/_   \_'--`(  )'--'_/     __     _\(_)/_
_\( )/_            /(_)\      .--'/()\'--.    | /  \ |   /(O)\
 /(O)\  //  \\         _     /  /` '' `\  \  \_\\  //_/
       _\\()//_     _\(_)/_    |        |      //()\\ 
 jgs  / //  \\ \     /(o)\      \      /       \\  //
       | \__/ |""")
        print("Your ending is to die poisoned.")
        print("Game over.")
    elif northOrSouth == "South":
        print("The south is a calm and peaceful path. There you find a horse that helps you reach your goal faster and without getting tired.")
        print(r"""                       \       ,
                                     |\.--._/|
                                    /\ )  )\\/
                                   /(   \  / \
                                  /(   J `(   \
                                 / ) | _\     /
                                /|)  \  eJ    L
                               |  \ L \   L   L
                              /  \  J  `. J   L
                              |  )   L   \/   \
                             /  \    J   (\   /
           _....___         |  \      \   \```
    ,.._.-'        '''--...-||\     -. \   \
  .'.=.'                    `         `.\ [ Y
 /   /                                  \]  J
Y / Y                                    Y   L
| | |          \                         |   L
| | |           Y                        A  J
|   I           |                       /I\ /
|    \          I             \        ( |]/|
J     \         /._           /        -tI/ |
 L     )       /   /'-------'J           `'-:.
 J   .'      ,'  ,' ,     \   `'-.__          \
  \ T      ,'  ,'   )\    /|        ';'---7   /
   \|    ,'L  Y...-' / _.' /         \   /   /
    J   Y  |  J    .'-'   /         ,--.(   /
     L  |  J   L -'     .'         /  |    /\
     |  J.  L  J     .-;.-/       |    \ .' /
     J   L`-J   L____,.-'`        |  _.-'   |
      L  J   L  J                  ``  J    |
      J   L  |   L                     J    |
       L  J  L    \                    L    \
       |   L  ) _.'\                    ) _.'\
       L    \('`    \                  ('`    \
        ) _.'\`-....'                   `-....'
       ('`    \
        `-.___/   sk""")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("You finally reach the castle!")
        print("As soon as you enter the structure, two doors open: a red one and a blue one.")
        print("Which one will you cross?")
        redOrBlue = input().capitalize()
        if redOrBlue == "Red":
            print("You arrive at the beast's lair.")
            print("The battle begins now.")
            print("The beast wakes up and looks into your eyes.")
            print("Quickly it starts opening its mouth to devour you!")
            print(r"""                                       \/
                                       ^`'.
                                       ^   `'.
             (                         ^      `'.
           )  )        \/              ^         `'.
         (   ) @       /^              ^            `'.
       )  )) @@  )    /  ^             ^               `'.
      ( ( ) )@@      /    ^            ^                  `'.
    ))  ( @@ @ )    /      ^           ^                     `'.
   ( ( @@@@@(@     /       |\_/|,      ^                        `'.
  )  )@@@(@@@     /      _/~/~/~|C     ^                           `'.
((@@@(@@@@@(     /     _(@)~(@)~/\C    ^                              `'.
  ))@@@(@@)@@   /     /~/~/~/~/`\~`C   ^             __.__               `'.
   )@@@@(@@)@@@(     (o~/~o)^,) \~ \C  ^          .' -_'-'"...             `.
    ( (@@@)@@@(@@@@@@_~^~^~,-/\~ \~ \C/^        /`-~^,-~-`_~-^`;_           `.
      @ )@@@(@@@@@@@   \^^^/  (`^\.~^ C^.,  /~^~^~^/_^-_`~-`~-~^\- /`'-./`'-. ;
       (@ (@@@@(@@      `''  (( ~  .` .,~^~^-`-^~`/'^`-~ _`~-`_^-~\         ^^
           @jgs@             (((` ~ .-~-\ ~`-_~`-/_-`~ `- ~-_- `~`;
          /                 /~((((` . ~-~\` `  ~ |:`-_-~_~`  ~ _`-`;
         /   Art by        /~-((((((`.\-~-\ ~`-`~^\- ^_-~ ~` -_~-_`~`;
        /     joan stark  /-~-/(((((((`\~-~\~`^-`~`\ -~`~\-^ -_~-_`~-`;
       /                 /~-~/  `((((((|-~-|((`.-~.`Y`_,~`\ `,- ~-_`~-`;
      /              ___/-~-/     `"|~-~|"''    /~-^ .'    `:~`-_`~-~`;
     /         _____/  /~-~/           |-~-|      /-~-~.`      `:~^`-_`^-:
    /    _____/        ((((            ((((      (((((`           `:~^-_~-`;
    \___/                                                          _^-~`;
                                                                    `:~-^`:
                                                                  ,`~-~`,`
                                                                 ,"`~.,'
                                                               ,"-`,"`
                                                             ,"_`,"`
                                                            ,","`
                                                         ;~-~_~~;
                                                          '. ~.'""")
            print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("You have two options: Jump into its mouth or Dodge.")
            jumpOrDodge = input().capitalize()
            if jumpOrDodge == "Jump":
                print("You are swallowed by the monster!")
                print("But you manage to stay alive inside its belly!")
                print("You make a cut from the inside out, thus defeating the beast!")
                print("You are the hero!")
                print("The sun rises for a new world, this time, more peaceful!")
                print(r"""              |
                    \       /
                      .-"-.
                 --  /     \  --
`~~^~^~^~^~^~^~^~^~^-=======-~^~^~^~~^~^~^~^~^~^~^~`
`~^_~^~^~-~^_~^~^_~-=========- -~^~^~^-~^~^_~^~^~^~`
`~^~-~~^~^~-^~^_~^~~ -=====- ~^~^~-~^~_~^~^~~^~-~^~`
`~^~^~-~^~~^~-~^~~-~^~^~-~^~~^-~^~^~^-~^~^~^~^~~^~-`
                  jgs""")
            elif jumpOrDodge == "Dodge":
                print("You try to dodge but the dragon's tail hits your legs.")
                print("You fall to the ground and before you can get up, the beast crushes you with its paw.")
                print(r"""                                 |                                           
                                 ||                                          
       -==-____        _--_   ___||___   _--_        ____-==-                
          ---__----___/ __ \--  || |  --/ __ \___----__---                   
               ---__ / /  \ \   \\ /   / /  \ \ __---                        
                    -\|    \ \  _\/_  / /    |/-                             
                   __/ \_()/\ \//  \\/ /\()_/ \__                            
                  /_ \ / ~~  `-'    `-'  ~~ \ / _\                           
                 |/_\ |(~/   /\  /\  /\   \~)| /_\|                          
                  /_  | /   (O ` \/ ' O)   \ |  _\                           
                   _\ \_\/\___--~~~~--___/\/_/ /_                            
                  /    _/\^\ V~~V/~V~~V /^/\_    \                           
                  \/\ / \ \^\  |( /    /^/ / \ /\/                           
                     \\   /\^\  \\\   /^/\   //                              
'The Great Mottled     \ | /\^\  \/  /^/\ | /                                
      Dragon'            |( /\_\^__^/_/\ )|                                  
-Psyra Silverscale-      | \\__--__--__// |                                  
                        /~~~~~~~~~~~~~~~~~~\                                 
                       |/|  /\  /\/\  /\  |\|                                
                       ||| | | ( () ) | | |||                                
                       |\|  \/  \/\/  \/  |/|                                
                        \__________________/                                 
                        | (____------____) |""")
                print("You are crushed.")
                print("Game over!")
        elif redOrBlue == "Blue":
            print("You enter the chamber and soon find it strange how empty it is.")
            print("You wonder what might be happening but it's already too late.")
            print("Ghosts appear from everywhere and you have nowhere to run.")
            print(r"""                  .-.
         heehee      /aa \_
                   __\-  / )                 .-.
         .-.      (__/    /        haha    _/oo \
       _/ ..\       /     \               ( \v  /__
      ( \  u/__    /       \__             \/   ___)
       \    \__)   \_.-._._   )  .-.       /     \
       /     \             `-`  / ee\_    /       \_
    __/       \               __\  o/ )   \_.-.__   )
   (   _._.-._/     hoho     (___   \/           '-'
jgs '-'                        /     \
                             _/       \    teehee
                            (   __.-._/""")
            print("You die.")
            print("Game over.")
elif userChoice == "No":
    print("You rest by the fire like a coward.")
    print(r"""        (                 ,&&&.
            )                .,.&&
           (  (              \=__/
               )             ,'-'.
         (    (  ,,      _.__|/ /|
          ) /\ -((------((_|___/ |
        (  // | (`'      ((  `'--|
      _ -.;_/ \\--._      \\ \-._/.
     (_;-// | \ \-'.\    <_,\_\`--'|
     ( `.__ _  ___,')      <_,-'__,' 
jrei  `'(_ )_)(_)_)'""")
else:
    print("Invalid option!")