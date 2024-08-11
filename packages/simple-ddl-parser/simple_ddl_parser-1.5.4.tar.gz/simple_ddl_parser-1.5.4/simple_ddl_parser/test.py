from simple_ddl_parser import DDLParser
import pprint

ddl = """ create or replace table if not exists TABLE_DATA_SRC.EXT_PAYLOAD_MANIFEST_WEB (
       id bigint,
       derived bigint as (id * 10)
       )
    location = @ADL_Azure_Storage_Account_Container_Name/entity
    auto_refresh = false
    file_format = (TYPE=JSON NULL_IF=('field') DATE_FORMAT=AUTO TRIM_SPACE=TRUE)
    stage_file_format = (TYPE=JSON NULL_IF=())
    ;"""


"""DROP TABLE IF EXISTS contacts;

    CREATE TABLE contacts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        fullname varchar(101) GENERATED ALWAYS AS (CONCAT(first_name,' ',last_name)),
        email VARCHAR(100) NOT NULL
    );"""


"""CREATE EXTERNAL TABLE `database`.`table` (
    column1 string,
    column2 string
)
PARTITIONED BY
(
    column3 integer
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
ESCAPED BY '\\'
LINES TERMINATED BY '\n'
STORED AS TEXTFILE
LOCATION 's3://somewhere-in-s3/prefix1'
TBLPROPERTIES (
  'parquet.compression'='GZIP'
)"""

result = DDLParser(ddl, debug=True).run()
pprint.pprint(result)


