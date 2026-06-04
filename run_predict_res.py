# run_main.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import argparse
import DEMO_APCNet

if __name__ == "__main__":

    parser = argparse.ArgumentParser('predict best residue')
    
    parser.add_argument('--checkpoint', '-c', type=str, default='resources/checkpoint',help='path to load checkpoint')
    parser.add_argument('--model_type', '-m', type=str, default='APCNetT', choices=['APCNetT', 'APCNetT-1st', 'APCNetAA', 'APCNetAL'], 
                        help='APCNetT for thermostability, APCNetAA for acid-tolerance, APCNetAL for alkaline-tolerance')
    parser.add_argument('--weights_type', '-w', type=str, default='best', choices=['best', 'last'], 
                        help='best for best model weights, last for last model weights')
    parser.add_argument('--input_path', '-i', type=str, default='resources/dataset/data_for_APCNet/pred', help='predict dataset path')
    parser.add_argument('--output_file', '-o', type=str, default='output/aa_pred.csv', help='result file name')
    
    args = parser.parse_args()
    DEMO_APCNet.main_predict_res(args.checkpoint, args.model_type, args.weights_type, args.input_path, args.output_file)

    print("Done!")
