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
"""Utilities for Unit tests for Weather Symbols"""

from typing import Any, Dict


def wxcode_decision_tree() -> Dict[str, Dict[str, Any]]:
    """
    Define an example decision tree to test the weather symbols code.

    Returns:
        A dictionary containing the queries that comprise the decision
        tree.
    """
    queries = {
        "lightning": {
            "if_true": "lightning_cloud",
            "if_false": "heavy_precipitation",
            "if_diagnostic_missing": "if_false",
            "probability_thresholds": [0.3],
            "threshold_condition": ">=",
            "condition_combination": "",
            "diagnostic_fields": [
                "probability_of_number_of_lightning_flashes_per_unit_area_in_vicinity_above_threshold"  # noqa: E501
            ],
            "diagnostic_thresholds": [[0.0, "m-2"]],
            "diagnostic_conditions": ["above"],
        },
        "lightning_cloud": {
            "if_true": 29,
            "if_false": 30,
            "probability_thresholds": [0.5],
            "threshold_condition": ">=",
            "condition_combination": "",
            "diagnostic_fields": ["probability_of_shower_condition_above_threshold"],
            "diagnostic_thresholds": [[1.0, 1]],
            "diagnostic_conditions": ["above"],
        },
        "heavy_precipitation": {
            "if_true": "heavy_precipitation_cloud",
            "if_false": "precipitation_in_vicinity",
            "probability_thresholds": [0.5],
            "threshold_condition": ">=",
            "condition_combination": "",
            "diagnostic_fields": [
                "probability_of_lwe_precipitation_rate_above_threshold"
            ],
            "diagnostic_thresholds": [[1.0, "mm hr-1"]],
            "diagnostic_conditions": ["above"],
        },
        "heavy_precipitation_cloud": {
            "if_true": "heavy_snow_shower",
            "if_false": "heavy_snow_continuous",
            "probability_thresholds": [0.5],
            "threshold_condition": ">=",
            "condition_combination": "",
            "diagnostic_fields": ["probability_of_shower_condition_above_threshold"],
            "diagnostic_thresholds": [[1.0, 1]],
            "diagnostic_conditions": ["above"],
        },
        "heavy_snow_shower": {
            "if_true": 26,
            "if_false": "heavy_rain_or_sleet_shower",
            "probability_thresholds": [0.0],
            "threshold_condition": "<",
            "condition_combination": "",
            "diagnostic_fields": [
                [
                    "probability_of_lwe_sleetfall_rate_above_threshold",
                    "+",
                    "probability_of_rainfall_rate_above_threshold",
                    "-",
                    "probability_of_lwe_snowfall_rate_above_threshold",
                ]
            ],
            "diagnostic_thresholds": [
                [[1.0, "mm hr-1"], [1.0, "mm hr-1"], [1.0, "mm hr-1"]]
            ],
            "diagnostic_conditions": [["above", "above", "above"]],
        },
        "heavy_rain_or_sleet_shower": {
            "if_true": 14,
            "if_false": 17,
            "probability_thresholds": [0.0],
            "threshold_condition": "<",
            "condition_combination": "",
            "diagnostic_fields": [
                [
                    "probability_of_lwe_sleetfall_rate_above_threshold",
                    "+",
                    "probability_of_lwe_snowfall_rate_above_threshold",
                    "-",
                    "probability_of_rainfall_rate_above_threshold",
                ]
            ],
            "diagnostic_thresholds": [
                [[1.0, "mm hr-1"], [1.0, "mm hr-1"], [1.0, "mm hr-1"]]
            ],
            "diagnostic_conditions": [["above", "above", "above"]],
        },
        "heavy_snow_continuous": {
            "if_true": 27,
            "if_false": "heavy_rain_or_sleet_continuous",
            "probability_thresholds": [0.0],
            "threshold_condition": "<",
            "condition_combination": "",
            "diagnostic_fields": [
                [
                    "probability_of_lwe_sleetfall_rate_above_threshold",
                    "+",
                    "probability_of_rainfall_rate_above_threshold",
                    "-",
                    "probability_of_lwe_snowfall_rate_above_threshold",
                ]
            ],
            "diagnostic_thresholds": [
                [[1.0, "mm hr-1"], [1.0, "mm hr-1"], [1.0, "mm hr-1"]]
            ],
            "diagnostic_conditions": [["above", "above", "above"]],
        },
        "heavy_rain_or_sleet_continuous": {
            "if_true": 15,
            "if_false": 18,
            "probability_thresholds": [0.0],
            "threshold_condition": "<",
            "condition_combination": "",
            "diagnostic_fields": [
                [
                    "probability_of_lwe_sleetfall_rate_above_threshold",
                    "+",
                    "probability_of_lwe_snowfall_rate_above_threshold",
                    "-",
                    "probability_of_rainfall_rate_above_threshold",
                ]
            ],
            "diagnostic_thresholds": [
                [[1.0, "mm hr-1"], [1.0, "mm hr-1"], [1.0, "mm hr-1"]]
            ],
            "diagnostic_conditions": [["above", "above", "above"]],
        },
        "precipitation_in_vicinity": {
            "if_true": "snow_in_vicinity",
            "if_false": "drizzle_mist",
            "probability_thresholds": [0.5],
            "threshold_condition": ">=",
            "condition_combination": "",
            "diagnostic_fields": [
                "probability_of_lwe_precipitation_rate_in_vicinity_above_threshold"
            ],
            "diagnostic_thresholds": [[0.1, "mm hr-1"]],
            "diagnostic_conditions": ["above"],
        },
        "snow_in_vicinity": {
            "if_true": "snow_in_vicinity_cloud",
            "if_false": "rain_or_sleet_in_vicinity",
            "probability_thresholds": [0.0],
            "threshold_condition": "<",
            "condition_combination": "",
            "diagnostic_fields": [
                [
                    "probability_of_lwe_sleetfall_rate_above_threshold",
                    "+",
                    "probability_of_rainfall_rate_above_threshold",
                    "-",
                    "probability_of_lwe_snowfall_rate_above_threshold",
                ]
            ],
            "diagnostic_thresholds": [
                [[0.03, "mm hr-1"], [0.03, "mm hr-1"], [0.03, "mm hr-1"]]
            ],
            "diagnostic_conditions": [["above", "above", "above"]],
        },
        "snow_in_vicinity_cloud": {
            "if_true": "heavy_snow_shower_in_vicinity",
            "if_false": "heavy_snow_continuous_in_vicinity",
            "probability_thresholds": [0.5],
            "threshold_condition": ">=",
            "condition_combination": "",
            "diagnostic_fields": ["probability_of_shower_condition_above_threshold"],
            "diagnostic_thresholds": [[1.0, 1]],
            "diagnostic_conditions": ["above"],
        },
        "heavy_snow_shower_in_vicinity": {
            "if_true": 26,
            "if_false": 23,
            "probability_thresholds": [0.5],
            "threshold_condition": ">=",
            "condition_combination": "",
            "diagnostic_fields": [
                "probability_of_lwe_precipitation_rate_in_vicinity_above_threshold"
            ],
            "diagnostic_thresholds": [[1.0, "mm hr-1"]],
            "diagnostic_conditions": ["above"],
        },
        "heavy_snow_continuous_in_vicinity": {
            "if_true": 27,
            "if_false": 24,
            "probability_thresholds": [0.5],
            "threshold_condition": ">=",
            "condition_combination": "",
            "diagnostic_fields": [
                "probability_of_lwe_precipitation_rate_in_vicinity_above_threshold"
            ],
            "diagnostic_thresholds": [[1.0, "mm hr-1"]],
            "diagnostic_conditions": ["above"],
        },
        "rain_or_sleet_in_vicinity": {
            "if_true": "rain_in_vicinity_cloud",
            "if_false": "sleet_in_vicinity_cloud",
            "probability_thresholds": [0.0],
            "threshold_condition": "<",
            "condition_combination": "",
            "diagnostic_fields": [
                [
                    "probability_of_lwe_sleetfall_rate_above_threshold",
                    "+",
                    "probability_of_lwe_snowfall_rate_above_threshold",
                    "-",
                    "probability_of_rainfall_rate_above_threshold",
                ]
            ],
            "diagnostic_thresholds": [
                [[0.03, "mm hr-1"], [0.03, "mm hr-1"], [0.03, "mm hr-1"]]
            ],
            "diagnostic_conditions": [["above", "above", "above"]],
        },
        "rain_in_vicinity_cloud": {
            "if_true": "heavy_rain_shower_in_vicinity",
            "if_false": "heavy_rain_continuous_in_vicinity",
            "probability_thresholds": [0.5],
            "threshold_condition": ">=",
            "condition_combination": "",
            "diagnostic_fields": ["probability_of_shower_condition_above_threshold"],
            "diagnostic_thresholds": [[1.0, 1]],
            "diagnostic_conditions": ["above"],
        },
        "heavy_rain_shower_in_vicinity": {
            "if_true": 14,
            "if_false": 10,
            "probability_thresholds": [0.5],
            "threshold_condition": ">=",
            "condition_combination": "",
            "diagnostic_fields": [
                "probability_of_lwe_precipitation_rate_in_vicinity_above_threshold"
            ],
            "diagnostic_thresholds": [[1.0, "mm hr-1"]],
            "diagnostic_conditions": ["above"],
        },
        "heavy_rain_continuous_in_vicinity": {
            "if_true": 15,
            "if_false": 12,
            "probability_thresholds": [0.5],
            "threshold_condition": ">=",
            "condition_combination": "",
            "diagnostic_fields": [
                "probability_of_lwe_precipitation_rate_in_vicinity_above_threshold"
            ],
            "diagnostic_thresholds": [[1.0, "mm hr-1"]],
            "diagnostic_conditions": ["above"],
        },
        "sleet_in_vicinity_cloud": {
            "if_true": 17,
            "if_false": 18,
            "probability_thresholds": [0.5],
            "threshold_condition": ">=",
            "condition_combination": "",
            "diagnostic_fields": ["probability_of_shower_condition_above_threshold"],
            "diagnostic_thresholds": [[1.0, 1]],
            "diagnostic_conditions": ["above"],
        },
        "drizzle_mist": {
            "if_true": "drizzle_is_rain",
            "if_false": "drizzle_cloud",
            "probability_thresholds": [0.5, 0.5],
            "threshold_condition": ">=",
            "condition_combination": "AND",
            "diagnostic_fields": [
                "probability_of_lwe_precipitation_rate_above_threshold",
                "probability_of_visibility_in_air_below_threshold",
            ],
            "diagnostic_thresholds": [[0.03, "mm hr-1"], [5000.0, "m"]],
            "diagnostic_conditions": ["above", "below"],
        },
        "drizzle_cloud": {
            "if_true": "drizzle_is_rain",
            "if_false": "mist_conditions",
            "probability_thresholds": [0.5, 0.5],
            "threshold_condition": ">=",
            "condition_combination": "AND",
            "diagnostic_fields": [
                "probability_of_lwe_precipitation_rate_above_threshold",
                "probability_of_low_type_cloud_area_fraction_above_threshold",
            ],
            "diagnostic_thresholds": [[0.03, "mm hr-1"], [0.85, 1]],
            "diagnostic_conditions": ["above", "above"],
        },
        "drizzle_is_rain": {
            "if_true": 11,
            "if_false": "mist_conditions",
            "probability_thresholds": [0.0],
            "threshold_condition": "<",
            "condition_combination": "",
            "diagnostic_fields": [
                [
                    "probability_of_lwe_sleetfall_rate_above_threshold",
                    "+",
                    "probability_of_lwe_snowfall_rate_above_threshold",
                    "-",
                    "probability_of_rainfall_rate_above_threshold",
                ]
            ],
            "diagnostic_thresholds": [
                [[0.03, "mm hr-1"], [0.03, "mm hr-1"], [0.03, "mm hr-1"]]
            ],
            "diagnostic_conditions": [["above", "above", "above"]],
        },
        "mist_conditions": {
            "if_true": "fog_conditions",
            "if_false": "no_precipitation_cloud",
            "probability_thresholds": [0.5],
            "threshold_condition": ">=",
            "condition_combination": "",
            "diagnostic_fields": ["probability_of_visibility_in_air_below_threshold"],
            "diagnostic_thresholds": [[5000.0, "m"]],
            "diagnostic_conditions": ["below"],
        },
        "fog_conditions": {
            "if_true": 6,
            "if_false": 5,
            "probability_thresholds": [0.5],
            "threshold_condition": ">=",
            "condition_combination": "",
            "diagnostic_fields": ["probability_of_visibility_in_air_below_threshold"],
            "diagnostic_thresholds": [[1000.0, "m"]],
            "diagnostic_conditions": ["below"],
        },
        "no_precipitation_cloud": {
            "if_true": "overcast_cloud",
            "if_false": "partly_cloudy",
            "probability_thresholds": [0.5],
            "threshold_condition": ">=",
            "condition_combination": "",
            "diagnostic_fields": [
                "probability_of_low_and_medium_type_cloud_area_fraction_above_threshold"
            ],
            "diagnostic_thresholds": [[0.8125, 1]],
            "diagnostic_conditions": ["above"],
        },
        "overcast_cloud": {
            "if_true": 8,
            "if_false": 7,
            "probability_thresholds": [0.5],
            "threshold_condition": ">=",
            "condition_combination": "",
            "diagnostic_fields": [
                "probability_of_low_type_cloud_area_fraction_above_threshold"
            ],
            "diagnostic_thresholds": [[0.85, 1]],
            "diagnostic_conditions": ["above"],
        },
        "partly_cloudy": {
            "if_true": 3,
            "if_false": 1,
            "probability_thresholds": [0.5],
            "threshold_condition": ">=",
            "condition_combination": "",
            "diagnostic_fields": [
                "probability_of_low_and_medium_type_cloud_area_fraction_above_threshold"
            ],
            "diagnostic_thresholds": [[0.1875, 1]],
            "diagnostic_conditions": ["above"],
        },
    }

    return queries
