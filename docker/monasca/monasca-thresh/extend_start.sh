#!/bin/bash

# Create log and data directories, with appropriate permissions
MONASCA_LOG_DIR="/var/log/kolla/monasca"
MONASCA_DATA_DIR="/var/lib/monasca-thresh/data"
if [[ ! -d "$MONASCA_LOG_DIR" ]]; then
    mkdir -p $MONASCA_LOG_DIR
fi
if [[ ! -d "$MONASCA_DATA_DIR" ]]; then
    mkdir -p $MONASCA_DATA_DIR
fi
if [[ $(stat -c %U:%G ${MONASCA_LOG_DIR}) != "monasca:kolla" ]]; then
    chown monasca:kolla ${MONASCA_LOG_DIR}
fi
if [[ $(stat -c %U:%G ${MONASCA_DATA_DIR}) != "monasca:kolla" ]]; then
    chown monasca:kolla ${MONASCA_DATA_DIR}
fi
if [[ $(stat -c %a ${MONASCA_LOG_DIR}) != "755" ]]; then
    chmod 755 ${MONASCA_LOG_DIR}
fi
if [[ $(stat -c %a ${MONASCA_DATA_DIR}) != "755" ]]; then
    chmod 755 ${MONASCA_DATA_DIR}
fi

if [[ $(ls -Ab ${MONASCA_DATA_DIR}) != "" ]]; then
    find ${MONASCA_DATA_DIR} -mindepth 1 -delete
fi

. /usr/local/bin/kolla_monasca_extend_start
