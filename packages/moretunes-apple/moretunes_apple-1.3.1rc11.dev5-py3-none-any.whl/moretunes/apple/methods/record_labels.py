from ..models import *
from ..token import MTAppleMusic


class RecordLabels(MTAppleMusic):
    def get_record_label(
            self,
            item_id: str,
            storefront: str,
            extend: list[str] | None = None,
            include: list[str] | None = None,
            lang: str | None = None,
            views: list[str] | None = None,
    ) -> RecordLabelsResponse:
        """Fetch a record label by using its identifier."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/record-labels/{item_id}"
        req_map = {'params': {}}
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if views is not None:
            req_map["params"]["views"] = ','.join(str(x) for x in views)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: RecordLabelsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_record_label_view(
            self,
            item_id: str,
            storefront: str,
            view: str,
            extend: list[str] | None = None,
            include: list[str] | None = None,
            lang: str | None = None,
            limit: int | None = None,
            attr_fields: list[str] | None = None,
    ) -> RelationshipViewResponse:
        """
        Fetch related resources for a single record label’s relationship
        view
        """
        method = "GET"
        url = f"/v1/catalog/{storefront}/record-labels/{item_id}/view/{view}"
        req_map = {'params': {}}
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if limit is not None:
            req_map["params"]["limit"] = limit
        
        if attr_fields is not None:
            req_map["params"]["with"] = ','.join(str(x) for x in attr_fields)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: RelationshipViewResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_record_labels(
            self,
            storefront: str,
            ids: list[str],
            extend: list[str] | None = None,
            include: list[str] | None = None,
            lang: str | None = None,
    ) -> RecordLabelsResponse:
        """Fetch one or more record labels by using their identifiers."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/record-labels"
        req_map = {'params': {}}
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        req_map["params"]["ids"] = ','.join(str(x) for x in ids)
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: RecordLabelsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result
