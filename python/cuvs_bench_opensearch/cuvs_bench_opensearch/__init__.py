#
# SPDX-FileCopyrightText: Copyright (c) 2025-2026, NVIDIA CORPORATION.
# SPDX-License-Identifier: Apache-2.0
#

"""
cuvs-bench OpenSearch backend plugin.

Registers the OpenSearch backend and config loader with cuvs-bench via
setuptools entry points. Install with:

    pip install cuvs-bench[opensearch]

The backend is auto-discovered and registered when the entry point is loaded.
"""

from .backend import OpenSearchBackend, OpenSearchConfigLoader, register

__all__ = [
    "OpenSearchBackend",
    "OpenSearchConfigLoader",
    "register",
]
