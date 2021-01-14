ma=input("要給予的最大記憶體(G):")
mi=input("要給予的最小記憶體(G):")
name=input("伺服器啟動檔名稱(.jar):")
string=f"@echo off\njava -Xms{int(mi)*1024}M -Xmx{int(ma)*1024}M -jar {name}.jar nogui"
f = open("start.bat",'w')
f.write(string)
f.close()
