from pyspark.sql import SparkSession, Row
from datetime import datetime, timedelta
import sys
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import functions
from pyspark.sql.functions import lit,unix_timestamp
from constants import SRC_ROOT, DELTA_RT, DELTA_EXT, DELTA_CAT, HANA_DLFS_JAR, HANA_DLFS_CERTFILE, HANA_DLFS_KEYFILE, HANA_DLFS_ENDPOINT, HANA_DLFS_AFS, HANA_DLFS_IMPL, HANA_DLFS_KEYSTORE, HANA_DLFS_PWD, HANA_DLFS_PKG
from pyspark import SparkContext
from pyspark import SparkConf



def test_dataframe(spark, current_date):
    # Check if delta table exists
    yesterday_date = current_date - timedelta(days=1)
    test_data = [
        Row(Key='Day 1', DATE=yesterday_date.strftime('%y.%m.%d'), EMPLOYEE_ID='XYZ', KEYFIGURE=123),
        Row(Key='Day 2', DATE=current_date.strftime('%y.%m.%d'), EMPLOYEE_ID='XYZ', KEYFIGURE=321)
    ]
    # spark.createDataFrame(test_data).write.format("delta").mode("overwrite").save(delta_table_path)
    return spark.createDataFrame(test_data)

def read_conf(filename: str) -> SparkConf:
    config = dict()
    with open("hdl-spark.conf") as fp:
        line = fp.readline().strip().split()
        while line:
            if line[0][0] == '#': 
                line = fp.readline().strip().split()
                continue
            config[line[0]] = line[1]
            if line[1] == 'True':
                config[line[0]] = True
            elif line[1] == 'False':
                config[line[0]] = False
            elif line[1].isdigit():
                config[line[0]] = int(line[1])
            line = fp.readline().strip().split()
    conf = SparkConf()
    print("\n********************\nCONFIG:")
    for k,v in config.items():
        print(f"{k}: {v}")
        conf.set(k,v)
    print("********************\n")
    return conf

    
if __name__ == "__main__":
    # Initialize SparkSession

    ENTRYPOINT = "hdlfs://64230620-ccff-4c63-98db-9fc4b38b1db8.files.hdl.prod-us20.hanacloud.ondemand.com"
    CERT = "/Users/D051079/GitHub/hdltools/certificates/hdlmt4.pem"
    KEY = "/Users/D051079/GitHub/hdltools/certificates/hdlmt4.key"
    CONF = "hdl-spark.conf"

    thh_conf = False
    if thh_conf: 
        conf = read_conf(CONF)
        conf.setAppName("DeltaTableManipulation")
        conf.set('spark.hadoop.fs.hdlfs.ssl.certfile', CERT)
        conf.set('spark.hadoop.fs.hdlfs.ssl.keyfile', KEY)


    # My SETTING
    # spark.hadoop.fs.hdlfs.impl com.sap.hana.datalake.files.HdlfsFileSystem
    # spark.hadoop.fs.AbstractFileSystem.hdlfs.impl com.sap.hana.datalake.files.Hdlfs
    # spark.executor.userClassPathFirst True
    # spark.jars /Users/D051079/jars/sap-hdlfs-2.0.22.jar
    # spark.jars.packages io.delta:delta-spark_2.12:3.0.0
    # spark.sql.extensions io.delta.sql.DeltaSparkSessionExtension
    # spark.sql.catalog.spark_catalog org.apache.spark.sql.delta.catalog.DeltaCatalog
    
    else: 
        config = {
            # 'spark.jars.packages': 'com.sap.hana.datalake.files:sap-hdlfs:3.0.3,io.delta:delta-core_2.12',
            'spark.jars.packages': 'com.sap.hana.datalake.files:sap-hdlfs:3.0.3,io.delta:delta-spark_2.12:3.0.0',
            # spark.jars': '/Users/D051079/jars/sap-hdlfs-2.0.22.jar',
            # 'spark.hadoop.fs.defaultFS': ENTRYPOINT,
            'spark.hadoop.fs.AbstractFileSystem.hdlfs.impl': HANA_DLFS_AFS,
            'spark.hadoop.fs.hdlfs.impl': HANA_DLFS_IMPL,
            'spark.hadoop.fs.hdlfs.ssl.certfile': CERT,
            'spark.hadoop.fs.hdlfs.ssl.keyfile': KEY,
            'spark.sql.extensions': DELTA_EXT,
            'spark.sql.catalog.spark_catalog': DELTA_CAT,
        }
        conf = SparkConf()
        print("\n********************\nCONFIG:")
        for k,v in config.items():
            print(f"{k}: {v}")
            conf.set(k,v)
        print("********************\n")
        conf.setAppName("DeltaTableManipulation")

    spark = SparkSession.builder.config(conf=conf).getOrCreate()

    # Define Delta table pat
    delta_table_path = f'{ENTRYPOINT}/basic-delta'
    print(f"Endpoint: {delta_table_path}")

    # Get current system date
    current_date = datetime.now()

    # Create or edit delta table
    df = test_dataframe(spark, current_date)
    df.show()
    df.write.format("delta").mode("overwrite").save(delta_table_path)
    

    # Stop SparkSession
    spark.stop()
