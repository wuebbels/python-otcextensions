#!/usr/bin/env python3
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
"""
Retry a task or terminate the impact of a task
"""

import openstack

openstack.enable_logging(True)
conn = openstack.connect()

cluster_name_or_id = '3b300b4e-2aa9-45c0-b898-a9e6fa319922'
job_id = '0249620d-1c4a-4211-943a-ced7b9a3cda5'
retry_mode = 'abort'

cluster = conn.css.find_cluster(cluster_name_or_id)

conn.css.retry_cluster_upgrade_job(cluster, job_id, retry_mode)