""" File to allow running tests locally """

import asyncio
from uuid import uuid4

from enums import CaseType
from utils.api import Api
from utils.playwright_utils import (
    create_context_and_page,
    fetch_html_and_screenshots,
    goto_url_with_timeout
)


class LocalTests:
    """
    Class to run tests locally
    """
    def __init__(self,
            url,
            api_key,
            use_existing_instance=False,
            update_status_function=None,
            in_container=False,
            playwright_page=None,
            host_url=None):
        """ Initialize the LocalTests class """
        # pylint: disable=too-many-arguments
        self.api = Api(
            api_key,
            host_url=host_url
        )
        self.url = url
        self.use_existing_instance = use_existing_instance
        self.update_status_function=update_status_function
        self.context = None
        self.page = playwright_page
        self.in_container = in_container

    def run(self):
        """Run the workflow synchronously"""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(self.run_tests_locally())

    async def run_tests_locally(self):
        """
        Run the E2E test workflow 
        """
        # pylint: disable=too-many-arguments
        job_id = str(uuid4())

        try:
            if self.page is None:
                self.context, self.page = await create_context_and_page(
                    use_existing_instance=self.use_existing_instance,
                    in_container=self.in_container
                )
            return await self.run_algorithm(job_id)

        finally:
            if self.context:
                await self.context.close()

    async def run_algorithm(self, job_id):
        # pylint: disable=too-many-arguments, too-many-locals
        """
        Run the overall testing algorithm.
        """
        cases = self.api.list_cases()
        testing_cases = cases['testingCases']

        for case in testing_cases:
            case_id, case_info, case_type = self.extract_case_details(case)

            if case_type != CaseType.ROUTE.value:
                raise ValueError(f'Invalid Case Type: {case_id} | {case_type}')

            page_url = f'{self.url.rstrip("/")}/{case_info.lstrip("/")}'
            self.page = await goto_url_with_timeout(self.page, page_url)
            html, screenshots = await fetch_html_and_screenshots(self.page)
            status = self.api.test_case(job_id, case_id, html, screenshots)

            if self.update_status_function:
                self.update_status_function(status)

        return status


    def extract_case_details(self, case):
        """
        Extract case details from the provided case
        """
        return case['caseId'], case['origin'], case['caseName']
