print("Wecome to Nokia Menu\nPick an Option\n")

print("""       
                    Menu

                  1. Phonebook
                  2. Messages
                  3. Chat
                  4. Call register
                  5. Set tones
                  6. Settings
                  7. Call divert
                  8. Games
                  9. Calculator
                  10. Reminders
                  11. Clock
                  12. Profiles
                  13. SIM services 
                  0.back \n   """)

menu = int(input("Pick an Option from 1- 13\n "))  
    
match (menu):

    case 1:
            print("""
               phone_book:
               1. Search\n
               2. Service Nos.\n
               3. Add name\n
               4. Erase\n
               5. Edit\n
               6. Assign tone\n
               7. Send b’card\n
                          
             """)

phoneBook = int(input("Enter Number "))

if phoneBook == 8:
    print("""   
                           Options\n
                          1. Type of view
                          2. Memory status 
                              
                                """    
                                    )

    case 2: 
        print("""       
                          Messages
                          1. Write messages
                          2. Inbox
                          3. Outbox
                          4. Picture messages
                          5. Templates
                          6. Smileys
                          7. Message settings
                          8. Info service
                          9. Voice mailbox number
                          10. Service command editor\n
                                              """)

                message_settings = int(input("Enter Number "))

                if message_settings == 7:

                    print("""       Message settings\n

                                  1. Set
                                  2. Common \n"""
                                   )


                set = int(input("Enter Number "))       
                if set == 1: 
                    print("""   Set

                                     1. Message centre number
                                     2. Messages sent as
                                     3. Message validity \n"""    
                                            )


                 else: 
                    print("""      Common\n

                                   1. Delivery reports
                                   2. Reply via same centre
                                   3. Character support \n"""
                                        )


    case 3: 
        print("Chat")
    
     case 4: 
            
            call_register = int(input("Enter Number"))
            if call_register == 5: 
                print("""    Show call duration

                                1. Last call duration
                                2. All calls’ duration
                                3. Received calls’ duration
                                4. Dialled calls’ duration
                                5. Clear timers  \n"""
                           )

             if call_register == 6: 
                print("""   Show call costs

                                        1. Last call cost
                                        2. All calls’ cost
                                        3. Clear counters \n"""
                            )
             if call_register == 7: 
                print(""" Call cost settings
                                     1. Call cost limit
                                     2. Show costs in \n"""

                            )

    case 5: 
        print("""                
                        Tones
                         1. Ringing tone
                         2. Ringing volume
                         3. Incoming call alert
                         4. Composer
                         5. Message alert tone
                         6. Keypad tones
                         7. Warning and game tones
                         8. Vibrating alert
                         9. Screen saver \n"""
                 )

      case 6: 
          print("""     
                         Settings
                         1. Call settings
                         2. Phone settings
                         3. Security settings
                         4. Restore factory settings \n"""
                )

            settings = int(input("Enter Number"))
            if settings == 1: 
                     print("""  Call settings
                                    1. Automatic redial
                                    2. Speed dialling
                                    3. Call waiting options
                                    4. Own number sending
                                    5. Phone line in use
                                    6. Automatic answer  \n"""
                            )
             if settings == 2: 
                    print("""  Phone settings
                                1. Language
                                2. Cell info display
                                3. Welcome note
                                4. Network selection
                                5. Lights2
                                6. Confirm SIM service actions  \n """
                                
               if security_settings == 3: 
                     print("""  Security settings
                                    1. PIN code request
                                    2. Call barring service
                                    3. Fixed dialling
                                    4. Closed user group
                                    5. Phone security
                                    6. Change access codes \n"""                   
                            )
                 case 7:
                    print("Call divert")

                case 8:
                    print("Games")

                case 9:
                    print("Calculator")

                case 10:
                    print("Reminders")

                case 11: 
                    print("""          Clock
                                1. Alarm clock
                                2. Clock settings
                                3. Date setting
                                4. Stopwatch
                                5. Countdown timer
                                6. Auto update of date and time \n """
                 )
                case 12:
                    print("Profiles")

                case 13:
                    print("Sim services")

       
                












              
