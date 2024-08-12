from enum import Enum

''' Test step definitions'''


class TestStepType(str, Enum):
    # supported types for test step deployment
    MANUAL_STEP = "manual_step"
    EB_COMPONENT = "EB_Component"


class TestStepSubType(str, Enum):
    # supported subtypes for test step deployment
    ACTION = "Action"
    END = "END"


''' Test flows definitions'''


class TestFlowType(str, Enum):
    SINGLE_STEP = "single_step"


class ExecutionStatus(str, Enum):
    TIMEOUT = "TIMEOUT"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    COMPLETED_SUCCESSFULLY = "COMPLETED"
    COMPLETED_WITH_ERROR = "FAILED"
    STOPPED = "STOPPED"


class ExecutionResult(str, Enum):
    PASSED = "PASSED"
    FAILED = "FAILED"
    NOT_EVALUATED = "NOT_EVALUATED"
