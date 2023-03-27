import os

print("\nRun HR-VITON to generate final image\n")
print(os.getcwd())
terminnal_command = "python og_test_generator.py --cuda True --test_name aa --tocg_checkpoint ./eval_models/weights/v0.1/mtviton.pth --gpu_ids 0 --gen_checkpoint ./eval_models/weights/v0.1/gen.pth --datasetting unpaired --data_list test_pairs.txt --dataroot ./data3 --output_dir ./output"
os.system(terminnal_command)