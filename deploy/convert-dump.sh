#!/usr/bin/env bash
grep -Eiv '^create schema \w+;' | grep -Eiv '^alter .* owner to .*;' | sed 's/masterlist./public./g' | grep -v '^\-\-'
