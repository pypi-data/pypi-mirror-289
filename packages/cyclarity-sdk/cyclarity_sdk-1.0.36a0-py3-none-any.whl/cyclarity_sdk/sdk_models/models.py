from typing import Optional, Union
from pydantic import BaseModel, Field, field_validator
import jsonschema
from .types import TestStepType, TestStepSubType, TestFlowType, ExecutionStatus  # noqa
from clarity_common import RunningEnvType, PackageType
# from common.models.common_models.models import ExecutionMetadata
from clarity_common import ExecutionMetadata
''' Test step definitions'''


class ExecutionConfig(BaseModel):
    # noqa for future use when expert builder and execution engine will be matured enough
    package_type: PackageType = Field(PackageType.ZIP, running_env="package type ZIP file or PIP package")  # noqa
    running_env: Optional[RunningEnvType] = Field(RunningEnvType.IOT,
                                                  running_env="label for the running env, AWS, IOT - when it will be relevant we would need to define enum for that")  # noqa
    location: Optional[str] = Field(None, running_env="url of the pip repository / S3 file which contained the runnable code")  # noqa
    package_version: Optional[str] = Field(None, running_env="pip package version")  # noqa
    package_name: Optional[str] = Field(None, running_env="pip package name")
    docker_image_url: Optional[str] = Field(None, running_env="URL of the docker image if running in docker")  # noqa
    entrypoint: Optional[str] = Field(None, running_env="entrypoint of the runnable")  # noqa


class ParamsSchema(BaseModel):
    in_params: dict = Field({})
    out_params: dict = Field({})

    @field_validator('in_params', 'out_params')
    def validate_json_schema(cls, params):
        try:
            jsonschema.Draft7Validator.check_schema(params)
        except jsonschema.exceptions.SchemaError as e:
            raise ValueError(f"Invalid JSON schema: {e}")
        return params


class TestStep(BaseModel):
    step_id: str = Field(None,
                         description="step_id")  # noqa none because we might want to support anonymus steps execution in the future
    step_name: str = Field(description="name")
    step_version: str = Field(description="version")
    description: Optional[str] = Field('', description="description")
    step_type: TestStepType = Field(description="type")
    step_subtype: TestStepSubType = Field(TestStepSubType.ACTION, description="subtype")  # noqa
    execution_config: ExecutionConfig = Field(ExecutionConfig(), description="instructions")  # noqa
    params_schema: ParamsSchema = Field(ParamsSchema(), description="json schema of in and out params")  # noqa


class TestStepInstance(TestStep):
    params_config: dict


''' Expected configs structures per flow types'''


class SingleStepFlowConfig(BaseModel):
    #  Config for test flow type SingleStep
    step: Union[TestStep, str] = Field(description="actual step or step_id")


''' Test flows definitions'''


class TestFlow(BaseModel):
    test_id: str = Field(None,
                         description="test_id")  # noqa none because we might want to support anonymus tests execution in the future
    test_name: str = Field(description="test name")
    description: str = Field('', description="test description")
    params_config: dict = Field({}, description="instance of the needed test flow parameters with values")  # noqa
    test_type: TestFlowType = Field(description="flow type")
    test_config: Union[SingleStepFlowConfig, dict] = Field(
        description="configuration correspond to the test flow")  # noqa can support also other config types


''' Test plan definition'''


class TestPlan(BaseModel):
    # noqa This model shouldn't be on API!, it should move to execution manager when it will be developed.
    plan: Union[list[TestFlow], list[str]] = Field(description="list of explicit flows structures or flows ids")  # noqa
    plan_name: Optional[str] = Field(None,
                                     description="the name of the plan")  # noqa we might want to execute unsaved plans (by choosing tests)
    description: Optional[str] = Field('', description="description")


class ExecutionPlan(BaseModel):
    # noqa This model shouldn't be on API!, it should move to execution manager when it will be developed.
    agent_id: str = Field(
        description="list of ids of the agentt that runs the test for example IOT device id - it's a list for future support in more then 1 device")  # noqa
    execution_id: str = Field(description="execution id")
    project_id: str = Field(description="Project_id")
    test_plan: Union[TestPlan, str] = Field(
        description="Snapshot of the plan which executes in the current execution (not pointers by id)")  # noqa


''' Structures that the ExecutionEngine export to the IOT device and expect to receive from IOT device'''  # noqa


class ExecutionState(BaseModel):
    '''Data structure to be send via topic::execution-state'''
    execution_metadata: ExecutionMetadata
    percentage: int
    status: ExecutionStatus
    error_message: Optional[str]
