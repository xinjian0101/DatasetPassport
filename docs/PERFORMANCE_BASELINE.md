# Performance Baseline

DatasetPassport should remain useful on ordinary local machines before optional acceleration is introduced.

## Baseline dimensions

Measure at least:

- input format;
- record count;
- average record size;
- total input bytes;
- peak memory usage;
- wall-clock duration;
- records processed per second;
- duplicate rate;
- enabled privacy rules.

## Suggested fixture sizes

| Tier | Records | Purpose |
|---|---:|---|
| Small | 1,000 | developer smoke test |
| Medium | 100,000 | routine local audit |
| Large | 1,000,000 | scalability characterization |

## Measurement rules

- Run each fixture at least three times.
- Report median duration.
- Record Python version and operating system.
- Keep fixture generation deterministic.
- Separate parsing time from report serialization when possible.
- Do not benchmark with production personal data.

## Performance risks

The current implementation stores record fingerprints in memory. Memory usage therefore grows with the number of unique records. Future work may add partitioned processing, on-disk fingerprint storage, or approximate duplicate detection.

## Regression policy

A change that increases median processing time by more than 15 percent on the medium fixture should include an explanation or optimization follow-up. Memory regressions should be documented even when execution time improves.

## Publication format

Store benchmark date, commit SHA, fixture checksum, machine summary, command arguments, three raw runs, median result, and reviewer notes.
