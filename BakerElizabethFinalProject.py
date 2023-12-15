"""
Name: MolCalc
Author: Elizabeth Baker
Last Modified: 14DEC2023
Purpose: This program will accept an atomic number and a number of atoms.
It will output the molecular weight of the molecule.
"""

import tkinter
from breezypythongui import EasyFrame

#chem_dict contains the atomic symbols and masses as key : value pairs
chem_dict = {
    "H" : 1.008,
    "He" : 4.003,
    "Li" : 6.94,
    "Be" : 9.012,
    "B" : 10.81,
    "C" : 12.011,
    "N" : 14.007,
    "O" : 15.999,
    "F" : 18.998,
    "Ne" : 20.180,
    "Na" : 22.990,
    "Mg" : 24.305,
    "Al" : 26.982,
    "Si" : 28.085,
    "P" : 30.974,
    "S" : 32.06,
    "Cl" : 35.45,
    "Ar" : 39.948,
    "K" : 39.098,
    "Ca" : 40.078,
    "Sc" : 44.956,
    "Ti" : 47.867,
    "V" : 50.942,
    "Cr" : 51.996,
    "Mn" : 54.938,
    "Fe" : 55.845,
    "Co" : 58.933,
    "Ni" : 58.693,
    "Cu" : 63.546,
    "Zn" : 65.38,
    "Ga" : 69.723,
    "Ge" : 72.630
    }

#create window for input
class MolCalc(EasyFrame):
    def __init__(self):
        """Create main window"""
        EasyFrame.__init__(self,title="MolCalc")
        self.expression = ""
        self.rowCount = 2#self.rowCount initializes the rows that the new lines will be started on in the newLine function
        self.massList = [0.0] #initialize the list of masses that will be added together at the end of calcMass function

        #Define GUI components
        self.addLabel(text="Atomic symbol:",row=0,column=0,sticky="NSEW")
        #self.entry_box allows user to input the atomic symbol of an atom in their molecule
        self.entry_box = self.addTextField(text="",row=1,column=0,columnspan=4,rowspan=1,sticky="NSEW")
        self.addLabel(text="Number of atoms:",row=0,column=1,columnspan=4,sticky="NSEW")
        #self.InputField allows user to input the number of atoms of a particular element as an integer
        self.InputField = self.addIntegerField(value=0,row=1,column=1,columnspan=4,rowspan=4)
        self.addButton(text="Calculate Molar Mass",row=119,column=6,command=self.calcMass,sticky="NSEW")
        #outputFieldFloat displays the molar mass
        self.addLabel(text="Molar mass:",row=118,column=0,columnspan=1,sticky="NSEW")
        self.outputFieldFloat = self.addFloatField(value = 0.0,row=119,column=1,width=12,precision=4,state="readonly")
        #outputFieldText displays success and error messages
        self.addLabel(text="Messages:",row=118,column=2,columnspan=1,sticky="NSEW")
        self.outputFieldText = self.addTextField(text="",row=119,column=3,width=36,state="readonly")
        #button to add new line
        self.addAtom = self.addButton(text="Add atom",row=1,column=6,command=self.addLine,sticky="NSEW")

    def calcMass(self):
        """Gets molar mass of atom from dictionary and calculates molar mass.
        Also places mass of each element in the massList list."""
        atSym = self.entry_box.getText() #the atomic symbol of desired atom
        if atSym not in chem_dict:
            #this will prompt the user to check that their atomic symbol was typed correctly
            self.outputFieldText.setText("Error: atomic symbol not recognized.")
            self.outputFieldFloat.setNumber(0.0)
        else:
            #shows that it "sees" the text in the dict and gets the atomic mass
            self.outputFieldText.setText("Success: atomic symbol recognized")
            atMass = chem_dict.get(atSym, None) #the atomic mass of desired atom
        num = self.InputField.getNumber() #the number of atoms of the desired atom
        calcMass = atMass * num #the atomic mass of the specified number of atoms
        #pass each calcMass calculation to massList
        self.massList.append(calcMass)
        totalMass = 0 #initialize the accumulator to find total mass of the molecule
        for mass in self.massList:
            #add each element in massList together to produce totalMass
            totalMass = totalMass + mass #add the masses of each atom in the molecule together
        self.outputFieldFloat.setNumber(totalMass)

    def addLine(self):
        """Adds a new line so user can add more atoms to their calculation"""
        self.calcMass()
        self.entry_box = self.addTextField(text="",row=self.rowCount,column=0,columnspan=4,rowspan=1,sticky="NSEW")
        self.InputField = self.addIntegerField(value=0,row=self.rowCount,column=1,columnspan=4,rowspan=4)
        self.addAtom["state"] = "disabled"
        self.addAtom = self.addButton(text="Add atom",row=self.rowCount,column=6,command=self.addLine,sticky="NSEW")
        self.rowCount += 1
        

def main():
    MolCalc().mainloop()

if __name__ == "__main__":
    main()