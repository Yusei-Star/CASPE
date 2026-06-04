# run_main.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import argparse
import DEMO_CAS

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='locating critical residues in proteins')
    
    parser.add_argument('--checkpoint', '-c', type=str, default="resources/checkpoint",help='Model checkpoint location')
    parser.add_argument('--model_type', '-m', type=str, default="CASPET-2",  choices=["CASPET-1", "CASPET-2", "CASPET-3","CASPET-4", "CASPEA"], help='model_type for CAS, CASPET for thermostability and CASPEA for pH tolerance')
    parser.add_argument('--num_cutoff', '-n', type=int, default=5, help='residues to be selected, num_cutoff*3 will be selected')
    parser.add_argument('--input_file', '-i', type=str, default="resources/dataset/data_for_CAS/locate.txt", help='input file for fasta sequences')
    parser.add_argument('--output_file', '-o', type=str, default="output/test_CAS_value.json", help='output file for CAS result values')
    
    args = parser.parse_args()
    DEMO_CAS.main_get_site(args.checkpoint, args.model_type, args.num_cutoff, args.input_file, args.output_file)
    
    print("Done!")
    