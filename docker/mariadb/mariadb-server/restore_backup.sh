#!/usr/bin/env bash

set -eu
set -o pipefail

BACKUP_DIR=/backup/

restore_full() {
    rm -rf /var/lib/mysql/*
    rm -rf /var/lib/mysql/\.[^\.]*
    mariabackup --copy-back --target-dir $BACKUP_DIR/restore/full
}

if [ -n "${BACKUP_TYPE}" ]; then
    case "${BACKUP_TYPE}" in
        "full")
            restore_full
            ;;
        "incremental")
            #TODO: find a way to use incremental backup nicely
            exit 1
            ;;
        *)
            echo "Only full or incremental options are supported."
            exit 1
            ;;
    esac
else
    echo "You need to specify either full or incremental backup options."
    exit 1
fi
