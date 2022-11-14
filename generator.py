import json


def Parser(file_name,pdf):
    with open (f"{file_name}.txt",'w') as f:
        for i in range(0,1):
            pageObj = pdf.getPage(i)

            try:
                txt = pageObj.extract_text()
            except:
                pass
            else:
                f.write(txt)
    f.close()

    file_path = '746860-1.txt'
    x = open(file_path)
    dict = {}
    data=''
    for i in x:
        if "Employer:" in i:
            str = i.split(' ')
            j = 1
            while(str[j]!="Claimant:"):
                data+= str[j]
                data +=" "
                j+=1 
            dict["Employer"] = data

        if "Claimant:" in i:
            data = ''
            str = i.split('\n')
            str1 = str[0].split(" ")
            pos = str1.index('Claimant:')+1
            for j in range (pos,len(str1)):
                data += str1[j]
                data += " "
            dict["Claimant"] = data

        if "Location:" in i :
            data = ''
            str = i.split(' ')
            j = 1
            while(str[j]!="Claim"):
                data+= str[j]
                data +=" "
                j+=1 
            dict["Location"] = data
        

        if "Claim -" in i :
            data = ''
            str = i.split('\n')
            str1 = str[0].split(" ")
            pos = str1.index('Claim')+2
            for j in range (pos,len(str1)):
                data += str1[j]
                data += " "
            dict["Claim"] = data

        if "Claim #:" in i:
            data = ''
            str = i.split(' ')
            j = 2
            while(str[j]!="Carrier:"):
                data+= str[j]
                data +=" " 
                j+=1
            dict["Claim "] = data

        if "Carrier:" in i :
            data = ''
            str = i.split('\n')
            str1 = str[0].split(" ")
            pos = str1.index('Carrier:')+1
            for j in range (pos,len(str1)):
                data += str1[j]
                data += " "
            dict["Carrier"] = data
        
        if "DOI:" in i:
            data = ''
            str = i.split(' ')
            j = 1
            while(str[j]!="Claims"):
                data+= str[j]
                data +=" " 
                j+=1
            dict["DOI"] = data

        if "Claims Examiner:" in i :
            data = ''
            str = i.split('\n')
            str1 = str[0].split(" ")
            pos = str1.index('Examiner:')+1
            for j in range (pos,len(str1)):
                data += str1[j]
                data += " "
            dict["Claims Examiner"] = data
        
        if "DOB:" in i:
            data = ''
            str = i.split(' ')
            j = 1
            while(str[j]!="Review"):
                data+= str[j]
                data +=" " 
                j+=1
            dict["DOB"] = data
        
        if "Review #:" in i :
            data = ''
            str = i.split('\n')
            str1 = str[0].split(" ")
            pos = str1.index('#:')+1
            for j in range (pos,len(str1)):
                data += str1[j]
                data += " "
            dict["Review"] = data

        if "Received Date:" in i:
            data = ''
            str = i.split(' ')
            j = 2
            while(str[j]!="TPA:"):
                data+= str[j]
                data +=" " 
                j+=1
            dict["Recieved Date"] = data  

        if "TPA:" in i :
            data = ''
            str = i.split('\n')
            str1 = str[0].split(" ")
            pos = str1.index('TPA:')+1
            data += " "
            dict["TPA"] = data

        if "Provider:" in i:
            data = ''
            str = i.split(' ')
            j = 1
            while(str[j]!="#"):
                data+= str[j]
                data +=" " 
                j+=1
            dict["Requesting"] = data

        if "Requests:" in i :
            data = ''
            str = i.split('\n')
            str1 = str[0].split(" ")
            pos = str1.index('Requests:')+1
            data += str1[pos]
            data += " "
            dict["Requests"] = data
        
        if "Phone: (" in i:
            data = ''
            str = i.split(' ')
            j = 1
            while(str[j]!="Jurisdiction:"):
                data+= str[j]
                data +=" " 
                j+=1
            dict["Phone"] = data
        
        if "Jurisdiction:" in i :
            data = ''
            str = i.split('\n')
            str1 = str[0].split(" ")
            pos = str1.index('Jurisdiction:')+1
            data += str1[pos]
            data += " "
            dict["Jurisdiction"] = data

        if "Specialty:" in i:
            data = ''
            str = i.split(' ')
            j = 1
            while(str[j]!="Review"):
                data+= str[j]
                data +=" " 
                j+=1
            dict["Specialty"] = data

        if "Level:" in i :
            data = ''
            str = i.split('\n')
            str1 = str[0].split(" ")
            pos = str1.index('Level:')+1
            for j in range (pos,len(str1)):
                data += str1[j]
                data += " "
            dict["Review Level"] = data

        if "Review Type:" in i:
            data = ''
            str1 = i.split('\n')
            str = str1[0].split(" ")
            j = 1
            while(str[j]!="UR"):
                data+= str[j]
                data +=" " 
                j+=1
            data+=str[j]
            dict["Review Type"] = data



    with open(f"{file_name}.json","w") as f:
        json_data = json.dumps(dict,indent=4)
        f.write(json_data)