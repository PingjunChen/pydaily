# -*- coding: utf-8 -*-

import os, sys

FILE_PATH = os.path.abspath(__file__)
TEST_PATH = os.path.dirname(os.path.dirname(FILE_PATH))
PRJ_PATH = os.path.dirname(TEST_PATH)
sys.path.insert(0, os.path.join(PRJ_PATH, "pydaily"))

from mtm import PTBTokenizer

def test_ptbtokenizer():
    ptb_token = PTBTokenizer()
    # sample_report = "Section of bladder contains areas of transitional cell \
    #     carcinoma. No area of invasion can be identified. A marked acute and \
    #     chronic inflammatory reaction with eosinophils is noted together with \
    #     some necrosis. Sections are examined at six levels. Section of lymph \
    #     node contains normal node with reactive germinal centers."
    # report_tokens = ptb_token.tokenize(sample_report)
    # print(report_tokens)
