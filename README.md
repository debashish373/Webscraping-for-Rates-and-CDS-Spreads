# How to use the files in this repository?

```python
pip install -r requirements.txt
cd src
```

## For sovereign 5Y CDS

To get the sovereign CDS prices list from CNBC, you need to use the following command in the terminal:

```python
python main.py --extract CDS
```

To get the sovereign CDS prices for a single sovereign:

```python
python main.py --extract CDS --name 'UK CDS 5YR'
```

## For Rates

To get the list of rates for select countries run the following command in the terminal:

```python
python main.py --extract RATES
```

Alternatively, to get the US treasury 10 yr rates, for instance, run the following:

```python
python main.py --extract RATES --name 'US-10YR'
```
