class Parents():
    def __init__(self, last_name, eye_color):
        print ("Parents Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last name: " + self.last_name)
        print("Eye color: " + self.eye_color)


class Child(Parents):
    def __init__(self, last_name, eye_color, number_of_toys):
        print ("Child Constructor Called")
        Parents.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last name: " + self.last_name)
        print("Eye color: " + self.eye_color)
        print("Number of Toys: " + str(self.number_of_toys))

#billy_cyrus = Parents("Cyrus", "blue")
#billy_cyrus.show_info()

#print(billy_cyrus.last_name)



miley_cyrus = Child("Cyrus", "blue", 5)
miley_cyrus.show_info()


