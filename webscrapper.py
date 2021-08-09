# Format of the webplayer link (for playlist):
# https://open.spotify.com/playlist/{PLAYLIST_ID}
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


import csv_writer
# from WebScraperForAllMusic import parserForInformation


master_dict = {}

def getEngineers():
    """
    
    """
    # Open webdriver


    playlist_link = input("Please input the Album URL from Jaxsta... ")



    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Initialize what we'll return
    songwriters = []
    producers = []


    # Go to the Spotify Playlist link in the Web Player
    browser.get(playlist_link)
    # Maximize the window
    browser.maximize_window()
    # Give it time just in case
    time.sleep(3)
    time_counter = 0
    # Get a list of all Songwriters and Producers by
    # Going through each song...
    track_to_name = {}
    try:
        for song_number in range(1, 50):
            temp_track = browser.find_element_by_xpath(f"//section[@class = '_content_v2a3yb']/div[1]/div/div[{song_number}]/h2").text
            track_to_name[song_number] = temp_track
    except selenium.common.exceptions.NoSuchElementException:
        print("done")
        print(track_to_name)

    type_to_person = {}
    people_to_credit = []
    tracks = []

    album = browser.find_element_by_xpath(f"//div[@class = '_info_aisfd5']/h1").text
    artist = browser.find_element_by_xpath(f"//span[@class = '_oxford-item_47qd1x']/a").text
    credit_types = []
    try:
        for credit_section in range(1, 15):
            temp_credit = browser.find_element_by_xpath(f"//div[@class = '_group-item_18llld ember-view'][{credit_section}]/h4").text
            if temp_credit == "Engineers":
                try:
                    for credits in range(1, 50):
                        credit_type = browser.find_element_by_xpath(f"//div[@class = '_group-item_18llld ember-view'][{credit_section}]/div[2]/div[{credits}]/div[1]").text
                        if credit_type not in credit_types:
                            credit_type.append(credit_types)
                        for person_number in range(1, 50):
                            try:
                                person_to_credit = browser.find_element_by_xpath(f"//div[@class = '_group-item_18llld ember-view'][{credit_section}]/div[2]/div[{credits}]/div[2]/div[{person_number}]/a").text
                                print(person_to_credit)
                                tracks_section = browser.find_element_by_xpath(f"//div[@class = '_group-item_18llld ember-view'][{credit_section}]/div[2]/div[{credits}]/div[2]/div[{person_number}]/span").text
                                tracks_to_credit = tracks_section.split("Tracks: ")[1].split(",")
                                # tracks_string = ""
                                # first = True
                                # for track in tracks_to_credit:
                                #         if first:
                                #             tracks_string += track    
                                #             first = False
                                #         else:
                                #             tracks_string += f", {track}"
                                if person_to_credit not in people_to_credit:
                                    people_to_credit.append(person_to_credit)
                                    tracks.append(album)
                                # tracks.append(tracks_string +  ' on ' + album + f" ({credit_type})")
                                # tracks.append(str(len(tracks_to_credit)) +  ' songs on ' + album + f" (by {artist}) as {credit_type}")
                            except selenium.common.exceptions.NoSuchElementException:
                                pass
                except selenium.common.exceptions.NoSuchElementException:
                    print("Got credits")
    except selenium.common.exceptions.NoSuchElementException:
        print("done")
    
    print(credit_types)
    return [people_to_credit, tracks]
    

# print(getEngineers())
# csv_writer.print_name_with_type_and_works(getEngineers())

print(csv_writer.check_final())
