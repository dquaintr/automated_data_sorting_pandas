"""

"""
#import pandas and read the excel file
import pandas as pd


input_file = 'C:/Users/ar-daniel.quaintrell/Documents/test.xlsx'
output_file = 'C:/Users/ar-daniel.quaintrell/Documents/finished_file3.xlsx'


class CUFiltering:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def gnb_id_filtering(self):
        build_info_df = pd.read_excel(input_file)
        if build_info_df.empty:
            print('File is Empty!!!')
        else:
            #create new dataframe where condition is met
            output_df = build_info_df[build_info_df["gNodeb_Id"]> 100000]
            col_list = ["gNodeb_Id", "Build"]
            output_df = output_df[col_list]
            output_df.to_excel(output_file, index=False)

    def execute(self):
        self.read_validate_input_file()


if __name__ == '__main__':
    _obj = CUFiltering(input_file, output_file)
    _obj.gnb_id_filtering()
