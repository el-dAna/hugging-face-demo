[![Sync to Hugging Face hub](https://github.com/el-dAna/hugging-face-demo/actions/workflows/main.yml/badge.svg)](https://github.com/el-dAna/hugging-face-demo/actions/workflows/main.yml)
# hugging-face-demo

### To call microservice, do something like this
'''bash
curl -X 'GET' \
  'https://miniature-barnacle-6xw995p94v725r5w-8000.app.github.dev/add/5/5' \
  -H 'accept: application/json'
'''

### Build docker image
'docker build .'
'docker image ls'
'docker run -p 127.0.0.1:8080:8080 image_id_here'
kill a process using same address
'ps -ef | grep python'
'kill -9'
