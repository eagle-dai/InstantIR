from huggingface_hub import snapshot_download
import os
import requests

def check_proxy():
    proxy_url = os.getenv("HTTPS_PROXY")
    if not proxy_url:
        print("No proxy found in HTTPS_PROXY environment variable. Proceeding without proxy.")
        return None

    try:
        print(f"Checking proxy: {proxy_url}")
        response = requests.get("https://huggingface.co", proxies={"http": proxy_url, "https": proxy_url}, timeout=10)
        if response.status_code == 200:
            print("Proxy is working!")
            return proxy_url
        else:
            print(f"Proxy returned status code: {response.status_code}. Proceeding without proxy.")
            return None
    except Exception as e:
        print(f"Proxy check failed: {e}. Proceeding without proxy.")
        return None

def download_models():
    output_dir = "./model"
    os.makedirs(output_dir, exist_ok=True)

    proxy_url = check_proxy()

    models = [
        # {"repo_id": "stabilityai/stable-diffusion-xl-base-1.0"},
        # {"repo_id": "facebook/dinov2-large"},
        {"repo_id": "InstantX/InstantIR"}
    ]

    for model in models:
        try:
            print(f"Downloading model from {model['repo_id']}...")
            file_path = snapshot_download(
                repo_id=model["repo_id"],
                local_dir=output_dir + "/" + model["repo_id"],
                proxies={"http": proxy_url, "https": proxy_url} if proxy_url else None
            )
            print(f"Downloaded to {file_path}\n")
        except Exception as e:
            print(f"Failed to download {model['repo_id']}: {e}\n")

if __name__ == "__main__":
    download_models()
