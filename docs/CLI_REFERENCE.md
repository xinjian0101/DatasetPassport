# Command-Line Reference

## Basic command

```bash
python main.py <dataset> [options]
```

## Positional argument

### `dataset`

Path to a CSV, JSON, or JSONL file.

## Options

### `--required`

Comma-separated required field names.

```bash
--required instruction,output,source
```

### `--license`

Declared license label for the reviewed batch.

```bash
--license apache-2.0
```

### `-o`, `--output`

Path for the JSON report.

```bash
-o reports/dataset-passport.json
```

## Examples

### JSONL

```bash
python main.py examples/data.jsonl --required instruction,output,source -o report.json
```

### CSV

```bash
python main.py records.csv --required id,text,label,source -o csv-report.json
```

### JSON

```bash
python main.py records.json --required id,text -o json-report.json
```

## Exit behavior

The current MVP raises a clear error when the input format is unsupported or a record cannot be parsed. Future versions may add stable exit codes for review and blocking findings.

## Reproducibility

Store the command, input checksum, Python version, scanner commit, required-field list, declared license value, and report checksum with each review.
