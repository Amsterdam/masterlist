#!/usr/bin/env bash
grep -Eiv '^create schema \w+;' \
    | grep -Eiv '^alter .* owner to .*;' \
    | sed 's/masterlist./public./g' \
    | grep -v '^\-\-' \
    | sed -E 's/^CREATE TABLE (.*) \(/DROP TABLE IF EXISTS \1 cascade; CREATE TABLE \1 \(/g'
    # | sed -E 's/^CREATE TYPE (\w+.\w+) (.*)/DROP TYPE \1; CREATE TYPE \1 \2/g' \
    # | sed -E 's/^CREATE SEQUENCE (\w+.\w+)/DROP SEQUENCE \1; CREATE SEQUENCE \1/g'
