def split_before_each_uppercases(formula):
    word=""
    index=1
    new_formula[]=[]
    if formula[0].isupper():
       word+=formula[0]
       while index<=len(formula) :
             if formula[index].isupper()==False:
                word+=formula[index]
                index+=1
             elif formula[index].isupper(): 
                  new_formula.append(word)
                  word=formula[index]
                  index+=1

    new_formula.append(word)
    return new_formula
                    
                
                
                
                
            


def split_at_first_digit(formula):
    word=""
    num=""
    for split in formula:
        if split.isdighit():
            num+=split
        else:
            word+=split
    if num=='':
        num="1"
    return word ,num 

