#!/bin/bash

# 특정 날짜에 해당하는s3를 받아오는 스크립트


date_array=(29)
data_source='cData_day2'

for date in "${date_array[@]}"
do
  aws s3 cp s3://storelink-prod-fstore-src/$data_source/2022/04/$date ./2022/04/$date --recursive
done
