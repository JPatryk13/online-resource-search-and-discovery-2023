from typing import Sequence
import os

from google.cloud import enterpriseknowledgegraph as ekg


def ekg_search(
    project_id: str,
    location: str,
    search_query: str,
    languages: Sequence[str] = None,
    types: Sequence[str] = None,
    limit: int = 2,
) -> None:
    # Create a client
    client = ekg.EnterpriseKnowledgeGraphServiceClient()

    # The full resource name of the location
    # e.g. projects/{project_id}/locations/{location}
    parent = client.common_location_path(project=project_id, location=location)

    # Initialize request argument(s)
    request = ekg.SearchRequest(
        parent=parent,
        query=search_query,
        languages=languages,
        types=types,
        limit=limit,
    )

    # Make the request
    response = client.search(request=request)

    print(f"Search Query: {search_query}\n")

    # Extract and print date from response
    for item in response.item_list_element:
        result = item.get("result")

        print(f"Name: {result.get('name')}")
        print(f"- Description: {result.get('description')}")
        print(f"- URL: {result.get('url')}")

        print("\n")


if __name__ == '__main__':

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '...'

    project_id = 'document-discovery-poc'
    location = 'global'  # Values: 'global'
    search_query = 'fotokeramika'
    languages = ['en']  # Optional: List of ISO 639-1 Codes
    types = ['Corporation']  # Optional: List of schema.org types to return
    limit = 10  # Optional: Number of entities to return

    ekg_search(project_id, location, search_query, languages, types, limit)
