#!/usr/bin/env bash
python tests/test_shoppinglist.py > /dev/null &
nosetests --with-coverage