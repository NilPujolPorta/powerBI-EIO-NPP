cd ../PandoraFMS_API-NPP/PandoraAPI
PandoraFMS_API.cpython-39.pyc -q
cd ../../CatbackupAPI-NPP\CatBackupAPI\
CatbackupAPI_NPP.cpython-39.pyc -q
cd ../../SynologyAPI-NPP\SynologyAPI\
synology_API.cpython-39.pyc -qe
cd ../../powerBI

copy /b/v/y/z ..\CatbackupAPI-NPP\CatBackupAPI\dadesCatBackup.json .
copy /b/v/y/z ..\PandoraFMS_API-NPP\PandoraAPI\dadesPandora.json .
copy /b/v/y/z ..\SynologyAPI-NPP\SynologyAPI\dadesSynology.json .