import shutil

import pytest


@pytest.mark.dependency(name="test_exist")
def test_exist(stu_answer):
    assert stu_answer.exists()


@pytest.mark.xfail(reason="not needed for this assessment")
@pytest.mark.dependency(
    name="test_content",
    depends=['test_exist'],
    scope="session",
)
def test_content(stu_answer_content, stu_answer, artifacts):
    """Test content only if the solution file exists."""
    # back up the answer file in case something happens so we can inspect
    # manually later.
    shutil.copy(stu_answer, artifacts)  # should not fail
    assert len(stu_answer_content) > 0
