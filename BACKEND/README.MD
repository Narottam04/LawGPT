# Installation Guide

## Step 1

Download Cuda 11.8 and Cudann along with VS dependency.

Installation Video Link: https://www.youtube.com/watch?v=StH5YNrY0mE&t=330s

Important: Cuda version should be 11.8

## Step 2

```
git clone <this repo>
```

```
cd backend
```

```
python -m .venv venv
```

```
.venv/Scripts/activate
```

## Step 3

```
    pip install -r requirements.txt
```

```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

```
pip install auto-gptq --extra-index-url https://huggingface.github.io/autogptq-index/whl/cu118/
```

## Step 4

```
uvicorn app:app
```

## For running LAmini model

First follow all above steps

```
git lfs install
```

```
git clone https://huggingface.co/MBZUAI/LaMini-T5-738M
```

```
uvicorn Lamini:app
```
