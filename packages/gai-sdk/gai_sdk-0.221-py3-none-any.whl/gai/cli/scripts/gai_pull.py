# requires pip install huggingface-hub
import os
from huggingface_hub import snapshot_download

from gai.lib.common.utils import get_app_path
from pathlib import Path

os.environ["HF_HUB_ENABLED_HF_TRANSFER"]="1"
import time

hf_hub = {
    "instructor-sentencepiece":{
        "repo_id":"hkunlp/instructor-large",
        "local_dir":"instructor-large",
        "revision":"54e5ffb8d484de506e59443b07dc819fb15c7233"
    },
    "exllamav2-mistral7b":{
        "repo_id":"bartowski/Mistral-7B-Instruct-v0.3-exl2",
        "local_dir":"exllamav2-mistral7b",
        "revision":"1a09a351a5fb5a356102bfca2d26507cdab11111"
    },
    "sd1.5-automatic1111":{
        "repo_id":"runwayml/stable-diffusion-v1-5",
        "local_dir":"Stable-diffusion",
        "revision":"1d0c4ebf6ff58a5caecab40fa1406526bca4b5b9"
    },
    "xttsv2-coqui":{
        "local_dir":"xttsv2-coqui",
    }
}

def pull(console, model_name):
    app_dir = get_app_path()
    if not model_name:
        console.print("[red]Model name not provided[/]")
        return
    hf_model=hf_hub.get(model_name,None)

    if model_name != "xttsv2-coqui":
        if not hf_model:
            console.print(f"[red]Model {model_name} not found[/]")
            return

        start=time.time()
        console.print(f"[white]Downloading... {model_name}[/]")
        local_dir=f"{app_dir}/models/"+hf_model["local_dir"]
        snapshot_download(
            repo_id=hf_model["repo_id"],
            local_dir=local_dir,
            revision=hf_model["revision"],
            )
        end=time.time()
        duration=end-start
        download_size=Path(local_dir).stat().st_size
    else:
        start=time.time()
        console.print(f"[white]Downloading... {model_name}[/]")
        local_dir=f"{app_dir}/models/"+hf_model["local_dir"]

        import os
        os.environ["COQUI_TOS_AGREED"]="1"
        from TTS.utils.manage import ModelManager
        mm =  ModelManager(output_prefix=local_dir)
        model_name="tts_models/multilingual/multi-dataset/xtts_v2"
        mm.download_model(model_name)
        
        end=time.time()
        duration=end-start
        download_size=Path(local_dir).stat().st_size

    from rich.table import Table
    table = Table(title="Download Information")
    # Add columns
    table.add_column("Model Name", justify="left", style="bold yellow")
    table.add_column("Time Taken (s)", justify="right", style="bright_green")
    table.add_column("Size (Mb)", justify="right", style="bright_green")
    table.add_column("Location", justify="right", style="bright_green")

    # Add row with data
    table.add_row(model_name, f"{duration:4}", f"{download_size:2}", f"{app_dir}/models/{model_name}")

    # Print the table to the console
    console.print(table)  

