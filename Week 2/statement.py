# use of if statement 
#Let us consider the movie "Avengers" This is a 13+ movie.

print('Please enter your date of birth')
birth_year = int(input())   

current_year = 2024
age = current_year - birth_year
if age >= 13:
    print('You can watch the movie')
    print('Enjoy the movie')
else:
    print('You cannot watch the movie')
    print('You are not allowed to watch this movie')
print('Thank you for using the program')