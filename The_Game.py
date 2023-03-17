import random as rnd #Firstly, importing the random library to generate a random number in range.

def askNumber(): #Defining the first function where the actual number game will run. Naming it 'askNumber'.
    global number_of_games
    global answer #As inside the function setting answer and the attempts to be global with keyword 'global' so can keep calling them
    global attempts #The previous comment.
    attempts = 3 #Setting the number of attempts to be 3 in every game
    answer = rnd.randint(1, 20) #The computer will generate a random number in the given range and naming it 'answer'
    
    while attempts > 0: #The game will continue as long as the number of attempts is more than 0.
        
        the_guess = input('Please guess a number between 1 and 20: ') #Using 'input' to generate a window for users to input their guess.
        
        if the_guess.isnumeric(): #Firstly, checking that the user input is number.
        
            if int(the_guess) == answer:#Converting the input into integer and if equals with the answer then prints the below string.
                
                attempts-=1 #Taking away 1 attempt 
                print(f'You won! {answer} is the correct answer. You guessed {3 - attempts} times.') #Using the f-string to format it and input the correct answer.
                
                number_of_games += 1 #Adding 1 to the count of number of games after every game
                TheGame() #Calling the TheGame() function from the below cell.
                
                return #Returning the result so it won't stay spiralling into here when you want to finish the game.
                    
            elif int(the_guess) > answer: #Giving a hint and saying that the answer is lower if the guess is higer and printing the below by using f-strings again.
            
                attempts -= 1 #Taking away 1 attempt.
                print(f'{the_guess} is incorrect. The answer is smaller than {the_guess}. You have {attempts} attempts left.')
            
            elif int(the_guess) < answer: #Giving a hint that the answer is bigger than the guess and printing the below using f-strings.
            
                attempts -= 1 #Taking away 1 attempt
                print(f'{the_guess} is incorrect. The answer is greater than {the_guess}. You have {attempts} attempts left.')
                
        else: #If the input is not a number, print the below error message.
            print('!Please enter a number!')
            
    else: #If the attempts reaches 0, printing the below message and using f-strings to format the statement.
        print(f'You Lost! you have {attempts} attempts left. The correct answer was {answer}.')
        
        number_of_games +=1 #Adding 1 to the count after every game
        
        TheGame() #Calling the below function to ask whether want to play again
       
        return #Returning the result so it won't stay spiralling into here when you want to finish the game.
        
def TheGame(): #Definging a function where the user is asked whether they wish to play the game again
    
    while True: #While that is true and the game is running then the follow happens
        
        play_again = input('Do you wish to play again? Y/N: ') #Generating a window for the user to select yes or no.
        
        if play_again.lower()=='y': #If user selects yes, then calling the askNumber(), the game function again. Using .lower for it to accept non-capital inputs.
           
            askNumber() #Calling the game function
            
            return #Returning the result so it won't stay spiralling into here when you want to finish the game.
            
        elif play_again.lower()=='n': #If player selects no, then print the below statements. 
            
            print(f'Thank you for playing! You played {number_of_games} games.') #f-string is used to format the string and add the values in there.
            
            return #Returning the result so it won't stay spiralling into here when you want to finish the game.
            
def FullGame(): #Need to define a new function to count the number of games
    global number_of_games #setting the number of games to global value
    number_of_games = 0 #Starting from 0
    askNumber() #Then calling the game function
    
FullGame() #To play the game
