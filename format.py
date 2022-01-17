import json
finaldata = []

with open("unformatted.txt", "r",encoding="utf-8") as filestream:
    for line in filestream:
        currentline = line.split(":")
        phonenum = currentline[0]
        fbid = currentline[1]
        name = currentline[2]
        surname = currentline[3]
        sex = currentline[4]
        extra = currentline[5] + currentline[6] # remove if error is thrown
        
        data = {
                    "phonenum":phonenum,
                    "fbid":fbid,
                    "name":name,
                    "surname":surname,
                    "sex":sex,
                    "extra":extra
                    }
                    
            
        finaldata.append(data)
        


### this formats the json data and saves it to a new file
with open("formatted.txt", 'w') as json_file:
    json.dump(finaldata, json_file, 
                        indent=4,  
                        separators=(',',': '))