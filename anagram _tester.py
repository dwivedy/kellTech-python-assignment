def is_anagram(input1,input2):
    if(type(input1)==str and type(input2)==str ):
        if(sorted(input1)==sorted(input2)):
            return True
        else:
            return False
    else:
        return "Please provide valid inputs"

#Test cases
input1,input2='cellar', 'recall';
input3,input4 ='arm','elbow';

    
print(is_anagram(input1,input2))
print(is_anagram(input3,input4))
    
