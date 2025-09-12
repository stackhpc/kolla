#!/usr/bin/env bash

set -eu
set -o pipefail

BACKUP_DIR=/backup/
FULL_FILE="{$BACKUP_DIR/last_full.mbs}"
INC_FILE="{$BACKUP_DIR/last_inc.mbs}"

cleanup_previous() {
    rm -rf $BACKUP_DIR/restore
    rm -f $FULL_FILE
    rm -f $INC_FILE
}

change_prefix() {
    echo "Changing xtrabackup_* prefix to mariadb_backup_*"
    for file in xtrabackup_*; do
        mv "$file" "$(echo "$file" | sed s/xtrabackup_/mariadb_backup_)"
    done
}

get_last_full_filename() {
    return $(cat "${BACKUP_DIR}/last_full_file")
}

prepare_restore_full() {
    mkdir -p $BACKUP_DIR/restore/full
    gunzip -k -c $(get_last_full_filename) > $FULL_FILE
    mbstream -x -C $BACKUP_DIR/restore/full < $FULL_FILE
    pushd $BACKUP_DIR/restore/full
    change_prefix
    popd
    mariabackup --prepare --target-dir $BACKUP_DIR/restore/full
}

restore_full() {
    rm -rf /var/lib/mysql/*
    rm -rf /var/lib/mysql/\.[^\.]*
    mariabackup --copy-back --target-dir $BACKUP_DIR/restore/full
}

if [ -n "${BACKUP_TYPE}" ]; then
    case "${BACKUP_TYPE}" in
        "full")
            prepare_restore_full
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
