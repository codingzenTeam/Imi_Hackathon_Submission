import random
player_name = input("Enter your name")
print("Hello",player_name,",welcome to the guessing game!")
count=0
attempts=0


number = random.randint(1,250)
choice = "y"
while choice =="y":
    choice = choice.lower()
    guess = int(input("What number am I thinking of between 1 and 250? You only have 20 tries to guess the number correctly"))
    attempts=+1
    while guess != number:
        if guess > number:
                guess = int(input("You guessed too high. Try again"))
                attempts=+1
                count=count+0
        elif guess < number:
                guess = int(input("You guessed too low. Try again"))
                count=count+0
                attempts+=1
        
        if attempts >= 20:
            print("Game over, better luck next time")
            count=count-5
            choice=input("Do you wish to restart?(y/n)")
            break
        if attempts!=20 and guess==number:
            print("Hurray",player_name,",you won")
            
            print(count)
            choice=input("Do you wish to continue playing?\n (y/n)")

            
                






























































































































































































































































































































































































































































































































































































































































































































































#print("                       ...,?77??!~~~~!???77?<~.... \n ..?7`                           `7!.. \n .,=`          ..~7^`   I                  ?1. \n........  ..^            ?`  ..?7!1 .               ...??7 \n.        .7`        .,777.. .I.    . .!          .,7! \n ..     .?         .^      .l   ?i. . .`       .,^ \n b    .!        .= .?7???7~.     .>r .      .= \n .,.?4         , .^         1        `     4... \n J   ^         ,            5       `         ?<. \n .%.7;         .`     .,     .;                   .=. \n .+^ .,       .%      MML     F       .,             ?, \n P   ,,      J      .MMN     F        6               4. \n l    d,    ,       .MMM!   .t        ..               ,, \n ,    JMa..`         MMM`   .         .!                .; \n r   .M#            .M#   .%  .      .~                 ., \n dMMMNJ..!                 .P7!  .>    .         .         ,, \n .WMMMMMm  ?^..       ..,?! ..    ..   ,  Z7`        `?^..  ,, \n ?THB3       ?77?!        .Yr  .   .!   ?,              ?^C \n ?,                   .,^.` .%  .^      5. \n 7,          .....?7     .^  ,`        ?. \n `<.                 .= .`'           1 \n ....dn... ... ...,7..J=!7,           ., \n ..=     G.,7  ..,o..  .?    J.           F \n .J.  .^ ,,,t  ,^        ?^.  .^  `?~.      F \n r %J. $    5r J             ,r.1      .=.  .% \n r .77=?4.    ``,     l ., 1  .. <.       4., .$..    .X..   .n..  ., J. r .`  J.       `' \n .?`  .5        `` .%   .% .' L.'    t \n ,. ..1JL          .,   J .$.?`      .              \n 1.          .=` ` .J7??7<.. .; \n JS..    ..^      L        7.: \n `> ..       J.  4.  \n +   r `t   r ~=..G. \n =   $  ,.  J \n 2   r   t  .; \n .,7!  r   t`7~..  j.. \n j   7~L...$=.?7r   r ;?1. \n 8.      .=    j ..,^   .. \n r        G              . \n .,7,        j,           .>=. \n .J??,  `T....... %             .. \n ..^     <.  ~.    ,.             .D \n .?`        1   L     .7.........?Ti..l \n ,`           L  .    .%    .`!       `j, \n .^             .  ..   .`   .^  .?7!?7+. 1 \n .`              .  .`..`7.  .^  ,`      .i.; \n .7<..........~<<3?7!`    4. r  `          G% \n J.` .!           % \n JiJ           .` \n .1.          \n ?1.     .'         \n 7<..%")