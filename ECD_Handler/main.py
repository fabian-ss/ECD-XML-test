import os
import json
import xml.etree.ElementTree as ET

class ECDHandler:

    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        default_config = {
            "custom_dir": "",  # Custom directory
            "xml_dir": "xml repo",
            "liquidacion_num": 0
        }
        try:
            with open("config.json", "r") as f:
                config = json.load(f)
            # Combine the loaded configuration with the default configuration
            default_config.update(config)
        except FileNotFoundError:
            # If the file is not found, the default settings are used
            pass
        return default_config

    def get_home_dir(self):
        return os.path.expanduser("~")


    def sumar_montos_xml(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Get all possible values ​​of "num_liq" in XML file
        liquidacion_nums = {int(liq.get("num_liq")) for liq in root.findall('.//liquidacion')}

        # Check if the value of "liquidacion_num" is within the valid range
        if self.config["liquidacion_num"] not in liquidacion_nums:
            file_name = os.path.basename(xml_file)
            print(f"The value of 'liquidacion_num' in the configuration ({self.config['liquidacion_num']}) is not found in the XML file '{file_name}'. Continuing with the next file.\n")
            return None  # Return 0 or any other default value

        total_facturas = 0.0
        for factura in root.findall('.//liquidacion[@num_liq="{}"]/facturas/factura'.format(self.config["liquidacion_num"])):
            for concepto in factura.findall('.//concepto'):
                monto_total = concepto.find('monto_total')
                if monto_total is not None:
                    total_facturas += float(monto_total.text)

        return total_facturas

    def process_files_dir(self, files):
        for file in files:
            file_msg_aux = ["", "", '-' * 30]
            file_msg_aux[0] = os.path.basename(file)

            total_facturas = self.sumar_montos_xml(file)
            if total_facturas is not None:
                print("File name:", os.path.basename(file))
                print("Total invoice amount:", total_facturas, end="\n\n")

    def main(self):
        if self.config["custom_dir"]:
            current_dir = self.config["custom_dir"]
        else:
            current_dir = os.path.dirname(os.path.abspath(__file__))

        xml_files_dir = os.path.join(current_dir, self.config["xml_dir"])  # Directory containing the XML files

        # Check if xml repo directory exists
        if not os.path.exists(xml_files_dir):
            print(f"The directory {self.config['xml_dir']} does not exist.")
            print("Full path:", xml_files_dir)
            return

        # Get the list of XML files in the directory
        files = [os.path.join(xml_files_dir, f) for f in os.listdir(xml_files_dir) if f.endswith(".xml")]

        if not files:
            print(f"No XML files found in the directory {self.config['xml_dir']}.")
            print("Full path:", xml_files_dir)
            return

        files = sorted(files)  # Sort files alphabetically by name

        print("\n# ECD Handler Program\n")
        print("Files will be selected from:", xml_files_dir + "\n")

        self.process_files_dir(files)

if __name__ == "__main__":
    handler = ECDHandler()
    handler.main()