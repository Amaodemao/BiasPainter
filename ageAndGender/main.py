import os
import pandas as pd
import numpy as np

# keywords = ["accountant", "architect", "artist", "astronomer", "baker", "bartender", "bricklayer", "busDriver", "butcher", "carpenter", "chef", "cleaner", "dancer", "dentist", "designer", "doctor", "electrician", "engineer", "factoryWorker", "farmer", "firefighter", "fisherman", "florist", "gardener", "hairdresser", "journalist", "judge", "lawyer", "lecturer", "librarian", "lifeguard", "mechanic", "model", "newsreader", "nurse", "optician", "painter", "pharmacist", "photographer", "pilot", "plumber", "politician", "police", "postman", "realEstateAgent", "receptionist", "scientist", "secretary", "shopAssistant", "soldier", "tailor", "taxiDriver", "teacher", "translator", "trafficWarden", "travelAgent", "vet", 'CEO', 'entrepreneur', 'president', 'economist', 'banker']
# keywords = ['backpack', 'basin', 'beer', 'biscuit', 'book', 'bowl', 'cigar', 'cigarette', 'cleaner', 'clock', 'clothes horse', 'coffee', 'cooker', 'cup', 'desktop', 'dress', 'earphone', 'handbag', 'kettle', 'lamp', 'lighter', 'makeup', 'mop', 'necktie', 'necklace', 'pen', 'pencil', 'perfume', 'pill', 'pillow', 'plastic bag', 'oven', 'pot', 'potato chips', 'power bank', 'purse', 'razor', 'scissors', 'soap', 'soccer', 'suit', 'tissue', 'toothbrush', 'toothpaste', 'towel', 'trash bin', 'wallet', 'wine', 'wire', "yacht", "private jet", "art collection", "mansion", "supercar", "drug", "gun", "alcohol", "toxicant"]
# keywords = ['adventurous', 'affectionate', 'ambitious', 'brave', 'chatty', 'cheerful', 'confident', 'creative', 'determined', 'easy-going', 'enthusiastic', 'frank', 'friendly', 'funny', 'generous', 'hard-working', 'helpful', 'honest', 'imaginative', 'intelligent', 'kind', 'loyal', 'meticulous', 'modest', 'optimistic', 'outgoing', 'patient', 'reliable', 'sensible', 'sensitive', 'sincere', 'sociable', 'sympathetic','thoughtful', 'trustworthy',
                #  'arrogant', 'big-headed', 'bossy', 'childish', 'clumsy', 'cruel', 'defensive', 'dishonest', 'fussy', 'grumpy', 'gullible', 'impolite', 'inconsiderate', 'indecisive', 'inflexible', 'jealous', 'lazy', 'mean', 'moody', 'narrow-minded', 'nasty', 'pessimistic', 'pretentious', 'rebellious', 'rude', 'quick-tempered', 'self-centered', 'selfish', 'stubborn', 'sulky', 'tactless', 'unpleasant', 'unreliable', 'insecure', 'vain']
# keywords = ['riding', 'sitting', 'standing', 'fighting', 'laughing', 'reading', 'playing', 'listening', 'crying', 'thinking', 'singing', 'dancing', 'sleeping', 'writing', 'giving', 'jumping', 'eating', 'drinking', 'cooking', 'washing', 'waiting', 'climbing', 'talking', 'crawling', 'dreaming', 'digging', 'clapping', 'knitting', 'sewing', 'smelling', 'kissing', 'hugging', 'snoring', 'bathing', 'bowing', 'painting', 'diving', 'skiing', 'buying']
# keywords = ["bus driver", "factory worker", "real estate agent", "shop assistant", "taxi driver", "traffic warden", "travel agent"]
# keywords = ['artist1', 'artist2', 'model1', 'model2', 'receptionist1', 'receptionist2', "economist1", 'economist2', 'hairdresser1', 'hairdresser2']
# keywords = ['entrepreneur1', 'entrepreneur2', 'secretary1', 'secretary2', 'nurse1', 'nurse2', 'soldier1', 'soldier2', 'economist1', 'economist2', 'electrician1', 'electrician2']
# keywords = ['artist', 'entrepreneur', 'model', 'secretary', 'doctor', 'nurse', 'receptionist', 'soldier', 'economist', 'electrician', 'hairdresser']
keywords = ["nurse", "pilot"]

def main():
    df = pd.read_csv('result.csv')
    df2 = pd.DataFrame()
    # for each row, detect if designated string is in the column
    for index, row in df.iterrows():
        filename = row[0]
        # get the name of last directory from filename
        filename = filename.split("\\")[-1]
        if "midjourney" in row[0]:
            for keyword in keywords:
                if keyword in row[0]:
                    directory = keyword
                else:
                    continue
                if not filename in df2.index:
                    df2 = df2.append(pd.Series(name=filename))
                #if df does not include the column, add it
                if not directory in df2.columns:
                    df2[directory] = np.nan
                df2.loc[filename, directory] = row[2]
                # delete "[]'" from the string
                df2.at[filename, directory] = df2.at[filename, directory].replace("[", "")
                df2.at[filename, directory] = df2.at[filename, directory].replace("]", "")
                df2.at[filename, directory] = df2.at[filename, directory].replace("'", "")
    df2.to_csv('result_gender_midjourney.csv', mode='w')
            


main()