$ python3 AE_run.py -p1 data/rna.csv 
                    -p2 data/prot.csv 
                    -p3 data/scnv.csv 
                    -m 0 -s 0 -d cpu
Training model...
epoch: 1 | loss: 4.7630
epoch: 2 | loss: 4.2692
epoch: 3 | loss: 3.9827
epoch: 4 | loss: 3.8254
epoch: 5 | loss: 3.7433
epoch: 6 | loss: 3.6917
epoch: 7 | loss: 3.6653
epoch: 8 | loss: 3.6447
epoch: 9 | loss: 3.6317
epoch: 10 | loss: 3.6186
epoch: 11 | loss: 3.6113
epoch: 12 | loss: 3.6042
epoch: 13 | loss: 3.5968
epoch: 14 | loss: 3.5968
epoch: 15 | loss: 3.5932
epoch: 16 | loss: 3.5900
epoch: 17 | loss: 3.5866
epoch: 18 | loss: 3.5833
epoch: 19 | loss: 3.5786
epoch: 20 | loss: 3.5792
epoch: 21 | loss: 3.5783
epoch: 22 | loss: 3.5707
epoch: 23 | loss: 3.5672
epoch: 24 | loss: 3.5658
epoch: 25 | loss: 3.5644
epoch: 26 | loss: 3.5587
epoch: 27 | loss: 3.5562
epoch: 28 | loss: 3.5506
epoch: 29 | loss: 3.5473
epoch: 30 | loss: 3.5395
epoch: 31 | loss: 3.5354
epoch: 32 | loss: 3.5274
epoch: 33 | loss: 3.5248
epoch: 34 | loss: 3.5179
epoch: 35 | loss: 3.5100
epoch: 36 | loss: 3.5033
epoch: 37 | loss: 3.4923
epoch: 38 | loss: 3.4901
epoch: 39 | loss: 3.4763
epoch: 40 | loss: 3.4749
epoch: 41 | loss: 3.4608
epoch: 42 | loss: 3.4556
epoch: 43 | loss: 3.4470
epoch: 44 | loss: 3.4323
epoch: 45 | loss: 3.4222
epoch: 46 | loss: 3.4142
epoch: 47 | loss: 3.4011
epoch: 48 | loss: 3.3907
epoch: 49 | loss: 3.3806
epoch: 50 | loss: 3.3726
epoch: 51 | loss: 3.3689
epoch: 52 | loss: 3.3518
epoch: 53 | loss: 3.3418
epoch: 54 | loss: 3.3295
epoch: 55 | loss: 3.3167
epoch: 56 | loss: 3.3028
epoch: 57 | loss: 3.3000
epoch: 58 | loss: 3.2906
epoch: 59 | loss: 3.2701
epoch: 60 | loss: 3.2594
epoch: 61 | loss: 3.2540
epoch: 62 | loss: 3.2446
epoch: 63 | loss: 3.2286
epoch: 64 | loss: 3.2142
epoch: 65 | loss: 3.2048
epoch: 66 | loss: 3.1983
epoch: 67 | loss: 3.1878
epoch: 68 | loss: 3.1785
epoch: 69 | loss: 3.1632
epoch: 70 | loss: 3.1542
epoch: 71 | loss: 3.1451
epoch: 72 | loss: 3.1337
epoch: 73 | loss: 3.1281
epoch: 74 | loss: 3.1167
epoch: 75 | loss: 3.1035
epoch: 76 | loss: 3.0971
epoch: 77 | loss: 3.0954
epoch: 78 | loss: 3.0713
epoch: 79 | loss: 3.0740
epoch: 80 | loss: 3.0624
epoch: 81 | loss: 3.0470
epoch: 82 | loss: 3.0352
epoch: 83 | loss: 3.0274
epoch: 84 | loss: 3.0246
epoch: 85 | loss: 3.0187
epoch: 86 | loss: 2.9962
epoch: 87 | loss: 2.9945
epoch: 88 | loss: 2.9960
epoch: 89 | loss: 2.9920
epoch: 90 | loss: 2.9742
epoch: 91 | loss: 2.9592
epoch: 92 | loss: 2.9482
epoch: 93 | loss: 2.9459
epoch: 94 | loss: 2.9364
epoch: 95 | loss: 2.9333
epoch: 96 | loss: 2.9104
epoch: 97 | loss: 2.9167
epoch: 98 | loss: 2.9037
epoch: 99 | loss: 2.8956
epoch: 100 | loss: 2.8759
Get the latent layer output...
/home/azureuser/MoGCN_br/AE_run.py:42: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/MMAE_model.pkl')
Extract features...
  0%|                                                                                                                                    | 0/10 [00:00<?, ?it/s]/home/azureuser/MoGCN_br/AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
 10%|████████████▍                                                                                                               | 1/10 [00:01<00:11,  1.28s/it]/home/azureuser/MoGCN_br/AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
 20%|████████████████████████▊                                                                                                   | 2/10 [00:02<00:10,  1.28s/it]/home/azureuser/MoGCN_br/AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
 30%|█████████████████████████████████████▏                                                                                      | 3/10 [00:03<00:09,  1.30s/it]/home/azureuser/MoGCN_br/AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
 40%|█████████████████████████████████████████████████▌                                                                          | 4/10 [00:05<00:07,  1.31s/it]/home/azureuser/MoGCN_br/AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
 50%|██████████████████████████████████████████████████████████████                                                              | 5/10 [00:06<00:06,  1.31s/it]/home/azureuser/MoGCN_br/AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
 60%|██████████████████████████████████████████████████████████████████████████▍                                                 | 6/10 [00:07<00:05,  1.32s/it]/home/azureuser/MoGCN_br/AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
 70%|██████████████████████████████████████████████████████████████████████████████████████▊                                     | 7/10 [00:09<00:03,  1.31s/it]/home/azureuser/MoGCN_br/AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
 80%|███████████████████████████████████████████████████████████████████████████████████████████████████▏                        | 8/10 [00:10<00:02,  1.30s/it]/home/azureuser/MoGCN_br/AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
 90%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████▌            | 9/10 [00:11<00:01,  1.30s/it]/home/azureuser/MoGCN_br/AE_run.py:84: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  mmae = torch.load('model/AE/model_{}.pkl'.format(epoch))
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10/10 [00:13<00:00,  1.30s/it]
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
#
#
#
#
#
#
#

$ python3 SNF.py -p data/rna.csv \
                    data/prot.csv \
                    data/scnv.csv \
                    -m seuclidean
Load data files...
(122, 10735) (122, 7748) (122, 23693)
Start similarity network fusion...
Save fused adjacency matrix...
/home/azureuser/.local/lib/python3.12/site-packages/seaborn/matrix.py:560: UserWarning: Clustering large matrix with scipy. Installing `fastcluster` may give better performance.
  warnings.warn(msg)
/home/azureuser/.local/lib/python3.12/site-packages/seaborn/matrix.py:530: ClusterWarning: scipy.cluster: The symmetric non-negative hollow observation matrix looks suspiciously like an uncondensed distance matrix
  linkage = hierarchy.linkage(self.array, method=self.method,
/home/azureuser/.local/lib/python3.12/site-packages/seaborn/matrix.py:560: UserWarning: Clustering large matrix with scipy. Installing `fastcluster` may give better performance.
  warnings.warn(msg)
/home/azureuser/.local/lib/python3.12/site-packages/seaborn/matrix.py:530: ClusterWarning: scipy.cluster: The symmetric non-negative hollow observation matrix looks suspiciously like an uncondensed distance matrix
  linkage = hierarchy.linkage(self.array, method=self.method,
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
                     -ts data/test_sample.csv 
                     -m 1 -d gpu -p 20
loading data...
Calculating the laplace adjacency matrix...
Begin training model...
Epoch: 10.00 | loss train: 1.5981 | acc train: 0.4943
Epoch: 20.00 | loss train: 1.4515 | acc train: 0.4943
Epoch: 30.00 | loss train: 1.4190 | acc train: 0.5057
Epoch: 40.00 | loss train: 1.4831 | acc train: 0.5057
Epoch: 50.00 | loss train: 1.4872 | acc train: 0.5057
Training finished.
The best epoch model is  29
/home/azureuser/MoGCN_br/GCN_run.py:214: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  GCN_model.load_state_dict(torch.load('model/GCN/{}.pkl'.format(best_epoch)))
Finished!

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
                     -ts data/test_sample.csv 
                     -m 1 -d gpu -p 20
                     
Using device: cpu
Loading data...
loading data...
Calculating the laplace adjacency matrix...

Calculating class weights...
Class distribution: {0: 15, 1: 4, 2: 50, 3: 20, 4: 4, 5: 22, 6: 3, 7: 4}
Class weights: {0: 1.0166667, 1: 3.8125, 2: 0.305, 3: 0.7625, 4: 3.8125, 5: 0.6931818, 6: 5.0833335, 7: 3.8125}

Starting train-test mode...
/home/azureuser/.local/lib/python3.12/site-packages/torch/optim/lr_scheduler.py:62: UserWarning: The verbose parameter is deprecated. Please use get_last_lr() to access the learning rate.
  warnings.warn(
Epoch:  10 | Loss: 2.0047 | Acc: 0.2759
Training predictions: {1: 12, 2: 46, 3: 2, 5: 19, 6: 8}
Epoch:  20 | Loss: 1.9196 | Acc: 0.3103
Training predictions: {1: 9, 2: 32, 3: 4, 5: 29, 6: 7, 7: 6}
Epoch:  30 | Loss: 1.9220 | Acc: 0.2529
Training predictions: {1: 17, 2: 33, 3: 2, 5: 26, 6: 3, 7: 6}
Epoch:  40 | Loss: 1.9380 | Acc: 0.2069
Training predictions: {1: 18, 2: 22, 3: 6, 5: 24, 6: 4, 7: 13}
Epoch:  50 | Loss: 1.9604 | Acc: 0.2644
Training predictions: {1: 11, 2: 31, 3: 5, 5: 24, 6: 10, 7: 6}
Epoch:  60 | Loss: 1.9200 | Acc: 0.2414
Training predictions: {1: 18, 2: 27, 3: 1, 5: 25, 6: 8, 7: 8}
Epoch:  70 | Loss: 1.9414 | Acc: 0.2069
Training predictions: {1: 14, 2: 28, 3: 5, 5: 25, 6: 5, 7: 10}
Early stopping at epoch 74

Training finished. Best epoch: 54
/home/azureuser/MoGCN_br/GCN_run.py:190: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  checkpoint = torch.load('model/GCN/best_model.pkl')

Evaluating on test set...

Raw logits (first 3 samples):
tensor([[-0.5108,  0.4718,  0.5808,  0.2779, -1.5153,  0.4929,  0.3216,  0.4083],
        [-0.5108,  0.4718,  0.5808,  0.2779, -1.5153,  0.4929,  0.3216,  0.4083],
        [-0.5108,  0.4718,  0.5808,  0.2779, -1.5153,  0.4929,  0.3216,  0.4083]])

Predictions distribution:
{2: 35}

Test results: Loss=2.3956, Acc=0.1714, F1=0.0502

Prediction probabilities (first 3 samples):
tensor([[0.0597, 0.1595, 0.1778, 0.1314, 0.0219, 0.1629, 0.1372, 0.1497],
        [0.0597, 0.1595, 0.1778, 0.1314, 0.0219, 0.1629, 0.1372, 0.1497],
        [0.0597, 0.1595, 0.1778, 0.1314, 0.0219, 0.1629, 0.1372, 0.1497]])
Finished!
azureuser@mybigvm:~/MoGCN_br$ 

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
                     -ts data/test_sample.csv 
                     -m 1 -d gpu -p 20

Using device: cpu
Loading data...
Loading data...
Processing adjacency matrix...
Normalizing features...

Calculating class weights...
Class distribution: {0: 29, 1: 14, 2: 57, 3: 17, 4: 5}
Class weights: {0: 0.8413793, 1: 1.7428571, 2: 0.4280702, 3: 1.4352942, 4: 4.88}

Starting train-test mode...
/home/azureuser/.local/lib/python3.12/site-packages/torch/optim/lr_scheduler.py:62: UserWarning: The verbose parameter is deprecated. Please use get_last_lr() to access the learning rate.
  warnings.warn(
Epoch:  10 | Loss: 1.4597 | Acc: 0.4598
Training predictions: {0: 7, 1: 24, 2: 20, 3: 20, 4: 16}
Epoch:  20 | Loss: 1.1772 | Acc: 0.6552
Training predictions: {0: 10, 1: 15, 2: 22, 3: 28, 4: 12}
Epoch:  30 | Loss: 1.0059 | Acc: 0.6552
Training predictions: {0: 12, 1: 11, 2: 22, 3: 28, 4: 14}
Epoch:  40 | Loss: 0.8252 | Acc: 0.7126
Training predictions: {0: 15, 1: 10, 2: 22, 3: 31, 4: 9}
Epoch:  50 | Loss: 0.7195 | Acc: 0.7471
Training predictions: {0: 15, 1: 7, 2: 28, 3: 26, 4: 11}
Epoch:  60 | Loss: 0.6038 | Acc: 0.7931
Training predictions: {0: 14, 1: 7, 2: 30, 3: 24, 4: 12}
Epoch:  70 | Loss: 0.6099 | Acc: 0.7816
Training predictions: {0: 14, 1: 12, 2: 27, 3: 25, 4: 9}
Epoch:  80 | Loss: 0.5996 | Acc: 0.8161
Training predictions: {0: 15, 1: 11, 2: 32, 3: 21, 4: 8}
Epoch:  90 | Loss: 0.6099 | Acc: 0.7816
Training predictions: {0: 14, 1: 13, 2: 31, 3: 22, 4: 7}
Epoch: 100 | Loss: 0.5563 | Acc: 0.8276
Training predictions: {0: 14, 1: 11, 2: 32, 3: 22, 4: 8}
Epoch: 110 | Loss: 0.6109 | Acc: 0.7931
Training predictions: {0: 15, 1: 10, 2: 31, 3: 23, 4: 8}
Early stopping at epoch 118

Training finished. Best epoch: 98
/home/azureuser/MoGCN_br/GCN_run.py:190: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  checkpoint = torch.load('model/GCN/best_model.pkl')

Evaluating on test set...

Raw logits (first 3 samples):
tensor([[ 3.4772,  0.6877, -3.5212, -1.0820,  0.0340],
        [ 1.7355,  1.3732, -2.5318, -2.3984,  1.4394],
        [ 3.1944,  0.7918, -3.1755, -1.8768,  0.6694]])

Predictions distribution:
{0: 13, 1: 3, 2: 12, 3: 6, 4: 1}

--
Test results: Loss=0.5862, Acc=0.8000, F1=0.8538
-- 

Prediction probabilities (first 3 samples):
tensor([[9.0514e-01, 5.5623e-02, 8.2667e-04, 9.4769e-03, 2.8930e-02],
        [4.0487e-01, 2.8184e-01, 5.6762e-03, 6.4866e-03, 3.0112e-01],
        [8.4852e-01, 7.6772e-02, 1.4529e-03, 5.3242e-03, 6.7929e-02]])
Finished!
