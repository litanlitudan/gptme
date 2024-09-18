from collections.abc import Callable
from dataclasses import dataclass
from typing import Literal, TypedDict

Files = dict[str, str | bytes]
Status = Literal["success", "error", "timeout"]


@dataclass
class ResultContext:
    """
    Context for the result of a test.
    """

    files: Files
    stdout: str
    stderr: str
    exit_code: int


@dataclass
class CaseResult:
    """
    Result of a single test case on the execution of a prompt.
    """

    name: str
    passed: bool
    code: str
    duration: float


@dataclass
class ExecResult:
    """
    Result of executing a prompt.
    """

    name: str
    status: Status
    results: list[CaseResult]
    timings: dict[str, float]
    stdout: str
    stderr: str
    run_stdout: str
    run_stderr: str


class ExecTest(TypedDict):
    """
    Test case for executing a prompt.
    """

    name: str
    files: Files
    run: str
    prompt: str
    expect: dict[str, Callable[[ResultContext], bool]]