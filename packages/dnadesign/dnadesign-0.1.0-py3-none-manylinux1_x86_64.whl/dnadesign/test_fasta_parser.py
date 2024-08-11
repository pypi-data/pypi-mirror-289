import pytest
import os
from .fasta_parser import parse_fasta_from_c_file, parse_fasta_from_c_string, FastaRecord

def test_parse_fasta_from_c_string():
    fasta_data = ">test\nATCG\n"
    records = parse_fasta_from_c_string(fasta_data)
    assert len(records) == 1
    assert records[0].identifier == "test"
    assert records[0].sequence == "ATCG"
