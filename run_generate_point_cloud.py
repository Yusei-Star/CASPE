# run_main.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import argparse
import DEMO_MICRO_ENV

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Generate point cloud data for APCNet model')
    
    # Dataset parameters
    parser.add_argument('--input_dir', '-i', type=str, default='resources/dataset/data_for_Micro_Env/pred/pqr', help='PQR directory path')
    parser.add_argument('--json_pqr_site', '-j', type=str, default='resources/dataset/data_for_Micro_Env/pred/pqr_site.json', help='critical sites file path')
    parser.add_argument('--output_dir', '-o',type=str, default='resources/dataset/data_for_APCNet',help='H5 output directory path, generate for APCNet')

    args = parser.parse_args()
    DEMO_MICRO_ENV.mian_generate_point_cloud(args.input_dir, args.json_pqr_site, args.output_dir)
    print('Done!')