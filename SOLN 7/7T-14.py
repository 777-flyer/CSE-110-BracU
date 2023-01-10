def indexing_char (sentence,position):
    
    main_sentence = sentence[0]
    length = len(sentence)
    removed_string = ""
    
    for index in range (1,length):
        if index % position != 0:
            main_sentence += sentence[index]
        else:
            removed_string += sentence[index]
            
    main_sentence += removed_string
    
    return main_sentence


sentence = input("Sir,Please enter your desired input: ")
position = int(input("Sir,Please enter the index number: "))

#function calling

print(indexing_char (sentence,position))