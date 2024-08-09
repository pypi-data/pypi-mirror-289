import logging
import os.path
import uuid
from pathlib import Path
from typing import Literal, Protocol

from problem_designer.problems.scheduling.generator.typedef import (
    IntermediateGeneratedProblem,
)
from problem_designer.problems.scheduling.open_shop.generated_problem import (
    GeneratedProblem,
    Job,
    Resource,
    Task,
)

logger = logging.getLogger(__name__)


def _encode_file_path(igp: IntermediateGeneratedProblem, file_ending: str) -> str:
    """
    Encodes the problem into a file name
    Args:
        igp: The generated problem
        file_ending: Which ending should be used

    Returns: the file name
    """
    return (
        "_".join(
            [
                igp.problem_configuration.meta.get_global_identifier(),
                str(igp.number_of_jobs),
                str(igp.number_of_machines),
            ]
        )
        + f"{file_ending}"
    )


def write_taillard(igp: IntermediateGeneratedProblem, path: Path) -> Path:
    """
    Writes the generated problem in taillard format to a given file.
    Defined here: http://jobshop.jjvh.nl/explanation.php
    Args:
        igp: The intermediate problem
        path: Where to save the file

    Returns: generated file path

    """
    file_path = Path(path) / _encode_file_path(igp, ".taillard")
    with open(file_path, "w") as f:
        f.write(f"{igp.number_of_jobs} " f"{igp.number_of_machines}\n")
        # write processing times
        for job in sorted(igp.job_to_processing_times.keys()):
            for processing_time in igp.job_to_processing_times[job]:
                f.write(f"{processing_time} ")
            f.write("\n")
        # write order of machine mapping
        for job in sorted(igp.map_machine_to_task.keys()):
            for mapping in igp.map_machine_to_task[job]:
                # taillard defines mapping index to start at 1
                f.write(f"{mapping + 1} ")
            f.write("\n")
    return file_path


def write_standard(igp: IntermediateGeneratedProblem, path: Path) -> Path:
    """
    Writes the generated problem in standard format to a given file.
    Defined here: http://jobshop.jjvh.nl/explanation.php
    Args:
        igp: The generated problem
        path: path where to save the file

    Returns: the file name

    """
    file_path = Path(path) / _encode_file_path(igp, ".standard")
    with open(file_path, "w") as f:
        f.write(
            f"{igp.problem_configuration.parameter_space.number_of_jobs} "
            f"{igp.problem_configuration.parameter_space.number_of_machines}\n"
        )
        # write processing times
        for job in sorted(igp.job_to_processing_times.keys()):
            for mapping, processing_time in zip(igp.map_machine_to_task[job], igp.job_to_processing_times[job]):
                f.write(f"{mapping} {processing_time} ")
            f.write("\n")
    return file_path


def write_json(igp: IntermediateGeneratedProblem, path: Path) -> Path:
    tasks = {}
    jobs = {}
    resources = {}
    for job_id in sorted(igp.job_to_processing_times.keys()):
        jobs[job_id] = Job(
            job_id=job_id,
            tasks=[],
            due_date=None,
            release_time=None,
        )
        for mapping, processing_time in zip(igp.map_machine_to_task[job_id], igp.job_to_processing_times[job_id]):
            task_id = uuid.uuid4()
            tasks[str(task_id)] = Task(
                task_id=str(task_id), resource_ids=[str(mapping)], job_id=job_id, processing_time=processing_time
            )
            if resources.get(str(mapping), None) is None:
                resources[str(mapping)] = Resource(
                    resource_id=str(mapping),
                    setup_times=None,
                    teardown_times=None,
                    unavailable_times=None,
                )
            jobs[job_id].tasks.append(str(task_id))

    gp = GeneratedProblem(
        tasks=tasks,
        resources=resources,
        jobs=jobs,
    )

    if os.path.isdir(str(path)):
        # if path is a directory, append filename and ending
        path = Path(str(path) + "\\output.json")
    # save json file and schema
    with open(path, "w") as f:
        f.write(gp.json(indent=2))
    with open(f"{str(path)}.schema", "w") as f:
        f.write(gp.schema_json(indent=2))
    logger.info("Successfully saved " + str(path))
    return path


class Writer(Protocol):
    def write(self, igp: IntermediateGeneratedProblem):
        raise NotImplementedError


class OpenShopWriter:
    def __init__(
        self,
        output_path: Path,
        format: Literal["taillard", "standard", "json"],
        **kwargs,
    ):
        super().__init__()
        self._output_path = output_path
        self._format = format

    def write(self, igp: IntermediateGeneratedProblem):
        self._output_path.parent.mkdir(parents=True, exist_ok=True)
        if self._format == "taillard":
            logger.info(write_taillard(igp, self._output_path))
        elif self._format == "json":
            logger.info(write_json(igp, self._output_path))
        else:
            logger.info(write_standard(igp, self._output_path))
