#!/bin/bash

# hugo list all > before.csv
hugo
export IPFS_DEPLOY_PINATA__API_KEY=38581eeb587581f76928
export IPFS_DEPLOY_CLOUDFLARE__API_EMAIL=beau.cronin@gmail.com
export IPFS_DEPLOY_CLOUDFLARE__ZONE=teetotality.blog
export IPFS_DEPLOY_CLOUDFLARE__RECORD=_dnslink.teetotality.blog
source secrets.sh
ipd -p pinata -d cloudflare -O

hugo list all > current.csv

python publish.py

rm prev.csv
mv current.csv prev.csv
