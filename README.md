<p align="center">
  <img src="https://github.com/user-attachments/assets/05771732-46ce-4d4a-86c0-8f4ed14a34dd"  height=100>
</p>

# IPO: Iterative Preference Optimization for Text-to-Video Generation

[![arXiv](https://img.shields.io/badge/arXiv-2502.02088-b31b1b.svg)](https://arxiv.org/abs/2502.02088) [![Project Page](https://img.shields.io/badge/Project-Website-blue)](https://yangxlarge.github.io/ipoc//) [![Hugging Face 2B ckpt](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Ckpt2B-yellow)](https://huggingface.co/Fudan-FUXI/IPOC-2B-v1.0) [![Hugging Face 5B ckpt](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Ckpt5B-yellow)](https://huggingface.co/Fudan-FUXI/IPOC-5B-v1.0)

This repo contains IPO pre-trained weights, training/sampling code, for our paper IPO: Iterative Preference Optimization for Text-to-Video Generation.

## News

- (🔥 New) ```2025/2/26```💥: We open source our model after post-training using the IPO method on 5B, **[IPOC-5B-v1.0](https://huggingface.co/Fudan-FUXI/IPOC-5B-v1.0)，and we use more data to train the reward model after optimization.

- (🔥 New) ```2025/2/26```💥: We open source our model after post-training using the IPO method on cogvideo-2B, **[IPOC-2B-v1.0](https://huggingface.co/Fudan-FUXI/IPOC-2B-v1.0)

## ✅ TODO List

- [x] Release IPOC-2B-v1.0 weights  
- [x] Release IPOC-5B-v1.0 weights 
- [ ] Support WANX 2.1  
- [ ] Open-source training code  
- [ ] Open-source training data 


## Table of Contents

1. Comparison of video demos
2. Introduction
3. Model Usage
4. Citation
5. Acknowledgements

## Comparison of video demos

<table border="0" style="width: 100%; text-align: center; margin-top: 1px;">

  <!-- 第一行标题 -->
  <tr>
    <td colspan="4" style="text-align: left; font-weight: bold; padding: 10px 0;">IPO-2B</td>
  </tr>
  <!-- 第一行视频 -->
  <tr>
    <td><video src="https://github.com/user-attachments/assets/8e2e313b-f1ff-4125-943d-fa7ed1c0f6e7" width="100%" controls autoplay loop muted></video></td>
    <td><video src="https://github.com/user-attachments/assets/92cb6fad-122b-42da-be29-2f6b6d6dec6d" width="100%" controls autoplay loop muted></video></td>
    <td><video src="https://github.com/user-attachments/assets/8eb52605-dd9f-4110-9171-7aec2354fc97" width="100%" controls autoplay loop muted></video></td>
    <td><video src="https://github.com/user-attachments/assets/10f6d858-76fa-4c8c-8f43-03462ee8308e" width="100%" controls autoplay loop muted></video></td>
  </tr>
  <tr>
    <td><video src="https://github.com/user-attachments/assets/f79d2e16-17e3-4033-a25b-c1236b22a189" width="100%" controls autoplay loop muted></video></td>
    <td><video src="https://github.com/user-attachments/assets/3aec3357-e290-4c64-8d37-25b4a81412a4" width="100%" controls autoplay loop muted></video></td>
    <td><video src="https://github.com/user-attachments/assets/68ccef90-d632-4c5e-a8a6-7aa8a4727c83" width="100%" controls autoplay loop muted></video></td>
    <td><video src="https://github.com/user-attachments/assets/3f17e155-145b-4281-acbb-9f821faa969d" width="100%" controls autoplay loop muted></video></td>
  </tr>

  <!-- 第二行标题 -->
  <tr>
    <td colspan="4" style="text-align: left; font-weight: bold; padding: 10px 0;">CogvideoX-2B</td>
  </tr>
  <!-- 第二行视频 -->
  <tr>
    <td><video src="https://github.com/user-attachments/assets/4261861a-e43f-4df4-b0fb-3d6245dcafe9" width="100%" controls autoplay loop muted></video></td>
    <td><video src="https://github.com/user-attachments/assets/ed81d4ad-1f38-431e-9f1c-21df355e9acc" width="100%" controls autoplay loop muted></video></td>
    <td><video src="https://github.com/user-attachments/assets/d6186fd0-8cf4-454d-a0e6-2c2a2a6c94a2" width="100%" controls autoplay loop muted></video></td>
    <td><video src="https://github.com/user-attachments/assets/ce7c6b2a-978c-4b97-a934-a65310443db6" width="100%" controls autoplay loop muted></video></td>
  </tr>
  <tr>
    <td><video src="https://github.com/user-attachments/assets/d0cefb93-c08e-42c3-9996-220f52a83ff2" width="100%" controls autoplay loop muted></video></td>
    <td><video src="https://github.com/user-attachments/assets/319f55a2-235c-4a96-af9a-ff8580fb34c3" width="100%" controls autoplay loop muted></video></td>
    <td><video src="https://github.com/user-attachments/assets/25620239-3c74-4df3-920c-45f76fd3917b" width="100%" controls autoplay loop muted></video></td>
    <td><video src="https://github.com/user-attachments/assets/f891cf3f-35b0-4f46-8777-e4e2fef73459" width="100%" controls autoplay loop muted></video></td>
  </tr>

</table>

## Introduction
We propose to align video foundation models with human preferences from the perspective of post-training in this paper. Consequently, we introduce an Iterative Preference Optimization strategy to enhance generated video quality by incorporating human feedback. Specifically, IPO exploits a critic model to justify video generations for pairwise ranking as in Direct Preference Optimization or point-wise scoring as in Kahneman-Tversky Optimization. Given this, IPO optimizes video foundation models with guidance of signals from preference feedback, which helps improve generated video quality in subject consistency, motion smoothness and aesthetic quality, etc. In addition, IPO incorporates the critic model with the multi-modality large language model, which enables it to automatically assign preference labels without need of retraining or relabeling. In this way, IPO can efficiently perform multi-round preference optimization in an iterative manner, without the need of tediously manual labeling. Comprehensive experiments demonstrate that the proposed IPO can effectively improve the video generation quality of a pretrained model and help a model with only 2B parameters surpass the one with 5B parameters. Besides, IPO achieves new state-of-the-art performance on VBench benchmark.

<p align="center">
  <img width="80%" src="https://github.com/user-attachments/assets/6f95dd55-7586-4f12-bd62-adf28b9b8ca8">
</p>


## Model Usage

### inference

```
pip install -r requirements.txt
python scripte/inference.py --prompts ""
```
## 🔗 Citation

If you find [IPO](https://arxiv.org/abs/2502.02088) useful for your research and applications, please cite using this BibTeX:
```BibTeX
@article{yang2025ipo,
  title={Ipo: Iterative preference optimization for text-to-video generation},
  author={Yang, Xiaomeng and Tan, Zhiyu and Li, Hao},
  journal={arXiv preprint arXiv:2502.02088},
  year={2025}
}
```

## Acknowledgements

We greatly appreciate the contribution of [CogvideoX](https://github.com/THUDM/CogVideo) to open source. Our IPO is based on the CogvideoX  model for post training, which is consistent in usage with CogvideoX.



