import json

import urllib3
from sawsi.aws import shared
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from sawsi.shared.dict_util import convert_dynamodb_document_to_dict
from typing import Literal

http = urllib3.PoolManager()

service = 'es'

class OpenSearchAPI:
    """
    API Gateway Management API
    """
    def __init__(self, domain_endpoint_url, credentials=None, region=shared.DEFAULT_REGION):
        """
        :param credentials: {
            "aws_access_key_id": "str",
            "aws_secret_access_key": "str",
            "region_name": "str",
            "profile_name": "str",
        }
        """
        self.boto3_session = shared.get_boto_session(credentials)
        self.cache = {}
        self.domain_endpoint_url = domain_endpoint_url
        if self.domain_endpoint_url.endswith('/'):
            # 뒤에 슬레쉬 짜름
            self.domain_endpoint_url = self.domain_endpoint_url[:-1]
        self.region = region

    def _http_request(self, method, url, body, region):
        signed_request = self._sign_request(method, url, body=body, region=region)
        response = http.request(
            method,
            signed_request.url,
            body=signed_request.body,
            headers=signed_request.headers
        )
        # status = response.status
        # response_body = response.data.decode('utf-8')
        return response

    def _sign_request(self, method, url, body, region):
        # BOTO3 서명
        credentials = self.boto3_session.get_credentials()
        headers = {'Content-Type': 'application/json'}
        request = AWSRequest(method=method, url=url, data=body, headers=headers)
        SigV4Auth(credentials, service, region).add_auth(request)
        return request.prepare()

    def run(self, method: Literal["GET", "POST", "PUT", "DELETE"], path, body):
        url = f'{self.domain_endpoint_url}/{path}'
        response = self._http_request(method, url, body, region=self.region)
        return response

    def put_document(self, index_name: str, doc_id: str, document: dict):
        path = f"{index_name}/_doc/{doc_id}"
        doc_body = convert_dynamodb_document_to_dict(document)
        doc_body = json.dumps(doc_body)
        response = self.run('PUT', path, doc_body)
        return response

    def delete_document(self, index_name: str, doc_id: str):
        path = f"{index_name}/_doc/{doc_id}"
        response = self.run('DELETE', path, None)
        return response

