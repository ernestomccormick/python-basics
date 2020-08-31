from chef import Chef


class Chinese_chef(Chef):
    # (Chef) means that Chinese_chef inherits from the class Chef
    def make_fried_rice(self):
        print("The chef makes fried rice")

    def make_special_dish(self):
        print("The chef makes wonton")
