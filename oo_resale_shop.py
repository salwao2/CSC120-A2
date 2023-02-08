from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory: list

    # How will you set up your constructor?

    def __init__(self) -> None:
        self.inventory = []

    # Remember: in python, all constructors have the same name (__init__)
    #def __init__():
    #pass # You'll remove this when you fill out your constructor

    # What methods will you need?

    # (self) reference to the blueprint of def buyComp

    def comp_buy(self, comp_description, serial, year, comp_memory, comp_pt, comp_hdc, comp_os, comp_price): #when someone comes to buy a computer they need to tell you this info. You can pass in the price and every computer has the same price or look at refurbish code
        c = Computer (comp_description, serial, year, comp_memory, comp_pt, comp_hdc, comp_os, comp_price) #passing parameters into to the Computer constructor (class) pasing it into the system to store in the inventory
        self.inventory.append(c)

    def comp_sell(self, c:Computer):
        if c in self.inventory:
            self.inventory.remove(c)
            print("Item", c, "sold!")
        else: print("Item", c,"not found in inventory. Please select another item to sell.")

    def print_inventory(self):
        if not self.inventory:
            print("No inventory to display") 
        else:
            for c in self.inventory:
                c.print_details()
                print()
        

    def comp_refurbish(self, c:Computer, new_os):
        if c in self.inventory:
            computer = c

            if int(computer.year_made) < 2000:
                computer.price = 0 
            elif int(computer.year_made)< 2012:
                computer.price = 250
            elif int(computer.year_made) <2018:
                computer.price = 550
            else:
                computer.price = 1000
        
            if new_os is not None:
                computer.operating_system = new_os
        else:
            print("Item", self.inventory[0].description, "not found. Please select another item to refurbish.")

  
def main():

    my_store = ResaleShop()
    

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    my_store.comp_buy("Mac Pro (Late 2013)", "3YP8301RFS89", 2017, 512, "3.5 GHc 6-Core Intel Xeon E5", 1024, "macOS Big Sur", 1800)
    print("Buying", my_store.inventory[0].description)
    print("Adding to inventory...")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    my_store.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item:", my_store.inventory[0].description, ", updating OS", my_store.inventory[0].operating_system, "to", new_OS)
    print("Updating inventory...")
    my_store.comp_refurbish(my_store.inventory[0], new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    my_store.print_inventory()
    print("Done.\n")

    #Now, let's sell it!
    my_store.comp_sell(my_store.inventory[0])
    my_store.print_inventory()


    # Make sure it worked by checking inventory
    print("Checking inventory...")
    my_store.print_inventory()
    print("Done.\n")

main()