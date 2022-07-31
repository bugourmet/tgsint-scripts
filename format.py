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
        location = currentline[5]
        extra = ' '.join(str(x) for x in currentline[6:9]) 
        data = {
                    "phonenum":phonenum,
                    "fbid":fbid,
                    "name":name,
                    "surname":surname,
                    "sex":sex,
                    "location":location,
                    "extra":extra
                    }
                    
            
        finaldata.append(data)
        
with open("formatted.txt", 'w') as json_file:
    json.dump(finaldata, json_file, 
                        indent=4,  
                        separators=(',',': '))