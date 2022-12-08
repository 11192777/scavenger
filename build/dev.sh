git fetch qingyu
git reset --hard qingyu/dev
npm install -C ../web/
nohup python dev.py > scavenger.log 2>&1 &
nohup npm run dev-local -C ../web/ > scavenger-web.log 2>&1 &
