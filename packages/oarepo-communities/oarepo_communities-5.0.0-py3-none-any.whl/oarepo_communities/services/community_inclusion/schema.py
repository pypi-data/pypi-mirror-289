# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 CERN.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Record communities schema."""

from invenio_requests.customizations import CommentEventType
from marshmallow import Schema, ValidationError, fields, validate, validates


class CommunitySchema(Schema):
    """Schema to define a community id."""

    id = fields.String(required=True)
    comment = fields.Nested(CommentEventType.marshmallow_schema)


class RecordCommunitiesSchema(Schema):
    """Record communities schema."""

    communities = fields.List(
        fields.Nested(CommunitySchema), validate=validate.Length(min=1), required=True
    )

    @validates("communities")
    def validate_communities(self, value):
        # check unique ids
        uniques = set()
        duplicated = set()
        for community in value:
            com_id = community["id"]
            if com_id in uniques:
                duplicated.add(com_id)
            uniques.add(com_id)

        if duplicated:
            raise ValidationError(
                "Duplicated communities {com_ids}.".format(com_ids=duplicated)
            )
