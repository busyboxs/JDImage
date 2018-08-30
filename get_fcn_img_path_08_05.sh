sql="
    select sku, img_path, url
    from
    (
        
	    select sku, img_path, url, item_third_cate_cd
	    from
            tmp.com_trans0727_3
    ) a
    join
    (
        select item_third_cate_cd
        from 
        tmp.tmp_add_third_cate_cd_08_06    
    ) b
    on a.item_third_cate_cd = b.item_third_cate_cd
"
hive -e "$sql" > fcn_img_path_08_06_add
