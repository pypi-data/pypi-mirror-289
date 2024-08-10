"""
Deal with Async HTTP Jobs

Async HTTP jobs have typically 3 endpoint:

* `POST /jobs`: create an async job, the endpoint responds with a job id
* `GET /jobs/<id>/status`: returns the jobs status
* `GET /jobs/<id>/results`: returns the data from the completed job
"""

from dataclasses import dataclass, field
from typing import Iterable, List
from uuid import UUID

import requests

from wscli.api_utils.api_url import ApiUrl
from wscli.api_utils.call_config import CallConfig
from wscli.api_utils.utils import hit_api


def check_async_job_results(response: requests.Response) -> bool:
    """check if a async job retrieve response is valid"""
    if response.status_code != 200:
        return False
    # TODO: need to implement more tests!!!
    return True


def check_async_job_status(
    response: requests.Response,
    status_key: str = "status",
    done_status: str = "done",
) -> bool:
    if response.status_code != 200:
        return False
    status = response.json().get(status_key, None)
    if not status:
        return False
    return status == done_status


@dataclass
class Checker:
    """check the status of an Async Job"""

    api_url: ApiUrl | None = None
    call_config: CallConfig | None = None
    status_key: str = "status"
    done_status: str = "done"
    _status: bool = field(init=False, default=False)

    def __bool__(self):
        return bool(self._status)

    def __call__(self) -> bool:
        if not self.api_url:
            # status check can't be executed without an api url...
            return True
        if not self.call_config:
            # status check can't be executed without a call config...
            return True
        if not self._status:
            # check every time if the status is still false
            status_response = hit_api(
                api_url=self.api_url,
                call_config=self.call_config,
            )
            self._status = check_async_job_status(
                status_response,
                status_key=self.status_key,
                done_status=self.done_status,
            )
        return self._status


@dataclass
class Retriever:
    api_url: ApiUrl = ApiUrl()
    checker: Checker | None = None
    retrieve_config: CallConfig = field(default_factory=CallConfig.api_get)
    _results: requests.Response | None = field(init=False, default=None)

    def __call__(self) -> requests.Response | None:
        if self._results:
            return self._results
        if self.checker is not None:
            if not self.checker():
                return None
        results_response = hit_api(
            endpoint="",
            api_url=self.api_url,
            call_config=self.retrieve_config,
        )
        if not check_async_job_results(results_response):
            return None
        self._results = results_response
        return self._results


@dataclass
class AsyncJob:
    id: UUID
    retriever: Retriever | None = None

    def __hash__(self):
        return hash(self.id)

    def __call__(self) -> requests.Response | None:
        if not self.retriever:
            return None
        return self.retriever()


@dataclass
class AsyncJobs:
    jobs: List[AsyncJob] = field(default_factory=list)

    def __post_init__(self):
        if len(self) != len(set(self.jobs)):
            raise KeyError("all jobs must be uniques...")

    def __len__(self):
        return len(self.jobs)

    def __bool__(self):
        return bool(self.jobs)

    def __iter__(self):
        for job in self.jobs:
            yield job

    @property
    def ids(self) -> Iterable[UUID]:
        for job in self:
            yield job.id

    def append(self, new_job: AsyncJob):
        if new_job in self.jobs:
            raise KeyError("cannot append duped index")
        self.jobs.append(new_job)

    def extend(self, jobs: List[AsyncJob]):
        for job in jobs:
            self.append(job)

    def by_id(self, job_id: UUID) -> AsyncJob:
        try:
            return next(job for job in self if job.id == job_id)
        except StopIteration as err:
            raise KeyError from err
