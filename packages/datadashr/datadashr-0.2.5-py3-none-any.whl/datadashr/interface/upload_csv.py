import panel as pn
import pandas as pd
import os
import glob
import uuid
import polars as pl
from datadashr import DataDashr
from datadashr.config import logger

class UploadCSVPage:
    def __init__(self):
        self.file_input = pn.widgets.FileInput(name='Upload CSV', accept='.csv')
        self.upload_button = pn.widgets.Button(name='Upload', button_type='primary')
        self.folder_input = pn.widgets.TextInput(name='Folder Path', placeholder='Enter path to the folder containing CSV files')
        self.load_folder_button = pn.widgets.Button(name='Load Folder', button_type='primary')
        self.df = None
        self.view = self.create_view()

    def create_view(self):
        return pn.Column(
            pn.pane.Markdown("# Upload CSV"),
            self.file_input,
            self.upload_button,
            pn.pane.Markdown("# Load CSVs from Folder"),
            self.folder_input,
            self.load_folder_button,
        )

    def upload_csv(self, event):
        if not self.file_input.value:
            logger.error("File CSV non caricato. Carica un file per continuare.")
            return

        # Directory per salvare i file CSV
        csv_directory = 'your_csv_directory'

        # Assicurati che la directory esista
        if not os.path.exists(csv_directory):
            os.makedirs(csv_directory)

        # Genera un nome file casuale per evitare conflitti
        file_name = f"{uuid.uuid4()}.csv"
        file_path = os.path.join(csv_directory, file_name)

        # Crea il file e scrivi il contenuto del file input
        with open(file_path, 'wb') as f:
            f.write(self.file_input.value)

        import_data = {
            'sources': [
                {
                    "source_name": "uploaded_csv",
                    "file_path": file_path,
                    "source_type": "csv",
                    "description": "Uploaded CSV file for analysis.",
                },
            ],
        }

        self.df = DataDashr(
            data=import_data,
            verbose=False,
            enable_cache=True,
            format_type='panel',
            reset_db=True,
        )

        try:
            self.df.df = pl.read_csv(file_path, infer_schema_length=10000, null_values=['-', ''])
        except Exception as e:
            logger.error(f"Error {e} decoding the CSV file. Try loading a file with a different encoding.")
            return

    def load_folder(self, event):
        folder_path = self.folder_input.value
        self.load_all_csv_from_folder(folder_path)

    def load_all_csv_from_folder(self, folder_path):
        csv_files = glob.glob(os.path.join(folder_path, '*.csv'))
        for csv_file in csv_files:
            try:
                data = pd.read_csv(csv_file)
                # Process the CSV file as needed
                print(f"Loaded {csv_file}")
            except Exception as e:
                print(f"Failed to load {csv_file}: {e}")
