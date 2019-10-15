# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:36:41 2019

@author: Amzad - derived from Version1
"""

def compute_prefix(pattern):
    pattern_length = len(pattern)
    prefix = {
        0 : 0
    }
    
    for index in range(1,pattern_length):
        k = prefix[index-1]
        while k>0 and pattern[index] != pattern[k]:
            k = prefix[k-1]
        if pattern[index] == pattern[k]:
            k = k+1
        prefix[index] = k

    return prefix


def kmp_matcher(string,pattern):
    prefix = compute_prefix(pattern)
    string_length = len(string)
    pattern_length = len(pattern)
    #print(string_length,pattern_length,string,pattern)

    found_at_indices = []
    index = 0
    q = 0

    dna = {
        'a' : 't',
        't' : 'a',
        'g' : 'c',
        'c' : 'g'
    }
    
    while index < string_length:
        #print(pattern[q])
        if dna[pattern[q]] == string[index]:
            q = q+1
            index = index + 1
        if q == pattern_length:
            found_at_indices.append(index-pattern_length)
            q = prefix[q-1]
        elif index < string_length and dna[pattern[q]] != string[index]:
            if q != 0:
                q = prefix[q-1] 
            else:
                index = index + 1

    return found_at_indices

#This Function get a Pattern String and result all possible substring for it.
def get_substring_indices(pattern):
    end_index = len(pattern) - 1
    return { pattern[j:j+i+1] : {'start' : j, 'end' : j+i} for i in range(end_index,-1,-1) for j in range(0,end_index+1) if j+i <= end_index and i+2>6 }

def combinationTry(filterdata,list_dict_Pattern_indices):
    print("Start ", filterdata, "  ", list_dict_Pattern_indices)
    combinationlist = []
    notfilterYet = []
    #notfilter_dict_pattern=[]
    global count_filter
    global initialCountFilterMember
    if count_filter == 0:
        initialCountFilterMember = len(filterdata)
    print("Start initialCountFilterMember ", initialCountFilterMember)
#    global combination_after_filter
#    combination_after_filter = []
    
#    dict_pattern_list = []
#    for key,value in dict_Pattern_indices.items():
#        dict_pattern_list.append([key,value])
#    
#    print("List version of dictPatternindices ", dict_pattern_list)
    
    if len(filterdata) > 0 and count_filter < initialCountFilterMember:        
         # Start Index of a String, String, Start index of that in a Pattern
        
        k = 0
        j = 1
        l = 0
        m = 1
        
        count_filter += 1
        
        
        while k < len(filterdata) and j < len(filterdata): 
            print("starting k", k, "j", j, "l", l, "m", m)
            if filterdata[k][0] == list_dict_Pattern_indices[l][0]:
                #Test to see the first item will get added as a pattern      
                oneMatch = True
                SLI = filterdata[k][1] + len(filterdata[k][0]) - 1 # 6
                print("SLI when k ", SLI, k)
                PLI = list_dict_Pattern_indices[l][1][0] + len(list_dict_Pattern_indices[l][0]) - 1 # 15
                print("PLI when l ", PLI, l)
                nextSLS =  filterdata[j][1] # 9
                print("nextSLS when j ", nextSLS, j)
                #print("nextSLS when j SLI ", nextSLS, j, SLI  )
                if nextSLS > SLI: # jodi boro hoi tahole search the pattern in list dict
                    KeepGoing = True
                    while KeepGoing:                        
                        if list_dict_Pattern_indices[m][0] == filterdata[j][0]: # ttgctagca # ttgctagca
                            print("When EQ ",list_dict_Pattern_indices[m][0], filterdata[j][0], "m ", m, "j ", j)
                            SLI = filterdata[k][1] + len(filterdata[k][0]) - 1
                            nextSLS =  filterdata[j][1]                            
                            PLI = list_dict_Pattern_indices[l][1][0] + len(list_dict_Pattern_indices[l][0]) - 1
                            nextPLS =  list_dict_Pattern_indices[m][1][0] #30
                            print("when EQ SLI nextSLS PLI nextPLS", SLI, nextSLS, PLI, nextPLS)
                            if nextPLS > PLI: 
                                print("difference ", nextSLS - SLI, nextPLS - PLI)
                                if nextSLS - SLI == nextPLS - PLI:  # 3 4  
                                    print("elif nextPLS nextSLS - SLI == nextPLS - PLI ", nextPLS, PLI)
                                    print("elif nextSLS nextSLS - SLI == nextPLS - PLI ", nextSLS, SLI)
                                    
                                    if len(filter_match)>0:
                                        duplicate = 0
                                        while duplicate < len(filter_match):
                                            if filter_match[duplicate][0] == filterdata[k][1]:
                                                filter_match.append([filterdata[j][1],filterdata[j][0],list_dict_Pattern_indices[m][1][0]])
                                                combinationlist.append(filterdata[j][1])
                                                break
                                            else:
                                                if duplicate == len(filter_match):
                                                    filter_match.append([filterdata[k][1],filterdata[k][0],list_dict_Pattern_indices[l][1][0]])
                                                    filter_match.append([filterdata[j][1],filterdata[j][0],list_dict_Pattern_indices[m][1][0]])
                                                    combinationlist.append(filterdata[k][1])
                                                    combinationlist.append(filterdata[j][1])
                                                else:
                                                    duplicate += 1                                                
                                    else:
                                        filter_match.append([filterdata[k][1],filterdata[k][0],list_dict_Pattern_indices[l][1][0]])
                                        filter_match.append([filterdata[j][1],filterdata[j][0],list_dict_Pattern_indices[m][1][0]])
                                        combinationlist.append(filterdata[k][1])
                                        combinationlist.append(filterdata[j][1])                                                
                                    
                                    
                                    print("When Match in k",k, "j", j, "l",l,"m",m )
                                    k = j
                                    j += 1
                                    l = m
                                    m += 1                                    
                                    print("When Match after update in k",k, "j",j, "l",l,"m",m )
                                    break
                                elif nextSLS - SLI < nextPLS - PLI:
                                    print("elif nextPLS nextSLS - SLI < nextPLS - PLI ", nextPLS, PLI)
                                    print("elif nextSLS nextSLS - SLI < nextPLS - PLI ", nextSLS, SLI)
                                    if m == len(list_dict_Pattern_indices) - 1:
                                        print("I am here adding the non match ", m )
                                        notfilterYet.append(filterdata[j])
                                        print("Not Filter Adding ",filterdata[j] )
                                        j += 1                                        
                                        m = l + 1
                                    else:
                                        print("Not Filter Adding ",filterdata[j] )
                                        notfilterYet.append(filterdata[j])
                                        j += 1                                        
                                        m = l + 1
                                        
                                else:
                                    print("elif nextPLS nextSLS - SLI > nextPLS - PLI ", nextPLS, PLI)
                                    print("elif nextSLS nextSLS - SLI > nextPLS - PLI ", nextSLS, SLI)
                                    if m == len(list_dict_Pattern_indices) - 1:
                                        print("I am here adding the non match ", m )
                                        print("Not Filter Adding ",filterdata[j] )
                                        notfilterYet.append(filterdata[j])
                                        j += 1
                                        m = l + 1
                                    else:
                                        
                                        m += 1
                            else:
                                print("when EQ but nextPLS not > PLI :  SLI nextSLS PLI nextPLS", SLI, nextSLS, PLI, nextPLS)
                                if m == len(list_dict_Pattern_indices) - 1:
                                    print("Not Filter Adding ",filterdata[j] )
                                    notfilterYet.append(filterdata[j])
                                    j += 1
                                    if j == len(filterdata) - 1:
                                        notfilterYet.append(filterdata[j])                                    
                                    KeepGoing = False
                                else:
                                    m += 1
                                    print("As EQ but nextPLS not > PLI incremented m", m)
                        else:
                            print("If string NE: ",list_dict_Pattern_indices[m][0], filterdata[j][0], "m ", m, "j ", j)
                            print("nextSLS when not match nextSLS SLI PLI", nextSLS, SLI, PLI)                         
                            if m == len(list_dict_Pattern_indices) - 1:
                                notfilterYet.append(filterdata[j])
                                print("Not Filter Adding ",filterdata[j] )
                                j += 1
                                if j == len(filterdata) - 1:
                                     notfilterYet.append(filterdata[j])
                                    
                                KeepGoing = False
                            else:                            
                                m += 1
                
                else:
                    print("Not Filter Adding as nextSLS < SLI",filterdata[j] )
                    notfilterYet.append(filterdata[j])
                    j += 1
                    #print("Not Filter Adding ", j )
                if oneMatch and m == len(list_dict_Pattern_indices)-1:
                    filter_match.append([filterdata[k][1],filterdata[k][0],list_dict_Pattern_indices[l][1][0]])
                    combinationlist.append(filterdata[k][1])
                    for i in range(len(notfilterYet)):
                        if notfilterYet[i][0] == filterdata[k][0]:
                            if notfilterYet[i][1]== filterdata[k][1]:
                                print("in loooooop ",notfilterYet[i][0], notfilterYet[i][1])
                                notfilterYet.pop(i)
                                break
                    break
            else:                
                l += 1
                m += 1
        if len(combinationlist) > 0:
            count_filter += len(combinationlist)
    #print("combinationlist ", combinationlist)
    
    #print("notfilter_dict_pattern ", notfilter_dict_pattern)
    print("filter_match ",filter_match)
    if len(combinationlist) > 0:
        combination_after_filter.append(combinationlist)
    print("combination_after_filter", combination_after_filter)
    print("notfilterYet ", notfilterYet )
    print("list_dict_Pattern_indices ",list_dict_Pattern_indices)
    temp = 0
    tempDict = 0
    while temp < (len(filter_match)):
        #print("temp", temp, "tempDict", tempDict)
        #print(filter_match[temp][1],list_dict_Pattern_indices[tempDict][0],filter_match[temp][2], list_dict_Pattern_indices[tempDict][1][0])
        if filter_match[temp][1] in [list_dict_Pattern_indices[j][0] for j in range(len(list_dict_Pattern_indices))]:
#            print(filter_match[temp][1],list_dict_Pattern_indices[tempDict][0],filter_match[temp][2], list_dict_Pattern_indices[tempDict][1][0])
#            print("temp", temp, "tempDict", tempDict)
            if filter_match[temp][1] == list_dict_Pattern_indices[tempDict][0] and filter_match[temp][2] == list_dict_Pattern_indices[tempDict][1][0]:
                list_dict_Pattern_indices.pop(tempDict)
                temp += 1
                tempDict = 0
            else:
                if tempDict < len(list_dict_Pattern_indices) - 1:
                    tempDict += 1
                else:
                    temp += 1
        else:
            temp += 1
    
    
#    print("After cleaning the data ", list_dict_Pattern_indices )    
#                
#    print("Current count_filter ", count_filter)
#    
#    print("End initialCountFilterMember ", initialCountFilterMember)
#    if count_filter == initialCountFilterMember - 1:
#        count_filter = 0
#        combinationTry(notfilterYet,list_dict_Pattern_indices)
#    else:
#        combinationTry(notfilterYet,list_dict_Pattern_indices)
    if len(filterdata)>0:
        combinationTry(notfilterYet,list_dict_Pattern_indices)
    


#def display(combination_value,filtered_match_map,string,pattern):
#    comb_string = ""
#    comb_pattern = ""
#    comb_bond = ""
#    last_string_indices = 0
#    last_pattern_indices = 0
#    
#    for i in range(len(combination_value)):
#        string_indices = combination_value[i]
#        flag = True
#        k = 0
#        while flag:
#            if comb_string == "" and comb_pattern == "" and comb_bond == "":                
#                if filtered_match_map[k][0] == string_indices:
#                    pattern_indices = filtered_match_map[k][2]
#                    distance_emptyString = pattern_indices - string_indices                   
#                    
#                    comb_string += distance_emptyString*" " + string[:(string_indices + len(filtered_match_map[k][1]))]
#                    comb_bond += " " 
#                    comb_pattern += pattern[:(filtered_match_map[k][2]+len(filtered_match_map[k][1]))]
#                    last_string_indices = filtered_match_map[k][0] + len(filtered_match_map[k][1]) -1
#                    last_pattern_indices = filtered_match_map[k][2] + len(filtered_match_map[k][1]) -1
#                    print (i,len(combination_value))
#                    print("raise hand in start position")
#                    if i == len(combination_value) - 1:
#                        print("raise hand in start if position")
#                        if last_string_indices < len(string):
#                            comb_string += string[last_string_indices+1:len(string)]
#                        if last_pattern_indices < len(pattern):
#                            comb_pattern += pattern[last_pattern_indices+1:len(pattern)]
#                    
#                    flag = False
#                    k += 1
#                else:
#                    if k < len(filtered_match_map):
#                        k += 1
#                    else:
#                        break
#            else:
#                if filtered_match_map[k][0] == string_indices:                    
#                    pattern_indices = filtered_match_map[k][2]
#                    
#                    comb_string += string[last_string_indices+1:string_indices] + string[string_indices:(string_indices+len(filtered_match_map[k][1]))]
#                    comb_bond += " "
#                    comb_pattern += pattern[last_pattern_indices+1:filtered_match_map[k][2]] + pattern[(filtered_match_map[k][2]):(filtered_match_map[k][2]+len(filtered_match_map[k][1]))]
#                    last_string_indices = filtered_match_map[k][0] + len(filtered_match_map[k][1]) -1
#                    last_pattern_indices = filtered_match_map[k][2] + len(filtered_match_map[k][1]) -1
#                    print (i,len(combination_value))
#                    print("raise hand in in progress position")
#                    if i == len(combination_value) - 1:
#                        print("raise hand in in progress if position")
#                        if last_string_indices < len(string):
#                            comb_string += string[last_string_indices+1:len(string)]
#                        if last_pattern_indices < len(pattern):
#                            comb_pattern += pattern[last_pattern_indices+1:len(pattern)]
#                    flag = False
#                    k += 1
#                else:
#                    k += 1
#    print("Combination :", combination_count)
#    print("Actual :", string)
#    print("String : ",comb_string)
#    print("Pattern: ", comb_pattern) 
#    print("Actual : ", pattern )
#    resultcombinaton = [comb_string,comb_pattern]
#    return resultcombinaton

def display(combination_value,filtered_match_map,string,pattern):
    comb_string = ""
    comb_pattern = "" 
    comb_bond = ""
    last_string_indices = 0
    last_pattern_indices = 0
    
    for i in range(len(combination_value)):
        string_indices = combination_value[i]
        flag = True
        k = 0
        while flag:
            if comb_string == "" and comb_pattern == "" and comb_bond == "":                
                if filtered_match_map[k][0] == string_indices:
                    pattern_indices = filtered_match_map[k][2]
                    distance_emptyString = pattern_indices - string_indices                 
                    
                    comb_string += distance_emptyString*" " + string[:(string_indices + len(filtered_match_map[k][1]))]
                    #comb_bond += " " 
                    #Added
                    comb_bond += distance_emptyString*" " + len(string[:string_indices])*" " + len(string[string_indices:(len(filtered_match_map[k][1])+string_indices)])*"|"
                    comb_pattern += pattern[:(filtered_match_map[k][2]+len(filtered_match_map[k][1]))]
                    last_string_indices = filtered_match_map[k][0] + len(filtered_match_map[k][1]) -1
                    last_pattern_indices = filtered_match_map[k][2] + len(filtered_match_map[k][1]) -1
                    print (i,len(combination_value))
                    print("raise hand in start position")
                    if i == len(combination_value) - 1:
                        print("raise hand in start if position")
                        if last_string_indices < len(string):
                            comb_string += string[last_string_indices+1:len(string)]
                        if last_string_indices < len(string):
                            comb_bond += len(string[last_string_indices+1:len(string)])*" "
                        if last_pattern_indices < len(pattern):
                            comb_pattern += pattern[last_pattern_indices+1:len(pattern)]
                    
                    flag = False
                    k += 1
                else:
                    if k < len(filtered_match_map):
                        k += 1
                    else:
                        break
            else:
                if filtered_match_map[k][0] == string_indices:                    
                    pattern_indices = filtered_match_map[k][2]
                    
                    comb_string += string[last_string_indices+1:string_indices] + string[string_indices:(string_indices+len(filtered_match_map[k][1]))]
                    #comb_bond += " "
                    #Added
                    comb_bond += len(string[last_string_indices+1:string_indices])*" " + len(string[string_indices:(string_indices+len(filtered_match_map[k][1]))])*"|"
                    comb_pattern += pattern[last_pattern_indices+1:filtered_match_map[k][2]] + pattern[(filtered_match_map[k][2]):(filtered_match_map[k][2]+len(filtered_match_map[k][1]))]
                    last_string_indices = filtered_match_map[k][0] + len(filtered_match_map[k][1]) -1
                    last_pattern_indices = filtered_match_map[k][2] + len(filtered_match_map[k][1]) -1
                    print (i,len(combination_value))
                    print("raise hand in in progress position")
                    if i == len(combination_value) - 1:
                        print("raise hand in in progress if position")
                        if last_string_indices < len(string):
                            comb_string += string[last_string_indices+1:len(string)]
                        if last_string_indices < len(string):
                            comb_bond += len(string[last_string_indices+1:len(string)])*" "
                        if last_pattern_indices < len(pattern):
                            comb_pattern += pattern[last_pattern_indices+1:len(pattern)]
                    flag = False
                    k += 1
                else:
                    k += 1
    print("Combination :", combination_count)
    print("Actual :", string)
    print("String : ",comb_string)
    #Added
    print("Bondin : ", comb_bond)
    print("Pattern: ", comb_pattern)
    print("Actual : ", pattern )
    resultcombinaton = [comb_string,comb_bond,comb_pattern]
    return resultcombinaton

def pattern_matcher(pattern,string):
    pattern_length = len(pattern)
    string_length = len(string)
    i = 0
    #print(i,string_length,pattern_length)
    while i < string_length - pattern_length:   
        #print("Pattern ", pattern, "match ", string[i:(i+pattern_length-1)] )
        if pattern == string[i:(i+pattern_length)]:
            #print("Here ", string[i:(i+pattern_length-1)],"  ====   ",pattern)
            #diction[pattern]= i
            try:
                if i not in dict_Pattern_indices[pattern]:
                    dict_Pattern_indices.setdefault(pattern, []).append(i)
                i = i + pattern_length
            except:
                dict_Pattern_indices.setdefault(pattern, []).append(i)
        else:
            i += 1



def mainFunc(RNA,mRNA):
    string = RNA.lower()
    pattern = mRNA.lower()
    
    global combination_count
    
    
    print(string,pattern)
    
    testResponse = "Test is good"
    print(testResponse)
    
    
    pattern_map = get_substring_indices(pattern)
    test_match = {}
    for pattern_key in pattern_map.keys():
        found_at_indices = kmp_matcher(string,pattern_key)
        
        if found_at_indices:
            print("Pattern :", pattern_key, " Found at Indices ", found_at_indices)
            
            for i in found_at_indices:
                test_match[pattern_key] = found_at_indices
                
    
    OccuranceList = []
    for k,l in test_match.items():
        for r in range(len(l)):
            OccuranceList.append([k,l[r]])
    
    #Sorting the List by the Lower Indices
    OccuranceList.sort(key=lambda x: x[1])
    print("Occurance ", OccuranceList) 
    filterdata = []
    for i in range(len(OccuranceList)):
        if len(filterdata) == 0:
            filterdata.append(OccuranceList[i])
        else:            
            if OccuranceList[i][1] in [filterdata[j][1] for j in range(len(filterdata))]:
                for j in range(len(filterdata)):
                    if filterdata[j][1]==OccuranceList[i][1]:
                        if len(filterdata[j][0]) < len(OccuranceList[i][0]):
                            filterdata[j][0] = OccuranceList[i][0]
			    print("OccuranceList[i][1] ", OccuranceList[i][0])
                            print("filterdata[j][0] ", filterdata[j][0])
                            break                 
            else:
                filterdata.append(OccuranceList[i])
    print("RNA Indices filterdata:", filterdata)
    global dict_Pattern_indices
    dict_Pattern_indices = {}
    for j in range(len(filterdata)):
        #print(filterdata[j][0])
        pattern_matcher(filterdata[j][0],pattern)
    
    #print("Pattern Indices :", dict_Pattern_indices)
    
    
    list_dict_Pattern_indices = []
    for i,j in dict_Pattern_indices.items():
        if len(j)>1:
            for k in range(len(j)):
                list_dict_Pattern_indices.append([i,[j[k]]])
        else:
            list_dict_Pattern_indices.append([i,j])
        
    
    list_dict_Pattern_indices.sort(key=lambda x: x[1]) 
    
    global count_filter
    count_filter = 0
    global filter_match
    global combination_after_filter
    filter_match = []
    combination_after_filter=[]
    combinationTry(filterdata,list_dict_Pattern_indices)
    
    print("SSI_String_PSI : ", filter_match)
    print("Final Combination ", combination_after_filter)
    
    combination_count = 0
    matchingCombination = []
    for i in range(len(combination_after_filter)):
        data= combination_after_filter[i]
        if isinstance(data, int):            
            intData = [data]
            combination_count += 1
            output = display(intData,filter_match,string,pattern)
            if len(output)>0:
                matchingCombination.append(output)
            
        else:
            combination_count += 1
            output = display(data,filter_match,string,pattern)
            if len(output)>0:
                matchingCombination.append(output)
    
    return matchingCombination

if __name__ == "__main__":
    print("Hello This is called in same page")
    string = ""
    pattern = ""
    combination_count = 0
    count_filter = 0
