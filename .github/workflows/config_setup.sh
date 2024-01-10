#!/bin/bash

echo "config = {" > tast_manager_project/tast_manager_project/config.py
echo "      'SECRET_KEY': '${{ secrets.SECRET_KEY }}'," >> tast_manager_project/tast_manager_project/config.py
echo "      'SECRET_1': '${{ secrets.SECRET_URL }}'," >> tast_manager_project/tast_manager_project/config.py
echo "}" >> tast_manager_project/tast_manager_project/config.py