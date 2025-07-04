"""
This script demonstrates how to generate a video from a text prompt using CogVideoX with 🤗Huggingface Diffusers Pipeline.

Note:
    This script requires the `diffusers>=0.30.0` library to be installed， after `diffusers 0.31.0` release,
    need to update.

Run the script:
    $ python cli_demo.py --prompt "A girl ridding a bike." --model_path THUDM/CogVideoX-2b

"""

import argparse
import torch
from diffusers import CogVideoXPipeline, CogVideoXDDIMScheduler, CogVideoXDPMScheduler
from diffusers.utils import export_to_video
import json
import os

def generate_video(
    prompt: str,
    model_path: str,
    output_path: str = "./output.mp4",
    num_inference_steps: int = 50,
    guidance_scale: float = 6.0,
    num_videos_per_prompt: int = 2,
    dtype: torch.dtype = torch.bfloat16,
):
    """
    Generates a video based on the given prompt and saves it to the specified path.

    Parameters:
    - prompt (str): The description of the video to be generated.
    - model_path (str): The path of the pre-trained model to be used.
    - output_path (str): The path where the generated video will be saved.
    - num_inference_steps (int): Number of steps for the inference process. More steps can result in better quality.
    - guidance_scale (float): The scale for classifier-free guidance. Higher values can lead to better alignment with the prompt.
    - num_videos_per_prompt (int): Number of videos to generate per prompt.
    - dtype (torch.dtype): The data type for computation (default is torch.bfloat16).

    """

    # 1.  Load the pre-trained CogVideoX pipeline with the specified precision (bfloat16).
    # add device_map="balanced" in the from_pretrained function and remove the enable_model_cpu_offload()
    # function to use Multi GPUs.

    pipe = CogVideoXPipeline.from_pretrained(model_path, torch_dtype=dtype)
    
    pipe = pipe.to("cuda")

    pipe. enable_model_cpu_offload()


    # 2. Set Scheduler.
    # Can be changed to `CogVideoXDPMScheduler` or `CogVideoXDDIMScheduler`.
    # We recommend using `CogVideoXDDIMScheduler` for CogVideoX-2B and `CogVideoXDPMScheduler` for CogVideoX-5B.
    # pipe.scheduler = CogVideoXDDIMScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing")
    pipe.scheduler = CogVideoXDPMScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing")

    # 3. Enable CPU offload for the model, enable tiling.
    # turn off if you have multiple GPUs or enough GPU memory(such as H100) and it will cost less time in inference
    #pipe.enable_sequential_cpu_offload()
    pipe.vae.enable_slicing()
    pipe.vae.enable_tiling()

    # 4. Generate the video frames based on the prompt.
    # `num_frames` is the Number of frames to generate.
    # This is the default value for 6 seconds video and 8 fps,so 48 frames and will plus 1 frame for the first frame.
    # for diffusers `0.30.1` and after version, this should be 49.

    video = pipe(
        prompt=prompt,
        num_videos_per_prompt=num_videos_per_prompt,  # Number of videos to generate per prompt
        num_inference_steps=num_inference_steps,  # Number of inference steps
        num_frames=49,  # Number of frames to generate，changed to 49 for diffusers version `0.31.0` and after.
        use_dynamic_cfg=True,  ## This id used for DPM Sechduler, for DDIM scheduler, it should be False
        guidance_scale=guidance_scale,  # Guidance scale for classifier-free guidance, can set to 7 for DPM scheduler
        generator=torch.Generator().manual_seed(42),  # Set the seed for reproducibility
    ).frames[0]


    os.makedirs(f"sample_video/",exist_ok=True)
    export_to_video(video, f"sample_video/{str(seed_1)}_{prompt[:50]}.mp4", fps=8)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a video from a text prompt using CogVideoX")
    parser.add_argument("--prompt", type=str,  help="The description of the video to be generated")
    parser.add_argument(
        "--model_path", type=str, default="Fudan-FUXI/IPOC-2B-v1.0", help="The path of the pre-trained model to be used"
    )
    parser.add_argument(
        "--output_path", type=str, default="./output1.mp4", help="The path where the generated video will be saved"
    )
    parser.add_argument(
        "--num_inference_steps", type=int, default=50, help="Number of steps for the inference process"
    )
    parser.add_argument("--guidance_scale", type=float, default=6.0, help="The scale for classifier-free guidance")
    parser.add_argument("--num_videos_per_prompt", type=int, default=1, help="Number of videos to generate per prompt")
    parser.add_argument(
        "--dtype", type=str, default="bfloat16", help="The data type for computation (e.g., 'float16' or 'bfloat16')"
    )

    args = parser.parse_args()
    dtype = torch.float16 if args.dtype == "float16" else torch.bfloat16

    args.prompt="A young woman walking down a busy city street."
    generate_video(
        prompt=args.prompt,
        model_path=args.model_path,
        output_path=args.output_path,
        num_inference_steps=args.num_inference_steps,
        guidance_scale=args.guidance_scale,
        num_videos_per_prompt=args.num_videos_per_prompt,
        dtype=dtype,
    )
