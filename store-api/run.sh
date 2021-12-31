#! /usr/bin/bash
echo " __Starting in development mode___"
uvicorn app.main:app --reload
# Todo: write to start env & run app both