# 
### mm/dd/yyyy ###
d=$(date +"%Y-%m-%d %T")
git add .
git commit -m "vault backup ${d}" 
git push
