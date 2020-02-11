# -*- coding: utf-8 -*-

import os, sys

import subprocess
import tempfile
import itertools


# path to the stanford corenlp jar
STANFORD_CORENLP_3_4_1_JAR = 'stanford-corenlp-3.4.1.jar'

# punctuations to be removed from the sentences
PUNCTUATIONS = ["''", "'", "``", "`", "-LRB-", "-RRB-", "-LCB-", "-RCB-", \
        ".", "?", "!", ",", ":", "-", "--", "...", ";"]


class PTBTokenizer:
    """Python wrapper of Stanford PTBTokenizer"""

    def tokenize(self, report):
        cmd = ['java', '-cp', STANFORD_CORENLP_3_4_1_JAR, \
                'edu.stanford.nlp.process.PTBTokenizer', \
                '-preserveLines', '-lowerCase']

        # ======================================================
        # save sentences to temporary file
        # ======================================================
        path_to_jar_dirname=os.path.dirname(os.path.abspath(__file__))
        tmp_file = tempfile.NamedTemporaryFile(delete=False, dir=path_to_jar_dirname)
        tmp_file.write(report.strip().encode())
        tmp_file.close()

        # ======================================================
        # tokenize sentence
        # ======================================================
        cmd.append(os.path.basename(tmp_file.name))
        p_tokenizer = subprocess.Popen(cmd, cwd=path_to_jar_dirname, \
                stdout=subprocess.PIPE)
        tokenized_report = p_tokenizer.communicate(input=report)[0]
        # remove temp file
        os.remove(tmp_file.name)

        tokenized_report = tokenized_report.decode()
        report_tokens = [w for w in tokenized_report.split(' ') \
                         if w not in PUNCTUATIONS]

        return report_tokens
