python3 GCN_run.py \
  -fd result/latent_data.csv \
  -ad result/SNF_fused_matrix.csv \
  -ld Giodata/sample_classes.csv \
  -ts Giodata/test_sample.csv \
  -m 1 -d gpu -p 20
Loading data...
Calculating the Laplacian adjacency matrix...
Begin training model...
Epoch: 10.00 | loss train: 0.8953 | acc train: 0.3421
Epoch: 20.00 | loss train: 0.7086 | acc train: 0.4868
Epoch: 30.00 | loss train: 0.7486 | acc train: 0.4737
Epoch: 40.00 | loss train: 0.7076 | acc train: 0.5000
Epoch: 50.00 | loss train: 0.7160 | acc train: 0.5132
Training finished.
The best epoch model is  33

-

/home/azureuser/MoGCN_/GCN_run.py:197: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  GCN_model.load_state_dict(torch.load(f'model/GCN/{best_epoch}.pkl'))
Finished!

-


azureuser@mybigvm:~/MoGCN_$ 

py test.py 
['Sample', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']

/home/azureuser/PROJECTS_ALL/Python/MoGCN/test.py:61: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.

-

  GCN_model.load_state_dict(torch.load(model_path))
  Sample_ID
0   A1-A0SF
1   A1-A0SJ
2   A1-A0SK
3   A1-A0SO
4   A1-A0SQ
Test set results: Accuracy = 0.7647, F1 Score = 0.7059
     Sample  Predicted_Label
0   A1-A0SF                0
1   A1-A0SJ                0
2   A1-A0SK                2
3   A1-A0SO                2
4   A1-A0SQ                0
..      ...              ...
63  A7-A0DC                0
64  A7-A13D                2
65  A7-A13E                2
66  A7-A26E                0
67  A7-A26G                0

[68 rows x 2 columns]
--
Comparison Results: Accuracy = 0.7647, F1 Score = 0.7059
--
azureuser@mybigvm:~/PROJECTS_ALL/Python/MoGCN$ 