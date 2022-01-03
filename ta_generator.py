#!/usr/bin/python3
# -*- coding:utf-8 -*-
#
# Copyright (c) 2022-present Arnold Andreasson
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

import pathlib
import logging
import yaml
import subprocess
import zipfile


class GeneratorTadaridaD():
    """ """
    def __init__(self):
        """ """
        # Config.
        self.path_to_tadatrida = "TadaridaD"
        self.base_dir = ""
        self.regenerate = False
        self.clean_up_td = False
        self.zip_target_path = ""
        # Work.
        self.dir_list = []

    # def load_config(self, config_file="Tadarida-D/python/tadarida_config.yaml"):
    # def load_config(self, config_file="Tadarida-D/python/ta_generator_config.yaml"):
    def load_config(self, config_file="ta_generator_config.yaml"):
        """ """
        config_path = pathlib.Path(config_file)
        with open(config_path) as file:
            dwca_config = yaml.load(file, Loader=yaml.FullLoader)

        if "pathToTadatridaD" in dwca_config:
            self.tadatrida_d = dwca_config["pathToTadatridaD"]
        if "baseDir" in dwca_config:
            self.base_dir = dwca_config["baseDir"]
        if "zipTargetPath" in dwca_config:
            self.zip_target_path = dwca_config["zipTargetPath"]

    def build_dir_list(self):
        """ """
        self.dir_list = []
        base_dir_path = pathlib.Path(self.base_dir)
        tmp_dir_list = [f for f in base_dir_path.iterdir() if f.is_dir()]
        # Only use directories containing wav files.
        for tmp_dir in tmp_dir_list:
            # print("DEBUG: dir:", tmp_dir)
            wav_files = list(pathlib.Path(tmp_dir).glob('*.wav'))
            # print("DEBUG: wav:", str(wav_files))
            if len(wav_files) > 0:
                self.dir_list.append(str(tmp_dir))
        # print("DEBUG: wav:", str(self.dir_list))

    def generate_ta(self):
        """ """
        # print("DEBUG: tadatrida_d: ", self.tadatrida_d)
        # print("DEBUG: dir_list: ", self.dir_list)

        for wav_dir in sorted(self.dir_list):
            print("\nDEBUG: Generates: ", wav_dir)
            list_files = subprocess.run([self.tadatrida_d, wav_dir])
            print("Finished with exit code: %d" % list_files.returncode)

    def cleanup(self):
        """ """
        for wav_dir in sorted(self.dir_list):
            print("\nDEBUG: Cleanup: ", wav_dir)

            # Get list of wav files.

            # Iterate over ta files. Remove if on wav file.

    def create_zip(self):
        """ """
        zip_target_path = pathlib.Path(self.zip_target_path)
        if not zip_target_path.exists():
            zip_target_path.mkdir(parents=True)

        # for wav_dir in sorted(self.dir_list):
        #     print("\nDEBUG: Cleanup: ", wav_dir)

        # Get list of wav files.
        ta_files = list(pathlib.Path(self.base_dir).glob('**/*.ta'))
        for ta_file in ta_files:
            print("DEBUG: TA-file: ", ta_file)

        # Zip...
        zip_target_file = pathlib.Path(zip_target_path, "tadarida_ta_files.zip")
        with zipfile.ZipFile(zip_target_file,"w", zipfile.ZIP_DEFLATED) as zip:
                # writing each file one by one
                for file in ta_files:
                    file_zip_path = str(file).replace("/mnt/usb4tb/rec2022", "")
                    zip.write(file, file_zip_path)



# MAIN.
if __name__ == "__main__":
    """ """
    generator = GeneratorTadaridaD()
    generator.load_config()
    generator.build_dir_list()
    # generator.generate_ta()
    # generator.cleanup()
    generator.create_zip()
