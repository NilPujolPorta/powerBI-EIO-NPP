from SynologyAPI import synology_API
from catbackupAPI import CatbackupAPI_NPP
from PandoraAPI import PandoraFMS_API
from HyperbackupAPI2 import HyperbackupAPI2_NPP
from refresher import refresher
import argparse

__version__= "0.2.2"
def main(args=None):
    
    parser = argparse.ArgumentParser(description='Serveix per actualitzar dashboard de PowerBI desktop localment.')
    parser.add_argument('-q', '--quiet', help='Nomes mostra els errors i el missatge de acabada per pantalla.', action="store_false")
    parser.add_argument('-v', '--versio', help='Mostra la versio', action='version', version='refresh-PowerBI v'+__version__)
    args = parser.parse_args(args)

    rutaExcelPandora = "C:\\ns/excelPandora.xlsx"
    rutaExcelSynology = "C:\\ns/excelSynology.xlsx"
    rutaJSONSynology = "C:\\ns/dadesSynology.json"
    rutaJSONCatbackup ="C:\\ns/dadesCatbackup.json"
    rutaJSONPandora ="C:\\ns/dadesPandora.json"
    rutaJSONHyperbackup2="C:\\ns/dadesHyperBackup2.json"

    rutaChromePortable=""

    rutaPBIX="C:\\ns/apis.pbix"
    if args.quiet:
        PandoraFMS_API.main(['-q','-e','-f',rutaExcelPandora,'--json-file',rutaJSONPandora])
        CatbackupAPI_NPP.main(['-q','--json-file',rutaJSONCatbackup])#'--portable-chrome-path', rutaChromePortable
        synology_API.main(['-q','-e','--json-file',rutaJSONSynology,'-f',rutaExcelSynology])
        HyperbackupAPI2_NPP.main(['-q','--json-file',rutaJSONHyperbackup2])#'--portable-chrome-path', rutaChromePortable
    else:
        PandoraFMS_API.main(['-e','-f',rutaExcelPandora,'--json-file',rutaJSONPandora])
        CatbackupAPI_NPP.main(['--json-file',rutaJSONCatbackup])
        synology_API.main(['-e','--json-file',rutaJSONSynology,'-f',rutaExcelSynology])
        HyperbackupAPI2_NPP.main(['--json-file',rutaJSONHyperbackup2])#'--portable-chrome-path', rutaChromePortable
    try:
        refresher.main(['-f',rutaPBIX])
    except:
        print("Error en refrescar. Assegura't que el fitxer existeix")

if __name__ =='__main__':
    main()