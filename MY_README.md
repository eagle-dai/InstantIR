## Installation

**NOTE**: python < 3.11

```
cd <current directory>
python -m venv ./venv

source ./venv/bin/activate
# To activate venv on Windows (cmd) : .\venv\Scripts\activate
# To activate venv on Windows (bash): source ./venv/Scripts/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Download pre-trained models
See README.md

## Demo
```

# optional, e.g., if you are behind a proxy
export HTTP_PROXY=http://proxy2:8082
export HTTPS_PROXY=http://proxy2:8082

cd <current directory>
INSTANTIR_PATH=. python gradio_demo/app.py
```
Launch via your browser at http://localhost:7860
