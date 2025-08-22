import os
import csv

class ExoplanetLog:
    def __init__(self, base_folder= "Exoplanet_Log"):
        self.base_folder= base_folder
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def add_system(self, name_sys):
        system_folder= os.path.join(self.base_folder, name_sys)
        os.makedirs(system_folder, exist_ok=True)

        system_params = os.path.join(system_folder, "stellar_params.csv")
        if not os.path.exists(system_params):
            open(system_params, "w").close()

        print(f"System {name_sys} created in {system_folder}.")


    def add_exoplanet(self, name_system, name_exo):
        """Create the folder of an exoplanet"""
        system_folder = os.path.join(self.base_folder, name_system)
        if not os.path.exists(system_folder):
            raise FileNotFoundError(f"The system {name_system} does not exist. First create the system with add_system().")

        exo_folder = os.path.join(system_folder, name_exo)
        os.makedirs(exo_folder, exist_ok=True)

        lc_file = os.path.join(exo_folder, "lc_initial_data.csv")
        ref_file = os.path.join(exo_folder, "references.csv")

        for file in [lc_file, ref_file]:
            if not os.path.exists(file):
                open(file, "w").close()

        print(f"Exoplanet {name_exo} created for the system {name_system}.")
        return {"lc_data": lc_file, "references": ref_file}

    def add_stellar_params(self, name_system):
        '''Guarda parametros estelares en su respectivo archivo CSV'''
        system_folder = os.path.join(self.base_folder, name_system)
        system_file = os.path.join(system_folder, "stellar_params.csv")

        if not os.path.exists(system_file):
            raise FileNotFoundError(f"The system {name_system} doesn't have a parameter file.")

        headers = ["Ra", "Dec", "Teff(K)", "log_g", "RV", "stellar_density", "M0", "R0", "L0"]
        data = []

        print(f'Enter stellar parameters for {name_system} (If not found, just press enter): ')
        row = []
        for h in headers:
            val = input(f'{h}: ')
            row.append(val)
        data.append(row)

        write_header = os.path.getsize(system_file) == 0
        with open(system_file, 'a', newline='') as file:
            writer = csv.writer(file)
            if write_header:
                writer.writerow(headers)
            writer.writerows(data)
            print('Stellar parameters added successfully.')

    def add_lc_data(self, name_system, name_exo):
        '''Permite guardar datos de curvas de luz a un archivo CSV'''
        exo_folder = os.path.join(self.base_folder, name_system, name_exo)
        lc_file = os.path.join(exo_folder, "lc_initial_data.csv")
        headers = ["Date", "DIT", "Instrument", "Reference Star", "Filter", "BJD_i", "BJD_f"]
        datos = []
        print("Insert the data from the lightcurve (To stop, just press enter when date is being asked):")
        while True:
            fila = []
            fecha = input("Date: ")
            if fecha == "":
                break
            fila.append(fecha)
            for h in headers[1:]:
                fila.append(input(f"{h}: "))
            datos.append(fila)

        write_header = os.path.getsize(lc_file) == 0
        with open(lc_file, "a", newline="") as f:
            writer = csv.writer(f)
            if write_header:
                writer.writerow(headers)
            writer.writerows(datos)
        print("Lightcurve saved.")
    
    def log_ref(self, name_system, name_exo):

        """Pide links de referencias y notas, y los guarda en un archivo CSV"""

        exo_folder = os.path.join(self.base_folder, name_system, name_exo)
        ref_file = os.path.join(exo_folder, "references.csv")
        print("Insert the links from your references (Leave 'reference link' blank to finish):")
        referencias = []

        while True:
            link = input("Reference link: ")
            if link == "":
                break
            nota = input("Notes: ")
            referencias.append({"link": link, "nota": nota})

        write_header = os.path.getsize(ref_file) == 0
        with open(ref_file, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["link", "nota"])
            if write_header:
                writer.writeheader()
            writer.writerows(referencias)

        print("References saved.")

