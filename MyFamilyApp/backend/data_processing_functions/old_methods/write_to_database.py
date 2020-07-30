from MyFamilyApp.backend.models import Person
import re

unicode_to_digits_dic={
    'DIGIT ZERO':0,
    'DIGIT ONE':1,
    'DIGIT TWO':2,
    'DIGIT THREE':3,
    'DIGIT FOUR':4,
    'DIGIT FIVE':5,
    'DIGIT SIX':6,
    'DIGIT SEVEN':7,
    'DIGIT EIGHT':8,
    'DIGIT NINE':9
}

def write_to_database(givenData):
    count=1
    for key,value in givenData.items():
        person_id=[str(unicode_to_digits_dic[digit]) for digit in unicode_to_name(given_data=value['person_id'],numberdataTrigger=1)]
        person_id=int("".join(person_id))

        if(not(Person.objects.filter(person_id=person_id))):

            try:
                person=Person(same_vamsha=True)
                person.person_id=person_id
                person.full_name=value['name']
                if value['gender'] == "Male":
                    person.gender="M"
                    isFemale=False
                else:
                    person.gender="F"
                    isFemale=True
                spouses=value['spouses'][0]
                person.spouses=spouses
                batch_no=[str(unicode_to_digits_dic[digit]) for digit in unicode_to_name(given_data=value['batch_no'],numberdataTrigger=1)]
                batch_no=int("".join(batch_no))
                person.batch_no=batch_no
                
                try:
                    father_pk=[str(unicode_to_digits_dic[digit]) for digit in unicode_to_name(given_data=value['father_pk'],numberdataTrigger=1)]
                    father_pk=int("".join(father_pk))
                    father=Person.objects.get(person_id=father_pk)
                    person.father=father
                except Exception as e:pass

                person.remarks=value['comments']
                person.contact_number=value['contact_numbers']
                person.email=value['email']
                person.save()
                if(isFemale):
                    haveChild=create_daughther_children(person,value['childrens'])
                    if(not(haveChild)):
                        person.remarks="No Child"
                    person.save()
            except Exception as e: print(e);print(e.__class__)

        try:
            if((Person.objects.get(person_id=person_id))):
                try:
                    person=Person.objects.get(person_id=person_id)
                    person.update(full_name=value['name'])
                    spouses=value['spouses']

                    if value['gender'] == "Male":
                        isFemale=False
                    else:
                        isFemale=True

                    person.update(spouses=spouses)

                    person.update(batch_no=value['batch_no'])

                    father=None
                    try:
                        father_pk=[str(unicode_to_digits_dic[digit]) for digit in unicode_to_name(given_data=value['father_pk'],numberdataTrigger=1)]
                        father_pk=int("".join(father_pk)) 
                        father=Person.objects.get(person_id=father_pk)
                    except :pass

                    person.father=father
                    person.update(remarks=value['comments'])
                    person.update(contact_number=value['contact_numbers'])
                    person.update(email=value['email'])
                    if(isFemale):
                        haveChild=create_daughther_children(person,value['childrens'])
                        if(not(haveChild)):
                            person.update(remarks="No Child")
                
                except Exception as e: pass
        except Exception as e: pass

        print(f"Processed {count} datas out of {len(givenData)} items")
        count+=1

#Function to convert unicode to unicodename (for eg: 1 will be ['DIGIT ONE] and a will be ['SMALL LETTER A'])
def unicode_to_name(given_data=[],numberdataTrigger=0):
    import unicodedata
    final_data=[]
    try:
        data_with_DEVANAGARI=[unicodedata.name(result) for result in given_data]
        if(numberdataTrigger==1):
            data_name_with_splitted_DEVANAGAI=[re.split("DEVANAGARI\s",result) for result in data_with_DEVANAGARI]
            final_data=[result for i in data_name_with_splitted_DEVANAGAI for result in i if not(result=='')]
        else:
            unicode_symbols_list=["DEVANAGARI\s","LETTER\s","VOWEL\sSIGN\s","SIGN\s","LATIN\sSMALL\sLETTER\s","LATIN\sSMALL\s","LATIN\sCAPITAL\sLETTER\s","LATIN\sCAPITAL\s"]
            data_name_with_removed_DEVANAGARI=data_with_DEVANAGARI[::]
            for symbol in unicode_symbols_list:
                data_name_with_removed_DEVANAGARI=[re.sub(symbol,"",result) for result in data_name_with_removed_DEVANAGARI]
            final_data=data_name_with_removed_DEVANAGARI[::]
    except Exception as e:
        final_data=[unicodedata.name(result) for result in given_data]
    return final_data

#Function to write collected same bansa daughter childrens data in another database 
def create_daughther_children(mother,childrens):
    haveChild=False
    for child in childrens:
        try:
            a_child=Person(same_vamsha=False,person_id=0)
            if(not(child['name']=='' or child['name']==None) and not(child['gender']=='' or child['gender']==None)):                
                try:
                    a_child.name=child['name']
                    if child['gender'] == "Male":
                        a_child.gender="M"
                    else:
                        a_child.gender="F"
                    a_child.mother=mother
                    ChildFilteredContactNumbers=filter_phone_numbers(child['child_comment'])
                    if(not(ChildFilteredContactNumbers==False)):
                        if(len(ChildFilteredContactNumbers)==1):
                            a_child.primary_contact_number=ChildFilteredContactNumbers[0][0]
                        elif(len(ChildFilteredContactNumbers)==2):
                            a_child.primary_contact_number=ChildFilteredContactNumbers[0][0]
                            a_child.secondary_contact_number=ChildFilteredContactNumbers[1][0]
                        else:
                            pass                                                    
                    a_child.comment="Gautam Batch End"
                    a_child.save()
                    haveChild=True
                except Exception as e:pass
        except:pass

    return haveChild

#Function to filter phone numbers and arrange it in countrycode+phone number format from given data
def filter_phone_numbers(givenData):
    numberFound=False
    latestCountryCodeFound=None
    phoneNumbers=[]
    phoneNumberFound=False
    if(not(givenData=="" or givenData==None)):
        numbers=re.split("/",givenData)
        numberCount=1
        for a_number in numbers:
            if(not(latestCountryCodeFound==None)):
                if re.findall("[+]\d\d\d-",a_number)==[] and re.findall("[+]\d-",a_number)==[] and re.findall("[+]\d-",a_number)==[]:
                    phoneNumbers.append([latestCountryCodeFound+"-"+a_number])
                else:
                    phoneNumbers.append([a_number])
                numberCount+=1
            else:
                countryCodeFormats=["[+]\d\d\d-","[+]\d\d-","[+]\d-"]
                for ccf in countryCodeFormats:
                    cc="".join(re.findall(ccf,a_number))
                    if(not(cc==None or cc==[] or cc=="")):
                        cc=re.sub("[+]","[+]",cc)
                        phoneNumber=re.sub(cc,"",a_number)
                        cc=re.sub("[-]","",re.sub("\]","",re.sub("\[","",cc)))
                        phoneNumbers.append([cc+"-"+phoneNumber])
                        phoneNumberFound=True
                        latestCountryCodeFound=cc
                        numberCount+=1        
    return phoneNumbers if phoneNumberFound else False  