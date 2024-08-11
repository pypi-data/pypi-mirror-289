# Genetic sequence data files generator

Used for generating data files (Coverage files, VCF files, ...) in order to
test database design.

## NEWS

### 1.1.0 - 2024-08-10

 * Allow to output gzipped files with gen-fasta and gen-fastq.
 * New gen-fastq script to generate FASTQ files.

### 1.0.1 - 2024-05-30

 * gen-vcf: correct usage of file path to pass to mutation-simulator.
 * gen-fasta: disable header tag line (comment line) by default.
