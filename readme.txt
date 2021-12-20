				____----====Funció de cada fitxer====----____

==Dashboard_vs2.0.vbs== --> executa Dashboard.bat en rerefons(background)

==*.json== --> son les dades que donen les diferents apis mes una llegenda feta manualment per millor organització

==apis.pbix== --> es el dashboard de PowerBI que conjunta totes les dades dels *.json

==Dashboard.bat== --> Executa els python, actualitza els *.json,
actualitza el dashboard i el deixa obert. Per fer un dashboard automtic aquest fitxer s'hauria d'executar cada x temps.

==executar tot excepte dashboard.bat== --> Fa el mateix que Dashboard.bat pero sense obrir ni actualitzar el dashboard de PowerBI

==Refresh== --> es la carpeta que conte el programa per actualitzar el PowerBI

==requirments.txt== --> te el nom de tots els paquets requerits pel funcionament del programa