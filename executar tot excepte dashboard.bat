cd ../PandoraFMS_API-NPP
PandoraFMS_API.cpython-39.pyc -q
cd ../CatbackupAPI-NPP
CatbackupAPI-NPP.cpython-39.pyc -q
cd ../SynologyAPI-NPP
synology_API.cpython-39.pyc -q
cd ../powerBI

copy /b/v/y/z ..\CatbackupAPI-NPP\dadesCatBackup.json .
copy /b/v/y/z ..\PandoraFMS_API-NPP\dadesPandora.json .
copy /b/v/y/z ..\SynologyAPI-NPP\dadesSynology.json .