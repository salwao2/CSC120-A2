
    #Class

    #This class is for the computer

class Computer:

    #Attributes

    #Attributes for the computer

    description: str
    serial_num: str
    year_made: int
    memory: int
    processor_type: str
    hard_drive_capacity: int
    operating_system: str
    price: int


    #Constructor

    #The constructor for the computer

    def __init__(self, comp_description, serial, year, comp_memory, comp_pt, comp_hdc, comp_os, comp_price) -> None:
        self.description = comp_description
        self.serial_num = serial
        self.year_made = year
        self.memory = comp_memory
        self.processor_type = comp_pt
        self.hard_drive_capacity = comp_hdc
        self.operating_system = comp_os
        self.price = comp_price


    #Methods

    #This includes all the details about the computer, which is called in the resale shop in the print_inventory method

    def print_details(self):
        print(self.description)
        print(self.serial_num)
        print(self.year_made)
        print(self.memory)
        print(self.processor_type)
        print(self.hard_drive_capacity)
        print(self.operating_system)
        print(self.price)

        


    
        