import os, time, textwrap, pwinput
user_history = {}
user_favorites = {}
user_payments = {}
data_user = []
data_book = [["Introduction to Algorithms", "Academic"], ["Learning JavaScript Design Patterns", "Academic"], ["Python Programming: An Introduction to Computer Science", "Academic"], ["Programming Language Design and Implementation", "Academic"], ["Python untuk Programmer Pemula", "Academic"], ["Solo Leveling", "Comic"], ["Omniscient Reader's Viewpoint", "Comic"], ["The Beginning After The End", "Comic"], ["Mercenary Enrollment", "Comic"], ["The Novel's Extra", "Comic"], ["The Dream Class", "Novel"], ["America: Militaristic or Peaceful", "Novel"], ["The Great Gatsby", "Novel"], ["The Catcher in the Rye", "Novel"], ["The Alchemist", "Novel"], ["The Joy of Cooking", "Cook"], ["The Food Lab", "Cook"], ["Salt, Fat, Acid, Heat", "Cook"], ["The Flavor Bible", "Cook"], ["The Science of Good Cooking", "Cook"]]
escape = ("exit")
class books:
    def introductionToAlgorithms(username):
        clear_console()
        option = input("="*80 + "\n" + f"{'Introduction to Algorithms':^80}" + "\n" + "="*80 + "\n" + f"Description{':':>2} Introduction to Algorithms is a book by Thomas H. Cormen, Charles\n{'':>14}E. Leiserson, Ronald L. Rivest, and Clifford Stein.  The book has\n{'':>14}been widely used  as the textbook for  algorithms courses at many\n{'':>14}universities and is  commonly cited as a reference for algorithms\n{'':>14}in published papers.  It is also one of the most popular books on\n{'':>14}the subject, along with The Art of Computer Programming by Donald\n{'':>14}Knuth." + "\n" + "="*80 + "\n" + f"Genre{':':>6} Academic" + "\n" + f"Rating{':':>5} 9.00" + "\n" + f"Author{':':>5} Thomas H. Cormen" + "\n" + f"Publisher{':':>2} The MIT Press" + "\n" + f"Year{':':>7} 1990" + "\n" + f"Language{':':>3} English" + "\n" + f"Pages{':':>6} 1312" + "\n" + "="*80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+"\n"+ "4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser file:///C:/Users/DELL/OneDrive/Documents/VSCode/ALP%20Alpro%20(Python)/assets/download/introductionToAlgorithms.pdf")
            return books.introductionToAlgorithms(username)
        elif option == "2":
            return page.introductionToAlgorithms_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "Introduction to Algorithms")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.introductionToAlgorithms(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.introductionToAlgorithms(username)
    def learningJavaScriptDesignPatterns(username):
        clear_console()
        option = input("="*80 + "\n" + f"{'Learning JavaScript Design Patterns':^80}" + "\n" + "="*80 + "\n" + f"Rating{':':>5} 9.56" + "\n" + f"Author{':':>5} Addy Osmani" + "\n" + f"Publisher{':':>2} O'Reilly Media" + "\n" + f"Year{':':>7} 2012" + "\n" + f"Language{':':>3} English" + "\n" + f"Pages{':':>6} 254" + "\n" + "="*80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+ "\n"+"4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser file:///C:/Users/DELL/OneDrive/Documents/VSCode/ALP%20Alpro%20(Python)/assets/download/learningJavaScriptDesignPatterns.pdf")
            return books.learningJavaScriptDesignPatterns(username)
        elif option == "2":
            return page.learningJavaScriptDesignPatterns_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "Learning JavaScript Design Patterns")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.learningJavaScriptDesignPatterns(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.learningJavaScriptDesignPatterns(username)
    def pythonProgrammingAnIntroductionToComputerScience(username):
        clear_console()
        option = input("=" * 80 + "\n" + f"{'Python Programming: An Introduction to Computer Science':^80}" + "\n" + "=" * 80 + "\n" + f"Rating{':':>5} 9.81" + "\n" + f"Author{':':>5} Mark Lutz" + "\n" + f"Publisher{':':>2} O'Reilly Media" + "\n" + f"Year{':':>7} 2002" + "\n" + f"Language{':':>3} English" + "\n" + f"Pages{':':>6} 400" + "=" * 80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+"\n"+ "4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser file:///C:/Users/DELL/OneDrive/Documents/VSCode/ALP%20Alpro%20(Python)/assets/download/pythonProgrammingAnIntroductionToComputerScience.pdf")
            return books.pythonProgrammingAnIntroductionToComputerScience(username)
        elif option == "2":
            return page.learningJavaScriptDesignPatterns_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "Python Programming: An Introduction to Computer Science")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.pythonProgrammingAnIntroductionToComputerScience(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.pythonProgrammingAnIntroductionToComputerScience(username)
    def programmingLanguageDesignAndImplementation(username):
        clear_console()
        option = input("=" * 80+"\n"+f"{'Programming Language Design and Implementation':^80}"+"\n"+"=" * 80+"\n"+f"Rating{':':>5} 8.96"+"\n"+f"Author{':':>5} Andrew S. Tanen"+"\n"+f"Publisher{':':>2} O'Reilly Media"+"\n"+f"Year{':':>7} 1999"+"\n"+f"Language{':':>3} English"+"\n"+f"Pages{':':>6} 400"+"\n"+"=" * 80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+"\n"+ "4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser file:///C:/Users/DELL/OneDrive/Documents/VSCode/ALP%20Alpro%20(Python)/assets/download/programmingLanguageDesignAndImplementation.pdf")
            return books.programmingLanguageDesignAndImplementation(username)
        elif option == "2":
            return page.programmingLanguageDesignAndImplementation_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "Programming Language Design and Implementation")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.programmingLanguageDesignAndImplementation(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.programmingLanguageDesignAndImplementation(username)
    def pythonUntukProgrammerPemula(username):
        clear_console()
        option = input("=" * 80+"\n"+f"{'Python untuk Programmer Pemula':^80}"+"\n"+"=" * 80+"\n"+f"Rating{':':>5} 9.07"+"\n"+f"Author{':':>5} Eko Kurniawan"+"\n"+f"Publisher{':':>2} Gramedia"+"\n"+f"Year{':':>7} 2019"+"\n"+f"Language{':':>3} English"+"\n"+f"Pages{':':>6} 400"+"\n"+"=" * 80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+"\n"+ "4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser file:///C:/Users/DELL/OneDrive/Documents/VSCode/ALP%20Alpro%20(Python)/assets/download/pythonUntukProgrammerPemula.pdf")
            return books.pythonUntukProgrammerPemula(username)
        elif option == "2":
            return page.pythonUntukProgrammerPemula_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "Python untuk Programmer Pemula")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.pythonUntukProgrammerPemula(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.pythonUntukProgrammerPemula(username)
    def soloLeveling(username):
        clear_console()
        option = input("=" * 80+"\n"+f"{'Solo Leveling':^80}"+"\n"+"=" * 80+"\n"+f"Rating{':':>5} 9.49"+"\n"+f"Author{':':>5} Chugong"+"\n"+f"Publisher{':':>2} Webtoon"+"\n"+f"Year{':':>7} 2019"+"\n"+f"Language{':':>3} English"+"\n"+f"Pages{':':>6} 400"+"\n"+"=" * 80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+"\n"+ "4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser https://asuracomic.net/series/solo-leveling-9a5c738a/chapter/0")
            return books.soloLeveling(username)
        elif option == "2":
            return page.soloLeveling_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "Solo Leveling")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.soloLeveling(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.soloLeveling(username)
    def omniscientReadersViewpoint(username):
        clear_console()
        option = input("=" * 80+"\n"+f"{'Omniscient Readers Viewpoint':^80}"+"\n"+"=" * 80+"\n"+f"Rating{':':>5} 9.14"+"\n"+f"Author{':':>5} Sing Shong"+"\n"+f"Publisher{':':>2} Reaper Scans"+"\n"+f"Year{':':>7} 2019"+"\n"+f"Language{':':>3} English"+"\n"+f"Pages{':':>6} 400"+"\n"+"=" * 80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+"\n"+ "4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser https://asuracomic.net/series/omniscient-readers-viewpoint-b2ee4cd5/chapter/0")
            return books.omniscientReadersViewpoint(username)
        elif option == "2":
            return page.omniscientReadersViewpoint_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "Omniscient Readers Viewpoint")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.omniscientReadersViewpoint(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.omniscientReadersViewpoint(username)
    def theBeginningAfterTheEnd(username):
        clear_console()
        option = input("=" * 80+"\n"+f"{'The Beginning After The End':^80}"+"\n"+"=" * 80+"\n"+f"Rating{':':>5} 9.78"+"\n"+f"Author{':':>5} TurtleMe"+"\n"+f"Publisher{':':>2} Asura Scans"+"\n"+f"Year{':':>7} 2019"+"\n"+f"Language{':':>3} English"+"\n"+f"Pages{':':>6} 400"+"\n"+"=" * 80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+"\n"+ "4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser https://www.reaperscanss.com/manga/the-beginning-after-the-end/ch-001/")
            return books.theBeginningAfterTheEnd(username)
        elif option == "2":
            return page.theBeginningAfterTheEnd_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "The Beginning After The End")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theBeginningAfterTheEnd(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theBeginningAfterTheEnd(username)
    def mercenaryEnrollment(username):
        clear_console()
        option = input("=" * 80+"\n"+f"{'Mercenary Enrollment':^80}"+"\n"+"=" * 80+"\n"+f"Rating{':':>5} 9.23"+"\n"+f"Author{':':>5} Eyo"+"\n"+f"Publisher{':':>2} North Star"+"\n"+f"Year{':':>7} 2019"+"\n"+f"Language{':':>3} English"+"\n"+f"Pages{':':>6} 400"+"\n"+"=" * 80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+"\n"+ "4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser https://www.webtoons.com/id/action/high-school-soldier/prolog/viewer?title_no=2367&episode_no=1")
            return books.mercenaryEnrollment(username)
        elif option == "2":
            return page.mercenaryEnrollment_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "Mercenary Enrollment")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.mercenaryEnrollment(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.mercenaryEnrollment(username)
    def theNovelsExtra(username):
        clear_console()
        option = input("=" * 80+"\n"+f"{'The Novels Extra':^80}"+"\n"+"=" * 80+"\n"+f"Rating{':':>5} 8.67"+"\n"+f"Author{':':>5} J. D. Salinger"+"\n"+f"Publisher{':':>2} Little, Brown and Company"+"\n"+f"Year{':':>7} 2019"+"\n"+f"Language{':':>3} English"+"\n"+f"Pages{':':>6} 400"+"\n"+"=" * 80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+"\n"+ "4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser https://komiku.id/the-novels-extra-remake-chapter-01/")
            return books.theNovelsExtra(username)
        elif option == "2":
            return page.theNovelsExtra_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "The Novels Extra")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theNovelsExtra(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theNovelsExtra(username)
    def theDreamClass(username):
        clear_console()
        option = input("=" * 80+"\n"+f"{'The Dream Class':^80}"+"\n"+"=" * 80+"\n"+f"Rating{':':>5} 9.10"+"\n"+f"Author{':':>5} Michael Lewis"+"\n"+f"Publisher{':':>2} Gramedia"+"\n"+f"Year{':':>7} 2019"+"\n"+f"Language{':':>3} English"+"\n"+f"Pages{':':>6} 400"+"\n"+"=" * 80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+"\n"+ "4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser https://www.webtoons.com/id/thriller/from-dreams-to-freedom/episode-1/viewer?title_no=4133&episode_no=1")
            return books.theDreamClass(username)
        elif option == "2":
            return page.theDreamClass_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "The Dream Class")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theDreamClass(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theDreamClass(username)
    def americaMilitaristicOrPeaceful(username):
        clear_console()
        option = input("=" * 80+"\n"+f"{'America: Militaristic Or Peaceful':^80}"+"\n"+"=" * 80+"\n"+f"Rating{':':>5} 9.91"+"\n"+f"Author{':':>5} Tom Clancy"+"\n"+f"Publisher{':':>2} Penguin"+"\n"+f"Year{':':>7} 2019"+"\n"+f"Language{':':>3} English"+"\n"+f"Pages{':':>6} 400"+"\n"+"=" * 80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+"\n"+ "4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser file:///C:/Users/DELL/OneDrive/Documents/VSCode/ALP%20Alpro%20(Python)/assets/download/americaMilitaristicOrPeaceful.pdf")
            return books.americaMilitaristicOrPeaceful(username)
        elif option == "2":
            return page.americaMilitaristicOrPeaceful_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "America: Militaristic Or Peaceful")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.americaMilitaristicOrPeaceful(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.americaMilitaristicOrPeaceful(username)
    def theGreatGatsby(username):
        clear_console()
        option = input("=" * 80+"\n"+f"{'The Great Gatsby':^80}"+"\n"+"=" * 80+"\n"+f"Rating{':':>5} 9.37"+"\n"+f"Author{':':>5} F. Scott Fitzgerald"+"\n"+f"Publisher{':':>2} HarperCollins"+"\n"+f"Year{':':>7} 1925"+"\n"+f"Language{':':>3} English"+"\n"+f"Pages{':':>6} 256"+"\n"+"=" * 80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+ "\n"+"4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser file:///C:/Users/DELL/OneDrive/Documents/VSCode/ALP%20Alpro%20(Python)/assets/download/theGreatGatsby.pdf")
            return books.theGreatGatsby(username)
        elif option == "2":
            return page.theGreatGatsby_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "The Great Gatsby")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theGreatGatsby(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theGreatGatsby(username)
    def theCatcherInTheRye(username):
        clear_console()
        option = input("=" * 80+"\n"+f"{'The Catcher in the Rye':^80}"+"\n"+"=" * 80+"\n"+f"Rating{':':>5} 7.80"+"\n"+f"Author{':':>5} J. D. Salinger"+"\n"+f"Publisher{':':>2} Scribner"+"\n"+f"Year{':':>7} 1951"+"\n"+f"Language{':':>3} English"+"\n"+f"Pages{':':>6} 224"+"\n"+"=" * 80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+"\n"+ "4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser file:///C:/Users/DELL/OneDrive/Documents/VSCode/ALP%20Alpro%20(Python)/assets/download/theCatcherInTheRye.pdf")
            return books.theCatcherInTheRye(username)
        elif option == "2":
            return page.theCatcherInTheRye_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "The Catcher in the Rye")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theCatcherInTheRye(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theCatcherInTheRye(username)
    def theAlchemist(username):
        clear_console()
        option = input("=" * 80+"\n"+f"{'The Alchemist':^80}"+"\n"+"=" * 80+"\n"+f"Rating{':':>5} 6.70"+"\n"+f"Author{':':>5} Paulo Coelho"+"\n"+f"Publisher{':':>2} HarperCollins"+"\n"+f"Year{':':>7} 1988"+"\n"+f"Language{':':>3} English"+"\n"+f"Pages{':':>6} 208"+"\n"+"=" * 80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+"\n"+ "4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser file:///C:/Users/DELL/OneDrive/Documents/VSCode/ALP%20Alpro%20(Python)/assets/download/theAlchemist.pdf")
            return books.theAlchemist(username)
        elif option == "2":
            return page.theAlchemist_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "The Alchemist")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theAlchemist(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theAlchemist(username)
    def theJoyOfCooking(username):
        clear_console()
        option = input("=" * 80+"\n"+f"{'The Joy of Cooking':^80}"+"\n"+"=" * 80+"\n"+f"Rating{':':>5} 8.04"+"\n"+f"Author{':':>5} John Grisham"+"\n"+f"Publisher{':':>2} Penguin"+"\n"+f"Year{':':>7} 2019"+"\n"+f"Language{':':>3} English"+"\n"+f"Pages{':':>6} 304"+"\n"+"=" * 80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+ "\n"+"4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser file:///C:/Users/DELL/OneDrive/Documents/VSCode/ALP%20Alpro%20(Python)/assets/download/theJoyOfCooking.pdf")
            return books.theJoyOfCooking(username)
        elif option == "2":
            return page.theJoyOfCooking_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "The Joy of Cooking")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theJoyOfCooking(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theJoyOfCooking(username)
    def theFoodLab(username):
        clear_console()
        option = input("=" * 80+"\n"+f"{'The Food Lab':^80}"+"\n"+"=" * 80+"\n"+f"Rating{':':>5} 7.94"+"\n"+f"Author{':':>5} J. Kenji López-Alt"+"\n"+f"Publisher{':':>2} W. W. Norton & Company"+"\n"+f"Year{':':>7} 2019"+"\n"+f"Language{':':>3} English"+"\n"+f"Pages{':':>6} 304"+"\n"+"=" * 80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+"\n"+ "4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser file:///C:/Users/DELL/OneDrive/Documents/VSCode/ALP%20Alpro%20(Python)/assets/download/theFoodLab.pdf")
            return books.theFoodLab(username)
        elif option == "2":
            return page.theFoodLab_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "The Food Lab")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theFoodLab(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theFoodLab(username)
    def saltFatAcidHeat(username):
        clear_console()
        option = input("=" * 80+"\n"+f"{'Salt, Fat, Acid, Heat':^80}"+"\n"+"=" * 80+"\n"+f"Rating{':':>5} 7.76"+"\n"+f"Author{':':>5} Samin Nosrat"+"\n"+f"Publisher{':':>2} Simon & Schuster"+"\n"+f"Year{':':>7} 2019"+"\n"+f"Language{':':>3} English"+"\n"+f"Pages{':':>6} 304"+"\n"+"=" * 80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+"\n"+ "4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser https://www.yumpu.com/en/document/read/68964685/pdf-salt-fat-acid-heat-mastering-the-elements-of-good-cooking-pdf")
            return books.saltFatAcidHeat(username)
        elif option == "2":
            return page.saltFatAcidHeat_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "Salt, Fat, Acid, Heat")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.saltFatAcidHeat(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.saltFatAcidHeat(username)
    def theFlavorBible(username):
        clear_console()
        option = input("=" * 80+"\n"+f"{'The Flavor Bible':^80}"+"\n"+"=" * 80+"\n"+f"Rating{':':>5} 8.42"+"\n"+f"Author{':':>5} Karen Page, Andrew Dornenburg"+"\n"+f"Publisher{':':>2} Little, Brown and Company"+"\n"+f"Year{':':>7} 2019"+"\n"+f"Language{':':>3} English"+"\n"+f"Pages{':':>6} 304"+"\n"+"=" * 80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+"\n"+ "4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser file:///C:/Users/DELL/OneDrive/Documents/VSCode/ALP%20Alpro%20(Python)/assets/download/theFlavorBible.pdf")
            return books.theFlavorBible(username)
        elif option == "2":
            return page.theFlavorBible_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "The Flavor Bible")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theFlavorBible(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theFlavorBible(username)
    def theScienceOfGoodCooking(username):
        clear_console()
        option = input("=" * 80+"\n"+f"{'The Science of Good Cooking':^80}"+"\n"+"=" * 80+"\n"+f"Rating{':':>5} 7.15"+"\n"+f"Author{':':>5} Cook's Illustrated"+"\n"+f"Publisher{':':>2} America's Test Kitchen"+"\n"+f"Year{':':>7} 2019"+"\n"+f"Language{':':>3} English"+"\n"+f"Pages{':':>6} 304"+"\n"+"=" * 80 + "\n" + "1. Download" + "\n" + "2. Read" + "\n" +"3. Favorite"+"\n"+ "4. Back" + "\n" + "="*80 + "\n" + "Choose your option (1/2/3/4): ")
        if option == "1":
            clear_console()
            os.system("python -m webbrowser file:///C:/Users/DELL/OneDrive/Documents/VSCode/ALP%20Alpro%20(Python)/assets/download/theScienceOfGoodCooking.pdf")
            return books.theScienceOfGoodCooking(username)
        elif option == "2":
            return page.theScienceOfGoodCooking_page_1(username)
        elif option == "3":
            if username not in user_favorites:
                user_favorites[username] = []
            update_favorite(username, "The Science of Good Cooking")
            clear_console()
            print("="*80 + "\n\n\n\n" + "Successfully added to favorites.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theScienceOfGoodCooking(username)
        elif option == "4":
            return category(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            time.sleep(2)
            return books.theScienceOfGoodCooking(username)
class page:
    def introductionToAlgorithms_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "Introduction to Algorithms", "Page 1")
        print("=" * 80 + "\n" + "Data Structures" + "\n")
        print(textwrap.fill("This book also contains several data structures. A data structure is a way to store and organize data in order to facilitate access and modifications. No single data structure works well for all purposes, and so it is important to know the strengths and limitations of several of them.", 75))
        print("\nTechnique")
        print(textwrap.fill("Although you can use this book as a “cookbook” for algorithms, you may someday encounter a problem for which you cannot readily find a published algorithm (many of the exercises and problems in this book, for example). This book will teach you techniques of algorithm design and analysis so that you can develop algorithms on your own, show that they give the correct answer, and understand their efficiency. Different chapters address different aspects of algorithmic problem solving.", 75))
        print("\nHard Problems")
        print(textwrap.fill("Why are NP-complete problems interesting? First, although no efficient algorithm for an NP-complete problem has ever been found, nobody has ever proven that an efficient algorithm for one cannot exist. In other words, no one knows whether or not efficient algorithms exist for NP-complete problems. Second, the set of NP-complete problems has the remarkable property that if an efficient algorithm exists for any one of them, then efficient algorithms exist for all of them. This relationship among the NP-complete problems makes the lack of efficient solutions all the more tantalizing. Third, several NP-complete problems are similar, but not identical, to problems for which we do know of efficient algorithms. Computer scientists are intrigued by how a small change to the problem statement can cause a big change to the efficiency of the best known algorithm. You should know about NP-complete problems because some of them arise surprisingly often in real applications. If you are called upon to produce an efficient algorithm for an NP-complete problem, you are likely to spend a lot of time in a fruitless search. If you can show that the problem is NP-complete, you can instead spend your time developing an efficient algorithm that gives a good, but not the best possible, solution. As a concrete example, consider a delivery company with a central depot. Each day, it loads up each delivery truck at the depot and sends it around to deliver goods to several addresses. At the end of the day, each truck must end up back at the depot so that it is ready to be loaded for the next day. To reduce costs, the company wants to select an order of delivery stops that yields the lowest overall distance traveled by each truck. This problem is the well-known “traveling-salesman problem,” and it is NP-complete. It has no known efficient algorithm. Under certain assumptions, however, we know of efficient algorithms that give an overall distance which is not too far above the smallest possible.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.introductionToAlgorithms_page_2(username)
        elif options == "2":
            clear_console()
            return books.introductionToAlgorithms(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.introductionToAlgorithms_page_1(username)
    def introductionToAlgorithms_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "Introduction to Algorithms", "Page 2")
        print("=" * 80 + "\n" + "Parallelism" + "\n")
        print(textwrap.fill("For many years, we could count on processor clock speeds increasing at a steady rate. Physical limitations present a fundamental roadblock to ever-increasing clock speeds, however: because power density increases superlinearly with clock speed, chips run the risk of melting once their clock speeds become high enough. In order to perform more computations per second, therefore, chips are being designed to contain not just one but several processing “cores.” We can liken these multicore computers to several sequential computers on a single chip; in other words, they are a type of “parallel computer.” In order to elicit the best performance from multicore computers, we need to design algorithms with parallelism in mind. This model has advantages from a theoretical standpoint, and it forms the basis of several successful computer programs, including a championship chess program.", 75))
        print("\nEfficiency")
        print(textwrap.fill("Different algorithms devised to solve the same problem often differ dramatically in their efficiency. These differences can be much more significant than differences due to hardware and software. The first, known as insertion sort, takes time roughly equal to c1n2 to sort n items, where c1 is a constant that does not depend on n. That is, it takes time roughly proportional to n2. The second, merge sort, takes time roughly equal to c2n lg n, where lg n stands for log2 n and c2 is another constant that also does not depend on n. Insertion sort typically has a smaller constant factor than merge sort, so that c1 < c2. We shall see that the constant factors can have far less of an impact on the running time than the dependence on the input size n. Let’s write insertion sort’s running time as c1n  n and merge sort’s running time as c2n  lg n. Then we see that where insertion sort has a factor of n in its running time, merge sort has a factor of lg n, which is much smaller. (For example, when n D 1000, lg n is approximately 10, and when n equals one million, lg n is approximately only 20.) Although insertion sort usually runs faster than merge sort for small input sizes, once the input size n becomes large enough, merge sort’s advantage of lg n vs. n will more than compensate for the difference in constant factors. No matter how much smaller c1 is than c2, there will always be a crossover point beyond which merge sort is faster. For a concrete example, let us pit a faster computer (computer A) running insertion sort against a slower computer (computer B) running merge sort. They each must sort an array of 10 million numbers. (Although 10 million numbers might seem like a lot, if the numbers are eight-byte integers, then the input occupies about 80 megabytes, which fits in the memory of even an inexpensive laptop computer many times over.) Suppose that computer A executes 10 billion instructions per second (faster than any single sequential computer at the time of this writing) and computer B executes only 10 million instructions per second, so that computer A is 1000 times faster than computer B in raw computing power. To make the difference even more dramatic, suppose that the world’s craftiest programmer codes insertion sort in machine language for computer A, and the resulting code requires 2n2 instructions to sort n numbers. Suppose further that just an average programmer implements merge sort, using a high-level language with an inefficient compiler, with the resulting code taking 50n lg n instructions. To sort 10 million numbers, computer A takes", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.introductionToAlgorithms_page_1(username)
        elif options == "2":
            clear_console()
            return books.introductionToAlgorithms(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.introductionToAlgorithms_page_1(username)
    def learningJavaScriptDesignPatterns_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "Learning JavaScript Design Patterns", "Page 1")
        print("=" * 80 + "\n" + "Preface" + "\n")
        print(textwrap.fill("The world of JavaScript has come a long way since I wrote the first edition of Learning JavaScript Design Patterns over 10 years ago. At that time, I was working on large-scale web applications and found that the lack of structure and organization in JavaScript code made it difficult to maintain and scale those applications. Fast forward to today, and the web development landscape has changed dramatically. JavaScript has become one of the most popular programming languages in the world and is used for everything from simple scripts to complex web applications. The JavaScript language has evolved to include modules, promises, and async/await, which has heavily influenced how we architect applications. The way developers write components, such as with React, has also significantly impacted how they think about maintainability. This has resulted in the need for modern patterns that take these new changes into account. With the rise of modern libraries and frameworks like React, Vue, and Angular, developers are now building applications that are more complex than ever before. I recognized the need for an updated version of Learning JavaScript Design Patterns to reflect the changes in JavaScript and web application development. In this second edition of Learning JavaScript Design Patterns, I aim to help developers apply modern design patterns to their JavaScript code and React applications. The book covers more than 20 design patterns essential for building maintainable and scalable applications. The book is not just about design patterns but also about rendering and performance patterns, which are critical to the success of modern web applications.", 75))
        print("\nDesign Patterns")
        print(textwrap.fill("Design patterns provide a common vocabulary to structure code, making it easier to understand. They help enhance the quality of this connection to other developers. Knowledge of design patterns helps us identify recurring themes in requirements and map them to definitive solutions. We can rely on the experience of others who have encountered a similar problem and devised an optimized method to address it. This knowledge is invaluable as it paves the way for writing or refactoring code to make it maintainable. Whether on the server or client, JavaScript is a cornerstone of modern web application development. The previous edition of this book focused on several popular design patterns in the JavaScript context. Over the years, JavaScript has significantly evolved as a language in terms of features and syntax. It now supports modules, classes, arrow functions, and template literals that it did not previously. We also have advanced JavaScript libraries and frameworks that have made life easy for many web developers. How relevant, then, are design patterns in the modern JavaScript context? It's important to note that traditionally, design patterns are neither prescriptive nor language-specific. You can apply them when you think they fit, but you don’t have to. Like data structures or algorithms, you can still apply classic design patterns using modern programming languages, including JavaScript. You may not need some of these design patterns in modern frameworks or libraries where they are already abstracted. Conversely, the use of specific patterns may even be encouraged by some frameworks. In this edition, we are taking a pragmatic approach to patterns. We will explore why specific patterns may be the right fit for implementing certain features and if a pattern is still recommended in the modern JavaScript context.", 75))
        print("\nProto Patterns")
        print(textwrap.fill("From the moment a new pattern is proposed to its potential widespread adoption, a pattern may have to go through multiple rounds of deep inspection by the design community and software developers. This chapter talks about this journey of a newly introduced “proto-pattern” through a “pattern”-ity test until it is eventually recognized as a pattern if it meets the rule of three. This and the next chapter explore the approach to structuring, writing, presenting, and reviewing nascent design patterns. If you’d prefer to learn established design patterns first, you can skip these two chapters for the time being. Remember that not every algorithm, best practice, or solution represents what might be considered a complete pattern. There may be a few key ingredients missing, and the pattern community is generally wary of something claiming to be one without an extensive and critical evaluation. Even if something is presented to us which appears to meet the criteria for a pattern, we should not consider it as one until it has undergone suitable periods of scrutiny and testing by others. Looking back upon Alexander’s work once more, he claims that a pattern should be both a process and a “thing.” This definition is obtuse as he follows by saying that it is the process that should create the “thing.” This is why patterns generally focus on addressing a visually identifiable structure; we should be able to visually depict (or draw) a picture representing the structure resulting from placing the pattern into practice.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.learningJavaScriptDesignPatterns_page_2(username)
        elif options == "2":
            clear_console()
            return books.learningJavaScriptDesignPatterns(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.learningJavaScriptDesignPatterns_page_1(username)
    def learningJavaScriptDesignPatterns_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "Learning JavaScript Design Patterns", "Page 2")
        print("=" * 80 + "\n" + "Modern JavaScript" + "\n")
        print(textwrap.fill("JavaScript has been around for many decades now and has undergone multiple revisions. This book explores design patterns in the modern JavaScript context and uses modern ES2015+ syntax for all the examples discussed. This chapter discusses ES2015+ JavaScript features and syntax essential to further our discussion of design patterns in the current JavaScript context. Modular JavaScript allows you to logically split your application into smaller pieces called modules. A module can be imported by other modules that, in turn, can be imported by more modules. Thus, the application can be composed of many nested modules. In the world of scalable JavaScript, when we say an application is modular, we often mean it’s composed of a set of highly decoupled, distinct pieces of functionality stored in modules. Loose coupling facilitates easier maintainability of apps by removing dependencies where possible. If implemented efficiently, it allows you to see how changes to one part of a system may affect another.", 75))
        print("\nFrameworks")
        print(textwrap.fill("Over the last few years, some modern JavaScript libraries and frameworks— notably React—have introduced alternatives to classes. React Hooks make it possible to use React state and lifecycle methods without an ES2015 class component. Before Hooks, React developers had to refactor functional components as class components so that they handle state and lifecycle methods. This was often tricky and required an understanding of how ES2015 classes work. React Hooks are functions that allow you to manage a component’s state and lifecycle methods without relying on classes. Note that several other approaches to building for the web, such as the Web Components community, continue to use classes as a base for component development.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.learningJavaScriptDesignPatterns_page_1(username)
        elif options == "2":
            clear_console()
            return books.learningJavaScriptDesignPatterns(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.learningJavaScriptDesignPatterns_page_1(username)
    def pythonProgrammingAnIntroductionToComputerScience_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "Python Programming: An Introduction to Computer Science", "Page 1")
        print("=" * 80 + "\n" + "Hardware Basics" + "\n")
        print(textwrap.fill("You don't have to know all the details of how a computer works to be a successful programmer, but understanding the underlying principles will help you master the steps we go through to put our programs into action. It’s a bit like driving a car. Knowing a little about internal combustion engines helps to explain why you have to do things like fill the gas tank, start the engine, step on the accelerator, etc. You could learn to drive by just memorizing what to do, but a little more knowledge makes the whole process much more understandable. Let’s take a moment to “look under the hood” of your computer. Although different computers can vary significantly in specific details, at a higher level all modern digital computers are remarkably similar. Figure 1.1 shows a functional view of a computer. The central processing unit (CPU) is the “brain” of the machine. This is where all the basic operations of the computer are carried out. The CPU can perform simple arithmetic operations like adding two numbers and can also do logical operations like testing to see if two numbers are equal. The memory stores programs and data. The CPU can only directly access information that is stored in main memory (called RAM for Random Access Memory). Main memory is fast, but it is also volatile. That is, when the power is turned off, the information in the memory is lost. Thus, there must also be some secondary memory that provides more permanent storage. In a modern personal computer, this is usually some sort of magnetic medium such as a hard disk (also called a hard drive) or floppy. Humans interact with the computer through input and output devices. You are probably familiar with common devices such as a keyboard, mouse, and monitor (video screen). Information from input devices is processed by the CPU and may be shuffled off to the main or secondary memory. Similarly, when information needs to be displayed, the CPU sends it to one or more output devices.", 75))
        print("\nProgramming Language")
        print(textwrap.fill("Remember that a program is just a sequence of instructions telling a computer what to do. Obviously, we need to provide those instructions in a language that a computer can understand. It would be nice if we could just tell a computer what to do using our native language, like they do in science fiction movies. (“Computer, how long will it take to reach planet Alphalpha at maximum warp?”) Unfortunately, despite the continuing efforts of many top-flight computer scientists (including your author), designing a computer to understand human language is still an unsolved problem. Even if computers could understand us, human languages are not very well suited for describing complex algorithms. Natural language is fraught with ambiguity and imprecision. For example, if I say: “I saw the man in the park with the telescope,” did I have the telescope, or did the man? And who was in the park? We understand each other most of the time only because all humans share a vast store of common knowledge and experience. Even then, miscommunication is commonplace. Computer scientists have gotten around this problem by designing notations for expressing computations in an exact, and unambiguous way. These special notations are called programming languages. Every structure in a programming language has a precise form (its syntax) and a precise meaning (its semantics). A programming language is something like a code for writing down the instructions that a computer will follow. In fact, programmers often refer to their programs as computer code, and the process of writing an algorithm in a programming language is called coding. Python is one example of a programming language. It is the language that we will use throughout this book. You may have heard of some other languages, such as C++, Java, Perl, Scheme, or BASIC. Although these languages differ in many details, they all share the property of having well-defined, unambiguoussyntax and semantics. All of the languages mentioned above are examples of high-level computer languages. Although they are precise, they are designed to be used and understood by humans. Strictly speaking, computer hardware can only understand very low-level language known as machine language.", 75))
        print("\nMagic of Python")
        print(textwrap.fill("Now that you have all the technical details, it’s time to start having fun with Python. The ultimate goal is to make the computer do our bidding. To this end, we will write programs that control the computational processes inside the machine. You have already seen that there is no magic in this process, but in some ways programming feels like magic. The computational processes inside the computer are like magical spirits that we can harness for our work. Unfortunately, those spirits only understand a very arcane language that we do not know. What we need is a friendly Genie that can direct the spirits to fulfill our wishes. Our Genie is a Python interpreter. We can give instructions to the Python interpreter, and it directs the underlying spirits to carry out our demands. We communicate with the Genie through a special language of spells and incantations (i.e., Python). The best way to start learning about Python is to let our Genie out of the bottle and try some spells.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.pythonProgrammingAnIntroductionToComputerScience_page_2(username)
        elif options == "2":
            clear_console()
            return books.pythonProgrammingAnIntroductionToComputerScience(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.pythonProgrammingAnIntroductionToComputerScience_page_1(username)
    def pythonProgrammingAnIntroductionToComputerScience_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "Python Programming: An Introduction to Computer Science", "Page 2")
        print("=" * 80 + "\n" + "Chaos and Computers" + "\n")
        print(textwrap.fill("With very similar starting values, the outputs stay similar for a few iterations, but then differ markedly. By about the fifth iteration, there no longer seems to be any relationship between the two models. These two features of our chaos program, apparent unpredictability and extreme sensitivity to initial values, are the hallmarks of chaotic behavior. Chaos has important implications for computer science. It turns out that many phenomena in the real world that we might like to model and predict with our computers exhibit just this kind of chaotic behavior. You may have heard of the so-called butterfly effect. Computer models that are used to simulate and predict weather patterns are so sensitive that the effect of a single butterfly flapping its wings in New Jersey might make the difference of whether or not rain is predicted in Peoria. It's very possible that even with perfect computer modeling, we might never be able to measure existing weather conditions accurately enough to predict weather more than a few days in advance. The measurements simply can't be precise enough to make the predictions accurate over a longer time frame. As you can see, this small program has a valuable lesson to teach users of computers. As amazing as computers are, the results that they give us are only as useful as the mathematical models on which the programs are based. Computers can give incorrect results because of errors in programs, but even correct programs may produce erroneousresults if the models are wrong or the initial inputs are not accurate enough.", 75))
        print("\nExample Program")
        print(textwrap.fill("Notice that this describes one of many possible programs that could solve this problem. If Suzie had background in the field of Artificial Intelligence (AI), she might consider writing a program that would actually listen to the radio announcer to get the current temperature using speech recognition algorithms. For output, she might have the computer control a robot that goes to her closet and picks an appropriate outfit based on the converted temperature. This would be a much more ambitious project, to say the least! Certainly the robot program would also solve the problem identified in the requirements. The purpose of specification is to decide exactly what this particular program will do to solve a problem. Suzie knows better than to just dive in and start writing a program without first having a clear_console idea of what she is trying to build. Suzie is now ready to design an algorithm for her problem. She immediately realizes that this is a simple algorithm that follows a standard pattern: Input, Process, Output (IPO). Her program will prompt the user for some input information (the Celsius temperature), process it to convert to a Fahrenheit temperature, and then output the result by displaying it on the computer screen. Suzie could write her algorithm down in a computer language. However, the precision of writing it out formally tends to stifle the creative process of developing the algorithm. Instead, she writes her algorithm using pseudocode. Pseudocode is just precise English that describes what a program does. It is meant to communicate algorithms without all the extra mental overhead of getting the details right in any particular programming language.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.pythonProgrammingAnIntroductionToComputerScience_page_1(username)
        elif options == "2":
            clear_console()
            return books.pythonProgrammingAnIntroductionToComputerScience(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.pythonProgrammingAnIntroductionToComputerScience_page_1(username)
    def programmingLanguageDesignAndImplementation_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "Programming Language Design and Implementation", "Page 1")
        print("=" * 80 + "\n" + "General" + "\n")
        print(textwrap.fill("The book has been designed to be used as a textbook in an advanced undergraduate or introductory graduate course in computer science and related fields, but it can also be used by professionals who want to design and implement their own programming languages, regardless of whether these are intended for personal use only or they are hoped to become used by a large number of people. The book assumes that the reader is familiar with basic compiler techniques such as parsing and code generation at a level corresponding to an undergraduate introductory compilers course. It also assumes the reader has experience with programming in at least a couple of significantly different programming languages. In particular, the reader should have at least a bit experience with polymorphically typed functional languages with pattern matching (such as Standard ML, OCaml, F# or Haskell) imperative languages (primarily C), and object-oriented languages (such as Java or C#). If you haven’t already, you can try these languages (and others) out when they are mentioned in the book. There are plenty of online tutorials you can use for this. Like in most textbooks, each chapter concludes with a number of exercises. These are primarily intended to help the reader get a better understanding of the concepts in the chapter. For this reason, many sections in a chapter will conclude with a few suggestions of exercises that the reader is encouraged to try solving before continuing to the next section.", 75))
        print("\nProgramming Languages")
        print(textwrap.fill("This chapter will give a very brief and incomplete history of programming languages, focusing mainly on the early history up to the end of the 1960s. The early history of programming languages is closely linked to the early history of computers, so this will also be covered, though in lesser detail. Programming has its origin in mathematical procedures for solving equations, proving theorems and so forth, and the word “algorithm” (effective computational procedure) is, in fact, derived from the name of the mediaeval Persian mathematician Muhammad ibn M ¯us¯a al-Khw¯arizm¯i, who devised methods for performing calculations and solving equations. The main difference between mathematics and programming is that mathematical procedures and proofs are formulated in a mixture of formal notation and natural language, where a program is entirely formulated in a formal notation called a programming language. Mathematical logic, however, uses a completely formal notation for mathematical statements and proofs for the purpose of analysing these as mathematical objects and proving properties that are true of all statements and proofs expressible in the formal notation. An example of this is Gödel’s incompleteness theorem, which was proved by representing statements and proofs as numbers. Conversely, mathematical models of computation designed for proving properties of computers and programming, such as Turing machines and the lambda calculus, have influenced the design of programming languages.", 75))
        print("\nLambda Calculus")
        print(textwrap.fill("Before electronic computers were built, their future existence was predicted, and logicians made models of how such hypothetical computers could work in order to prove properties about the process of computation. One such model was made by Alan Turing in 1936, and attempted to simplify and formalise the kind of work done by human computers (people who by hand or using simple mechanical adding machines made calculations): These would have an essentially unbounded supply of paper on which they can write and erase symbols, but they can only look at a small area of paper at any one time. Turing simplified the paper supply to a single unbounded paper tape on which you can write and rewrite symbols. The machine would only be able to look at a single symbol at any one time, there would be a finite number of different symbols to read and write (in the simplest form, only 0 and 1), and the machine can move the tape one symbol left or right. To control this, the machine has a finite number of different internal states, and each state can read the symbol in the current tape position and depending on the symbol write a new symbol, move the tape left or right, and change to a new state. A selected state is the Start state, and the input to the computation would be written to the tape, pointed to by the read/write head. Another selected state is a Stop state, and when this is reached, the machine stops, and the contents of the tape pointed to by the read/write head is the output of the computation. Only a finite portion of the tape is initially non-blank, and after a finite number of steps, this is still true.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.programmingLanguageDesignAndImplementation_page_2(username)
        elif options == "2":
            clear_console()
            return books.programmingLanguageDesignAndImplementation(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.programmingLanguageDesignAndImplementation_page_1(username)
    def programmingLanguageDesignAndImplementation_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "Programming Language Design and Implementation", "Page 2")
        print("=" * 80 + "\n" + "Programmable Electronic" + "\n")
        print(textwrap.fill("Working programmable electronic computers were constructed in the 1940s. Programming these were done on the terms of the computer, sometimes by physically connecting wires between parts of the computer and sometimes by stringing together sequences of very simple operations, such as adding numbers and moving numbers between different parts of the computer memory, using a primitive form of what is today known as “machine code”. This programming was often done by the same people who were also employed to make calculations by hand or using mechanical calculators. These people were called “computers”, a name that is now mostly used for what was then called electronic computers, a term that compared the capabilities of these machines to the capabilities of their human counterparts. Human computers were in the 1940s and 1950s often women, so in the early days of electronic computers, most programmers were women. When computers were small and computer hours expensive compared to hours of labour, it made sense to spend a large effort on writing programs and less on making it easy to do so. But it was quickly discovered that making nontrivial programs at the very low level required by electronic computers was not only time-consuming, but also an error-prone process. So in the 1950s, high-level programming languages were invented: Formalised notations (using symbols found on a typical teletype terminal) that could be used to express programs in a form that was more readily understandable (for humans) than machine language, and employing higher-level concepts such as floating-point numbers, arrays, records, loops, subroutines, and so on. These high-level concepts were translated into machine code, so they did not, strictly speaking, allowmore ideas to be expressed than possible in machine language, they just, by employing high-level idioms, allowed these ideas to be expressed more easily, succinctly, and readably. High-level formalised notation also allows a degree of automatic detection of errors, as certain types of incorrect uses of high-level idioms can be detected by a computer program (such as a compiler or interpreter) and reported as errors, whereas machine code has no structure that can be exploited to this effect. Essentially, the high-level concepts introduce a structured syntax that can be verified against a formal grammar and type system, whereas programs in machine code can be seen as strings of words with no structure.", 75))
        print("\nPlankalkül")
        print(textwrap.fill("Since Plankalkül was not intended for automatic translation to machine language, its notation was made for human understanding rather than machine readability, though in such a way that it could mostly be typed on a typewriter with addition of a few hand-drawn symbols. Values in Plankalkül are multi-dimensional arrays of bits, which can be indexed to individual bits or to a row of bits, which can represent a binary number. Plankalkül uses a systematic naming convention: Input variables are written as V, intermediate variables as Z (for “Zwischenwerte”), constant names as C and result variables as R. To allow multiple variables of the same kind, the letters can be supplied with numeric indices. Additionally, a variable or constant can be a multi-dimensional array. Each variable or constant is explicitly typed using “structure types” such as 0 to indicate a single bit and 1.n to indicate an array of n bits. Unlike in modern programming languages, a variable, its index, component selection, and type are written on multiple lines, aligned to the same column.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.programmingLanguageDesignAndImplementation_page_1(username)
        elif options == "2":
            clear_console()
            return books.programmingLanguageDesignAndImplementation(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.programmingLanguageDesignAndImplementation_page_1(username)
    def pythonUntukProgrammerPemula_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "Python unruk Programmer Pemula", "Page 1")
        print("=" * 80 + "\n" + "Python" + "\n")
        print(textwrap.fill("Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically type-checked and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a 'batteries included' language due to its comprehensive standard library. Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0. Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2. Python consistently ranks as one of the most popular programming languages, and has gained widespread use in the machine learning community.", 75))
        print("\nHistory")
        print(textwrap.fill("Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL, capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his 'permanent vacation' from his responsibilities as Python's 'benevolent dictator for life' (BDFL), a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker (he has since come out of retirement and is self-titled 'BDFL-emeritus'). In January 2019, active Python core developers elected a five-member Steering Council to lead the project. The name Python is said to come from the British comedy series Monty Python's Flying Circus. Python 2.0 was released on 16 October 2000, with many major new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 2.7's end-of-life was initially set for 2015, then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3. No further security patches or other improvements will be released for it. While Python 2.7 and older versions are officially unsupported, a different unofficial Python implementation, PyPy, continues to support Python 2, i.e. '2.7.18+' (plus 3.10), with the plus meaning (at least some) 'backported security updates'.", 75))
        print("\nMaintain")
        print(textwrap.fill("Python 3.0 was released on 3 December 2008, with some new semantics and changed syntax. At least every Python release since (now unsupported) 3.5 has added some syntax to the language, and a few later releases have dropped outdated modules, or changed semantics, at least in a minor way. Since 7 October 2024, Python 3.13 is the latest stable release, and it and, for few more months, 3.12 are the only releases with active support including for bug fixes (as opposed to just for security) and Python 3.9, is the oldest supported version of Python (albeit in the 'security support' phase), due to Python 3.8 reaching end-of-life. Starting with 3.13, it and later versions have 2 years of full support (up from one and a half), followed by 3 years of security support (for same total support as before). Security updates were expedited in 2021 (and again twice in 2022, and more fixed in 2023 and in September 2024 for Python 3.12.6 down to 3.8.20), since all Python versions were insecure (including 2.7) because of security issues leading to possible remote code execution and web-cache poisoning.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.pythonUntukProgrammerPemula_page_2(username)
        elif options == "2":
            clear_console()
            return books.pythonUntukProgrammerPemula(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.pythonUntukProgrammerPemula_page_1(username)
    def pythonUntukProgrammerPemula_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "Python unruk Programmer Pemula", "Page 2")
        print("=" * 80 + "\n" + "Implementations" + "\n")
        print(textwrap.fill("CPython is the reference implementation of Python. It is written in C, meeting the C89 standard (Python 3.11 uses C11) with several select C99 features. CPython includes its own C extensions, but third-party extensions are not limited to older C versions—e.g. they can be implemented with C11 or C++. CPython compiles Python programs into an intermediate bytecode which is then executed by its virtual machine. CPython is distributed with a large standard library written in a mixture of C and native Python, and is available for many platforms, including Windows (starting with Python 3.9, the Python installer deliberately fails to install on Windows 7 and 8; Windows XP was supported until Python 3.5) and most modern Unix-like systems, including macOS (and Apple M1 Macs, since Python 3.9.1, with experimental installer), with unofficial support for VMS. Platform portability was one of its earliest priorities. (During Python 1 and 2 development, even OS/2 and Solaris were supported, but support has since been dropped for many platforms.) Codon is a language with an ahead-of-time (AOT) compiler, that (AOT) compiles a statically-typed Python-like language with 'syntax and semantics are nearly identical to Python's, there are some notable differences e.g. it uses 64-bit machine integers, for speed, not arbitrary like Python, and it claims speedups over CPython are usually on the order of 10-100x. It compiles to machine code (via LLVM) and supports native multithreading. Codon can also compile to Python extension modules that can be imported and used from Python.", 75))
        print("\nDevelopment")
        print(textwrap.fill("Python's development is conducted largely through the Python Enhancement Proposal (PEP) process, the primary mechanism for proposing major new features, collecting community input on issues, and documenting Python design decisions. Python coding style is covered in PEP 8. Outstanding PEPs are reviewed and commented on by the Python community and the steering council. Enhancement of the language corresponds with the development of the CPython reference implementation. The mailing list python-dev is the primary forum for the language's development. Specific issues were originally discussed in the Roundup bug tracker hosted at by the foundation. In 2022, all issues and discussions were migrated to GitHub. Development originally took place on a self-hosted source-code repository running Mercurial, until Python moved to GitHub in January 2017.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.pythonUntukProgrammerPemula_page_1(username)
        elif options == "2":
            clear_console()
            return books.pythonUntukProgrammerPemula(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.pythonUntukProgrammerPemula_page_1(username)
    def soloLeveling_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "Solo Leveling", "Page 1")
        print("=" * 80 + "\n" + "Introduction" + "\n")
        print(textwrap.fill("Solo Leveling, also alternatively translated as Only I Level Up (Korean: 나 혼자만 레벨업; RR: Na Honjaman Rebeleop), is a South Korean portal fantasy web novel written by Chugong. It was serialized in Kakao's digital comic and fiction platform KakaoPage beginning on July 25, 2016, and was later published by D&C Media under their Papyrus label since November 4, 2016. The novel has been licensed in English by Yen Press. A webtoon adaptation of Solo Leveling was first serialized in KakaoPage on March 4, 2018; it was illustrated by Jang Sung-rak (Dubu) and the webtoon's first season concluded on March 19, 2020, followed by its second season, which was released from August 2020 to December 2021. The webtoon has been licensed in English by Yen Press. Its individual chapters have been collected and published in thirteen volumes by D&C Media, as of June 2024.", 75))
        print("\nPlot")
        print(textwrap.fill("In a world where hunters — human warriors who possess supernatural abilities — must battle deadly monsters to protect mankind from certain annihilation, a notoriously weak hunter named Sung Jin-woo finds himself in a seemingly endless struggle for survival. One day, after narrowly surviving an overwhelmingly powerful double dungeon that nearly wipes out his entire party, a mysterious program called the System chooses him as its sole player and in turn, gives him the unique ability to level up in strength. This is something no other hunter is able to do, as a hunter's abilities are set once they awaken. Jinwoo then sets out on a journey as he fights against all kinds of enemies, both man and monster, to discover the secrets of the dungeons and the true source of his powers. He soon discovers that he has been chosen to inherit the position of Shadow Monarch, essentially turning him into an immortal necromancer who has absolute rule over the dead. He is the only Monarch who fights to save humanity, as the other Monarchs are all trying to kill him and wipe out the humans.", 75))
        print("\nCharacters")
        print(textwrap.fill("Sung Jin-woo (성진우; Seong Jinu) is the protagonist of the series. Originally a famously weak E-rank hunter, he gets the chance of a lifetime when he is selected as the Player of the System and is able to grow in strength without limit. Taking advantage of his new power, Jin-woo rises up to become the entire humanity's power, far stronger than the National Level Hunters. He eventually discovers the secret behind the System. Everything started from the never ending war between the Rulers and the Monarchs, two groups of extremely powerful humanoid beings created by a God. The previous Shadow Monarch, Ashborn, chooses and trains him through The System so he can be his successor.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.soloLeveling_page_2(username)
        elif options == "2":
            clear_console()
            return books.soloLeveling(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.soloLeveling_page_1(username)
    def soloLeveling_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "Solo Leveling", "Page 2")
        print("=" * 80 + "\n" + "Anime" + "\n")
        print(textwrap.fill("An anime television series adaptation was announced at Anime Expo 2022. It is produced by A-1 Pictures and directed by Shunsuke Nakashige, with Noboru Kimura writing the scripts, Tomoko Sudo designing the characters, and Hiroyuki Sawano composing the music. It was originally scheduled for 2023, but was later delayed and eventually aired from January 7 to March 31, 2024, on Tokyo MX and other networks. Crunchyroll licensed the series outside of Asia. Medialink licensed the series in Southeast Asia and Oceania (except Australia and New Zealand). The first episodes were screened from December 2023 in Tokyo, Seoul, Los Angeles, India, and Europe. The opening theme song is 'Level', performed by SawanoHiroyuki: Tomorrow X Together, while the ending theme song is 'Request', performed by Krage.", 75))
        print("\nContinuation")
        print(textwrap.fill("In April 2023, Kakao announced a sequel titled Solo Leveling: Ragnarok. The web novel began releasing through KakaoPage on April 10, 2023. The story is set after the events of Solo Leveling; the side story acts as a prelude. Sung Su-ho, the son of Sung Jin-woo and Cha Hae-in, inherited his father's powers as the Shadow Monarch. However, his powers and memories were locked as a child, so he can have a normal life. But when Gates started to open up around Earth again during his third year of university, Su-ho is chosen as a Player by the System. Therefore, Su-ho must become a Hunter in order to face the new threat that is related to his parents' disappearance. The web novel is written by Daul, who replaced Chugong, the writer of the original Solo Leveling web novel. Chugong revealed he decided to support Daul, saying he still experienced the same emotions he felt when he first began serializing the original web novel. The first 105 chapters debuted on KakaoPage on April 10, 2023.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.soloLeveling_page_1(username)
        elif options == "2":
            clear_console()
            return books.soloLeveling(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.soloLeveling_page_1(username)
    def omniscientReadersViewpoint_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "Omniscient Readers Viewpoint", "Page 1")
        print("=" * 80 + "\n" + "Introduction" + "\n")
        print(textwrap.fill("Omniscient Reader's Viewpoint, also alternatively translated as Omniscient Reader (Korean: 전지적 독자 시점; RR: Jeonjijeog Dogja Sijeom), is a South Korean web novel written by Sing Shong. It was first published on January 6, 2018, on the platform Munpia, and ended on February 2, 2020. Naver Webtoon published an ongoing webtoon adaptation created by Redice Studio for the Korean version and Line Webtoon for the English version in 2020. An anime television series adaptation has been announced.", 75))
        print("\nPlot")
        print(textwrap.fill("Kim Dokja, a 28-year-old office worker, has been the only reader of the web novel Three Ways to Survive an Apocalypse. In the novel, apocalypse descends upon the world in the form of scenarios: brutal challenges that humans are forced to endure. Immensely powerful, legendary beings called 'Constellations' watch from above, entertained by the bloodbath. The thousands of chapters of the novel follow the story of Yoo Joonghyuk, a person with a unique ability to transport back to the beginning of the apocalypse every time he dies. Through Yoo Joonghyuk's story, Dokja survives his own miserable life, comforted by the fact that the protagonist suffered worse and kept going despite it all. Dokja's aimless life grinds to a halt when his favorite web-novel is meant to end on the same day his tenure as an intern in his office ends. Suddenly, the story he's used to escape from reality for much of his life merges with real life, and the characters of the novel themselves appear, along with the carnage of the scenarios. Before the last chapter of the story is published, the city descends into carnage. As the only one who read the novel to the end and knows its plot, Kim is the only one who can fight for survival.", 75))
        print("\nCharacters")
        print(textwrap.fill("Kim Dokja (김독자; 金獨子; Gim Dokja) is the main protagonist of the series. He is a young man working an office job who has a passion for reading, his favorite web novel being 'Three Ways to Survive in a Ruined World'. However, his life takes a drastic turn when the events of the novel start unfolding in real life, and he is the only one who is aware of how the world will come to an end. With this knowledge, Dokja uses his understanding of the story to create the most perfect ending, consequently changing the world as he knows it. The group of allies and companions he gathers is known as Kim Dokja's Company.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.omniscientReadersViewpoint_page_2(username)
        elif options == "2":
            clear_console()
            return books.omniscientReadersViewpoint(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.omniscientReadersViewpoint_page_1(username)
    def omniscientReadersViewpoint_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "Omniscient Readers Viewpoint", "Page 2")
        print("=" * 80 + "\n" + "Web Novel" + "\n")
        print(textwrap.fill("The original Korean web novel, written by Sing Shong was first published on January 6, 2018, on the platform Munpia, and ended on February 2, 2020. The official sources are only Muipia and Naver. It has since then been compiled into 6 volumes, with the last volume containing only the epilogues. After the end of the original story, new side stories of the novel began getting published in the official sites. It first started publishing on February 15, 2024, and is currently ongoing. The Korean web novel finished the first season of the spin off series (side stories) on August 30, 2024, with 242 chapters and is set to return with its second season on September 22, 2024.", 75))
        print("\nWebtoon")
        print(textwrap.fill("An ongoing webtoon adaptation illustrated by Sleepy-C launched on Naver on May 26, 2020. Its first two collected volumes were released by A.Tempo Media on December 22, 2020, with nine collected volumes released as of March 2023. The webtoon was published digitally in English by Line Webtoon on August 18, 2020. In June 2023, IZE Press, an imprint of Yen Press, announced that they have licensed both the manhwa and novel for English publication.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.omniscientReadersViewpoint_page_1(username)
        elif options == "2":
            clear_console()
            return books.omniscientReadersViewpoint(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.omniscientReadersViewpoint_page_1(username)
    def theBeginningAfterTheEnd_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Beginning After The End", "Page 1")
        print("=" * 80 + "\n" + "Introduction" + "\n")
        print(textwrap.fill("The Beginning After the End is an American web novel series written by TurtleMe and illustrated by Fuyuki23. It began serialization on Tapas in January 2017. A webtoon adaptation, also illustrated by Fuyuki23, began serialization on Tapas in July 2018. Yen Press is publishing the webtoon in English; as of August 2024, six volumes have been released. An anime television series adaptation produced by Studio A-Cat is set to premiere in April 2025 on Fuji TV's +Ultra programming block.", 75))
        print("\nPremise")
        print(textwrap.fill("In the realm of Etharia, King Grey was a great ruler but with a sense of guilt for his past mistakes. When he dies of mysterious means, he was reincarnated in the realm of Dicathen as Arthur Leywin. With a second chance of living, Grey/Arthur explores his new home, with family and friends, but he then discovers there is a great danger hidden, and that he was not the only one who reincarnated.", 75))
        print("\nCharacters")
        print(textwrap.fill("Kim Dokja (김독자; 金獨子; Gim Dokja) is the main protagonist of the series. He is a young man working an office job who has a passion for reading, his favorite web novel being 'Three Ways to Survive in a Ruined World'. However, his life takes a drastic turn when the events of the novel start unfolding in real life, and he is the only one who is aware of how the world will come to an end. With this knowledge, Dokja uses his understanding of the story to create the most perfect ending, consequently changing the world as he knows it. The group of allies and companions he gathers is known as Kim Dokja's Company.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theBeginningAfterTheEnd_page_2(username)
        elif options == "2":
            clear_console()
            return books.theBeginningAfterTheEnd(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theBeginningAfterTheEnd_page_1(username)
    def theBeginningAfterTheEnd_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Beginning After The End", "Page 2")
        print("=" * 80 + "\n" + "Web Novel" + "\n")
        print(textwrap.fill("The original Korean web novel, written by Sing Shong was first published on January 6, 2018, on the platform Munpia, and ended on February 2, 2020. The official sources are only Muipia and Naver. It has since then been compiled into 6 volumes, with the last volume containing only the epilogues. After the end of the original story, new side stories of the novel began getting published in the official sites. It first started publishing on February 15, 2024, and is currently ongoing. The Korean web novel finished the first season of the spin off series (side stories) on August 30, 2024, with 242 chapters and is set to return with its second season on September 22, 2024.", 75))
        print("\nWebtoon")
        print(textwrap.fill("An ongoing webtoon adaptation illustrated by Sleepy-C launched on Naver on May 26, 2020. Its first two collected volumes were released by A.Tempo Media on December 22, 2020, with nine collected volumes released as of March 2023. The webtoon was published digitally in English by Line Webtoon on August 18, 2020. In June 2023, IZE Press, an imprint of Yen Press, announced that they have licensed both the manhwa and novel for English publication.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theBeginningAfterTheEnd_page_1(username)
        elif options == "2":
            clear_console()
            return books.theBeginningAfterTheEnd(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theBeginningAfterTheEnd_page_1(username)
    def mercenaryEnrollment_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "Mercenary Enrollment", "Page 1")
        print("=" * 80 + "\n" + "Introduction" + "\n")
        print(textwrap.fill("'High School Soldier,' also known by its Korean title 입학용병 (Ibhak Yongbyeong) and its unofficial English title 'Mercenary Enrollment,' is a captivating action manhwa written by YC and illustrated by Rak Hyun. It was first released on Naver Webtoon in November 2020 and quickly gained a strong following. The English and Indonesian translations are available on LINE Webtoon, where the series has garnered widespread acclaim for its gripping storyline and intense action scenes.", 75))
        print("\nStories")
        print(textwrap.fill("The story revolves around Yoo Leejin, a young man with a dark and tragic past. Leejin is the sole survivor of a horrific plane crash that occurred when he was just a child. After losing his family in the accident, he was forced into the brutal world of mercenaries, where he spent the next ten years of his life. Trained to survive and fight in the most dangerous circumstances, Leejin became a seasoned soldier at a very young age. After ten years of life-threatening missions and constant battles, Leejin finally leaves the mercenary world and returns to his hometown to start afresh. His goal is to live a quiet life and reunite with his younger sister, Yoo Dayeon, whom he has not seen in a decade. As a high school student, Leejin hopes to experience the normalcy of teenage life for the first time. However, his peaceful aspirations are soon disrupted.", 75))
        print("\nCharacters")
        print(textwrap.fill("Leejin discovers that his sister Dayeon is being bullied at school. Deeply protective of his only remaining family, Leejin cannot stand idly by. His instinct as a soldier and his love as a brother push him to intervene. He confronts the bullies, sending a clear_console message that his sister is no longer alone and will no longer be a victim. This marks the beginning of Leejin’s dual life as both a high school student and a silent protector. What sets 'High School Soldier' apart from other action manhwas is its unique blend of mercenary action and school life drama. Yoo Leejin’s character offers a fascinating contrast: he is a skilled and hardened soldier, yet he struggles to fit into the normal routines of high school life. This duality provides both intense fight scenes and moments of emotional depth as he navigates relationships, friendships, and family. The manhwa also explores themes of bullying and justice, shedding light on the difficulties faced by victims of harassment. Leejin’s interventions are not only physical but also strategic, as he uses his military training to dismantle power structures within the school. These moments are highly satisfying for readers, as they showcase his intelligence and skill, while also providing a strong emotional payoff.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.mercenaryEnrollment_page_2(username)
        elif options == "2":
            clear_console()
            return books.mercenaryEnrollment(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.mercenaryEnrollment_page_1(username)
    def mercenaryEnrollment_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "Mercenary Enrollment", "Page 2")
        print("=" * 80 + "\n" + "Popularity" + "\n")
        print(textwrap.fill("The art style of 'High School Soldier' is another highlight of the series. The fight scenes are dynamic and well-choreographed, with meticulous attention to detail that brings the action to life. The emotional expressions of the characters are also well-captured, adding depth to their interactions and making the story even more engaging. Since its release, 'High School Soldier' has received widespread praise and high ratings. On LINE Webtoon, the series holds an impressive 9.90/10 rating and has amassed over 200 million views and 1.4 million subscribers globally. Its popularity continues to grow, making it one of the standout titles in the action and school life genres.", 75))
        print("\nDate of Series")
        print(textwrap.fill("As of January 2025, the series has reached 213 episodes, and fans eagerly await new updates every Thursday. The consistent pacing and development of both the plot and the characters have kept readers invested in Yoo Leejin's journey. The balance between action-packed sequences and heartfelt moments ensures that the story remains fresh and exciting. 'High School Soldier'' is more than just an action-packed series; it is a story about family, resilience, and the fight for justice. Yoo Leejin's journey from a battle-hardened mercenary to a protective older brother and high school student resonates deeply with readers. The series' unique premise, strong character development, and emotional storytelling make it a must-read for fans of action, drama, and school life manhwas. For those interested, the manhwa is available to read for free on LINE Webtoon, where it continues to captivate audiences worldwide.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.mercenaryEnrollment_page_1(username)
        elif options == "2":
            clear_console()
            return books.mercenaryEnrollment(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.mercenaryEnrollment_page_1(username)
    def theNovelsExtra_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Novels Extra", "Page 1")
        print("=" * 80 + "\n" + "Introduction" + "\n")
        print(textwrap.fill("'The Novel's Extra' is a Korean web novel authored by Jee Gab Song, also known as 지갑송. The narrative centers on Kim Hajin, who awakens to find himself in a world he recognizes as the novel he authored but never completed. Strikingly, he inhabits the body of an unimportant extra character, rather than the protagonist. To navigate this predicament and seek a way back to his reality, Kim Hajin decides to adhere closely to the main storyline he originally devised. However, he soon discovers that this world has deviated from his initial creation, presenting unforeseen challenges and complexities.", 75))
        print("\nStories")
        print(textwrap.fill("A notable aspect of 'The Novel's Extra'' is its exploration of the relationship between a creator and their creation. Kim Hajin's intimate knowledge of the world's mechanics and characters provides him with unique advantages, yet the deviations from his original plot force him to adapt and grow alongside his creations. This dynamic adds depth to the narrative, as readers witness the interplay between predetermined destiny and the influence of free will within the story's universe.", 75))
        print("\nNovel")
        print(textwrap.fill("The novel delves into themes of identity and self-discovery, as Kim Hajin grapples with his new existence as an extra character. His journey is not just about returning to his original world but also about understanding his role within the narrative he once controlled. This introspective element resonates with readers, prompting reflections on the nature of authorship and the connections between writers and their stories. 'The Novel's Extra' has been well-received by readers, holding a rating of 4.2 out of 5 based on 2,416 votes on Novel Updates.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theNovelsExtra_page_2(username)
        elif options == "2":
            clear_console()
            return books.theNovelsExtra(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theNovelsExtra_page_1(username)
    def theNovelsExtra_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Novels Extra", "Page 2")
        print("=" * 80 + "\n" + "Popularity" + "\n")
        print(textwrap.fill("The novel's popularity has led to its licensing and complete translation into English, making it accessible to a broader audience. Readers can find the English version on platforms such as Wuxiaworld, where it has garnered a dedicated following. The availability of the complete translation allows new readers to immerse themselves fully in the intricate world Jee Gab Song has crafted. Spanning 481 chapters, including side stories, 'The Novel's Extra' offers an extensive and immersive reading experience. The main story comprises 379 chapters, with an additional 101 side story chapters that provide further depth and context to the overarching narrative. This expansive structure allows for comprehensive character development and intricate plot progression, keeping readers engaged throughout the journey.", 75))
        print("\nResolution")
        print(textwrap.fill("The novel's success has also sparked discussions and recommendations within the web novel community. It is often compared to other popular series such as 'The Second Coming of Gluttony' and 'Omniscient Reader's Viewpoint,' both of which share similar themes of characters navigating worlds they are intimately familiar with. These comparisons highlight the novel's impact and its contribution to the genre's evolution. 'The Novel's Extra' has inspired various fan works and discussions, with readers analyzing its complex narrative structure and character dynamics. The novel's unique premise and execution have made it a subject of interest among enthusiasts of the genre, fostering a community of readers who engage in in-depth discussions and analyses.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theNovelsExtra_page_1(username)
        elif options == "2":
            clear_console()
            return books.theNovelsExtra(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theNovelsExtra_page_1(username)
    def theDreamClass_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Dream Class", "Page 1")
        print("=" * 80 + "\n" + "Introduction" + "\n")
        print(textwrap.fill("'From Dreams to Freedom' is a Korean manhwa authored by 2L, categorized under the thriller genre. It has been serialized on LINE Webtoon Indonesia since April 16, 2022, and continues to be ongoing with over 70 episodes. The narrative centers on Jeongmin Choi, a high school student subjected to severe bullying orchestrated by her former childhood friend, Juhyeon Ha. The torment ranges from social exclusion to overt harassment, leading Jeongmin to seek solace through lucid dreaming—a practice where she gains control over her dreams to exact revenge on her tormentors.", 75))
        print("\nStories")
        print(textwrap.fill("In her dreamscape, Jeongmin encounters a mysterious man named Siyoon Baek, who offers assistance in her quest for vengeance. Accepting his help, Jeongmin's life begins to change as the boundaries between her dreams and reality blur, introducing unforeseen consequences and deeper entanglements with Siyoon. The manhwa delves into themes of bullying, psychological trauma, and the allure of escapism through lucid dreaming. It portrays Jeongmin's internal struggle between her desire for retribution and the moral complexities that accompany it, all while navigating the challenges of her daily life.", 75))
        print("\nStatistic")
        print(textwrap.fill("'From Dreams to Freedom' has garnered significant attention for its compelling storyline and distinctive art style. As of June 2024, it has amassed over 86.4 million views and 1.1 million subscribers on LINE Webtoon Indonesia, boasting a high rating of 9.83. The series updates regularly, with new episodes released every Saturday, keeping readers engaged with its suspenseful plot developments and character arcs. The consistent release schedule contributes to its growing popularity among thriller enthusiasts.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theDreamClass_page_2(username)
        elif options == "2":
            clear_console()
            return books.theDreamClass(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theDreamClass_page_1(username)
    def theDreamClass_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Dream Class", "Page 2")
        print("=" * 80 + "\n" + "Opinion" + "\n")
        print(textwrap.fill("Critics and readers have praised the manhwa for its realistic depiction of the psychological effects of bullying and the ethical dilemmas associated with revenge. The character development of Jeongmin, transitioning from a passive victim to an individual taking control of her circumstances, resonates with many readers. The artwork complements the dark and suspenseful tone of the narrative, with detailed illustrations that effectively convey the emotional turmoil and tension experienced by the characters. The visual representation of the dream sequences is particularly noted for its creativity and symbolism.", 75))
        print("\nPerspective")
        print(textwrap.fill("'From Dreams to Freedom' has sparked discussions regarding the use of lucid dreaming as a coping mechanism and its potential psychological implications. The manhwa encourages readers to reflect on the consequences of seeking escapism and the importance of addressing real-life issues directly. In conclusion, 'From Dreams to Freedom' stands out as a thought-provoking thriller that explores complex themes through a blend of psychological drama and supernatural elements. Its engaging plot, well-developed characters, and striking artwork make it a noteworthy addition to the manhwa genre, appealing to readers seeking depth and suspense in storytelling.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theDreamClass_page_1(username)
        elif options == "2":
            clear_console()
            return books.theDreamClass(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theDreamClass_page_1(username)
    def americaMilitaristicOrPeaceful_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "America: Militaristic Or Peaceful", "Page 1")
        print("=" * 80 + "\n" + "Globalization" + "\n")
        print(textwrap.fill("To the extent that its wars were limited in the nineteenth and early twentieth century, US warmaking is now global in the sense that the United States in its military doctrine and grand strategy concerns itself with “total domain awareness” and control. It approach is characterized by a kind of hyper-vigilance and hyper-interventionism that is, on occasion, pitch perfect. But more often than not, to borrow from the idiom of Harold Lasswell  – the great psychoanalyst of international relations  – it is a little paranoid and more than a little delusional about the potential to control people, faraway lands, and political outcomes (Lasswell 1935; see also Staub 1989). I explore three interrelated phenomena here. The first is the globalization of American war in the twentieth and twenty-first century. Second, I argue that the sources of the globalization of American war in the late twentieth century and in the current era are militarism, ethnocentrism and nationalism. I focus on militarism in this article, although all three are at play. And third, I argue that the consequences of these beliefs and the foreign policies that instantiate them, are counterproductive for the United States for the relative position of the United States in the world. And I show how and why that position is likely to shift over the next 75 years. The United States elite’s militarist beliefs, coupled with American’s unstable self-identity as an exceptional people and great power/super power, has set America up for a spectacular rise and the disastrous fall of hegemonic power. American exceptionalism, always a shaky proposition, is a myth. Like all imperial powers, the US has run the table and now run out of steam.", 75))
        print("\nSubjection")
        print(textwrap.fill("Great powers need economic assets to wage war. Gilpin and Kennedy suggested in the 1980s that rising powers overtake hegemons when their economic growth rates allow them to amass sufficient military power and economic influence (Gilpin 1981; Kennedy 1984). Hegemons want to maintain their dominance and can become aggressive in doing so, and rising powers may challenge hegemons if they think it is worthwhile. Meanwhile, as both Gilpin and Kennedy argue, the pursuit of power, overextension, and resistance can drain the economic assets of the hegemon. In the early 1990s Charles Tilly added a focus on the ways that warmaking bolsters statemaking. Tilly argued that war helps the state extract the resources and create the organizational and bureaucratic features of a state, enabling the state to be better able to wage war. Wars make states (Tilly 1992). And the United States did, of course, continue to make war. Though we tend to think of discrete wars during the seventeenth through the twentieth centuries, war was nearly continuous from the arrival of the English in the early 1600s and after the Revolutionary War through the 19th century. During this period the conduct of American war was often extremely brutal toward both combatants and non-combatants alike. First, the US expanded across the continent through war in the 18th and 19th century, taking land from Native Americans, fighting Britain in 1812 and barely avoiding another war with Britain again in 1838, and then a war with Mexico in 1848. By the end of the nineteenth century the US had essentially destroyed Native American resistance to its expansion and was poised to move beyond the continent, to Hawaii and the Caribbean.", 75))
        print("\nStatistic")
        print(textwrap.fill("Militarism is a cluster of core beliefs about military force that militarists and often the rest of us hold regardless of context. Specifically, militarists believe that force is always useful and that the wars our side initiates make us safer. Less often stated today, but a core element of early and mid-twentieth century militarism, is the view that war is glorious, noble and purifying. Militarism is a belief system, a worldview, where the use of military force to resolve disputes and remove potential threats to “security” is understood to be effective, efficient, legitimate, praiseworthy and even glorious.1 Militarists assume that the use of force in domestic and foreign politics is natural, expected, and effective in most instances, and they recognize few limits to the effective use of force. Security is understood to be a zerosum commodity; if you have it, I don’t. We can’t all feel secure at the same time. Further, a strong military deters potential aggressors; there is no security dilemma, where what I do to feel secure may make an adversary feel less secure and therefore defensively aggressive. Threats and the use of force will cause others to back down. Militarism as a belief system assumes that a strong military deters aggressors. Further, the amount of military spending is positively correlated with military capacity and security. And, moreover, there is the assumption that military spending is good for the economy. Militarists can only see the upside of military spending, and discount the damaging and distorting effects of military spending.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.americaMilitaristicOrPeaceful_page_2(username)
        elif options == "2":
            clear_console()
            return books.americaMilitaristicOrPeaceful(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.americaMilitaristicOrPeaceful_page_1(username)
    def americaMilitaristicOrPeaceful_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "America: Militaristic Or Peaceful", "Page 2")
        print("=" * 80 + "\n" + "History" + "\n")
        print(textwrap.fill("On the road to war, militarists put moral and practical blinders on. They claim preventive war is legitimate because they believe that the other does not deserve to become an equal or surpass them. They believe that preemptive war and first strikes are generally successful, even despite evidence that they fail about half the time. They believe that escalation and war are controllable and that quagmires and stalemate are for the other guy. Further, they think that conquest is valuable, resources gained through force are cumulative. They exaggerate the value of international gains and wider spheres of influence, and worry that their reputation for keeping commitments and following through on threats will be tarnished should they seek negotiated threats. This view is summarized by the Latin saying, si vi pacem, para bellum – if you want peace prepare for war. Indeed, war works and is good for you. Once at war, militarists believe their own rhetoric, that war will be quick, decisive, and cheap in blood and treasure. They will be home before the leaves fall or the snow falls, or by whatever the next season is and they will be greeted by those they conquer as liberators and by those at home as heroes.", 75))
        print("\nOpportunity")
        print(textwrap.fill("Militarist beliefs may become the lens through which actors see each other and construct knowledge about their social world. The institutionalization of militarist beliefs can and does yield a world that fulfills these expectations. Militarization is a process, specifically the social, psychological, political, and economic mobilization of a group’s resources for the use or threat of violence and the ascription of extraordinary virtue to those who use military force. In a militarized culture, the majority takes war and mobilization for it for granted, understands “security” in military terms, and devotes a large share of economic and cultural resources to military and military-related purposes (Lutz 2004). In a state of continuous mobilization, the distinction between wartime (and all the things that context is said to allow) and peacetime blur. “Wartime becomes a justification for the rule of law that bends in favor of the security state” (Dudziak 2012: 3-4).", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.americaMilitaristicOrPeaceful_page_1(username)
        elif options == "2":
            clear_console()
            return books.americaMilitaristicOrPeaceful(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.americaMilitaristicOrPeaceful_page_1(username)
    def theGreatGatsby_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Great Gatsby", "Page 1")
        print("=" * 80 + "\n" + "Globalization" + "\n")
        print(textwrap.fill("He didn’t say any more but we’ve always been unusually communicative in a reserved way, and I understood that he meant a great deal more than that. In consequence I’m inclined to reserve all judgments, a habit that has opened up many curious natures to me and also made me the victim of not a few veteran bores. The abnormal mind is quick to detect and attach itself to this quality when it appears in a normal person, and so it came about that in college I was unjustly accused of being a politician, because I was privy to the secret griefs of wild, unknown men. Most of the confidences were unsought—frequently I have feigned sleep, preoccupation, or a hostile levity when I realized by some unmistakable sign that an intimate revelation was quivering on the horizon—for the intimate revelations of young men or at least the terms in which they express them are usually plagiaristic and marred by obvious suppressions.", 75))
        print("\nProstitution")
        print(textwrap.fill("And, after boasting this way of my tolerance, I come to the admission that it has a limit. Conduct may be founded on the hard rock or the wet marshes but after a certain point I don’t care what it’s founded on. When I came back from the East last autumn I felt that I wanted the world to be in uniform and at a sort of moral attention forever; I wanted no more riotous excursions with privileged glimpses into the human heart. Only Gatsby, the man who gives his name to this book, was exempt from my reaction—Gatsby who represented everything for which I have an unaffected scorn. If personality is an unbroken series of successful gestures, then there was something gorgeous about him, some heightened sensitivity to the promises of life, as if he were related to one of those intricate machines that register earthquakes ten thousand miles away.", 75))
        print("\nEvolution")
        print(textwrap.fill("I never saw this great-uncle but I’m supposed to look like him—with special reference to the rather hard-boiled painting that hangs in Father’s office. I graduated from New Haven in 1915, just a quarter of a century after my father, and a little later I participated in that delayed Teutonic migration known as the Great War. I enjoyed the counter-raid so thoroughly that I came back restless. Instead of being the warm center of the world the middle-west now seemed like the ragged edge of the universe—so I decided to go east and learn the bond business. Everybody I knew was in the bond business so I supposed it could support one more single man. All my aunts and uncles talked it over as if they were choosing a prep-school for me and finally said, ‘Why—yees’ with very grave, hesitant faces. Father agreed to finance me for a year and after various delays I came east, permanently, I thought, in the spring of twenty-two.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theGreatGatsby_page_2(username)
        elif options == "2":
            clear_console()
            return books.theGreatGatsby(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theGreatGatsby_page_1(username)
    def theGreatGatsby_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Great Gatsby", "Page 2")
        print("=" * 80 + "\n" + "History" + "\n")
        print(textwrap.fill("There was so much to read for one thing and so much fine health to be pulled down out of the young breath-giving air. I bought a dozen volumes on banking and credit and investment securities and they stood on my shelf in red and gold like new money from the mint, promising to unfold the shining secrets that only Midas and Morgan and Maecenas knew. And I had the high intention of reading many other books besides. I was rather literary in college—one year I wrote a series of very solemn and obvious editorials for the ‘Yale News’—and now I was going to bring back all such things into my life and become again that most limited of all specialists, the ‘well-rounded man.’ This isn’t just an epigram—life is much more successfully looked at from a single window, after all.", 75))
        print("\nOpportunity")
        print(textwrap.fill("It was a matter of chance that I should have rented a house in one of the strangest communities in North America. It was on that slender riotous island which extends itself due east of New York and where there are, among other natural curiosities, two unusual formations of land. Twenty miles from the city a pair of enormous eggs, identical in contour and separated only by a courtesy bay, jut out into the most domesticated body of salt water in the Western Hemisphere, the great wet barnyard of Long Island Sound. They are not perfect ovals—like the egg in the Columbus story they are both crushed flat at the contact end—but their physical resemblance must be a source of perpetual confusion to the gulls that fly overhead. To the wingless a more arresting phenomenon is their dissimilarity in every particular except shape and size.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theGreatGatsby_page_1(username)
        elif options == "2":
            clear_console()
            return books.theGreatGatsby(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theGreatGatsby_page_1(username)
    def theCatcherInTheRye_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Catcher in the Rye", "Page 1")
        print("=" * 80 + "\n" + "Normalize" + "\n")
        print(textwrap.fill("If you really want to hear about it, the first thing you'll probably want to know is where I was born, an what my lousy childhood was like, and how my parents were occupied and all before they had me, and all that David Copperfield kind of crap, but I don't feel like going into it, if you want to know the truth. In the first place, that stuff bores me, and in the second place, my parents would have about two hemorrhages apiece if I told anything pretty personal about them. They're quite touchy about anything like that, especially my father. They're nice and all--I'm not saying that--but they're also touchy as hell. Besides, I'm not going to tell you my whole goddam autobiography or anything. I'll just tell you about this madman stuff that happened to me around last Christmas just before I got pretty run-down and had to come out here and take it easy. I mean that's all I told D.B. about, and he's my brother and all. He's in Hollywood. That isn't too far from this crumby place, and he comes over and visits me practically every week end. He's going to drive me home when I go home next month maybe. He just got a Jaguar. One of those little English jobs that can do around two hundred miles an hour. It cost him damn near four thousand bucks. He's got a lot of dough, now. He didn't use to. He used to be just a regular writer, when he was home. He wrote this terrific book of short stories, The Secret Goldfish, in case you never heard of him. The best one in it was 'The Secret Goldfish.' It was about this little kid that wouldn't let anybody look at his goldfish because he'd bought it with his own money. It killed me. Now he's out in Hollywood, D.B., being a prostitute. If there's one thing I hate, it's the movies. Don't even mention them to me.", 75))
        print("\nExecutive")
        print(textwrap.fill("Where I want to start telling is the day I left Pencey Prep. Pencey Prep is this school that's in Agerstown, Pennsylvania. You probably heard of it. You've probably seen the ads, anyway. They advertise in about a thousand magazines, always showing some hotshot guy on a horse jumping over a fence. Like as if all you ever did at Pencey was play polo all the time. I never even once saw a horse anywhere near the place. And underneath the guy on the horse's picture, it always says: 'Since 1888 we have been molding boys into splendid, clear_console-thinking young men.' Strictly for the birds. They don't do any damn more molding at Pencey than they do at any other school. And I didn't know anybody there that was splendid and clear_console-thinking and all. Maybe two guys. If that many. And they probably came to Pencey that way.", 75))
        print("\nRevolution")
        print(textwrap.fill("There were never many girls at all at the football games. Only seniors were allowed to bring girls with them. It was a terrible school, no matter how you looked at it. I like to be somewhere at least where you can see a few girls around once in a while, even if they're only scratching their arms or blowing their noses or even just giggling or something. Old Selma Thurmer--she was the headmaster's daughter--showed up at the games quite often, but she wasn't exactly the type that drove you mad with desire. She was a pretty nice girl, though. I sat next to her once in the bus from Agerstown and we sort of struck up a conversation. I liked her. She had a big nose and her nails were all bitten down and bleedy-looking and she had on those damn falsies that point all over the place, but you felt sort of sorry for her. What I liked about her, she didn't give you a lot of horse manure about what a great guy her father was. She probably knew what a phony slob he was.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theCatcherInTheRye_page_2(username)
        elif options == "2":
            clear_console()
            return books.theCatcherInTheRye(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theCatcherInTheRye_page_1(username)
    def theCatcherInTheRye_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Catcher in the Rye", "Page 2")
        print("=" * 80 + "\n" + "History" + "\n")
        print(textwrap.fill("The reason I was standing way up on Thomsen Hill, instead of down at the game, was because I'd just got back from New York with the fencing team. I was the goddam manager of the fencing team. Very big deal. We'd gone in to New York that morning for this fencing meet with McBurney School. Only, we didn't have the meet. I left all the foils and equipment and stuff on the goddam subway. It wasn't all my fault. I had to keep getting up to look at this map, so we'd know where to get off. So we got back to Pencey around two-thirty instead of around dinnertime. The whole team ostracized me the whole way back on the train. It was pretty funny, in a way. The other reason I wasn't down at the game was because I was on my way to say good-by to old Spencer, my history teacher. He had the grippe, and I figured I probably wouldn't see him again till Christmas vacation started. He wrote me this note saying he wanted to see me before I went home. He knew I wasn't coming back to Pencey.", 75))
        print("\nOpportunity")
        print(textwrap.fill("I forgot to tell you about that. They kicked me out. I wasn't supposed to come back after Christmas vacation on account of I was flunking four subjects and not applying myself and all. They gave me frequent warning to start applying myself--especially around midterms, when my parents came up for a conference with old Thurmer--but I didn't do it. So I got the ax. They give guys the ax quite frequently at Pencey. It has a very good academic rating, Pencey. It really does.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theCatcherInTheRye_page_1(username)
        elif options == "2":
            clear_console()
            return books.theCatcherInTheRye(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theCatcherInTheRye_page_1(username)
    def theAlchemist_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Alchemist", "Page 1")
        print("=" * 80 + "\n" + "Normalize" + "\n")
        print(textwrap.fill("If you really want to hear about it, the first thing you'll probably want to know is where I was born, an what my lousy childhood was like, and how my parents were occupied and all before they had me, and all that David Copperfield kind of crap, but I don't feel like going into it, if you want to know the truth. In the first place, that stuff bores me, and in the second place, my parents would have about two hemorrhages apiece if I told anything pretty personal about them. They're quite touchy about anything like that, especially my father. They're nice and all--I'm not saying that--but they're also touchy as hell. Besides, I'm not going to tell you my whole goddam autobiography or anything. I'll just tell you about this madman stuff that happened to me around last Christmas just before I got pretty run-down and had to come out here and take it easy. I mean that's all I told D.B. about, and he's my brother and all. He's in Hollywood. That isn't too far from this crumby place, and he comes over and visits me practically every week end. He's going to drive me home when I go home next month maybe. He just got a Jaguar. One of those little English jobs that can do around two hundred miles an hour. It cost him damn near four thousand bucks. He's got a lot of dough, now. He didn't use to. He used to be just a regular writer, when he was home. He wrote this terrific book of short stories, The Secret Goldfish, in case you never heard of him. The best one in it was 'The Secret Goldfish.' It was about this little kid that wouldn't let anybody look at his goldfish because he'd bought it with his own money. It killed me. Now he's out in Hollywood, D.B., being a prostitute. If there's one thing I hate, it's the movies. Don't even mention them to me.", 75))
        print("\nExecutive")
        print(textwrap.fill("Where I want to start telling is the day I left Pencey Prep. Pencey Prep is this school that's in Agerstown, Pennsylvania. You probably heard of it. You've probably seen the ads, anyway. They advertise in about a thousand magazines, always showing some hotshot guy on a horse jumping over a fence. Like as if all you ever did at Pencey was play polo all the time. I never even once saw a horse anywhere near the place. And underneath the guy on the horse's picture, it always says: 'Since 1888 we have been molding boys into splendid, clear_console-thinking young men.' Strictly for the birds. They don't do any damn more molding at Pencey than they do at any other school. And I didn't know anybody there that was splendid and clear_console-thinking and all. Maybe two guys. If that many. And they probably came to Pencey that way.", 75))
        print("\nRevolution")
        print(textwrap.fill("There were never many girls at all at the football games. Only seniors were allowed to bring girls with them. It was a terrible school, no matter how you looked at it. I like to be somewhere at least where you can see a few girls around once in a while, even if they're only scratching their arms or blowing their noses or even just giggling or something. Old Selma Thurmer--she was the headmaster's daughter--showed up at the games quite often, but she wasn't exactly the type that drove you mad with desire. She was a pretty nice girl, though. I sat next to her once in the bus from Agerstown and we sort of struck up a conversation. I liked her. She had a big nose and her nails were all bitten down and bleedy-looking and she had on those damn falsies that point all over the place, but you felt sort of sorry for her. What I liked about her, she didn't give you a lot of horse manure about what a great guy her father was. She probably knew what a phony slob he was.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theAlchemist_page_2(username)
        elif options == "2":
            clear_console()
            return books.theAlchemist(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theAlchemist_page_1(username)
    def theAlchemist_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Alchemist", "Page 2")
        print("=" * 80 + "\n" + "History" + "\n")
        print(textwrap.fill("The reason I was standing way up on Thomsen Hill, instead of down at the game, was because I'd just got back from New York with the fencing team. I was the goddam manager of the fencing team. Very big deal. We'd gone in to New York that morning for this fencing meet with McBurney School. Only, we didn't have the meet. I left all the foils and equipment and stuff on the goddam subway. It wasn't all my fault. I had to keep getting up to look at this map, so we'd know where to get off. So we got back to Pencey around two-thirty instead of around dinnertime. The whole team ostracized me the whole way back on the train. It was pretty funny, in a way. The other reason I wasn't down at the game was because I was on my way to say good-by to old Spencer, my history teacher. He had the grippe, and I figured I probably wouldn't see him again till Christmas vacation started. He wrote me this note saying he wanted to see me before I went home. He knew I wasn't coming back to Pencey.", 75))
        print("\nOpportunity")
        print(textwrap.fill("I forgot to tell you about that. They kicked me out. I wasn't supposed to come back after Christmas vacation on account of I was flunking four subjects and not applying myself and all. They gave me frequent warning to start applying myself--especially around midterms, when my parents came up for a conference with old Thurmer--but I didn't do it. So I got the ax. They give guys the ax quite frequently at Pencey. It has a very good academic rating, Pencey. It really does.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theAlchemist_page_1(username)
        elif options == "2":
            clear_console()
            return books.theAlchemist(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theAlchemist_page_1(username)
    def theJoyOfCooking_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Joy of Cooking", "Page 1")
        print("=" * 80 + "\n" + "Normalize" + "\n")
        print(textwrap.fill("If you really want to hear about it, the first thing you'll probably want to know is where I was born, an what my lousy childhood was like, and how my parents were occupied and all before they had me, and all that David Copperfield kind of crap, but I don't feel like going into it, if you want to know the truth. In the first place, that stuff bores me, and in the second place, my parents would have about two hemorrhages apiece if I told anything pretty personal about them. They're quite touchy about anything like that, especially my father. They're nice and all--I'm not saying that--but they're also touchy as hell. Besides, I'm not going to tell you my whole goddam autobiography or anything. I'll just tell you about this madman stuff that happened to me around last Christmas just before I got pretty run-down and had to come out here and take it easy. I mean that's all I told D.B. about, and he's my brother and all. He's in Hollywood. That isn't too far from this crumby place, and he comes over and visits me practically every week end. He's going to drive me home when I go home next month maybe. He just got a Jaguar. One of those little English jobs that can do around two hundred miles an hour. It cost him damn near four thousand bucks. He's got a lot of dough, now. He didn't use to. He used to be just a regular writer, when he was home. He wrote this terrific book of short stories, The Secret Goldfish, in case you never heard of him. The best one in it was 'The Secret Goldfish.' It was about this little kid that wouldn't let anybody look at his goldfish because he'd bought it with his own money. It killed me. Now he's out in Hollywood, D.B., being a prostitute. If there's one thing I hate, it's the movies. Don't even mention them to me.", 75))
        print("\nExecutive")
        print(textwrap.fill("Where I want to start telling is the day I left Pencey Prep. Pencey Prep is this school that's in Agerstown, Pennsylvania. You probably heard of it. You've probably seen the ads, anyway. They advertise in about a thousand magazines, always showing some hotshot guy on a horse jumping over a fence. Like as if all you ever did at Pencey was play polo all the time. I never even once saw a horse anywhere near the place. And underneath the guy on the horse's picture, it always says: 'Since 1888 we have been molding boys into splendid, clear_console-thinking young men.' Strictly for the birds. They don't do any damn more molding at Pencey than they do at any other school. And I didn't know anybody there that was splendid and clear_console-thinking and all. Maybe two guys. If that many. And they probably came to Pencey that way.", 75))
        print("\nRevolution")
        print(textwrap.fill("There were never many girls at all at the football games. Only seniors were allowed to bring girls with them. It was a terrible school, no matter how you looked at it. I like to be somewhere at least where you can see a few girls around once in a while, even if they're only scratching their arms or blowing their noses or even just giggling or something. Old Selma Thurmer--she was the headmaster's daughter--showed up at the games quite often, but she wasn't exactly the type that drove you mad with desire. She was a pretty nice girl, though. I sat next to her once in the bus from Agerstown and we sort of struck up a conversation. I liked her. She had a big nose and her nails were all bitten down and bleedy-looking and she had on those damn falsies that point all over the place, but you felt sort of sorry for her. What I liked about her, she didn't give you a lot of horse manure about what a great guy her father was. She probably knew what a phony slob he was.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theJoyOfCooking_page_2(username)
        elif options == "2":
            clear_console()
            return books.theJoyOfCooking(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theJoyOfCooking_page_1(username)
    def theJoyOfCooking_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Joy of Cooking", "Page 2")
        print("=" * 80 + "\n" + "History" + "\n")
        print(textwrap.fill("The reason I was standing way up on Thomsen Hill, instead of down at the game, was because I'd just got back from New York with the fencing team. I was the goddam manager of the fencing team. Very big deal. We'd gone in to New York that morning for this fencing meet with McBurney School. Only, we didn't have the meet. I left all the foils and equipment and stuff on the goddam subway. It wasn't all my fault. I had to keep getting up to look at this map, so we'd know where to get off. So we got back to Pencey around two-thirty instead of around dinnertime. The whole team ostracized me the whole way back on the train. It was pretty funny, in a way. The other reason I wasn't down at the game was because I was on my way to say good-by to old Spencer, my history teacher. He had the grippe, and I figured I probably wouldn't see him again till Christmas vacation started. He wrote me this note saying he wanted to see me before I went home. He knew I wasn't coming back to Pencey.", 75))
        print("\nOpportunity")
        print(textwrap.fill("I forgot to tell you about that. They kicked me out. I wasn't supposed to come back after Christmas vacation on account of I was flunking four subjects and not applying myself and all. They gave me frequent warning to start applying myself--especially around midterms, when my parents came up for a conference with old Thurmer--but I didn't do it. So I got the ax. They give guys the ax quite frequently at Pencey. It has a very good academic rating, Pencey. It really does.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theJoyOfCooking_page_1(username)
        elif options == "2":
            clear_console()
            return books.theJoyOfCooking(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theJoyOfCooking_page_1(username)
    def theFoodLab_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Food Lab", "Page 1")
        print("=" * 80 + "\n" + "Normalize" + "\n")
        print(textwrap.fill("If you really want to hear about it, the first thing you'll probably want to know is where I was born, an what my lousy childhood was like, and how my parents were occupied and all before they had me, and all that David Copperfield kind of crap, but I don't feel like going into it, if you want to know the truth. In the first place, that stuff bores me, and in the second place, my parents would have about two hemorrhages apiece if I told anything pretty personal about them. They're quite touchy about anything like that, especially my father. They're nice and all--I'm not saying that--but they're also touchy as hell. Besides, I'm not going to tell you my whole goddam autobiography or anything. I'll just tell you about this madman stuff that happened to me around last Christmas just before I got pretty run-down and had to come out here and take it easy. I mean that's all I told D.B. about, and he's my brother and all. He's in Hollywood. That isn't too far from this crumby place, and he comes over and visits me practically every week end. He's going to drive me home when I go home next month maybe. He just got a Jaguar. One of those little English jobs that can do around two hundred miles an hour. It cost him damn near four thousand bucks. He's got a lot of dough, now. He didn't use to. He used to be just a regular writer, when he was home. He wrote this terrific book of short stories, The Secret Goldfish, in case you never heard of him. The best one in it was 'The Secret Goldfish.' It was about this little kid that wouldn't let anybody look at his goldfish because he'd bought it with his own money. It killed me. Now he's out in Hollywood, D.B., being a prostitute. If there's one thing I hate, it's the movies. Don't even mention them to me.", 75))
        print("\nExecutive")
        print(textwrap.fill("Where I want to start telling is the day I left Pencey Prep. Pencey Prep is this school that's in Agerstown, Pennsylvania. You probably heard of it. You've probably seen the ads, anyway. They advertise in about a thousand magazines, always showing some hotshot guy on a horse jumping over a fence. Like as if all you ever did at Pencey was play polo all the time. I never even once saw a horse anywhere near the place. And underneath the guy on the horse's picture, it always says: 'Since 1888 we have been molding boys into splendid, clear_console-thinking young men.' Strictly for the birds. They don't do any damn more molding at Pencey than they do at any other school. And I didn't know anybody there that was splendid and clear_console-thinking and all. Maybe two guys. If that many. And they probably came to Pencey that way.", 75))
        print("\nRevolution")
        print(textwrap.fill("There were never many girls at all at the football games. Only seniors were allowed to bring girls with them. It was a terrible school, no matter how you looked at it. I like to be somewhere at least where you can see a few girls around once in a while, even if they're only scratching their arms or blowing their noses or even just giggling or something. Old Selma Thurmer--she was the headmaster's daughter--showed up at the games quite often, but she wasn't exactly the type that drove you mad with desire. She was a pretty nice girl, though. I sat next to her once in the bus from Agerstown and we sort of struck up a conversation. I liked her. She had a big nose and her nails were all bitten down and bleedy-looking and she had on those damn falsies that point all over the place, but you felt sort of sorry for her. What I liked about her, she didn't give you a lot of horse manure about what a great guy her father was. She probably knew what a phony slob he was.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theFoodLab_page_2(username)
        elif options == "2":
            clear_console()
            return books.theFoodLab(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theFoodLab_page_1(username)
    def theFoodLab_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Food Lab", "Page 2")
        print("=" * 80 + "\n" + "History" + "\n")
        print(textwrap.fill("The reason I was standing way up on Thomsen Hill, instead of down at the game, was because I'd just got back from New York with the fencing team. I was the goddam manager of the fencing team. Very big deal. We'd gone in to New York that morning for this fencing meet with McBurney School. Only, we didn't have the meet. I left all the foils and equipment and stuff on the goddam subway. It wasn't all my fault. I had to keep getting up to look at this map, so we'd know where to get off. So we got back to Pencey around two-thirty instead of around dinnertime. The whole team ostracized me the whole way back on the train. It was pretty funny, in a way. The other reason I wasn't down at the game was because I was on my way to say good-by to old Spencer, my history teacher. He had the grippe, and I figured I probably wouldn't see him again till Christmas vacation started. He wrote me this note saying he wanted to see me before I went home. He knew I wasn't coming back to Pencey.", 75))
        print("\nOpportunity")
        print(textwrap.fill("I forgot to tell you about that. They kicked me out. I wasn't supposed to come back after Christmas vacation on account of I was flunking four subjects and not applying myself and all. They gave me frequent warning to start applying myself--especially around midterms, when my parents came up for a conference with old Thurmer--but I didn't do it. So I got the ax. They give guys the ax quite frequently at Pencey. It has a very good academic rating, Pencey. It really does.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theFoodLab_page_1(username)
        elif options == "2":
            clear_console()
            return books.theFoodLab(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theFoodLab_page_1(username)
    def saltFatAcidHeat_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "Salt, Fat, Acid, Heat", "Page 1")
        print("=" * 80 + "\n" + "Normalize" + "\n")
        print(textwrap.fill("If you really want to hear about it, the first thing you'll probably want to know is where I was born, an what my lousy childhood was like, and how my parents were occupied and all before they had me, and all that David Copperfield kind of crap, but I don't feel like going into it, if you want to know the truth. In the first place, that stuff bores me, and in the second place, my parents would have about two hemorrhages apiece if I told anything pretty personal about them. They're quite touchy about anything like that, especially my father. They're nice and all--I'm not saying that--but they're also touchy as hell. Besides, I'm not going to tell you my whole goddam autobiography or anything. I'll just tell you about this madman stuff that happened to me around last Christmas just before I got pretty run-down and had to come out here and take it easy. I mean that's all I told D.B. about, and he's my brother and all. He's in Hollywood. That isn't too far from this crumby place, and he comes over and visits me practically every week end. He's going to drive me home when I go home next month maybe. He just got a Jaguar. One of those little English jobs that can do around two hundred miles an hour. It cost him damn near four thousand bucks. He's got a lot of dough, now. He didn't use to. He used to be just a regular writer, when he was home. He wrote this terrific book of short stories, The Secret Goldfish, in case you never heard of him. The best one in it was 'The Secret Goldfish.' It was about this little kid that wouldn't let anybody look at his goldfish because he'd bought it with his own money. It killed me. Now he's out in Hollywood, D.B., being a prostitute. If there's one thing I hate, it's the movies. Don't even mention them to me.", 75))
        print("\nExecutive")
        print(textwrap.fill("Where I want to start telling is the day I left Pencey Prep. Pencey Prep is this school that's in Agerstown, Pennsylvania. You probably heard of it. You've probably seen the ads, anyway. They advertise in about a thousand magazines, always showing some hotshot guy on a horse jumping over a fence. Like as if all you ever did at Pencey was play polo all the time. I never even once saw a horse anywhere near the place. And underneath the guy on the horse's picture, it always says: 'Since 1888 we have been molding boys into splendid, clear_console-thinking young men.' Strictly for the birds. They don't do any damn more molding at Pencey than they do at any other school. And I didn't know anybody there that was splendid and clear_console-thinking and all. Maybe two guys. If that many. And they probably came to Pencey that way.", 75))
        print("\nRevolution")
        print(textwrap.fill("There were never many girls at all at the football games. Only seniors were allowed to bring girls with them. It was a terrible school, no matter how you looked at it. I like to be somewhere at least where you can see a few girls around once in a while, even if they're only scratching their arms or blowing their noses or even just giggling or something. Old Selma Thurmer--she was the headmaster's daughter--showed up at the games quite often, but she wasn't exactly the type that drove you mad with desire. She was a pretty nice girl, though. I sat next to her once in the bus from Agerstown and we sort of struck up a conversation. I liked her. She had a big nose and her nails were all bitten down and bleedy-looking and she had on those damn falsies that point all over the place, but you felt sort of sorry for her. What I liked about her, she didn't give you a lot of horse manure about what a great guy her father was. She probably knew what a phony slob he was.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.saltFatAcidHeat_page_2(username)
        elif options == "2":
            clear_console()
            return books.saltFatAcidHeat(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.saltFatAcidHeat_page_1(username)
    def saltFatAcidHeat_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "Salt, Fat, Acid, Heat", "Page 2")
        print("=" * 80 + "\n" + "History" + "\n")
        print(textwrap.fill("The reason I was standing way up on Thomsen Hill, instead of down at the game, was because I'd just got back from New York with the fencing team. I was the goddam manager of the fencing team. Very big deal. We'd gone in to New York that morning for this fencing meet with McBurney School. Only, we didn't have the meet. I left all the foils and equipment and stuff on the goddam subway. It wasn't all my fault. I had to keep getting up to look at this map, so we'd know where to get off. So we got back to Pencey around two-thirty instead of around dinnertime. The whole team ostracized me the whole way back on the train. It was pretty funny, in a way. The other reason I wasn't down at the game was because I was on my way to say good-by to old Spencer, my history teacher. He had the grippe, and I figured I probably wouldn't see him again till Christmas vacation started. He wrote me this note saying he wanted to see me before I went home. He knew I wasn't coming back to Pencey.", 75))
        print("\nOpportunity")
        print(textwrap.fill("I forgot to tell you about that. They kicked me out. I wasn't supposed to come back after Christmas vacation on account of I was flunking four subjects and not applying myself and all. They gave me frequent warning to start applying myself--especially around midterms, when my parents came up for a conference with old Thurmer--but I didn't do it. So I got the ax. They give guys the ax quite frequently at Pencey. It has a very good academic rating, Pencey. It really does.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.saltFatAcidHeat_page_1(username)
        elif options == "2":
            clear_console()
            return books.saltFatAcidHeat(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.saltFatAcidHeat_page_1(username)
    def theFlavorBible_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Flavor Bible", "Page 1")
        print("=" * 80 + "\n" + "Normalize" + "\n")
        print(textwrap.fill("If you really want to hear about it, the first thing you'll probably want to know is where I was born, an what my lousy childhood was like, and how my parents were occupied and all before they had me, and all that David Copperfield kind of crap, but I don't feel like going into it, if you want to know the truth. In the first place, that stuff bores me, and in the second place, my parents would have about two hemorrhages apiece if I told anything pretty personal about them. They're quite touchy about anything like that, especially my father. They're nice and all--I'm not saying that--but they're also touchy as hell. Besides, I'm not going to tell you my whole goddam autobiography or anything. I'll just tell you about this madman stuff that happened to me around last Christmas just before I got pretty run-down and had to come out here and take it easy. I mean that's all I told D.B. about, and he's my brother and all. He's in Hollywood. That isn't too far from this crumby place, and he comes over and visits me practically every week end. He's going to drive me home when I go home next month maybe. He just got a Jaguar. One of those little English jobs that can do around two hundred miles an hour. It cost him damn near four thousand bucks. He's got a lot of dough, now. He didn't use to. He used to be just a regular writer, when he was home. He wrote this terrific book of short stories, The Secret Goldfish, in case you never heard of him. The best one in it was 'The Secret Goldfish.' It was about this little kid that wouldn't let anybody look at his goldfish because he'd bought it with his own money. It killed me. Now he's out in Hollywood, D.B., being a prostitute. If there's one thing I hate, it's the movies. Don't even mention them to me.", 75))
        print("\nExecutive")
        print(textwrap.fill("Where I want to start telling is the day I left Pencey Prep. Pencey Prep is this school that's in Agerstown, Pennsylvania. You probably heard of it. You've probably seen the ads, anyway. They advertise in about a thousand magazines, always showing some hotshot guy on a horse jumping over a fence. Like as if all you ever did at Pencey was play polo all the time. I never even once saw a horse anywhere near the place. And underneath the guy on the horse's picture, it always says: 'Since 1888 we have been molding boys into splendid, clear_console-thinking young men.' Strictly for the birds. They don't do any damn more molding at Pencey than they do at any other school. And I didn't know anybody there that was splendid and clear_console-thinking and all. Maybe two guys. If that many. And they probably came to Pencey that way.", 75))
        print("\nRevolution")
        print(textwrap.fill("There were never many girls at all at the football games. Only seniors were allowed to bring girls with them. It was a terrible school, no matter how you looked at it. I like to be somewhere at least where you can see a few girls around once in a while, even if they're only scratching their arms or blowing their noses or even just giggling or something. Old Selma Thurmer--she was the headmaster's daughter--showed up at the games quite often, but she wasn't exactly the type that drove you mad with desire. She was a pretty nice girl, though. I sat next to her once in the bus from Agerstown and we sort of struck up a conversation. I liked her. She had a big nose and her nails were all bitten down and bleedy-looking and she had on those damn falsies that point all over the place, but you felt sort of sorry for her. What I liked about her, she didn't give you a lot of horse manure about what a great guy her father was. She probably knew what a phony slob he was.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theFlavorBible_page_2(username)
        elif options == "2":
            clear_console()
            return books.theFlavorBible(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theFlavorBible_page_1(username)
    def theFlavorBible_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Flavor Bible", "Page 2")
        print("=" * 80 + "\n" + "History" + "\n")
        print(textwrap.fill("The reason I was standing way up on Thomsen Hill, instead of down at the game, was because I'd just got back from New York with the fencing team. I was the goddam manager of the fencing team. Very big deal. We'd gone in to New York that morning for this fencing meet with McBurney School. Only, we didn't have the meet. I left all the foils and equipment and stuff on the goddam subway. It wasn't all my fault. I had to keep getting up to look at this map, so we'd know where to get off. So we got back to Pencey around two-thirty instead of around dinnertime. The whole team ostracized me the whole way back on the train. It was pretty funny, in a way. The other reason I wasn't down at the game was because I was on my way to say good-by to old Spencer, my history teacher. He had the grippe, and I figured I probably wouldn't see him again till Christmas vacation started. He wrote me this note saying he wanted to see me before I went home. He knew I wasn't coming back to Pencey.", 75))
        print("\nOpportunity")
        print(textwrap.fill("I forgot to tell you about that. They kicked me out. I wasn't supposed to come back after Christmas vacation on account of I was flunking four subjects and not applying myself and all. They gave me frequent warning to start applying myself--especially around midterms, when my parents came up for a conference with old Thurmer--but I didn't do it. So I got the ax. They give guys the ax quite frequently at Pencey. It has a very good academic rating, Pencey. It really does.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theFlavorBible_page_1(username)
        elif options == "2":
            clear_console()
            return books.theFlavorBible(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theFlavorBible_page_1(username)
    def theScienceOfGoodCooking_page_1(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Science of Good Cooking", "Page 1")
        print("=" * 80 + "\n" + "Normalize" + "\n")
        print(textwrap.fill("If you really want to hear about it, the first thing you'll probably want to know is where I was born, an what my lousy childhood was like, and how my parents were occupied and all before they had me, and all that David Copperfield kind of crap, but I don't feel like going into it, if you want to know the truth. In the first place, that stuff bores me, and in the second place, my parents would have about two hemorrhages apiece if I told anything pretty personal about them. They're quite touchy about anything like that, especially my father. They're nice and all--I'm not saying that--but they're also touchy as hell. Besides, I'm not going to tell you my whole goddam autobiography or anything. I'll just tell you about this madman stuff that happened to me around last Christmas just before I got pretty run-down and had to come out here and take it easy. I mean that's all I told D.B. about, and he's my brother and all. He's in Hollywood. That isn't too far from this crumby place, and he comes over and visits me practically every week end. He's going to drive me home when I go home next month maybe. He just got a Jaguar. One of those little English jobs that can do around two hundred miles an hour. It cost him damn near four thousand bucks. He's got a lot of dough, now. He didn't use to. He used to be just a regular writer, when he was home. He wrote this terrific book of short stories, The Secret Goldfish, in case you never heard of him. The best one in it was 'The Secret Goldfish.' It was about this little kid that wouldn't let anybody look at his goldfish because he'd bought it with his own money. It killed me. Now he's out in Hollywood, D.B., being a prostitute. If there's one thing I hate, it's the movies. Don't even mention them to me.", 75))
        print("\nExecutive")
        print(textwrap.fill("Where I want to start telling is the day I left Pencey Prep. Pencey Prep is this school that's in Agerstown, Pennsylvania. You probably heard of it. You've probably seen the ads, anyway. They advertise in about a thousand magazines, always showing some hotshot guy on a horse jumping over a fence. Like as if all you ever did at Pencey was play polo all the time. I never even once saw a horse anywhere near the place. And underneath the guy on the horse's picture, it always says: 'Since 1888 we have been molding boys into splendid, clear_console-thinking young men.' Strictly for the birds. They don't do any damn more molding at Pencey than they do at any other school. And I didn't know anybody there that was splendid and clear_console-thinking and all. Maybe two guys. If that many. And they probably came to Pencey that way.", 75))
        print("\nRevolution")
        print(textwrap.fill("There were never many girls at all at the football games. Only seniors were allowed to bring girls with them. It was a terrible school, no matter how you looked at it. I like to be somewhere at least where you can see a few girls around once in a while, even if they're only scratching their arms or blowing their noses or even just giggling or something. Old Selma Thurmer--she was the headmaster's daughter--showed up at the games quite often, but she wasn't exactly the type that drove you mad with desire. She was a pretty nice girl, though. I sat next to her once in the bus from Agerstown and we sort of struck up a conversation. I liked her. She had a big nose and her nails were all bitten down and bleedy-looking and she had on those damn falsies that point all over the place, but you felt sort of sorry for her. What I liked about her, she didn't give you a lot of horse manure about what a great guy her father was. She probably knew what a phony slob he was.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 1':^80}" + "\n" + "\n\n\n1. Next page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theScienceOfGoodCooking_page_2(username)
        elif options == "2":
            clear_console()
            return books.theScienceOfGoodCooking(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theScienceOfGoodCooking_page_1(username)
    def theScienceOfGoodCooking_page_2(username):
        clear_console()
        if username != "guest":
            update_history(username, "The Science of Good Cooking", "Page 2")
        print("=" * 80 + "\n" + "History" + "\n")
        print(textwrap.fill("The reason I was standing way up on Thomsen Hill, instead of down at the game, was because I'd just got back from New York with the fencing team. I was the goddam manager of the fencing team. Very big deal. We'd gone in to New York that morning for this fencing meet with McBurney School. Only, we didn't have the meet. I left all the foils and equipment and stuff on the goddam subway. It wasn't all my fault. I had to keep getting up to look at this map, so we'd know where to get off. So we got back to Pencey around two-thirty instead of around dinnertime. The whole team ostracized me the whole way back on the train. It was pretty funny, in a way. The other reason I wasn't down at the game was because I was on my way to say good-by to old Spencer, my history teacher. He had the grippe, and I figured I probably wouldn't see him again till Christmas vacation started. He wrote me this note saying he wanted to see me before I went home. He knew I wasn't coming back to Pencey.", 75))
        print("\nOpportunity")
        print(textwrap.fill("I forgot to tell you about that. They kicked me out. I wasn't supposed to come back after Christmas vacation on account of I was flunking four subjects and not applying myself and all. They gave me frequent warning to start applying myself--especially around midterms, when my parents came up for a conference with old Thurmer--but I didn't do it. So I got the ax. They give guys the ax quite frequently at Pencey. It has a very good academic rating, Pencey. It really does.", 75))
        options = input("=" * 80 + "\n" + f"{'PAGE 2':^80}" + "\n" + "\n\n\n1. Previous page" + "\n" + "2. Exit" + "\n" + "Choose your option (1/2): ")
        if options == "1":
            clear_console()
            return page.theScienceOfGoodCooking_page_1(username)
        elif options == "2":
            clear_console()
            return books.theScienceOfGoodCooking(username)
        else:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
            return page.theScienceOfGoodCooking_page_1(username)
def loading():
    clear_console()
    for _ in range(2):
        print("=" * 80 + "\n\n\n" + f"{'Loading.  ':>43}" + "\n\n\n" + "=" * 80)
        time.sleep(0.2)
        clear_console()
        print("=" * 80 + "\n\n\n" + f"{'Loading.. ':>43}" + "\n\n\n" + "=" * 80)
        time.sleep(0.2)
        clear_console()
        print("=" * 80 + "\n\n\n" + f"{'Loading...':>43}" + "\n\n\n" + "=" * 80)
        time.sleep(0.2)
        clear_console()
    return homepage(username)
def homepage(username):
    clear_console()
    option = input("=" * 80+"\n"+f"{'EZRID':^80}"+"\n"+"=" * 80+"\n"+"1. Login"+"\n"+"2. Sign up"+"\n"+"3. Guest"+"\n"+"=" * 80+"\n"+"Choose your option (1/2/3): ")
    if option == "1":
        clear_console()
        return login(username)
    elif option == "2":
        clear_console()
        return signup(username)
    elif option == "3":
        clear_console()
        return guest("guest")
    else:
        clear_console()
        print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
        time.sleep(2)
        return homepage(username)
def menupage(username):
    clear_console()
    option = input("=" * 80+"\n"+f"{'MENU':^80}"+"\n"+"=" * 80+"\n"+"1. Search"+"\n"+"2. Category"+"\n"+"3. Favorite"+"\n"+"4. History"+"\n"+"5. My Points"+"\n"+"6. Settings"+"\n"+"7. Logout"+"\n"+"=" * 80+"\n"+"Choose your option (1/2/3/4/5/6/7): ")
    if option == "1":
        clear_console()
        return search(username)
    elif option == "2":
        clear_console()
        return category(username)
    elif option == "3":
        if not data_user or username == "guest":
            clear_console()
            print("="*80 + "\n\n\n\n" + "Favorite is unavailable for guest accounts.\n\n\n\n" + "="*80)
            time.sleep(2)
            return menupage(username)
        clear_console()
        return favorite(username)
    elif option == "4":
        if not data_user or username == "guest":
            clear_console()
            print("="*80 + "\n\n\n\n" + "History is unavailable for guest accounts.\n\n\n\n" + "="*80)
            time.sleep(2)
            return menupage(username)
        clear_console()
        return history(username)
    elif option == "5":
        if not data_user or username == "guest":
            clear_console()
            print("="*80 + "\n\n\n\n" + "Payments is unavailable for guest accounts.\n\n\n\n" + "="*80)
            time.sleep(2)
            return menupage(username)
        clear_console()
        return payments(username)
    elif option == "6":
        if not data_user or username == "guest":
            clear_console()
            print("="*80 + "\n\n\n\n" + "Settings is unavailable for guest accounts.\n\n\n\n" + "="*80)
            time.sleep(2)
            return menupage(username)
        clear_console()
        return settings(username)
    elif option == "7":
        clear_console()
        return homepage(username)
    else:
        clear_console()
        print("="*80 + "\n\n\n\n" + "Invalid option. Please try again.\n\n\n\n" + "="*80)
        time.sleep(2)
        return menupage(username)
def login(username):
    if not data_user:
        print("=" * 80 + "\n\n\n\nNo user found. Please sign up first.\n\n\n\n"+"=" * 80)
        time.sleep(2)
        return homepage(username)
    clear_console()
    username = input("=" * 80+"\n"+f"{'LOGIN':^80}"+"\n"+"=" * 80+"\nWrite 'exit' to go back\n\nEnter your username or email: ").lower()
    if not username:
        clear_console()
        print("="*80+"\n\n\n\nUsername or email cannot be empty. Please try again.\n\n\n\n"+"="*80)
        time.sleep(2)
        return login(username)
    password = pwinput.pwinput(prompt="Enter your password: " ,mask="*").lower()
    if not password:
        clear_console()
        print("="*80+"\n\n\n\nPassword cannot be empty. Please try again.\n\n\n\n"+"="*80)
        time.sleep(2)
        return login(username)
    if escape in username or escape in password:
        clear_console()
        return homepage(username)
    for user in data_user:
        if (user[0] == username or user[2] == username) and user[1] == password:
            clear_console()
            print("="*80+"\n\n\n\nLogin successfully\n\n\n\n"+"="*80)
            time.sleep(2)
            return menupage(username)
    clear_console()
    print("="*80+"\n\n\n\nInvalid username or password\n\n\n\n"+"="*80)
    time.sleep(2)
    return login(username)
def signup(username):
    while True:
        clear_console()
        email = input("=" * 80+"\n"+f"{'SIGN UP':^80}"+"\n"+"=" * 80+"\nWrite 'exit' to go back\n\nEnter your email address: ").lower()
        if escape in email:
            clear_console()
            return homepage(username)
        if "@" not in email or "." not in email:
            clear_console()
            print("="*80+"\n\n\n\nInvalid email address\n\n\n\n"+"="*80)
            time.sleep(2)
            return signup(username)
        for gmail in data_user:
            if gmail[2] == email:
                clear_console()
                print("="*80+"\n\n\n\nEmail already exists\n\n\n\n"+"="*80)
                time.sleep(2)
                return signup(username)
        username = input("Enter your username: ").lower()
        if escape in username:
            clear_console()
            return homepage(username)
        for user in data_user:
            if user[0] == username:
                clear_console()
                print("="*80+"\n\n\n\nUsername already exists\n\n\n\n"+"="*80)
                time.sleep(2)
                return signup(username)
        password = pwinput.pwinput(prompt="Enter your password: ", mask="*").lower()
        confirm_password = pwinput.pwinput(prompt="Confirm your password: ", mask="*").lower()
        if escape in password or escape in confirm_password:
            clear_console()
            return homepage(username)
        if password != confirm_password:
            clear_console()
            print("="*80+"\n\n\n\nPassword does not match\n\n\n\n"+"="*80)
            time.sleep(2)
            continue
        elif password == confirm_password:
            data_user.append([username, password, email])
            clear_console()
            print("="*80+"\n\n\n\nSign up successfully\n\n\n\n"+"="*80)
            time.sleep(2)
            return menupage(username)
def guest(username):
    clear_console()
    print("="*80+"\n\n\n\n"+"You are using the guest account\n\n\n\n"+"="*80)
    time.sleep(2)
    return menupage(username)
def search(username):
    while True:
        clear_console()
        search_bar = input("=" * 80+"\n"+f"{'SEARCH':^80}"+"\n"+"=" * 80+"\n"+"Type 'exit' to go back"+"\n"+"\n\nSearch book: ").lower()
        found = False
        if not search_bar:
            clear_console()
            print("="*80+"\n\n\n\n"+"Please enter a book name\n\n\n\n"+"="*80)
            time.sleep(2)
            continue
        if escape in search_bar:
            clear_console()
            return menupage(username)
        for book in data_book:
            if search_bar == book[0].lower():
                found = True
                clear_console()
                update_history(username, book[0], "Cover Page")
                if book[0] == "Introduction to Algorithms":
                    books.introductionToAlgorithms(username)
                elif book[0] == "Learning JavaScript Design Patterns":
                    books.learningJavaScriptDesignPatterns(username)
                elif book[0] == "Python Programming: An Introduction to Computer Science":
                    books.pythonProgrammingAnIntroductionToComputerScience(username)
                elif book[0] == "Programming Language Design and Implementation":
                    books.programmingLanguageDesignAndImplementation(username)
                elif book[0] == "Python unruk Programmer Pemula":                        
                    books.pythonUntukProgrammerPemula(username)
                elif book[0] == "Solo Leveling":
                    books.soloLeveling(username)
                elif book[0] == "Omniscient Reader's Viewpoint":
                    books.omniscientReadersViewpoint(username)
                elif book[0] == "The Beginning After The End":
                    books.theBeginningAfterTheEnd(username)
                elif book[0] == "Mercenary Enrollment":
                    books.mercenaryEnrollment(username)
                elif book[0] == "The Novel's Extra":
                    books.theNovelsExtra(username)
                elif book[0] == "The Dream Class":
                    books.theDreamClass(username)
                elif book[0] == "America: Militaristic or Peaceful":
                    books.americaMilitaristicOrPeaceful(username)
                elif book[0] == "The Great Gatsby":
                    books.theGreatGatsby(username)
                elif book[0] == "The Catcher in the Rye":
                    books.theCatcherInTheRye(username)
                elif book[0] == "The Alchemist":
                    books.theAlchemist(username)
                elif book[0] == "The Joy of Cooking":
                    books.theJoyOfCooking(username)
                elif book[0] == "The Food Lab":
                    books.theFoodLab(username)
                elif book[0] == "Salt, Fat, Acid, Heat":
                    books.saltFatAcidHeat(username)
                elif book[0] == "The Flavor Bible":
                    books.theFlavorBible(username)
                elif book[0] == "The Science of Good Cooking":
                    books.theScienceOfGoodCooking(username)
                else:
                    print("="*80+"\n\n\n\n"+"Book details not available.\n\n\n\n"+"="*80)
                    input("="*80+"\n\n\n\n"+"Press enter to return.\n\n\n\n"+"="*80)
                    return search(username)
        if not found:
            clear_console()
            print("="*80+"\n\n\n\n"+"Book not found\n\n\n\n"+"="*80)
            time.sleep(2)
            return search(username)
def category(username):
    clear_console()
    cate = input("=" * 80+"\n"+f"{'CATEGORY':^80}"+"\n"+"=" * 80+"\n"+"1. Academic"+"\n"+"2. Comic"+"\n"+"3. Novel"+"\n"+"4. Cook"+"\n"+"5. Exit"+"\n"+"=" * 80+"\n"+"\nChoose your category (1/2/3/4/5): ")
    if cate == "1":
        academic_books = [book for book in data_book if book[1] == "Academic"]
        if not academic_books:
            clear_console()
            print("="*80+"\n\n\n\n"+"No academic books found\n\n\n\n"+"="*80)
            time.sleep(2)
            return category(username)
        else:
            clear_console()
            print("=" * 80 + "\n" + f"{'Academic Books':^80}" + "\n" + "=" * 80)
            for idx, book in enumerate(academic_books, 1):
                print(f"{idx}. {book[0]}")
            option = input("\nPress enter to go back...\n\nChoose your option (1/2/3/4/5): ")
            if option == "1":
                books.introductionToAlgorithms(username)
            elif option == "2":
                books.learningJavaScriptDesignPatterns(username)
            elif option == "3":
                books.pythonProgrammingAnIntroductionToComputerScience(username)
            elif option == "4":
                books.programmingLanguageDesignAndImplementation(username)
            elif option == "5":
                books.pythonUntukProgrammerPemula(username)
            elif option == "":
                return category(username)
            else:
                clear_console()
                print("="*80+"\n\n\n\nInvalid option\n\n\n\n"+"="*80)
                time.sleep(2)
                return category(username)
    elif cate == "2":
        comic_books = [book for book in data_book if book[1] == "Comic"]
        if not comic_books:
            clear_console()
            print("="*80+"\n\n\n\n"+"No comic books found\n\n\n\n"+"="*80)
            time.sleep(2)
            return category(username)
        else:
            clear_console()
            print("=" * 80 + "\n" + f"{'Comic Books':^80}" + "\n" + "=" * 80)
            for idx, book in enumerate(comic_books, 1):
                print(f"{idx}. {book[0]}")
            option = input("\nPress enter to go back...\n\nChoose your option (1/2/3/4/5): ")
            if option == "1":
                books.soloLeveling(username)
            elif option == "2":
                books.omniscientReadersViewpoint(username)
            elif option == "3":
                books.theBeginningAfterTheEnd(username)
            elif option == "4":
                books.mercenaryEnrollment(username)
            elif option == "5":
                books.theNovelsExtra(username)
            elif option == "":
                return category(username)
            else:
                clear_console()
                print("="*80+"\n\n\n\nInvalid option\n\n\n\n"+"="*80)
                time.sleep(2)
                return category(username)
    elif cate == "3":
        novel_books = [book for book in data_book if book[1] == "Novel"]
        if not novel_books:
            clear_console()
            print("="*80+"\n\n\n\n"+"No novel books found\n\n\n\n"+"="*80)
            time.sleep(2)
            return category(username)
        else:
            clear_console()
            print("=" * 80 + "\n" + f"{'Novel Books':^80}" + "\n" + "=" * 80)
            for idx, book in enumerate(novel_books, 1):
                print(f"{idx}. {book[0]}")
            option = input("\nPress enter to go back...\n\nChoose your option (1/2/3/4/5): ")
            if option == "1":
                books.theDreamClass(username)
            elif option == "2":
                books.americaMilitaristicOrPeaceful(username)
            elif option == "3":
                books.theGreatGatsby(username)
            elif option == "4":
                books.theCatcherInTheRye(username)
            elif option == "5":
                books.theAlchemist(username)
            elif option == "":
                return category(username)
            else:
                clear_console()
                print("="*80+"\n\n\n\nInvalid option\n\n\n\n"+"="*80)
                time.sleep(2)
                return category(username)
    elif cate == "4":
        cook_books = [book for book in data_book if book[1] == "Cook"]
        if not cook_books:
            clear_console()
            print("="*80+"\n\n\n\n"+"No cook books found\n\n\n\n"+"="*80)
            time.sleep(2)
            return category(username)
        else:
            clear_console()
            print("=" * 80 + "\n" + f"{'Cook Books':^80}" + "\n" + "=" * 80)
            for idx, book in enumerate(cook_books, 1):
                print(f"{idx}. {book[0]}")
            ioption = input("\nPress enter to go back...\n\nChoose your option (1/2/3/4/5): ")
            if option == "1":
                books.theJoyOfCooking(username)
            elif option == "2":
                books.theFoodLab(username)
            elif option == "3":
                books.saltFatAcidHeat(username)
            elif option == "4":
                books.theFlavorBible(username)
            elif option == "5":
                books.theScienceOfGoodCooking(username)
            elif option == "":
                return category(username)
            else:
                clear_console()
                print("="*80+"\n\n\n\nInvalid option\n\n\n\n"+"="*80)
                time.sleep(2)
                return category(username)
    elif cate == "5":
        return menupage(username)
    else:
        clear_console()
        print("="*80+"\n\n\n\n"+"Invalid category. Please try again.\n\n\n\n"+"="*80)
        time.sleep(2)
        return category(username)
def favorite(username):
    clear_console()
    print("=" * 80 + "\n" + f"{'FAVORITE':^80}" + "\n" + "=" * 80)
    if username not in user_favorites or not user_favorites[username]:
        print("You have no favorite books yet.")
    else:
        print(f"{'No.':<5}{'Book Title':<50}")
        print("=" * 80)
        for idx, entry in enumerate(user_favorites[username], 1):
            print(f"{idx:<5}{entry['book']:<50}")
    input("\n\nPress enter to return to the menu.")
    return menupage(username)

def update_favorite(username, book_title):
    if username == "guest":
        return
    if username not in user_favorites:
        user_favorites[username] = []
    user_favorites[username].append({"book": book_title})
    print("=" * 80 + "\n\n\n\n" + f"Added {book_title} to your favorite list.\n\n\n\n" + "=" * 80)
    time.sleep(2)
    return favorite(username)
def payments(username):
    clear_console()
    print("="*80 + "\n" + f"{'Payment Processing':^80}" + "\n" + "="*80)
    print("1. 10.000 Points")
    print("2. 20.000 Points")
    print("3. 30.000 Points")
    print("4. Exit")
    choose = input("Nominal (1/2/3/4): ")
    if choose == "1":
        clear_console()
        print("="*80 + "\n" + f"{'Payment Processing':^80}" + "\n" + "="*80)
        print("1. Credit Card")
        print("2. PayPal")
        option = input(int("Payment option (1/2): "))
        if option == "1":
            clear_console()
            print("="*80 + "\n" + f"{'Payment Processing':^80}" + "\n" + "="*80)
            cn = input("Card Number: ")
            cvv = input("CVV: ")
            exp_date = input("Expiration Date (MM/YY): ")
            print("Processing payment...\n")
            time.sleep(2)
            print("Payment successful!\n")
            print("="*80)
            time.sleep(2)
            return menupage(username)
        elif option == "2":
            clear_console()
            print("="*80 + "\n" + f"{'Payment Processing':^80}" + "\n" + "="*80)
            print("PayPal Account:")
            email = input("Email: ")
            password = input("Password: ")
            print("Processing payment...\n")
            time.sleep(2)
            print("Payment successful!\n")
            print("="*80)
            time.sleep(2)
            return menupage(username)
    if choose == "2":
        clear_console()
        print("="*80 + "\n" + f"{'Payment Processing':^80}" + "\n" + "="*80)
        print("1. Credit Card")
        print("2. PayPal")
        option = input(int("Payment option (1/2): "))
        if option == "1":
            clear_console()
            print("="*80 + "\n" + f"{'Payment Processing':^80}" + "\n" + "="*80)
            cn = input("Card Number: ")
            cvv = input("CVV: ")
            exp_date = input("Expiration Date (MM/YY): ")
            print("Processing payment...\n")
            time.sleep(2)
            print("Payment successful!\n")
            print("="*80)
            time.sleep(2)
            return menupage(username)
        elif option == "2":
            clear_console()
            print("="*80 + "\n" + f"{'Payment Processing':^80}" + "\n" + "="*80)
            print("PayPal Account:")
            email = input("Email: ")
            password = input("Password: ")
            print("Processing payment...\n")
            time.sleep(2)
            print("Payment successful!\n")
            print("="*80)
            time.sleep(2)
            return menupage(username)
    if choose == "3":
        clear_console()
        print("="*80 + "\n" + f"{'Payment Processing':^80}" + "\n" + "="*80)
        print("1. Credit Card")
        print("2. PayPal")
        option = input(int("Payment option (1/2): "))
        if option == "1":
            clear_console()
            print("="*80 + "\n" + f"{'Payment Processing':^80}" + "\n" + "="*80)
            cn = input("Card Number: ")
            cvv = input("CVV: ")
            exp_date = input("Expiration Date (MM/YY): ")
            print("Processing payment...\n")
            time.sleep(2)
            print("Payment successful!\n")
            print("="*80)
            time.sleep(2)
            return menupage(username)
        elif option == "2":
            clear_console()
            print("="*80 + "\n" + f"{'Payment Processing':^80}" + "\n" + "="*80)
            print("PayPal Account:")
            email = input("Email: ")
            password = input("Password: ")
            print("Processing payment...\n")
            time.sleep(2)
            print("Payment successful!\n")
            print("="*80)
            time.sleep(2)
            return menupage(username)
    if choose == "4":
        clear_console()
        return menupage(username)
    else:
        clear_console()
        print("="*80+"\n\n\n\nInvalid option\n\n\n\n"+"="*80)
        time.sleep(2)
        return payments(username)
def history(username):
    clear_console()
    print("=" * 80+"\n"+f"{'HISTORY':^80}"+"\n"+"=" * 80)
    if username == "guest":
        print("History is unavailable for guest accounts.")
    elif username not in user_history or not user_history[username]:
        print("You have no reading history yet.")
    else:
        print(f"{'No.':<5}{'Book Title':<50}{'Last Page Viewed':<20}")
        print("-" * 80)
        for idx, entry in enumerate(user_history[username], 1):
            print(f"{idx:<5}{entry['book']:<50}{entry['last_page']:<20}")
    input("\n\nPress enter to return to the menu.")
    return menupage(username)
def update_history(username, book_title, last_page):
    if username == "guest":
        return
    if last_page == "Cover Page":
        return
    if username not in user_history:
        user_history[username] = []
    for entry in user_history[username]:
        if entry['book'] == book_title:
            entry['last_page'] = last_page
            return
    user_history[username].append({'book': book_title, 'last_page': last_page})
def settings(username):
    clear_console()
    option = input("=" * 80+"\n"+f"{'SETTINGS':^80}"+"\n"+"=" * 80+"\n"+"1. Change email"+"\n"+"2. Change username"+"\n"+"3. Change password"+"\n"+"4. Exit"+"\n"+"=" * 80+"\n"+"\nChoose your option (1/2/3/4): ")
    if option == "1":
        return change_email(username)
    elif option == "2":
        return change_username(username)
    elif option == "3":
        return change_password(username)
    elif option == "4":
        return menupage(username)
    else:
        clear_console()
        print("Invalid option. Please try again.")
        time.sleep(2)
        return settings(username)
def change_email(username):
    clear_console()
    new_email = input("=" * 80 + "\n" + f"{'CHANGE EMAIL':^80}" + "\n" + "=" * 80 + "\n" + "Write 'exit' to go back\n\nEnter your new email: ").lower()
    if not new_email:
        clear_console()
        print("="*80 + "\n\n\n\n" + "Email cannot be empty. Please try again.\n\n\n\n" + "="*80)
        time.sleep(2)
        return change_email(username)
    if escape in new_email:
        clear_console()
        return settings(username)
    if "@" not in new_email or "." not in new_email:
        clear_console()
        print("="*80 + "\n\n\n\n" + "Invalid email format. Please try again.\n\n\n\n" + "="*80)
        time.sleep(2)
        return change_email(username)
    for user in data_user:
        if user[2] == new_email:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Email already exists\n\n\n\n" + "="*80)
            time.sleep(2)
            return change_email(username)
    for user in data_user:
        if user[0] == username:
            user[2] = new_email
            clear_console()
            print("="*80 + "\n\n\n\n" + "Email updated successfully\n\n\n\n" + "="*80)
            time.sleep(2)
            return settings(username)
    clear_console()
    print("="*80 + "\n\n\n\n" + "User not found. Please try again.\n\n\n\n" + "="*80)
    time.sleep(2)
    return settings(username)
def change_username(username):
    clear_console()
    new_username = input("=" * 80+"\n"+f"{'CHANGE USERNAME':^80}"+"\n"+"=" * 80+"\n"+"Write 'exit' to go back\n\nEnter your new username: ").lower()
    if escape in new_username:
        clear_console()
        return settings(username)
    for user in data_user:
        if new_username in data_user:
            clear_console()
            print("="*80 + "\n\n\n\n" + "Username already exists\n\n\n\n" + "="*80)
            time.sleep(2)
            return change_username(username)
        else:
            user[0] = new_username
            clear_console()
            print("="*80 + "\n\n\n\n" + "Username changed successfully\n\n\n\n" + "="*80)
            time.sleep(2)
            return settings(username)
def change_password(username):
    clear_console()
    print("=" * 80+"\n"+f"{'CHANGE PASSWORD':^80}"+"\n"+"=" * 80+"\n"+"Write 'exit' to go back\n\n")
    new_password = pwinput.pwinput(prompt="Enter your new password: ", mask="*").lower()
    if escape in new_password:
        clear_console()
        return settings(username)
    for user in data_user:
        user[1] = new_password
        clear_console()
        print("="*80 + "\n\n\n\n" + "Password changed successfully\n\n\n\n" + "="*80)
        time.sleep(2)
        return settings(username)
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
username = "guest"
while True:
    loading()
    username = homepage(username)
    menupage(username)