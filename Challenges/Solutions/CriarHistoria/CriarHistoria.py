print("Bem-vindo(a) à jornada do herói!")
print("Nessa aventura você deverá entrar dentro de um castelo para derrotar o dragão que vem destruindo todos os vilarejos dos arredores, e assim, salvar o mundo.")
print("Preparado? Se sim pegue sua espada!")

escolhaDoUsuario = input().capitalize()

if escolhaDoUsuario == "Sim":
    print("Você vai rumo à sua próxima aventura!")
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
    print("Você andará rumo ao norte ou ao sul para chegar no castelo?")
    norteOuSul = input().capitalize()
    if norteOuSul == "Norte":
        print("Você anda por um caminho estranho, e mal consegue enxergar onde pisa. Depois de 5 dias andando um grupo de aranhas caem sob você!")
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
        print("Seu final é morrer envenenado.")
        print("Fim de jogo.")
    elif norteOuSul == "Sul":
        print("O sul é um caminho calmo e pacífico. Nele você consegue achar um cavalo que lhe ajuda a chegar mais rápido ao objetivo e sem se cansar.")
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
        print("Você finalmente chega ao castelo!")
        print("Assim que você entra dentro da estrutura, duas portas se abrem: uma vermelha e uma azul.")
        print("Qual das duas você irá atravessar?")
        vermelhaOuAzul = input().capitalize()
        if vermelhaOuAzul == "Vermelha":
            print("Você chega no covil da fera.")
            print("A batalha começa agora")
            print("A fera acorda e olha nos seus olhos.")
            print("Rapidamente ela começa a abrir a boca para te devorar!")
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
                                                             ,"_`,"
                                                            ,","`
                                                         ;~-~_~~;
                                                          '. ~.'
            """)
            print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Você tem duas opções: Pular dentro da boca dela ou desviar")
            pularOuDesviar = input().capitalize()
            if pularOuDesviar == "Pular":
                print("Você é engolido pelo monstro!")
                print("Porém consegue ficar vivo dentro da barriga!")
                print("Você realiza um corte de dentro para fora, assim, derrotando a fera!")
                print("Você é o herói!")
                print("O sol nasce para um novo mundo, dessa vez, mais pacífico!")
                print(r"""              |
                    \       /
                      .-"-.
                 --  /     \  --
`~~^~^~^~^~^~^~^~^~^-=======-~^~^~^~~^~^~^~^~^~^~^~`
`~^_~^~^~-~^_~^~^_~-=========- -~^~^~^-~^~^_~^~^~^~`
`~^~-~~^~^~-^~^_~^~~ -=====- ~^~^~-~^~_~^~^~~^~-~^~`
`~^~^~-~^~~^~-~^~~-~^~^~-~^~~^-~^~^~^-~^~^~^~^~~^~-`
                  jgs""")
            elif pularOuDesviar == "Desviar":
                print("Você tenta desviar mas o rabo do dragão bate nas suas pernas.")
                print("Você cai no chão e antes que consiga levantar, a fera lhe esmaga com sua pata.")
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
                print("Você morre esmagado.")
                print("Fim de jogo!")
        elif vermelhaOuAzul == "Azul":
            print("Você entra na câmara e logo acha estranho o quão vazio ela está.")
            print("Você  pensa o que pode estar acontecendo mas já é tarde demais.")
            print("Fantasmas aparecem por todos os lados e você não tem pra onde correr.")
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
            print("Você morre.")
            print("Fim de jogo.")
elif escolhaDoUsuario == "Nao" or escolhaDoUsuario == "Não":
    print("Você descansa na fogueira como um covarde.")
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
    print("Opção inválida!")