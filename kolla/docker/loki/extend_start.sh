#!/bin/bash

if [[ ! -d "/var/log/kolla/loki" ]]; then
    mkdir -p /var/log/kolla/loki
fi
if [[ $(stat -c %a /var/log/kolla/loki) != "755" ]]; then
    chmod 755 /var/log/kolla/loki
fi
