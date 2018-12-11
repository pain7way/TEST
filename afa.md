
| 参数名称  | 备注 | 库    | 表  | 字段 |
|-------|:---:|:-----------:|:-------:|:-------:|
| item_id | 物料id物料唯一标识corpon_numbercno | src_qf_prod_coupon | src_qf_prod_coupon.coupon | c_no | 
| pool_id | 优惠券适合的广场id | src_qf_prod_coupon | src_qf_prod_coupon.coupon_store_rule | c_no |  
| tags | 标签信息，如品牌、业态等 | src_mall | src_mall.product | first_category,second_category,third_category |
| small_type | 优惠券类型，如代金券、兑换券、停车券等 | src_qf_prod_coupon | src_qf_prod_coupon.coupon | c_type |
| price_real | 优惠券售价 （增加优惠类型） | src_mall | src_mall.product | price |
| price_expect | 优惠券价值 有可能 投放过滤：投放时间（静态）和库存（去库存+锁库存剩下的） | src_qf_prod_coupon | src_qf_prod_coupon.coupon | c_value |
| vendor_desc | 商家的描述信息（增加商家-品牌/门店ID） | src_mall | src_mall.product | brand_id |
| publish | 1 - 上架（默认）， 0 - 下架| nan | nan | nan | 
| show_end_time | 投放开始时间 | app_compass | app_compass.baseinfo_goods | show_begin_time |
| show_end_time | 投放结束时间 | app_compass | app_compass.baseinfo_goods | show_end_time |
| cs_stock_num | 可用库存 | src_qf_prod_coupon | src_qf_prod_coupon.coupon_stock | cs_stock_num |
| item_desc | 优惠券描述信息，如标题或券的描述 | src_mall | src_mall.product | title,subtitle,description |
| item_desc | 优惠券描述信息，如标题或券的描述 | src_qf_prod_coupon | src_qf_prod_coupon.coupon | c_title,c_subtitle,c_person_each_limit,c_person_daily_each_limit,c_use_period,c_use_rule,c_expired_after_hours |
| store_id | 门店id | src_qf_prod_coupon | src_qf_prod_coupon.coupon_store_rule | csr_store_id   |
