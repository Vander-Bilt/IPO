# IPO

=======

# IPO: Iterative Preference Optimization for Text-to-Video Generation

[![arXiv](https://img.shields.io/badge/arXiv-2502.02088-b31b1b.svg)](https://arxiv.org/abs/2502.02088) [![Project Page](https://img.shields.io/badge/Project-Website-blue)](https://yangxlarge.github.io/ipoc//) [![Hugging Face 2B ckpt](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Ckpt2B-yellow)](https://huggingface.co/Fudan-FUXI/IPOC-2B-v1.0) [![Hugging Face 5B ckpt](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Ckpt5B-yellow)](https://huggingface.co/Fudan-FUXI/IPOC-5B-v1.0)

This repo contains IPO pre-trained weights, training/sampling code, for our paperIPO: Iterative Preference Optimization for Text-to-Video Generation.

## News

- (🔥 New) ```2025/2/26```💥: We open source our model after post-training using the IPO method on 5B, **[IPOC-5B-v1.0](https://huggingface.co/Fudan-FUXI/IPOC-5B-v1.0)，and we use more data to train the reward model after optimization.

- (🔥 New) ```2025/2/26```💥: We open source our model after post-training using the IPO method on cogvideo-2B, **[IPOC-2B-v1.0](https://huggingface.co/Fudan-FUXI/IPOC-2B-v1.0)

**## Table of Contents**

1. Video demos
2. [Model Usage](#4-model-usage)
3. [Citation](#7-citation)

## Video demo

### IPO-2B
<table border="0" style="width: 100%; text-align: center; margin-top: 1px;">
  <tr>
    <td><video src="https://github.com/user-attachments/assets/d7d6e991-5fd4-40ce-8c16-ab052ec1a809" width="100%" controls autoplay loop muted></video></td>
    <td><video src="https://github.com/user-attachments/assets/02bdafcd-dd8b-42cc-ae4d-3281a413009c" width="100%" controls autoplay loop muted></video></td>
    <td><video src="https://github.com/user-attachments/assets/02bdafcd-dd8b-42cc-ae4d-3281a413009c" width="100%" controls autoplay loop muted></video></td>
  </tr>

</table>
    



## Model Usage

### inference

```
pip install -r requirements.txt
python scripte/inference.py --prompts ""
```





  

