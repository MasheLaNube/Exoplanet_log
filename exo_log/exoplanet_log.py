import os
import csv

class ExoplanetLog:
    def __init__(self, base_folder= "Exoplanet_Log"):
        self.base_folder= base_folder
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def add_exoplanet(self, name_exo):
        """Create the folder of an exoplanet"""
        self.exo_folder= os.path.join(self.base_folder, name_exo)
        os.makedirs(self.exo_folder, exist_ok=True)

        """creation of csv files"""

        self.s_param_file= os.path.join(self.exo_folder, "stellar_params.csv")
        self.lc_file= os.path.join(self.exo_folder, "lc_initial_data.csv")
        self.ref_file= os.path.join(self.exo_folder, "references.csv")

        for file in [self.s_param_file, self.lc_file, self.ref_file]:
            if not os.path.exists(file):
                open(file, "w").close()
        print(f'Folder and files for {name_exo} created successfully.')

    def add_stellar_params(self):
        headers= ["Ra", "Dec", "Teff(K)", "log_g", "RV", "stellar_density", "M0", "R0", "L0"]
        data= []
        print('Enter stellar parameters (If not found, just press space buttom): ')
        row= []
        for h in headers:
            val= input(f'{h}: ')
            row.append(val)
        data.append(row)
        with open(self.s_param_file, 'a', newline='') as file:
            writer= csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)
            print('Stellar parameters added successfully.')

    def add_lc_data(self):
        headers = ["Date", "DIT", "Instrument", "Reference Star", "Filter", "BJD_i", "BJD_f"]
        datos = []
        print("Insert the data from the lightcurve (To stop, just add a space when date is being asked):")
        while True:
            fila = []
            fecha = input("Date: ")
            if fecha == "":
                break
            fila.append(fecha)
            for h in headers[1:]:
                fila.append(input(f"{h}: "))
            datos.append(fila)
            
        
        with open(self.lc_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(datos)
        print("Lightcurve saved.")
    
    def log_ref(self):
        """Pide links de referencias y los guarda en un archivo de texto"""
        print("Insert the links from your references (Leave blank to finish)):")
        referencias = []
        while True:
            ref = input("Reference: ")
            if ref == "":
                break
            referencias.append(ref)
        
        with open(self.ref_file, "a") as f:
            for r in referencias:
                f.write(r + "\n")
        print("References saved.")

