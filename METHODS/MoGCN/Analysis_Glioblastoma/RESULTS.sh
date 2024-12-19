$ python3 AE_run.py -p1 data/rna1.csv 
                    -p2 data/prot1.csv 
                    -p3 data/meth1.csv 
                    -m 0 -s 0 -d cpu -bs 32
Training model with batch size 32...
epoch: 1 | loss: 1.3145
epoch: 2 | loss: 0.3683


...


epoch: 98 | loss: 0.0995
epoch: 99 | loss: 0.1023
epoch: 100 | loss: 0.1012
Get the latent layer output...
Extract features...
  0%|                                           | 0/10 [00:00<....
 10%|████▏                                     | 1/10 [00:00<00:04,  
 20%|████████▍                                 | 2/10 [00:01<00:04,  
 30%|████████████▌                              | 3/10 [00:01<00:03,  
 40%|████████████████▊                         | 4/10 [00:02<00:03,  
 50%|█████████████████████                      | 5/10 [00:02<00:02,  
 60%|█████████████████████████▏                | 6/10 [00:03<00:02,  
 70%|█████████████████████████████▍            | 7/10 [00:04<00:01,  
 80%|█████████████████████████████████▌         | 8/10 [00:04<00:01,  
 90%|█████████████████████████████████████▊    | 9/10 [00:05<00:00,  
100%|█████████████████████████████████████████  | 10/10 [00:05<00:00,  1.78it/s]
#
#
#
#
#
#
#
#
#
#
$ python3 SNF.py -p data/rna1.csv 
                    data/prot1.csv 
                    data/meth1.csv 
                    -m seuclidean
Load data files...
(97, 1201) (97, 8359) (97, 1201)
Start similarity network fusion...
Save fused adjacency matrix...
Success! Results can be seen in result file
#
#
#
#
#
#
#
#
#
#
$ python3 GCN_run.py -fd result/latent_data.csv 
                     -ad result/SNF_fused_matrix.csv 
                     -ld data/sample_classes.csv 
                     -ts data/test_sample.csv -m 1 -d gpu -p 20
loading data...
Calculating the laplace adjacency matrix...
Begin training model...
Epoch: 10.00 | loss train: 0.8710 | acc train: 0.7037
Epoch: 20.00 | loss train: 0.6885 | acc train: 0.6667
Epoch: 30.00 | loss train: 0.6725 | acc train: 0.6296
Epoch: 40.00 | loss train: 0.6550 | acc train: 0.6667
Epoch: 50.00 | loss train: 0.7456 | acc train: 0.6667
Epoch: 60.00 | loss train: 0.6365 | acc train: 0.6296
Training finished.
The best epoch model is  42
[70 rows x 2 columns]
Finished!
azureuser@mybigvm:~/PROJECTS_ALL/MoGCN_Project/MoGCN$ 
