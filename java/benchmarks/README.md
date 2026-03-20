# CuVS Java API benchmarks

This maven project contains JMH benchmarks for the CuVS Java API (CAGRA, HNSW, device matrix).

## Prerequisites
- [CuVS libraries](https://docs.rapids.ai/api/cuvs/stable/build/#build-from-source)
- Build the CuVS-Java API (`./build.sh` from the parent directory)

## Run benchmarks

Build:
```shell
mvn clean verify
```
Run:
```shell
export RAFT_DEBUG_LOG_FILE=/dev/null
java -jar target/benchmarks.jar
```
The environment variable is needed to silence RAFT logging; RAFT emits some logs at INFO level when
building indices and queries, and writing them to stdout (the default) influences benchmark results.

## Overhead benchmarks (cuvs_bench comparison)

`CagraOverheadBenchmarks` and `HnswOverheadBenchmarks` measure build and search for Java vs native
overhead comparison. All params are configurable via `-p`:

```shell
# CAGRA (defaults match cuvs_bench test group)
java -jar target/benchmarks.jar CagraOverheadBenchmarks

# Override params
java -jar target/benchmarks.jar CagraOverheadBenchmarks -p graphDegree=64 -p size=50000

# HNSW
java -jar target/benchmarks.jar HnswOverheadBenchmarks -p ef=20 -p size=10000
```

Params: `graphDegree`, `intermediateGraphDegree`, `itopk`, `searchWidth`, `size`, `dims`, `numQueries`
(CAGRA); `graphDegree`, `intermediateGraphDegree`, `ef`, `size`, `dims`, `numQueries` (HNSW).

## Other options

Change dataset size and dimension:
```shell
java -jar target/benchmarks.jar -p size=4 -p dims=4
```
Use `java -jar target/benchmarks.jar -h` for details on options.
