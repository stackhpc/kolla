#!/bin/bash

if [[ ! -d "/var/log/kolla/alloy" ]]; then
    mkdir -p /var/log/kolla/alloy
fi
if [[ $(stat -c %a /var/log/kolla/alloy) != "755" ]]; then
    chmod 755 /var/log/kolla/alloy
fi
