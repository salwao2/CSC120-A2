
class Computer:

    # What attributes will it need?
    description: str
    serial_num: str
    year_made: int
    memory: int
    processor_type: str
    hard_drive_capacity: int
    operating_system: str
    price: int


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    #def __init__():
        #pass # You'll remove this when you fill out your constructor pass in certain attributes here
    def __init__(self, comp_description, serial, year, comp_memory, comp_pt, comp_hdc, comp_os, comp_price) -> None:
        self.description = comp_description
        self.serial_num = serial
        self.year_made = year
        self.memory = comp_memory
        self.processor_type = comp_pt
        self.hard_drive_capacity = comp_hdc
        self.operating_system = comp_os
        self.price = comp_price


    # What methods will you need?

    def print_details(self):
        print(self.description)
        print(self.serial_num)
        print(self.year_made)
        print(self.memory)
        print(self.processor_type)
        print(self.hard_drive_capacity)
        print(self.operating_system)
        print(self.price)

        

# def main():
#     my_computer = Computer(
#         "Mac Pro (Late 2013)",
#         "3YP8301RFS89",
#         2017, 512, "3.5 GHc 6-Core Intel Xeon E5",
#          1024, "macOS Big Sur", 1800)

#     # Print a little banner
#     print("-" * 21)
#     print("COMPUTER RESALE STORE")
#     print("-" * 21)

#     # Add it to the resale store's inventory
#     print("Buying", my_computer.description["description"])
#     print("Adding to inventory...")
#     computer_id = buy(my_computer)
#     print("Done.\n")

#     # Make sure it worked by checking inventory
#     print("Checking inventory...")
#     print_inventory()
#     print("Done.\n")

#     # Now, let's refurbish it
#     new_OS = "MacOS Monterey"
#     print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
#     print("Updating inventory...")
#     comp_refurbish(computer_id, new_OS)
#     print("Done.\n")

#     # Make sure it worked by checking inventory
#     print("Checking inventory...")
#     print_inventory()
#     print("Done.\n")
    
#     # Now, let's sell it!
#     print("Selling Item ID:", computer_id)
#     sell(computer_id)
    
#     # Make sure it worked by checking inventory
#     print("Checking inventory...")
#     print_inventory()
#     print("Done.\n")

# # Calls the main() function when this file is run
# if __name__ == "__main__": main()


    
        