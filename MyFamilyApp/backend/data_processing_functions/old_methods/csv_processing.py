import csv,os
VIEW_PY_DIRECTORY = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def load_data_from_csv(csv_fileName="BansawaliDatas.csv"):
    csv_loaded_datas=[] #ALL DATA LOADED FROM CSV
    csvLoaded_data_dic={} #ALL DATA STRUCTED IN INDIVIDUAL PERSON DICTONARY
    
    #Code to load data from csv and append in array
    with open(os.path.join(VIEW_PY_DIRECTORY,'Data_Files',csv_fileName)) as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=",")
        line_count=0 
        for row in csv_reader:
            if (row[0].isdigit()):
                csv_loaded_datas.append(row)
                line_count+=1
            else :
                if (line_count>0): #In line_count=0 header is there
                    csv_loaded_datas[len(csv_loaded_datas)-1].append(row)
    
    #Code to loop each data in 'csv_loaded_datas' array and structure individual person data in a dictonary
    for person_data in csv_loaded_datas:
        #Data columns that is the each header column in excel/csv
        data_columns=['PK','Name','Spouse','Pusta Number','Fathers PK','Child Name','Child Gender','Child PK','Remark','Primary Contact Number','Secondary Contact Number']
        no_of_data_column=len(data_columns)
        
        childrens=[]
        spouses=[person_data[3]]

        first_child={
            'child_pk':person_data[8],
            'gender':person_data[7],
            'name':person_data[6],
            'child_comment':person_data[9]
        }
        '''
        Condition to display data in children field in case of daughter child and in case of son with no child
        '''
        #Condition to display if daughter have no child
        if(not(first_child) and '#' in person_data[8]):
            if {'comment':"Gautam Batch End",'comment1':"No Child"} not in childrens:
                childrens.append({'comment':"Gautam Batch End",'comment1':"No Child"})
        if((first_child) and '#' in person_data[8] and (person_data[7]=='')):
            if {'comment':"Gautam Batch End",'comment1':"No Child"} not in childrens:
                childrens.append({'comment':"Gautam Batch End",'comment1':"No Child"})
        #Condition to display if daughter have child
        if((first_child) and '#' in person_data[8] and not(person_data[7]=='')):
            if {'comment':"Gautam Batch End",'comment1':"and childrens are : "} not in childrens:
                childrens.append({'comment':"Gautam Batch End",'comment1':"and childrens are : "})   

        #Condition to display if son have no child
        if(not(first_child) and person_data[8]=='' or person_data[8]==None and not('#' in person_data[8])):  
            if {'comment1':"No Child"} not in childrens:
                childrens.append({'comment1':"No Child"})    
        if((first_child) and (person_data[8]=='' or person_data[8]==None) and (person_data[7]=='') and not('#' in person_data[8])):
            if {'comment1':"No Child"} not in childrens:
                childrens.append({'comment1':"No Child"})

        childrens.append(first_child)       
        
        '''
        Upto now only the first child is appended , the below code structures in our format and appends every other child in our data
        '''
        
        if(len(person_data)>no_of_data_column):
            extra_childrens=len(person_data)-no_of_data_column
            for i in range(1,extra_childrens):
                child={
                    'child_pk':person_data[(no_of_data_column)+i][8],
                    'gender':person_data[(no_of_data_column)+i][7],
                    'name':person_data[(no_of_data_column)+i][6],
                    'child_comment':person_data[(no_of_data_column)+i][9]
                }
                childrens.append(child)
        
        #Individual person Dictonary
        person={
            'person_id':person_data[0],
            'name':person_data[1],
            'gender':person_data[2],
            'spouses':spouses,
            'batch_no':person_data[4],
            'father_pk':person_data[5],
            'childrens':childrens,
            'comments':person_data[9],
            'contact_numbers':person_data[10],
            'email':person_data[11]
        }
        csvLoaded_data_dic.update({person_data[0]:person})

    return csvLoaded_data_dic
