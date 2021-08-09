import csv
from csv import DictWriter
from tempfile import NamedTemporaryFile
import csv
from itertools import zip_longest
import check_repeat_names

def get_names(original_dict):
    """
    Original:
    {Person: {Credit Type: [Tracks]}}
    """
    # Get all the names
    return original_dict.keys()



def print_name_with_type_and_works(new_dict):
    people = new_dict[0]
    credits = new_dict[1]
    
    # old_names = []
    # old_credits = []
    # try:
    try:
        with open('engineers.csv', mode='a') as read_obj:
            # pass the file object to reader() to get the reader object
            writer = csv.DictWriter(read_obj, fieldnames=['Name', 'Credits'])

            for (person,credit) in zip(people, credits):
                write_row_dict = {}
                write_row_dict['Name'] = person
                write_row_dict['Credits'] = credit

                writer.writerow(write_row_dict)

    except:
        with open('engineers.csv', mode='w') as read_obj:
            # pass the file object to reader() to get the reader object
            writer = csv.DictWriter(read_obj, fieldnames=['Name', 'Credits'])
            writer.writeheader()

            for (person,credit) in zip(people, credits):
                write_row_dict = {}
                write_row_dict['Name'] = person
                write_row_dict['Credits'] = credit

                writer.writerow(write_row_dict)




def check_final():
    with open('engineers.csv', newline='') as read_obj:
        # pass the file object to reader() to get the reader object
        reader = csv.DictReader(read_obj)

        names = []
        albums = []
        for row in reader:
            names.append(row['Name'])
            albums.append(row['Credits'])
        
        check_repeat_names.check_repeats(names, albums)

                # print(row)
            # get total number of rows
            # print("Total no. of rows: %d"%(csv_reader.line_num))
            # print(rows)

            # for row in rows[1:]:
            #     old_names.append(row[0])
            #     old_credits.append(row[1])
    # except FileNotFoundError:
    #     print("couldn't read")


    # data = [old_names, old_credits]

    # for new_name in new_names:
    #     if new_name in data[0]:
    #         for i in range(len(data[0])):
    #             if new_name == data[0][i]:
    #                 data[1][i].append(new_dict[new_name])
    #     else:
    #         data[0].append(new_name)
    #         data[1].append(new_dict[new_name])


    # new_names.insert(0, 'Name')
    # new_credits.insert(0, 'Credits')
    

    




    # export_data = zip_longest(*data, fillvalue='')
    # with open('engineers.csv', 'w', newline='') as myfile:
    #   wr = csv.writer(myfile)
    #   wr.writerows(export_data)
    # myfile.close()
    

    
    
    
    # dict_name_to_info = {}
    # for (old_name, credits, tracks) in zip(got_names, got_credits, got_tracks):
    #     dict_name_to_info[old_name] = {'Credit Types': credits, 'Tracks': tracks}


    # # try:
    
    # print(new_dict.keys())

    # new_names = new_dict.keys()

    # for name in new_names:
    #     if name in dict_name_to_info.keys():
    #         old_credits_and_tracks = dict_name_to_info[name]
    #         old_credits = old_credits_and_tracks['Credit Types']
    #         old_tracks = old_credits_and_tracks['Tracks']

    #         for credit in old_credits:
    #             print(new_dict[name].keys())
    #             if credit not in new_dict[name].keys(): # these are the new credits for a person we already have
    #                 new_credit_type = credit
    #                 new_dict[name]['Credit Types'].append(credit)
    #         for track in old_tracks:
    #             if track not in new_dict[name]['Tracks']: # these are the new credits for a person we already have
    #                 new_dict[name]['Tracks'].append(track)
    #     else:
    #         new_credits = new_dict[name].keys() # in a keys list
    #         tracks_for_person = []
    #         credits_for_person = []
    #         for credit_type in new_credits:
    #             tracks_for_credit = new_dict[name][credit_type] # in a list
    #             for track in tracks_for_credit:
    #                 # If it isn't a duplicate
    #                 if track not in tracks_for_person:
    #                     tracks_for_person.append(track)
    #             # If it isn't a duplicate
    #             if credit_type not in credits_for_person:
    #                 credits_for_person.append(credit_type)
    #         dict_name_to_info[name] = {'Credit Types': credits_for_person, 'Tracks': tracks_for_person}
    #         # {Name: {Credit Types: ..., Tracks: ...}}
    
    # get_all_names = []
    # get_all_credits = []
    # get_all_tracks = []
    # for all_name in dict_name_to_info.keys():
    #     get_all_names.append(all_name)
    #     get_all_credits.append(dict_name_to_info[all_name]['Credit Types']) 
    #     get_all_tracks.append(dict_name_to_info[all_name]['Tracks']) 

    # # Get a list of all ISRC values we've already checked
    # # names = new_dict.keys()
    # # got_names = []
    # # got_credits = []
    # # got_tracks = []
    # # open file in read mode
    

    # # name_counter = 0
    # # for name in names:
    # #     credit_types = []
    # #     tracks = []
    # #     credits_to_sort = new_dict[name].keys()
    # #     for credit in credits_to_sort:
    # #         credit_types.append(credit)
    # #         temp_tracks = new_dict[name][credit]
    # #         for track in temp_tracks:
    # #             tracks.append(track)
    # #     new_and_old_dict['Name'].append(name)
    # #     # Check if the songs from the playlist are already in this CSV File 
    # #     if name not in got_names:
    # #         new_and_old_dict['Credit Types'].append(credit_types)
    # #         new_and_old_dict['Tracks'].append(tracks)
    # #         new_and_old_dict['Amount of Tracks'].append(len(tracks))
    # #     else: 
    # #         for past_credit in got_credits[name_counter]:
    # #             if past_credit not in credit_types:
    # #                 credit_types.append(past_credit)
    # #                 for past_track in new_dict[name][past_credit]:
    # #                     if past_track not in tracks:
    # #                         tracks.append(past_track)

    # #     new_and_old_dict[name] = [credit_types, tracks]
        
    # #     name_counter += 1

    # # # except FileNotFoundError:



    # new_and_old_dict = {'Name': get_all_names, 'Credit Types': get_all_credits, 'Tracks': get_all_tracks, 'Amount of Tracks': []}
    # for tracks in get_all_tracks:
    #     new_and_old_dict['Amount of Tracks'].append(len(tracks))
    # with open('engineers.csv', 'w', newline='') as file:
    #     fieldnames = ['Name', 'Credit Types', 'Tracks', 'Amount of Tracks']
            
    #     writer = csv.DictWriter(file, fieldnames=fieldnames)
    #     writer.writeheader()

    #     all_names = new_and_old_dict['Name']
    #     all_credits = new_and_old_dict['Credit Types']
    #     all_tracks = new_and_old_dict['Tracks']
    #     all_amounts = new_and_old_dict['Amount of Tracks']

    #     for (name, credits, tracks, amount) in zip(all_names, all_credits, all_tracks, all_amounts):
    #         row_to_write = {}
    #         row_to_write['Name'] = name
    #         row_to_write['Credit Types'] = credits
    #         row_to_write['Tracks'] = tracks
    #         row_to_write['Amount of Tracks'] = amount

    #         writer.writerow(row_to_write)



            