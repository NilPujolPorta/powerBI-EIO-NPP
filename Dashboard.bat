cd ../PandoraFMS_API-NPP
PandoraFMS_API.cpython-39.pyc -q
cd ../CatbackupAPI-NPP
CatbackupAPI-NPP.cpython-39.pyc -q
cd ../SynologyAPI-NPP\SynologyAPI
synology_API.cpython-39.pyc -q
cd ../powerBI

copy /b/v/y/z ..\CatbackupAPI-NPP\dadesCatBackup.json .
copy /b/v/y/z ..\PandoraFMS_API-NPP\dadesPandora.json .
copy /b/v/y/z ..\SynologyAPI-NPP\SynologyAPI\dadesSynology.json .

taskkill /F /IM PBIDesktop.exe
ping 192.0.2.2 -n 1 -w 2000 > nul

cd ../PowerBI_refresher-NPP/refresher
refresh.cpython-39.pyc -q
