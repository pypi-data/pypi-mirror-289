# Versions
VERSION_SPARK = '3.3.0'
VERSION_HDLFS = '3.0.3'
VERSION_SCALA = '2.12'
VERSION_DELTA = '2.2.0'

# HANA Data Lake, Files
HANA_DLFS_FILECONTAINER = '714f4b3c-533e-4c2c-a5f6-a5d7893a03f7'
HANA_DLFS_ENDPOINT = f'hdlfs://{HANA_DLFS_FILECONTAINER}.files.hdl.prod-eu10.hanacloud.ondemand.com' # EP in PM account
HANA_DLFS_REST = f'https://{HANA_DLFS_FILECONTAINER}.files.hdl.prod-eu10.hanacloud.ondemand.com/webhdfs/v1' # EP in PM account
#HANA_DLFS_ROOT = 'BDH-21269'
HANA_DLFS_PKG = f'com.sap.hana.datalake.files:sap-hdlfs:{VERSION_HDLFS}'
HANA_DLFS_AFS = 'com.sap.hana.datalake.files.Hdlfs'
HANA_DLFS_IMPL = 'com.sap.hana.datalake.files.HdlfsFileSystem'
HANA_DLFS_KEYSTORE = '/Users/I535445/Downloads/keystore.p12'
HANA_DLFS_PWD = 'Walldorf'

HANA_DLFS_CERTFILE = '/Users/I535445/Downloads/smoketest-replication-main/certificates/client/admin/client-chain.crt'
HANA_DLFS_KEYFILE = '/Users/I535445/Downloads/smoketest-replication-main/certificates/client/admin/client.key'

HANA_DLFS_JAR = '/Users/I535445/Downloads/sap-hdlfs-1.2.2.jar'



DELTA_RT = f'io.delta:delta-core_{VERSION_SCALA}:{VERSION_DELTA}'
DELTA_EXT = 'io.delta.sql.DeltaSparkSessionExtension'
DELTA_CAT = 'org.apache.spark.sql.delta.catalog.DeltaCatalog'

SRC_ROOT = '<PATH TO SRC_ROOT>'