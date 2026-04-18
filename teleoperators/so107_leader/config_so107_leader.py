#!/usr/bin/env python

# Copyright 2026 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass

from lerobot.teleoperators.config import TeleoperatorConfig


@dataclass
class SO107LeaderTeleopConfig(TeleoperatorConfig):
    port: str
    baud_rate: int = 1000000
    use_degrees: bool = True


@TeleoperatorConfig.register_subclass("so107_leader")
@dataclass
class SO107LeaderConfig(SO107LeaderTeleopConfig):
    pass
