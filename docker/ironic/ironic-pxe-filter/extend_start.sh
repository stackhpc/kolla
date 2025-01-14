#!/bin/bash

# NOTE(wszumski): This container must be in same process namespace as dnsmasq
rm -f /usr/lib/ironic/hostsdir/* && kill -HUP $(cat /run/ironic/dnsmasq.pid) || true

