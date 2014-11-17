#!/bin/bash



$year = $(date +%Y)
$month = $(date +%m)
$day = $(date +%d)

echo "http://www.etfos.unios.hr/?digitalni_raspored&m3=($year)-($month)-($day)&m4=3-7#raspored"

chromium-browser "http://www.gpp-osijek.com/files/polasci/zima/Jug2.pdf" "http://pljusak.com/retfala/wx.htm" "http://www.etfos.unios.hr/?digitalni_raspored&m4=3-7#raspored"
