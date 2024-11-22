def passowrd_system():
    correct_password="12345"
    max_attempt=5
    attempt=0
    while attempt< max_attempt:
        user_input= input('enter the password')
        attempt+=1
        if user_input==correct_password:
            print( 'Acces granted')
            return
        else:
          
            remaining_attempt=max_attempt-attempt
            if remaining_attempt>0:
                print( f'Incorrect password .you have {remaining_attempt} attempt left')
            else:
                print('maximmum attempt reached')
                return
if __name__ == "__main__":
    passowrd_system()