class Users:
    '''
    Class that generates new instances of users
    '''
    users_list = []
    # new_user =("Merciee","Mercy","Nzau","October","Mercy10")



    def __init__ (self,user_name,first_name,last_name,birth_month,password):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.birth_month = birth_month
        self.password = password