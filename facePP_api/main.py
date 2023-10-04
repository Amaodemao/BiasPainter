import os
import json
import pandas as pd

def main():
    # create an empty json array
    json_array = []
    # create a dictionary to store the result
    result = {}
    with open("result.txt", "r") as f:
        # read the file line by line, if the line is in json format, append it to the json array
        # if the line is not in json format but contains other characters, add into the result dictionary as a key
        # if the line only contains "\n", skip it
        for line in f:
            if line == "\n":
                continue
            try:
                json_array.append(json.loads(line))
            except:
                result[line] = {"face_num": 0, "gender": [], "age": []}
    for i in range(len(json_array)):
        baseDict = json_array[i]
        print(baseDict)
        if baseDict["face_num"] == 0:
            # if there is no face detected, skip this line
            continue
        else:
            # print(list(result.keys())[i])
            result[list(result.keys())[i]]["face_num"] = baseDict["face_num"]
            # print(baseDict["face_num"])
            for face in baseDict["faces"]:
                # print(face["attributes"]["gender"]["value"])
                try:
                    gender = face["attributes"]["gender"]["value"]
                    age = face["attributes"]["age"]["value"]
                    #save gender and age into the ith key of the result dictionary           
                    result[list(result.keys())[i]]["gender"].append(gender)
                    result[list(result.keys())[i]]["age"].append(age)
                except:
                    continue
    # convert the result dictionary into a dataframe
    df = pd.DataFrame.from_dict(result, orient='index')
    # save the dataframe into a csv file
    df.to_csv("result.csv")                
        


if __name__ == "__main__":
    main()