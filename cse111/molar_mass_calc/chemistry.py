from formula import parse_formula

def main():
    elements_dict = make_periodic_table()
    while True:
        chemical_symbol = input("Enter a chemical formula: ")
        try:
            symbol_quantity_list = parse_formula(chemical_symbol, elements_dict)
            break
        except ValueError:
            print("\nInvalid input. Try again.")

    while True:
        try:
            mass = float(input("Mass of the chemical sample in grams: "))
            break
        except ValueError:
            print ("\nInvalid input. Try again. (Enter a number without any units symbols)")

    name = get_formula_name(chemical_symbol)

    molar_mass = compute_molar_mass(symbol_quantity_list, elements_dict)
    
    moles = mass/molar_mass

    print()
    print (f"Chemical name: {name}")
    print (f"{molar_mass} grams/mole")
    print (f"{moles} moles")


# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # Do the following for each inner list in the
    # compound symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        # Get the atomic mass for the symbol from the dictionary.
        # Multiply the atomic mass by the quantity.
        # Add the product into the total molar mass.
    total_molar_mass = 0
    for i_list in symbol_quantity_list:
        symbol = i_list[SYMBOL_INDEX]
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        molar_mass = atomic_mass * i_list[QUANTITY_INDEX]
        total_molar_mass += molar_mass

    # Return the total molar mass.
    return total_molar_mass

def make_periodic_table():
    periodic_table_dict = {
    # symbol: [name, atomic_mass]
    "Ac":	["Actinium",	227],
    "Ag":	["Silver",	107.8682],
    "Al":	["Aluminum",	26.9815386],
    "Ar":	["Argon",	39.948],
    "As":	["Arsenic",	74.9216],
    "At":	["Astatine",	210],
    "Au":	["Gold",	196.966569],
    "B":	["Boron",	10.811],
    "Ba":	["Barium",	137.327],
    "Be":	["Beryllium",	9.012182],
    "Bi":	["Bismuth",	208.9804],
    "Br":	["Bromine",	79.904],
    "C":	["Carbon",	12.0107],
    "Ca":	["Calcium",	40.078],
    "Cd":	["Cadmium",	112.411],
    "Ce":	["Cerium",	140.116],
    "Cl":	["Chlorine",	35.453],
    "Co":	["Cobalt",	58.933195],
    "Cr":	["Chromium",	51.9961],
    "Cs":	["Cesium",	132.9054519],
    "Cu":	["Copper",	63.546],
    "Dy":	["Dysprosium",	162.5],
    "Er":	["Erbium",	167.259],
    "Eu":	["Europium",	151.964],
    "F":	["Fluorine",	18.9984032],
    "Fe":	["Iron",	55.845],
    "Fr":	["Francium",	223],
    "Ga":	["Gallium",	69.723],
    "Gd":	["Gadolinium",	157.25],
    "Ge":	["Germanium",	72.64],
    "H":	["Hydrogen",	1.00794],
    "He":	["Helium",	4.002602],
    "Hf":	["Hafnium",	178.49],
    "Hg":	["Mercury",	200.59],
    "Ho":	["Holmium",	164.93032],
    "I":	["Iodine",	126.90447],
    "In":	["Indium",	114.818],
    "Ir":	["Iridium",	192.217],
    "K":	["Potassium",	39.0983],
    "Kr":	["Krypton",	83.798],
    "La":	["Lanthanum",	138.90547],
    "Li":	["Lithium",	6.941],
    "Lu":	["Lutetium",	174.9668],
    "Mg":	["Magnesium",	24.305],
    "Mn":	["Manganese",	54.938045],
    "Mo":	["Molybdenum",	95.96],
    "N":	["Nitrogen",	14.0067],
    "Na":	["Sodium",	22.98976928],
    "Nb":	["Niobium",	92.90638],
    "Nd":	["Neodymium",	144.242],
    "Ne":	["Neon",	20.1797],
    "Ni":	["Nickel",	58.6934],
    "Np":	["Neptunium",	237],
    "O":	["Oxygen",	15.9994],
    "Os":	["Osmium",	190.23],
    "P":	["Phosphorus",	30.973762],
    "Pa":	["Protactinium",	231.03588],
    "Pb":	["Lead",	207.2],
    "Pd":	["Palladium",	106.42],
    "Pm":	["Promethium",	145],
    "Po":	["Polonium",	209],
    "Pr":	["Praseodymium",	140.90765],
    "Pt":	["Platinum",	195.084],
    "Pu":	["Plutonium",	244],
    "Ra":	["Radium",	226],
    "Rb":	["Rubidium",	85.4678],
    "Re":	["Rhenium",	186.207],
    "Rh":	["Rhodium",	102.9055],
    "Rn":	["Radon",	222],
    "Ru":	["Ruthenium",	101.07],
    "S":	["Sulfur",	32.065],
    "Sb":	["Antimony",	121.76],
    "Sc":	["Scandium",	44.955912],
    "Se":	["Selenium",	78.96],
    "Si":	["Silicon",	28.0855],
    "Sm":	["Samarium",	150.36],
    "Sn":	["Tin",	118.71],
    "Sr":	["Strontium",	87.62],
    "Ta":	["Tantalum",	180.94788],
    "Tb":	["Terbium",	158.92535],
    "Tc":	["Technetium",	98],
    "Te":	["Tellurium",	127.6],
    "Th":	["Thorium",	232.03806],
    "Ti":	["Titanium",	47.867],
    "Tl":	["Thallium",	204.3833],
    "Tm":	["Thulium",	168.93421],
    "U":	["Uranium",	238.02891],
    "V":	["Vanadium",	50.9415],
    "W":	["Tungsten",	183.84],
    "Xe":	["Xenon",	131.293],
    "Y":	["Yttrium",	88.90585],
    "Yb":	["Ytterbium",	173.054],
    "Zn":	["Zinc",	65.38],
    "Zr":	["Zirconium",	91.224],
    }
    return periodic_table_dict

def get_formula_name(chemical_formula):
    chemical_formulas = {
    "H2O": "Water",
    "NaCl": "Sodium Chloride",
    "CO2": "Carbon Dioxide",
    "O2": "Oxygen",
    "N2": "Nitrogen",
    "CH4": "Methane",
    "C6H12O6": "Glucose",
    "NH3": "Ammonia",
    "H2SO4": "Sulfuric Acid",
    "HCl": "Hydrochloric Acid",
    "NaOH": "Sodium Hydroxide",
    "C2H5OH": "Ethanol",
    "CO": "Carbon Monoxide",
    "NO": "Nitric Oxide",
    "NO2": "Nitrogen Dioxide",
    "SO2": "Sulfur Dioxide",
    "SO3": "Sulfur Trioxide",
    "CaCO3": "Calcium Carbonate",
    "NaHCO3": "Sodium Bicarbonate",
    "H2O2": "Hydrogen Peroxide",
    "Fe2O3": "Iron(III) Oxide",
    "SiO2": "Silicon Dioxide",
    "HCN": "Hydrogen Cyanide",
    "KMnO4": "Potassium Permanganate",
    "KOH": "Potassium Hydroxide",
    "MgCl2": "Magnesium Chloride",
    "Al2O3": "Aluminum Oxide",
    "AgNO3": "Silver Nitrate",
    "CuSO4": "Copper(II) Sulfate",
    "ZnCl2": "Zinc Chloride",
    "CH3COOH": "Acetic Acid",
    "C3H8": "Propane",
    "C4H10": "Butane",
    "HNO3": "Nitric Acid",
    "H3PO4": "Phosphoric Acid",
    "KCl": "Potassium Chloride",
    "Na2CO3": "Sodium Carbonate",
    "CaCl2": "Calcium Chloride",
    "MgO": "Magnesium Oxide",
    "KI": "Potassium Iodide",
    "NaF": "Sodium Fluoride",
    "LiCl": "Lithium Chloride",
    "BaSO4": "Barium Sulfate",
    "PbS": "Lead(II) Sulfide",
    "HgO": "Mercury(II) Oxide",
    "Cr2O3": "Chromium(III) Oxide",
    "TiO2": "Titanium Dioxide",
    "ZnO": "Zinc Oxide",
    "FeS2": "Iron Pyrite (Fool's Gold)",
    "NaNO3": "Sodium Nitrate",
    "K2CO3": "Potassium Carbonate",
    "Ca(OH)2": "Calcium Hydroxide",
    "Mg(OH)2": "Magnesium Hydroxide",
    "Al(OH)3": "Aluminum Hydroxide",
    "NH4Cl": "Ammonium Chloride",
    "C12H22O11": "Sucrose",
    "N2O": "Nitrous Oxide (Laughing Gas)",
    "H2S": "Hydrogen Sulfide",
    "SF6": "Sulfur Hexafluoride",
    "XeF4": "Xenon Tetrafluoride",
    "Rn": "Radon", # Elemental formula
    "Ar": "Argon", # Elemental formula
    "He": "Helium", # Elemental formula
    "Ne": "Neon", # Elemental formula
    "Kr": "Krypton", # Elemental formula
    "Au": "Gold", # Elemental formula
    "Ag": "Silver", # Elemental formula
    "Fe": "Iron", # Elemental formula
    "Cu": "Copper", # Elemental formula
    "Al": "Aluminum", # Elemental formula
    "Zn": "Zinc", # Elemental formula
    "Pb": "Lead", # Elemental formula
    "Sn": "Tin", # Elemental formula
    "Hg": "Mercury", # Elemental formula
    "Pt": "Platinum", # Elemental formula
    "Ni": "Nickel", # Elemental formula
    "Co": "Cobalt", # Elemental formula
    "Cr": "Chromium", # Elemental formula
    "Mn": "Manganese", # Elemental formula
    "P4": "White Phosphorus",
    "S8": "Cyclooctasulfur",
    "Cl2": "Chlorine",
    "Br2": "Bromine",
    "I2": "Iodine",
    "F2": "Fluorine",
    "HBr": "Hydrobromic Acid",
    "HI": "Hydroiodic Acid",
    "HF": "Hydrofluoric Acid",
    "KNO3": "Potassium Nitrate",
    "Na2SO4": "Sodium Sulfate",
    "CaSO4": "Calcium Sulfate",
    "FeSO4": "Iron(II) Sulfate",
    "FeCl3": "Iron(III) Chloride",
    "SnO2": "Tin(IV) Oxide",
    "PbO": "Lead(II) Oxide",
    "LiOH": "Lithium Hydroxide",
    "CsCl": "Cesium Chloride",
    "RbI": "Rubidium Iodide",
    "SrCO3": "Strontium Carbonate",
    "BaCl2": "Barium Chloride",
    "Ra": "Radium", # Elemental formula
    "U": "Uranium", # Elemental formula
    "Pu": "Plutonium", # Elemental formula
    "Cs": "Cesium", # Elemental formula
    "Fr": "Francium", # Elemental formula
    "BeO": "Beryllium Oxide",
    "B2H6": "Diborane",
    "SiH4": "Silane",
    "GeH4": "Germane",
    "AsH3": "Arsine",
    "SbH3": "Stibine",
    "BiH3": "Bismuthine",
    "HFO": "Hypofluorous Acid",
    "HClO": "Hypochlorous Acid",
    "HBrO": "Hypobromous Acid",
    "HIO": "Hypoiodous Acid"
    }

    if chemical_formula in chemical_formulas:
        name = chemical_formulas[chemical_formula]
    else:
        name = "Unknown Compound"

    
    return name


if __name__ == "__main__":
    main()