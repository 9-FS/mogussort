# Copyright (c) 2023 구FS, all rights reserved. Subject to the MIT licence in `licence.md`.
import datetime as dt
import hypothesis, hypothesis.strategies
import sys
import typing

sys.path.append("./")   # enables importing via parent directory
from mogussort.mogussort import mogussort


@hypothesis.settings(deadline=dt.timedelta(seconds=10))
@hypothesis.given(hypothesis.strategies.lists(hypothesis.strategies.integers(), max_size=8))
def test_mogussort(crew_in: list[typing.Any]) -> None:
    assert sorted(crew_in)==mogussort(crew_in)
    
    return