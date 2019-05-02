#!/usr/bin/python3

import os

if os.path.exists("soap.db"):
    print("Removing old database")
    os.remove("soap.db")

import makedb
print("Database created")

import csv_importer
print("CSV data imported")
