'''This is a simple trivia game where you need to answer the multiple-choice questions as they are displayed to you.'''

#Import key packages
import random

#Define the key function
def trivia():

    #All defined questions are listed here
    questions = {1:{"Q": "What is the capital city of New Zealand?\n Is it: a) Auckland, b) Wellington, c) Sydney or d) Christchurch?",
                "A": "b"},
                 2:{"Q":"In which UK country is the town Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch located?\n Is it: a) Scotland, b) England, c) Wales or d) Northern Ireland?",
                "A":"c"},
                 3:{"Q":"True or False: The dove animal often symbolizes peace in art.",
                "A":"true"},
                 4:{"Q":"What is the national flower of Australia?\n Is it: a) Waratah, b) Wattle, c) Banksia, or d) Jacaranda?",
                "A":"b"},
                5:{"Q":"What is the Chinese Zodiac animal for this year (2021)?\n Is it: a) Rat, b) Dragon, c) Ox, or d) Tiger?",
                "A":"d"},
                6:{"Q":"According to Monty Python and the Holy Grail, if a witch could float on water, what should it weigh the same as?\n Is it: a) A duck, b) Apples, c) Stones or d) Wood?",
                "A":"a"},
                7:{"Q":"How many crochets are equal to one semibreve?\n Is it: a) 2, b) 4, c) 6 or d) 8?",
                "A":"b"},
                8:{"Q":"Which geopolitical war ended in 1991 along with the collapse of the Soviet Union?\n Was it: a) The Cold War, b) The Red War or c) The Second World War?",
                "A":"a"},
                9:{"Q":"Which African country was the first to qualify for the FIFA world cup? In which year did they qualify?\n Was it: a) Egypt, 1930, b) Egypt, 1934, c) Morocco, 1930, or d) Morocco, 1934?",
                "A":"b"},
                10:{"Q":"True or False: Ultimate Frisbee (also known as ‘Ultimate’) is an international sport.",
                "A":"true"},
                11:{"Q":"Which country won the 2018 FIFA world cup?\n Was it: a) Japan, b) Belgium, c) England or d) France?",
                "A":"d"},
                12:{"Q":"Which iconic children’s character was created by the Rev. Wilbert Awdry to amuse his son who was sick with measles?\n Was it: a) Noddy, b) Paddington Bear, c) The Very Hungry Caterpillar, or d) Thomas the Tank Engine?",
                "A":"d"},
                13:{"Q":"What is the largest animal on the Earth?\n Is it: a) Beluga Whale, b) Blue Whale, c) Humpback Whale or d) Sperm Whale?",
                "A":"b"},
                14:{"Q":"Which Japanese emperor was in power during World War II?\n Was it: a) Mutsuhito, b) Hirohito, c) Yoshihito, or Akihito?",
                "A":"b"},
                15:{"Q":"Which dual monarchy collapsed after the First World War?\n Was it: a) Schleswig-Holstein, b) England-Scotland, c) Austria-Hungary or d) China-Japan?",
                "A":"c"},
                16:{"Q":"Which of these countries was previously known as Caledonia?\n Was it: a) Scotland, b) England, c) Wales, or Northern Ireland?",
                "A":"a"},
                17:{"Q":"Which of the following foreign (i.e. non-English) languages is most commonly spoken around the world?\n Is it: a) French, b) Spanish, c) Mandarin Chinese, or d) Arabic?",
                "A":"c"},
                18:{"Q":"Which African country is closest to Gibraltar?\n Is it: a) Egypt, b) Algeria, c) Libya or d) Morocco?",
                "A":"d"},
                19:{"Q":"Who painted American Gothic?\n Was it: a) Grant Wood, b) Vincent Van Gogh, c) Andy Warhol, or d) Michelangelo?",
                "A":"a"},
                20:{"Q":"Which of the following is a/the national flower of Japan?\n Is it: a) Thistle, b) Protea, c) Cherry blossom, or d) Lotus?",
                "A":"c"},
                21:{"Q":"According to Norse mythology, what is the name of the place where ancient Norse heroes chosen by Odin would go after death?\n Is it: a) Hades, b) Valhalla, c) Asgard, or d) Vyraj?",
                "A":"b"},
                22:{"Q":"In which of these countries might you wear hanbok?\n Would it be: a) Vietnam, b) Thailand, c) South Korea, or d) China?",
                "A":"c"},
                23:{"Q":"From which country did renowned director Ingmar Bergman come from?\n Was it: a) France, b) Germany, c) Sweden, or The United States?",
                "A":"c"},
                24:{"Q":"How many strings does a ukulele traditionally have?\n Is it: a) 2, b) 4, c) 6 or d) 8?",
                "A":"b"},
                25:{"Q":"Which country did Winston Churchill describe as “a riddle, wrapped in a mystery, inside an enigma”?\n Was it: a) Finland, b) Soviet Union/Russia, c) United States, or d) Switzerland?",
                "A":"b"},
                26:{"Q":"Which British politician was stuck on a zip wire while trying to promote the London Olympic Games in 2012?\n Was it: a) Theresa May, b) David Cameron, c) Jeremy Corbyn or d) Boris Johnson?",
                "A":"d"},
                27:{"Q":"The current world chess champion is Magnus Carlsen. Which country is he from?\n Is it: a) Norway, b) Sweden, c) Denmark or d) Germany?",
                "A":"a"},
                28:{"Q":"With the eventual inclusion of boxing, in which year were women finally able to compete in all sports in the Summer Olympics?\n Was it: a) 2008, b) 2012, or c) 2016?",
                "A":"b"},
                29:{"Q":"Which rugby team won the 2019 Rugby World Cup?\n Was it: a) New Zealand, b) France, c) United States or d) South Africa?",
                "A":"d"},
                30:{"Q":"Which children’s author is known for her stories about Noddy, The Famous Five and The Secret Seven?\n Is it: a) Enid Blyton, b) Roald Dahl, c) Dr. Seuss, or d) Agatha Christie?",
                "A":"a"},
                31:{"Q":"If animals can eat both plants and other animals, then they are known as what?\n Are they: a) Carnivores, b) Herbivores, or c) Omnivores?",
                "A":"c"},
                32:{"Q":"What is the largest organ in the human body?\n Is it: a) Heart, b) Liver, c) Skin or d) Large intestines?",
                "A":"c"},
                33:{"Q":"What is acrophobia?\n Is it a: a) fear of insects, b) fear of heights, c) fear of technology or d) fear of acne?",
                "A":"b"},
                34:{"Q":"Which Asian country was formed in 1947?\n Is it: a) Taiwan, b) Bangladesh, c) Singapore or d) Pakistan",
                "A":"d"},
                35:{"Q":"Which war took place between the House of Lancaster and the House of York?\n Was it: a) English Civil War, b) Wars of the Roses, or c) Glorious Revolution?",
                "A":"b"},
                36:{"Q":"True or False: Chewing gum in Singapore is illegal.",
                "A":"false"},
                37:{"Q":"Which game franchise was considered to have brought Nintendo’s waning sales back up in the 1990’s?\n Is it: a) Super Mario Bros., b) Pokémon, c) Sonic the Hedgehog or d) Zelda?",
                "A":"b"},
                38:{"Q":"In which part of the human body would you find the anterior cruciate ligament (aka ACL)?\n Is it: a) Knee, b) Elbow, c) Neck or d) Ankle?",
                "A":"a"},
                39:{"Q":"According to J.R.R. Tolkien, in which region do Hobbits commonly live?\n Is it: a) Mordor, b) Rohan, c) Gondor, or d) The Shire?",
                "A":"d"},
                40:{"Q":"Where were the 2018 Commonwealth Games held?\n Is it: a) Glasgow, b) Gold Coast, c) New Delhi or d) Melbourne?",
                "A":"b"},
                41:{"Q":"Which of the following current or former leaders pitched a film featuring the male lead Mamaduke Montmerency Burton.\n Is it: a) Tony Abbott, b) Donald Trump, c) Boris Johnson or d) David Cameron?",
                "A":"c"},
                42:{"Q":"Which country is closest to the Scilly Isles?\n Is it: a) UK, b) France, c) Haiti or d) Australia?",
                "A":"a"},
                43:{"Q":"In which ocean is Seychelles located?\n Is it: a) Pacific, b) Atlantic, c) Indian, or d) Arctic?",
                "A":"c"},
                44:{"Q":"What is on the Irish coat of arms?\n Is it: a) A lion, b) A potato, c) A harp, or d) A meadow?",
                "A":"c"},
                45:{"Q":"In which ancient civilisation would people have eaten a large meal known as cena?\n Is it a) Ottoman, b) Egyptian, c) Greece or d) Roman?",
                "A":"d"},
                46:{"Q":"In which country was the Lord of the Rings film series filmed?\n Was it: a) Wales, b) United States, c) New Zealand, or d) Germany?",
                "A":"c"},
                47:{"Q":"True or False: The first official use of the term Prime Minister in Britain started only in 1905.",
                "A":"true"},
                48:{"Q":"Which world leader was the first to have been tested positive for COVID-19?\n Is it: a) Jacinda Ardern, b) Donald Trump, c) Scott Morrison or d) Boris Johnson? ",
                "A":"d"},
                49:{"Q":"In which country and year was the first FIFA World Cup held?\n Was it: a) Italy, 1930, b) Italy, 1934, c) Uruguay, 1930 or d) Uruguay, 1934?",
                "A":"c"},
                50:{"Q":"Which British author wrote the novel Mary Poppins?\n Was it: a) P.L. Travers, b) Enid Blyton, c) Robert Louis Stevenson or d) A.A. Milne?",
                "A":"a"},
                51:{"Q":"In C.S. Lewis’ The Lion, The Witch and The Wardrobe, what does the Witch offer Edmund as a treat in exchange for the execution of his siblings?\n Is it: a) A chocolate bar, b) Money, c) A jewel or d) Turkish Delight?",
                "A":"d"},
                52:{"Q":"What is the rarest blood type in Australia?\n Is it: a) B-negative, b) AB-negative, c) O-positive, or d) AB-positive?",
                "A":"b"},
                53:{"Q":"What does the Periodic table symbol Na represent?\n Is it: a) Sodium, b) Nadium, c) Nitrate or d) Potassium?",
                "A":"a"},
                54:{"Q":"From which Charles Dickens novel does the character Ebenezer Scrooge originate?\n Was it: a) A Christmas Carol, b) A Tale of Two Cities, c) David Copperfield or d) Great Expectations?",
                "A":"a"},
                55:{"Q":"Which of the following wars was the shortest?\n Was it: a) The Anglo-Zanzibar War (1896), b) The Football War (1969), c) The Indo-Pakistani War (1971), or d) The Six Day War (1967)",
                "A":"a"},
                56:{"Q":"Who was the first human to travel into space?\n Was it: a) Neil Armstrong, b) Yuri Gagarin, c) Alan Shepard, or d) Gherman Titov?",
                "A":"b"},
                57:{"Q":"True or False: Japan fought in the First World War.",
                "A":"true"},
                58:{"Q":"From which country did the Mandate of Heaven originate?\n Was it: a) Egypt, b) Japan, c) Italy, or d) China?",
                "A":"d"},
                59:{"Q":"At which temperature are Celsius and Fahrenheit equal?\n Is it: a) -32 °C, b) -32 °C, c) 40 °C or d) -40 °C,?",
                "A":"d"},
                60:{"Q":"Which of the following is NOT a 'Weird Al' Yankovic song?\n Is it: a) I Want It That Way, b) Eat It, c) Couch Potato or d) White & Nerdy?",
                "A":"a"},
        }

    #Increment number of correct questions
    correct_questions = 0
    #Current question
    current_question = 0
    #Increment question numbers
    question_numbers = []
    #Define question numbers
    for i in range(1,(len(questions)+1)):
        question_numbers.append(i)
    #Sift through questions
    while len(question_numbers) > 0:
        #Choose a random question
        index = random.choice(question_numbers)
        #Print the questions as they appear
        try:
            #Print next question
            current_question += 1
            question = str(current_question) + ". " + questions[index]["Q"]
            print(question)
        except:
            continue
            #deal with it
        #Print your response to the question
        print('Please type a, b, c, d, true or false and then press ENTER.')
        #Compare answers
        ans = str(input()).lower()
        #Award a point if the answer is correct
        if ans == questions[index]["A"]:
            correct_questions += 1
            print('Correct!\n')
            question_numbers.remove(index)
        #Award no points if the answer is wrong
        else:
            correct_answer = 'Incorrect! The correct answer was ' + str(questions[index]["A"] + '\n')
            print(correct_answer)
            question_numbers.remove(index)
    
    #Print the final score
    if len(question_numbers) == 0:
        final_message = 'Your score was ' + str(correct_questions) + ' out of ' + str(len(questions))
        print(final_message)

#Call the key function
trivia()

