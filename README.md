# How to use the files in this repository?

## For sovereign 5Y CDS

To get the sovereign CDS prices list from CNBC, you need to use the following command in the terminal:

```python
pip install -r requirements.txt
cd src
python main.py --extract CDS
```

To get the sovereign CDS prices for a single sovereign, you need to use the following command in the terminal:

```python
pip install -r requirements.txt
cd src
python main.py --extract CDS --name 'UK CDS 5YR'
```

## For Rates

