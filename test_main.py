import pandas as pd


def test_0():
    answer = pd.read_csv("answer.csv")
    assert answer.shape == (20, 2)
    assert set(["NU_INSCRICAO", "NOTA_FINAL"]) == set(answer.columns)
