item  
-------
| 参数名称  | 备注 | 库    | 表  | 需要取出的字段 |
|-------|:---:|:-----------:|:-------:|:-------|
| item_id | 物料id物料唯一标识corpon_numbercno | src_qf_prod_coupon | src_qf_prod_coupon.coupon | c_no | 
| pool_id | 优惠券适合的广场id | src_qf_prod_coupon | src_qf_prod_coupon.coupon_store_rule | c_no |  
| tags | 标签信息，如品牌、业态等 | src_mall | src_mall.product | first_category<br>second_category<br>third_category |
| small_type | 优惠券类型，如代金券、兑换券、停车券等 | src_qf_prod_coupon | src_qf_prod_coupon.coupon | c_type |
| price_real | 优惠券售价 （增加优惠类型） | src_mall | src_mall.product | price |
| price_expect | 优惠券价值 有可能 投放过滤：投放时间（静态）和库存（去库存+锁库存剩下的） | src_qf_prod_coupon | src_qf_prod_coupon.coupon | c_value |
| vendor_desc | 商家的描述信息（增加商家-品牌/门店ID） | src_mall | src_mall.product | brand_id |
| publish | 1 - 上架（默认）， 0 - 下架|   |   |   | 
| show_end_time | 投放开始时间 | app_compass | app_compass.baseinfo_goods | show_begin_time |
| show_end_time | 投放结束时间 | app_compass | app_compass.baseinfo_goods | show_end_time |
| cs_stock_num | 可用库存 | src_qf_prod_coupon | src_qf_prod_coupon.coupon_stock | cs_stock_num |
| item_desc | 优惠券描述信息，如标题或券的描述 | src_mall | src_mall.product | title<br>subtitle<br>description |
| item_desc | 优惠券描述信息，如标题或券的描述 | src_qf_prod_coupon | src_qf_prod_coupon.coupon | c_title<br>c_subtitle<br>c_person_each_limit<br>c_person_daily_each_limit<br>c_use_period<br>c_use_rule<br>c_expired_after_hours |
| store_id | 门店id | src_qf_prod_coupon | src_qf_prod_coupon.coupon_store_rule | csr_store_id   |

action 
-------
| 参数名称  | 备注 | 库    | 表  | 字段 |
|-------|:---:|:-----------:|:-------:|:-------|
| item_id | 物料id，物料唯一标识 | src_qf_prod_coupon | src_qf_prod_coupon.coupon | c_no  |
| uid | imei/idfa，手机号、openID | src_qianfan | src_qianfan.wechat_mini_program_log | mobile  |
| uid_type | 0-imei/idfa，2- 手机号，3-openID |   |   |   |
| scene_id | 场景ID，sc_01：首页，sc_02：详情页，sc03：支付页 | src_qianfan | src_qianfan.wechat_mini_program_log | orig_info里的event_id  |
| action_type | 用户行为：1-曝光 2-点击 3-转换（购买） 4-点赞（核销） 5-评论（退款/购买但没核销） | src_qianfan | src_qianfan.wechat_mini_program_log | orig_info里的event_id  |
| session_id（改成tracr_id） | 向推荐引擎请求列表时由推荐引擎返回的session_id，用于A/Btesting分流和效果测试 | src_qianfan | src_qianfan.wechat_mini_program_log | distinct_id  |
| action_id | 行为发生时间戳，秒级时间戳(需要确定是请求前还是请求后曝光，event_id去确定-赵淑云) | src_qianfan | src_qianfan.wechat_mini_program_log | orig_info里的event_time  |
| pool_id | 优惠券适合的广场id（同item上报信息） | src_qf_prod_coupon | src_qf_prod_coupon.coupon_store_rule | c_no    |




需要从下表取出字段
-------
    src_qf_prod_coupon.coupon
    src_mall.product
    app_compass.baseinfo_goods
    src_qf_prod_coupon.coupon_stock
    src_qf_prod_coupon.coupon_store_rule
    src_qianfan.wechat_mini_program_log

| 库  | 表 | 字段   | 类型  | 备注 | 更新周期 |
|-------|:---:|:-----------:|:-------:|:-------|:-------|
| src_qf_prod_coupon | src_qf_prod_coupon.coupon | c_no | int | 券id | 每日 1点 数分钟  |
| src_qf_prod_coupon | src_qf_prod_coupon.coupon | c_value | int | 面值（分）/折扣 / 兑换券：多少件 | 每日 1点 数分钟  |
| src_qf_prod_coupon | src_qf_prod_coupon.coupon | c_type | int | 券类型（1：代金券 2: 礼品券 3：折扣券 4：停车券） | 每日 1点 数分钟  |
| src_qf_prod_coupon | src_qf_prod_coupon.coupon | c_title | string | 券标签 | 每日 1点 数分钟  |
| src_qf_prod_coupon | src_qf_prod_coupon.coupon | c_subtitle | string | 券标签 | 每日 1点 数分钟  |
| src_qf_prod_coupon | src_qf_prod_coupon.coupon | c_person_each_limit | string | 券标签 | 每日 1点 数分钟  |
| src_qf_prod_coupon | src_qf_prod_coupon.coupon | c_person_daily_each_limit | string | 券标签 | 每日 1点 数分钟  |
| src_qf_prod_coupon | src_qf_prod_coupon.coupon | c_use_period | string | 券标签 | 每日 1点 数分钟  |
| src_qf_prod_coupon | src_qf_prod_coupon.coupon | c_use_rule | string | 券标签 | 每日 1点 数分钟  |
| src_qf_prod_coupon | src_qf_prod_coupon.coupon | c_expired_after_hours | string | 券标签 | 每日 1点 数分钟  |
| src_mall | src_mall.product | detail | string | 券id | 每日 1点 数分钟  |
| src_mall | src_mall.product | first_category | bigint | 一级类目 | 每日 1点 数分钟  |
| src_mall | src_mall.product | second_category | bigint | 二级类目 | 每日 1点 数分钟  |
| src_mall | src_mall.product | third_category | bigint | 三级类目 | 每日 1点 数分钟  |
| src_mall | src_mall.product | title | string | 商品名称 | 每日 1点 数分钟  |
| src_mall | src_mall.product | subtitle | string | 副标题 | 每日 1点 数分钟  |
| src_mall | src_mall.product | description | string | 商品描述 | 每日 1点 数分钟  |
| src_mall | src_mall.product | price | int | 商品价格(分) | 每日 1点 数分钟  |
| src_mall | src_mall.product | brand_id | int | 品牌ID | 每日 1点 数分钟  |
| app_compass | app_compass.baseinfo_goods | coupon_id | string | 券id | 每日 6点半 1小时  |
| app_compass | app_compass.baseinfo_goods | show_begin_time | string | 投放开始时间 | 每日 6点半 2小时  |
| app_compass | app_compass.baseinfo_goods | show_end_time | string | 投放结束时间 | 每日 6点半 3小时  |
| src_qf_prod_coupon | src_qf_prod_coupon.coupon_stock | cs_stock_num | int | 可用数 | 每日 1点 数分钟  |
| src_qf_prod_coupon | src_qf_prod_coupon.coupon_stock | c_no | int | 券id | 每日 1点 数分钟  |
| src_qf_prod_coupon | src_qf_prod_coupon.coupon_store_rule | csr_plaza_id   | int | 广场id | 每日 1点 数分钟  |
| src_qf_prod_coupon | src_qf_prod_coupon.coupon_store_rule | c_no   | int | 券id  | 每日 1点 数分钟  |
| src_qf_prod_coupon | src_qf_prod_coupon.coupon_store_rule | csr_store_id   | int | 门店id | 每日 1点 数分钟  |
| src_qianfan	| src_qianfan.wechat_mini_program_log	| orig_info里的event_id	| int | | 每日 1点 数分钟  |
| src_qianfan	| src_qianfan.wechat_mini_program_log	| distinct_id	| string | | 每日 3点 数分钟  |
| src_qianfan	| src_qianfan.wechat_mini_program_log	| orig_info里的event_time	| string | | 每日 3点 数分钟  |
| src_qianfan	| src_qianfan.wechat_mini_program_log	| coupon_id	| int | | 每日 3点 数分钟  |




主表是 src_qf_prod_coupon.coupon 
-----------

| src_mall.product  | src_qf_prod_coupon.coupon |
|-------|:---:|
| detail里的id | c_no |

| app_compass.baseinfo_goods  | src_qf_prod_coupon.coupon |
|-------|:---:|
| coupon_id | c_no |

| src_qf_prod_coupon.coupon_stock  | src_qf_prod_coupon.coupon |
|-------|:---:|
| c_no | c_no |

| src_qf_prod_coupon.coupon_store_rule  | src_qf_prod_coupon.coupon |
|-------|:---:|
| c_no | c_no |


主表是 src_qianfan.wechat_mini_program_log
-----------
| src_qf_prod_coupon.coupon   | src_qianfan.wechat_mini_program_log |
|-------|:---:|
| c_no | coupon_id |


| src_qf_prod_coupon.coupon_store_rule   | src_qianfan.wechat_mini_program_log |
|-------|:---:|
| c_no   | coupon_id |













