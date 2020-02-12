#
# This file is part of Python Client Library for STAC.
# Copyright (C) 2019 INPE.
#
# Python Client Library for STAC is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""STAC Catalog module."""

from .link import Link


class Catalog(dict):
    """The STAC Catalog."""

    def __init__(self, data):
        """Initialize instance with dictionary data.

        :param data: Dict with catalog metadata.
        """
        super(Catalog, self).__init__(data or {})

    @property
    def stac_version(self):
        """:return: the STAC version."""
        return self['stac_version']

    @property
    def id(self):
        """:return: the catalog identifier."""
        return self['id']

    @property
    def title(self):
        """:return: the catalog title."""
        return self['title'] if 'title' in self else None

    @property
    def description(self):
        """:return: the catalog description."""
        return self['description']

    @property
    def links(self):
        """:return: a list of resources in the catalog."""
        return [Link(link) for link in self['links']]
