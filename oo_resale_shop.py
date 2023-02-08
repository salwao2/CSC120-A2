
#importing all the information from the computer file
from computer import *

#This class is for the Resale Shop
class ResaleShop:

    # Attributes: this attribute creates the inventory as a list
    inventory: list

    # Constructor: this constructor takes in the inventory as a list

    def __init__(self) -> None:
        self.inventory = []

    # Methods: Buy, Sell, Print Inventory, Refurbish

    #(self) is reference to the blueprint of def buyComp
    # Takes in parameters containing all the information about a computer adds it to the inventory and append adds c to the end of self.invetory list

    def comp_buy(self, comp_description, serial, year, comp_memory, comp_pt, comp_hdc, comp_os, comp_price): #when someone comes to buy a computer they need to tell you this info
        c = Computer (comp_description, serial, year, comp_memory, comp_pt, comp_hdc, comp_os, comp_price) #passing parameters into to the Computer constructor (class) pasing it into the system to store in the inventory
        self.inventory.append(c)
    
    #Takes in an c, removes the associated computer if it is the inventory, prints error message otherwise

    def comp_sell(self, c:Computer):
        if c in self.inventory:
            self.inventory.remove(c)
            print("Item", c, "sold!")
        else: print("Item", c,"not found in inventory. Please select another item to sell.")

    #Prints all the items in the inventory (if it isn't empty), prints error otherwise

    def print_inventory(self):
        if not self.inventory:
            print("No inventory to display") 
        else:
            for c in self.inventory:
                c.print_details() #prints the details of the inventory
                print()

    #This refurbishes the computer. If the computer is in the inventory, the year of the computer determines the price. If not in inventory prints error

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

  
#Executes the methods from above
def main():

    #Create the store
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