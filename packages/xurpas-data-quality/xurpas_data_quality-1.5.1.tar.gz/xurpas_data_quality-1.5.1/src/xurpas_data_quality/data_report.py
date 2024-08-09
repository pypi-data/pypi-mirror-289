import os
import warnings
from pathlib import Path
from typing import List, Tuple

import pandas as pd

from xurpas_data_quality.report import get_report, get_empty_report, get_comparison_report, get_error_report, get_test_report
from xurpas_data_quality.data import check_dtypes, describe, load_dataframe,validate_dataframe ,check_col_names, describe_invalid, check_data, convert_to_pandas
from xurpas_data_quality.config import Settings

warnings.filterwarnings("ignore", category=UserWarning, module='visions')

class DataReport:
    def __init__(self, 
                 file:str=None, 
                 df:pd.DataFrame|List[pd.DataFrame]|Tuple[pd.DataFrame,pd.DataFrame,List] =None, 
                 report_name:str=None, 
                 file_path:str=None,
                 data_types:dict=None,
                 minimal: bool=None,
                 **kwargs):
        
        """
        Initializes the DataReport object
        Args
            file:        The path of the file you want to analyze. If empty, df parameter must exist.
                         Only supports .csv, .xlsx, .parquet, and .orc file formats
            df:          Pandas DataFrame object of data to be analyzed, If using df, file must be empty.
            report_name: Name of the report. Defaults to 'Data Quality Report'
            file_path:   Path/ directory of where the report is to be saved
            data_types:  A dictionary containing the column names and their corresponding data types.
                         If empty, then the data types will be inferred.
            minimal:     Default is True. Check if you want minimal mode as your data report.
        """

        """Loading the config Section"""
        self.config = Settings()

        if report_name is not None:
            self.config.title=report_name
        if file_path is not None:
            def has_extension(file_path:str):
                return os.path.splitext(file_path)[1] != '' 
            
            if has_extension(file_path):
                self.config.file_path = file_path

            else:
                self.config.file_path = '/'.join([file_path,"report.html"])
                warnings.warn("File name not provided, saving as {file_path}/report.html")

        if not minimal:
            self.config.minimal = minimal

        """Checking dataframe input"""
        if isinstance(df, dict):
            df_frames = list(df.values())
            self.df = []
            for frame in df_frames:
                self.df.append(frame if isinstance(frame, pd.DataFrame) else convert_to_pandas(frame) )
                
            self.df_names = list(df.keys())
            self.render_empty = False

        elif isinstance(df, tuple):
            self.df = df[0] if isinstance(df[0], pd.DataFrame) else convert_to_pandas(df[0])
            self.df_invalid = df[1] if isinstance(df[1], pd.DataFrame) else convert_to_pandas(df[1])
            self.errors = df[2] if isinstance(df[2],list) else [df[2]]
            self.empty_df_invalid = True if not validate_dataframe(self.df_invalid) else False
            self.render_empty = True if not validate_dataframe(self.df) else False
        
        else:
            if file is not None:
                if df is not None:
                    raise KeyError("Only 'file' or 'df' should be used one at a time!")
                self.df = load_dataframe(file)

            else:
                if df is None:
                    raise ValueError("Please provide your data in 'file' or 'df' parameters!")
                
                self.df = df
                self.render_empty = True if not validate_dataframe(df) else False # checks if dataframe is empty

        """checking data types"""
        if data_types is not None:
            self.data_types = check_dtypes(check_col_names(data_types, df.columns))
        else:
            self.data_types = None

    def describe_dataframe(self):
        self.description = describe(df=self.df, data_types=self.data_types, config=self.config)
        if "cbs_shipment_distribution" in self.config.title:
            self.description.alerts = check_data(self.description.df)

    def describe_invalid_dataframe(self):
        self.description_invalid = describe_invalid(df=self.df_invalid, errors=self.errors, config=self.config)

    def get_data_quality_report(self, minimal:bool,report_name=None):
        self.describe_dataframe()
        report = get_report(self.description, minimal=minimal,name=report_name)
        return report.render()
    
    def _render_empty_report(self, name=None):
        report = get_empty_report(self.df, name)
        return report.render()
    
    def _render_comparison(self, name=None):
        self.describe_dataframe()
        report = get_comparison_report(self.description, self.df_names,name, self.config)
        return report.render()
    
    def _render_error_report(self, name=None):
        self.describe_invalid_dataframe()
        if self.render_empty:
            report = get_error_report(data=self.df,
                            invalid_data=self.description_invalid,
                            errors=self.errors, 
                            name = name, is_empty=self.render_empty, minimal=self.config.minimal)
        
        else:
            self.describe_dataframe()
            report = get_error_report(data=self.description,
                                    invalid_data=self.description_invalid,
                                    errors=self.errors, 
                                    name = name, is_empty=self.render_empty, minimal=self.config.minimal)
        return report.render()
    
    def __render_test_report(self):
        self.describe_dataframe()
        report = get_test_report(df=self.description, name=None)
        rendered_report = report.render()
        return rendered_report

    def to_file_test(self):
        output =Path(self.config.file_path)
        output.write_text(self.__render_test_report(), encoding='utf-8')

    def to_file(self):
        output = Path(self.config.file_path)
        if hasattr(self, 'errors'):
            print(f"saving error report as {self.config.file_path}")
            output.write_text(self._render_error_report(self.config.title), encoding='utf-8')
            print(f"saved!")

        elif self.render_empty:
            print(f"saving empty report as {self.config.file_path}")
            output.write_text(self._render_empty_report(self.config.title), encoding='utf-8')
            print("saved!")

        elif isinstance(self.df, list):
            print(f"saving comparison report!")
            output.write_text(self._render_comparison(self.config.title), encoding='utf-8')
            print('saved!')
        
        else:
            print(f"saving as {self.config.file_path}")
            if self.config.minimal:
                print("saving minimal version of report!")
                from minify_html import minify
                minified_report = minify(self.get_data_quality_report(self.config.minimal, self.config.title))
                output.write_text(minified_report, encoding='utf-8')
            else:
                output.write_text(self.get_data_quality_report(self.config.minimal, self.config.title), encoding='utf-8')
            
            print(f"saved!")