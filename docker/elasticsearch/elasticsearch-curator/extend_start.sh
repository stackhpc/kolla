#!/bin/bash

if [[ ! -d "/var/log/kolla/elasticsearch" ]]; then
    install -d -m 0755 -o elasticsearch -g elasticsearch /var/log/kolla/elasticsearch
fi
