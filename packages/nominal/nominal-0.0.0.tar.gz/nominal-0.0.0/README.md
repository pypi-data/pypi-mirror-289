# ⬖ Nominal
Python client for Nominal test data, storage, &amp; compute

🚧 WIP - API and syntax subject to change

## Install (TODO)

> pip install nominal

## Usage

### Upload a Dataset (3 lines)

```py
from nominal import Ingest

dataset = Ingest().read_csv('../data/penguins.csv')

dataset.upload()
```

### Upload a Run (3 lines)

```py
from nominal import Run

r = Run(path='../data/penguins.csv')

run.upload()
```

### Apply a Check to a Run

TODO
