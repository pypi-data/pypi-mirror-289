"""Core module to extract fits files and insert into db"""

from ..fits import FitsFile
from ..config import get_configs
import os
from pathlib import Path
from tqdm import tqdm
import pandas as pd
from ..adapters import DBWriter
import logging
from datetime import datetime


# Use the configured logger
log = logging.getLogger('fits2db')


def get_all_fits(paths: list)->list:
    """Searches recursive throught all folders of given list of paths for 
    fits files and gives them back.
    Args:
        paths (list): A list of paths to search recursivly for fits files

    Returns:
        list: Returns list of absolute paths of all fits files
    """
    all_fits_files = []
    for path in paths:
        if os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    if file.endswith(".fits"):
                        all_fits_files.append(os.path.join(root, file))
        elif os.path.isfile(path) and path.endswith(".fits"):
            all_fits_files.append(path)
    return all_fits_files


def flatten_and_deduplicate(input_list):
    unique_values = set()
    flat_list = []

    def flatten(item):
        if isinstance(item, list):
            for sub_item in item:
                flatten(sub_item)
        else:
            if item not in unique_values:
                unique_values.add(item)
                flat_list.append(item)

    flatten(input_list)
    return flat_list


class Fits2db:
    def __init__(self, config_path:str):
        self.config_path = Path(config_path)
        self.configs = get_configs(config_path)
        self.fits_file_paths = self.get_file_names()

    def get_file_names(self) -> list:
        """Return list of all absolute filepaths found from sourced
        given in config file

        Returns:
            list: List of absolute paths
        """
        paths = self.configs["fits_files"]["paths"]
        log.debug(f"paths {paths}")
        log.info("run function")
        return list(dict.fromkeys(get_all_fits(paths)))
    
    def get_file_infos(self) -> pd.DataFrame:

        meta = []
        for path in self.fits_file_paths:
            path = Path(path)
            absolute_path = path.resolve()
            file_meta = {
                "filename": path.name,
                "filepath":absolute_path.as_posix(),
                "last_file_mutation":datetime.fromtimestamp(os.path.getmtime(absolute_path))}
            meta.append(file_meta)
        df = pd.DataFrame(meta)
        log.debug(df)
        return df
        

    def get_table_names(self):
        self.all_table_names = []
        self.file_table_dict = {}
        for path in tqdm(self.fits_file_paths):
            path = Path(path)
            try:
                file = FitsFile(path)
                self.all_table_names.append(file.table_names)
                self.file_table_dict[path] = file.table_names
            except ValueError as err:
                log.error(err)

        self.all_table_names = flatten_and_deduplicate(self.all_table_names)
        return self.all_table_names, self.file_table_dict

    def create_table_matrix(self, output_format=None, output_file=None):
        all_table_names, file_table_dict = self.get_table_names()
        file_names = [path.name for path in file_table_dict.keys()]
        df = pd.DataFrame(index=file_names, columns=all_table_names)
        for path, tables in file_table_dict.items():
            file_name = path.name
            for table in tables:
                df.at[file_name, table] = "X"

        df = df.fillna("")

        if output_format and file_name:
            current_dir = os.getcwd()
            full_file_path = os.path.join(current_dir, output_file)
            if output_format.lower() == "csv":
                df.to_csv(full_file_path)
            elif output_format.lower() == "excel":
                df.to_excel(full_file_path, index=True)

        return df


    def build(self, reset:bool=True):
        log.debug(f"Start building db with reset = {reset}")
        writer = DBWriter(self.configs)
        if reset:
            writer.clean_db()
            log.debug("Clean db success start uploading files")
        for path in tqdm(self.fits_file_paths):
            path = Path(path)
            try:
                file = FitsFile(path)
                writer = DBWriter(self.configs, file)
                writer.upsert()

            except ValueError as err:
                log.error(f"\n {err}")

    def update_db(self):
        file_infos = self.get_file_infos()
        log.info(file_infos)
        writer = DBWriter(self.configs)
        db_file_infos = writer.get_db_file_infos()
        log.info(db_file_infos)
        merged_df = pd.merge(file_infos, db_file_infos, on=['filename', 'filepath'], how='left', suffixes=('_file', '_db'))


        filtered_df = merged_df[
            (merged_df['last_file_mutation_file'] > merged_df['last_file_mutation_db']) | 
            merged_df['last_file_mutation_db'].isna()
        ]

        result_df = filtered_df[['filename', 'filepath', 'last_file_mutation_file']].rename(
            columns={'last_file_mutation_file': 'last_file_mutation'}
        )
        log.info(result_df)
        fits_file_paths = result_df["filepath"].to_list()
        for path in tqdm(fits_file_paths):
            path = Path(path)
            try:
                file = FitsFile(path)
                writer = DBWriter(self.configs, file)
                writer.upsert()

            except ValueError as err:
                log.error(f"\n {err}")


    def upsert_to_db(self):
        log.debug("Start upsert to db")
        writer = DBWriter(self.configs)
        writer.clean_db()
        log.debug("Clean db success start uploading files")
        for path in tqdm(self.fits_file_paths):
            path = Path(path)
            try:
                file = FitsFile(path)
                writer = DBWriter(self.configs, file)
                writer.upsert()

            except ValueError as err:
                log.error(f"\n {err}")
