ommand line instructions


Git global setup

git config --global user.name "张凯"
git config --global user.email "zhangkai@cctv.cn"

Create a new repository

git clone git@git.cctv.cn:devops/home_index.git
cd home_index
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master

Existing folder

cd existing_folder
git init
git remote add origin git@git.cctv.cn:devops/home_index.git
git add .
git commit
git push -u origin master

Existing Git repository

cd existing_repo
git remote add origin git@git.cctv.cn:devops/home_index.git
git push -u origin --all
git push -u origin --tags
