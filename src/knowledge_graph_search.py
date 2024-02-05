from google.cloud import enterpriseknowledgegraph as ekg
import os
import json


class KnowledgeGraphSearch:
    def __init__(
            self,
            *,
            project_id: str,
            location: str = "global",
            languages: list[str] = ["en"],
            types: list[str] = ["Organization"]
    ) -> None:
        """
        Initialize client object, google project parent directory (access point) and variables later used for building a
        request.

        :param credential_path: path to the credential json file
        :param project_id: google project id
        :param location: project location?
        :param languages: list of ISO 639-1 Codes
        :param types: list of schema.org types to return
        """

        # Create a client
        self.client = ekg.EnterpriseKnowledgeGraphServiceClient()

        # The full resource name of the location
        # e.g. projects/{project_id}/locations/{location}
        self.parent = self.client.common_location_path(project=project_id, location=location)

        self.languages = languages
        self.types = types

    def search(self, query: str, *, entry_limit: int, path: str | None = None) -> dict:
        """
        Utilizes SearchRequest to generate request object and client object to search the Google Knowledge Graph. Uses
        _get_response_as_dict() method to convert the response to dictionary and (optionally) save it as json

        :param query: string of text to query the EKG against
        :param entry_limit: number of top matching entries to return from the graph
        :param path: optional, if set, forces the _get_response_as_dict() to write the dictionary to json file
        :return:
        """
        # Initialize request argument(s)
        request = ekg.SearchRequest(
            parent=self.parent,
            query=query,
            languages=self.languages,
            types=self.types,
            limit=entry_limit,
        )

        # Make the request
        response = self.client.search(request=request)

        return self._get_response_as_dict(response, path=path)

    @staticmethod
    def _get_response_as_dict(response: ekg.SearchResponse, *, path: str | None = None) -> dict:
        """
        Converts given response object into dictionary and optionally - if path set - saves the response as json file
        under the given path.

        :param response: SearchResponse object returned by the client.search() function
        :param path: path under which the dictionary (as json) is to be saved; if set to None (default) the dict will
        not be saved
        :return: dictionary with the response content
        """
        # Convert response object to dictionary
        response_as_json = response.__class__.to_json(response)
        response_as_dict = json.loads(response_as_json)

        if path:
            # save the response @ path
            with open(path, 'w') as f:
                json.dump(response_as_dict, f, indent=2)

        return response_as_dict


if __name__ == '__main__':
    
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '...'
    
    kgs = KnowledgeGraphSearch(
        project_id="..."
    )
    
    result = kgs.search("ing", entry_limit=10)
    print(result)

