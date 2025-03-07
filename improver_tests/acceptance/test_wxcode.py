# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# (C) British Crown Copyright 2017-2021 Met Office.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
"""Tests for the wxcode CLI"""

import pytest

from . import acceptance as acc

pytestmark = [pytest.mark.acc, acc.skip_if_kgo_missing]
CLI = acc.cli_name_with_dashes(__file__)
run_cli = acc.run_cli(CLI)

ALL_PARAMS = [
    "lightning_flashes_per_unit_area_in_vicinity_above",
    "low_and_medium_type_cloud_area_fraction_above",
    "low_type_cloud_area_fraction_above",
    "lwe_precipitation_rate_above",
    "lwe_precipitation_rate_in_vicinity_above",
    "lwe_sleetfall_rate_above",
    "lwe_snowfall_rate_above",
    "rainfall_rate_above",
    "shower_condition_above",
    "visibility_in_air_below",
]


@pytest.mark.slow
def test_basic(tmp_path):
    """Test basic wxcode processing"""
    kgo_dir = acc.kgo_root() / "wxcode"
    kgo_path = kgo_dir / "basic" / "kgo.nc"
    param_paths = [
        kgo_dir / "basic" / f"probability_of_{p}_threshold.nc" for p in ALL_PARAMS
    ]
    wxtree = kgo_dir / "wx_decision_tree.json"
    output_path = tmp_path / "output.nc"
    args = [
        *param_paths,
        "--wxtree",
        wxtree,
        "--model-id-attr",
        "mosg__model_configuration",
        "--output",
        output_path,
    ]
    run_cli(args)
    acc.compare(output_path, kgo_path)


@pytest.mark.slow
def test_native_units(tmp_path):
    """Test wxcode processing with non-SI units for threshold coordinates:
    precipitation: mm h-1
    visibility: feet
    """
    kgo_dir = acc.kgo_root() / "wxcode"
    kgo_path = kgo_dir / "basic" / "kgo.nc"
    param_paths = [
        kgo_dir / "native_units" / f"probability_of_{p}_threshold.nc"
        for p in ALL_PARAMS
    ]
    wxtree = kgo_dir / "wx_decision_tree.json"
    output_path = tmp_path / "output.nc"
    args = [
        *param_paths,
        "--wxtree",
        wxtree,
        "--model-id-attr",
        "mosg__model_configuration",
        "--output",
        output_path,
    ]
    run_cli(args)
    acc.compare(output_path, kgo_path)


def test_global(tmp_path):
    """Test global wxcode processing"""
    kgo_dir = acc.kgo_root() / "wxcode"
    kgo_path = kgo_dir / "global" / "kgo.nc"
    params = [param for param in ALL_PARAMS if "lightning" not in param]
    param_paths = [
        kgo_dir / "global" / f"probability_of_{p}_threshold.nc" for p in params
    ]
    wxtree = kgo_dir / "wx_decision_tree.json"
    output_path = tmp_path / "output.nc"
    args = [
        *param_paths,
        "--wxtree",
        wxtree,
        "--model-id-attr",
        "mosg__model_configuration",
        "--output",
        output_path,
    ]
    run_cli(args)
    acc.compare(output_path, kgo_path)


def test_insufficient_files(tmp_path):
    """Test wxcode processing with insufficient files"""
    kgo_dir = acc.kgo_root() / "wxcode"
    params = [
        "low_and_medium_type_cloud_area_fraction_above",
        "low_type_cloud_area_fraction_above",
        "lwe_snowfall_rate_above",
        "rainfall_rate_above",
    ]
    param_paths = [
        kgo_dir / "global" / f"probability_of_{p}_threshold.nc" for p in params
    ]
    wxtree = kgo_dir / "wx_decision_tree.json"
    output_path = tmp_path / "output.nc"
    args = [
        *param_paths,
        "--wxtree",
        wxtree,
        "--model-id-attr",
        "mosg__model_configuration",
        "--output",
        output_path,
    ]
    with pytest.raises(OSError):
        run_cli(args)


@pytest.mark.slow
def test_no_lightning(tmp_path):
    """Test wxcode processing with no lightning"""
    kgo_dir = acc.kgo_root() / "wxcode"
    kgo_path = kgo_dir / "basic" / "kgo_no_lightning.nc"
    param_paths = [
        kgo_dir / "basic" / f"probability_of_{p}_threshold.nc"
        for p in ALL_PARAMS
        if "lightning" not in p
    ]
    wxtree = kgo_dir / "wx_decision_tree.json"
    output_path = tmp_path / "output.nc"
    args = [
        *param_paths,
        "--wxtree",
        wxtree,
        "--model-id-attr",
        "mosg__model_configuration",
        "--output",
        output_path,
    ]
    run_cli(args)
    acc.compare(output_path, kgo_path)
