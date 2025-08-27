# Experimenting with Constitutional AI

## Configure your environment (once only)
1. Create (and activate!) a conda environment with Python 3.11 (I'll call it `cai` in this example)

    `conda create -n cai python=3.11`

    `conda activate cai`

2. Install poetry

    `pip install poetry`

3. Setup poetry environment

    `poetry install`

## Running the code

`poetry run python -m cai.cai_demo`

Once the code completes initialisation, you should see something like: 

`* Running on local URL:  http://127.0.0.1:7860`

Open a browser (e.g. Chrome) and copy that URL to launch the demo