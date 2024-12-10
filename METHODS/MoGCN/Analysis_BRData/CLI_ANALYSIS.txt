cloudycris4@krinux:~/MoGCN$ python3 AE_run.py -p1 data/rna.csv -p2 data/prot.csv -p3 data/mut.csv -m 0 -s 0 -d cpu
Training model...
epoch: 1 | loss: 3.6049
epoch: 2 | loss: 3.1737
epoch: 3 | loss: 2.9413
epoch: 4 | loss: 2.8283
epoch: 5 | loss: 2.7745
epoch: 6 | loss: 2.7459
epoch: 7 | loss: 2.7283
epoch: 8 | loss: 2.7172
epoch: 9 | loss: 2.7089
epoch: 10 | loss: 2.7034
epoch: 11 | loss: 2.6959
epoch: 12 | loss: 2.6927
epoch: 13 | loss: 2.6897
epoch: 14 | loss: 2.6856
epoch: 15 | loss: 2.6843
epoch: 16 | loss: 2.6814
epoch: 17 | loss: 2.6783
epoch: 18 | loss: 2.6760
epoch: 19 | loss: 2.6738
epoch: 20 | loss: 2.6715
epoch: 21 | loss: 2.6683
epoch: 22 | loss: 2.6653
epoch: 23 | loss: 2.6639
epoch: 24 | loss: 2.6611
epoch: 25 | loss: 2.6578
epoch: 26 | loss: 2.6546
epoch: 27 | loss: 2.6502
epoch: 28 | loss: 2.6482
epoch: 29 | loss: 2.6434
epoch: 30 | loss: 2.6422
epoch: 31 | loss: 2.6345
epoch: 32 | loss: 2.6298
epoch: 33 | loss: 2.6255
epoch: 34 | loss: 2.6192
epoch: 35 | loss: 2.6135
epoch: 36 | loss: 2.6077
epoch: 37 | loss: 2.5998
epoch: 38 | loss: 2.5961
epoch: 39 | loss: 2.5850
epoch: 40 | loss: 2.5787
epoch: 41 | loss: 2.5716
epoch: 42 | loss: 2.5636
epoch: 43 | loss: 2.5537
epoch: 44 | loss: 2.5470
epoch: 45 | loss: 2.5357
epoch: 46 | loss: 2.5289
epoch: 47 | loss: 2.5205
epoch: 48 | loss: 2.5081
epoch: 49 | loss: 2.5003
epoch: 50 | loss: 2.4877
epoch: 51 | loss: 2.4781
epoch: 52 | loss: 2.4686
epoch: 53 | loss: 2.4581
epoch: 54 | loss: 2.4485
epoch: 55 | loss: 2.4357
epoch: 56 | loss: 2.4320
epoch: 57 | loss: 2.4160
epoch: 58 | loss: 2.4087
epoch: 59 | loss: 2.3967
epoch: 60 | loss: 2.3836
epoch: 61 | loss: 2.3802
epoch: 62 | loss: 2.3737
epoch: 63 | loss: 2.3631
epoch: 64 | loss: 2.3530
epoch: 65 | loss: 2.3420
epoch: 66 | loss: 2.3345
epoch: 67 | loss: 2.3200
epoch: 68 | loss: 2.3142
epoch: 69 | loss: 2.3072
epoch: 70 | loss: 2.2962
epoch: 71 | loss: 2.2879
epoch: 72 | loss: 2.2733
epoch: 73 | loss: 2.2765
epoch: 74 | loss: 2.2645
epoch: 75 | loss: 2.2429
epoch: 76 | loss: 2.2498
epoch: 77 | loss: 2.2313
epoch: 78 | loss: 2.2277
epoch: 79 | loss: 2.2130
epoch: 80 | loss: 2.2109
epoch: 81 | loss: 2.2014
epoch: 82 | loss: 2.1922
epoch: 83 | loss: 2.1885
epoch: 84 | loss: 2.1800
epoch: 85 | loss: 2.1781
epoch: 86 | loss: 2.1657
epoch: 87 | loss: 2.1585
epoch: 88 | loss: 2.1452
epoch: 89 | loss: 2.1449
epoch: 90 | loss: 2.1385
epoch: 91 | loss: 2.1331
epoch: 92 | loss: 2.1230
epoch: 93 | loss: 2.1160
epoch: 94 | loss: 2.1072
epoch: 95 | loss: 2.1045
epoch: 96 | loss: 2.1006
epoch: 97 | loss: 2.0962
epoch: 98 | loss: 2.0873
epoch: 99 | loss: 2.0753
epoch: 100 | loss: 2.0790
Get the latent layer output...
AE_run.py:42: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/MMAE_model.pkl')
Extract features...
  0%|                                                    | 0/10 [00:00<?, ?it/s]AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
 10%|████▍                                       | 1/10 [00:01<00:09,  1.09s/it]AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
 20%|████████▊                                   | 2/10 [00:02<00:08,  1.06s/it]AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
 30%|█████████████▏                              | 3/10 [00:03<00:07,  1.05s/it]AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
 40%|█████████████████▌                          | 4/10 [00:04<00:06,  1.05s/it]AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
 50%|██████████████████████                      | 5/10 [00:05<00:05,  1.06s/it]AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
 60%|██████████████████████████▍                 | 6/10 [00:06<00:04,  1.06s/it]AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
 70%|██████████████████████████████▊             | 7/10 [00:07<00:03,  1.06s/it]AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
 80%|███████████████████████████████████▏        | 8/10 [00:08<00:02,  1.05s/it]AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
 90%|███████████████████████████████████████▌    | 9/10 [00:09<00:01,  1.07s/it]AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
100%|███████████████████████████████████████████| 10/10 [00:10<00:00,  1.06s/it]
Success! Results can be seen in result file
cloudycris4@krinux:~/MoGCN$ 


python3 SNF.py -p data/rna.csv data/prot.csv data/mut.csv -m seuclidean
Load data files...
(122, 10735) (122, 7748) (122, 9449)
Start similarity network fusion...
Save fused adjacency matrix...
/home/cloudycris4/.local/lib/python3.8/site-packages/seaborn/matrix.py:560: UserWarning: Clustering large matrix with scipy. Installing `fastcluster` may give better performance.
  warnings.warn(msg)
/home/cloudycris4/.local/lib/python3.8/site-packages/seaborn/matrix.py:530: ClusterWarning: scipy.cluster: The symmetric non-negative hollow observation matrix looks suspiciously like an uncondensed distance matrix
  linkage = hierarchy.linkage(self.array, method=self.method,
/home/cloudycris4/.local/lib/python3.8/site-packages/seaborn/matrix.py:560: UserWarning: Clustering large matrix with scipy. Installing `fastcluster` may give better performance.
  warnings.warn(msg)
/home/cloudycris4/.local/lib/python3.8/site-packages/seaborn/matrix.py:530: ClusterWarning: scipy.cluster: The symmetric non-negative hollow observation matrix looks suspiciously like an uncondensed distance matrix
  linkage = hierarchy.linkage(self.array, method=self.method,
Success! Results can be seen in result file
cloudycris4@krinux:~/MoGCN$ 





python3 GCN_run.py -fd result/latent_data.csv -ad result/SNF_fused_matrix.csv -ld data/sample_classes.csv -ts data/test_sample.csv -m 1 -d gpu -p 20
loading data...
Calculating the laplace adjacency matrix...
Begin training model...
Traceback (most recent call last):
  File "GCN_run.py", line 207, in <module>
    name = file.split('\\')[1]
IndexError: list index out of range
cloudycris4@krinux:~/MoGCN$ 




python3 GCN_run.py -fd result/latent_data.csv -ad result/SNF_fused_matrix.csv -ld data/sample_classes.csv -ts data/test_sample.csv -m 1 -d gpu -p 20
loading data...
Calculating the laplace adjacency matrix...
Begin training model...
Epoch: 10.00 | loss train: 1.2424 | acc train: 0.5287
Epoch: 20.00 | loss train: 1.2226 | acc train: 0.5287
Epoch: 30.00 | loss train: 1.2072 | acc train: 0.5287
Training finished.
The best epoch model is  12
/home/azureuser/MoGCN_br/GCN_run.py:214: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  GCN_model.load_state_dict(torch.load('model/GCN/{}.pkl'.format(best_epoch)))
Finished!



