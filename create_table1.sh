sql="
    drop table if exists tmp.tmp_add_third_cate_cd_08_06_test;
    create table if not exists tmp.tmp_add_third_cate_cd_08_06_test(
        item_third_cate_cd string
    )
    row format delimited fields terminated by '\t';
    load data local inpath 'cd.txt' overwrite into table tmp.tmp_add_third_cate_cd_08_06_test;
"
hive -e "$sql"
