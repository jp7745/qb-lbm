#!/usr/bin/env python3



# Copyright 2024 L3Harris Technologies, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#



import numpy as np 




print("loading A matrix...")
A = np.load("A_matrix.npz")["A"]
print("done.")

A_1_norm = np.linalg.norm(A, ord=1)
print(f"A 1 norm: {A_1_norm}")

A_inf_norm = np.linalg.norm(A, ord=np.inf)
print(f"A inf norm: {A_inf_norm}")

A_spec_norm_bound = np.sqrt(A_1_norm*A_inf_norm)
print(f"A spec bound (sqrt[(1-norm)x(inf-norm)]):  {A_spec_norm_bound}")

A_spec_norm = np.linalg.norm(A, ord=2)
print(f"A spec norm: {A_spec_norm}")






