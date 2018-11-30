#### 术语表

- Item：物料，即被推荐物品，推荐系统使用物料属性信息，用户标签及行为一起，生成推荐结果。物料分pool管理，一个物料可以属于一个或多个pool，获取推荐结果时，可以在指定pool中计算推荐结果。 
- Pool：物料池，被推荐物品的集合，用于管理只需要特定场景下出现的物料集合。如果物料只希望在某个场景下出现，可以在物料上报时指定pool，拉取推荐结果时，指定对应的pool即可。一个物料可以属于一个或多个pool。  
- TraceId： 用户行为ID，串联用户行为的会话ID，用户行为包括曝光、点击、效果转换、点赞等，用户行为按时序依次产生，需要业务传递traceId，标识点击、效果转换的动作是哪一次的曝光、点击产生的。 

#### Item上报

##### 接口描述

上报物料信息，包含物料（item）id、有效期、标签、标题、vendor描述、物料池（归属万达广场）等信息，相同item_id可以重复上传，字段信息以最后一次上传为准，上报方式：http-post-json，服务url：`待定`

##### 字段说明

输入参数各字段含义如下所示：dwd.coupon_product;dwd.couponnew_product


| 参数名称         | 类型      | 必传   | 备注                                     |
| ------------ | ------- | ---- | -------------------------------------- |
| request_id   | string  | Y    | 请求标识，格式：毫秒级时间戳_随机数，随机数建议三位以上           |
| data_type    | integer | Y    | 协议类型：1-item，2-action，物料上报取1            |
| item_id      | string  | Y    | 物料id，物料唯一标识。corpon_number；cno          |
| pool_id      | string  | Y    | 优惠券适合的广场id                             |
| publish      | integer | N    | 1 - 上架（默认）， 0 - 下架                     |
| item_desc    | string  | N    | 优惠券描述信息，如标题或券的描述                       |
| vendor_desc  | string  | N    | 商家的描述信息（增加商家-品牌/门店ID）                  |
| tags         | string  | N    | 标签信息，如品牌、业态等                           |
| item_time    | string  | Y    | item上线时间                               |
| expire_time  | string  | Y    | item过期时间，用于过期券的过滤                      |
| small_type   | string  | Y    | 优惠券类型，如代金券、兑换券、停车券等                    |
| price_real   | float   | Y    | 优惠券售价 （增加优惠类型）                         |
| price_expect | float   | Y    | 优惠券价值 有可能 投放过滤：投放时间（静态）和库存（去库存+锁库存剩下的） |

#### Action 上报

##### 接口描述

上报某一用户在特定场景下的行为，用户的行为包括曝光、点击、转换、点赞等， 上报用户行为时，必须指定用户行为的会话id。 开发者发送http-post-json获取服务结果，服务URL：`待定`

##### 字段说明

输入参数各字段含义如下所示：

| 参数名称                   | 类型      | 必传   | 备注                                       |
| ---------------------- | ------- | ---- | ---------------------------------------- |
| request_id             | string  | Y    | 请求标识，格式：毫秒级时间戳_随机数，随机数建议三位以上             |
| data_type              | integer | Y    | 协议类型：1-item，2-action，物料上报取1              |
| item_id                | string  | Y    | 物料id，物料唯一标识                              |
| uid                    | string  | Y    | imei/idfa，手机号、openID                     |
| uid_type               | integer | N    | 0-imei/idfa，2- 手机号，3-openID              |
| scene_id               | string  | Y    | 场景ID，sc_01：首页，sc_02：详情页，sc03：支付页         |
| action_type            | string  | Y    | 用户行为：1-曝光 2-点击 3-转换（购买） 4-点赞（核销） 5-评论（退款/购买但没核销） |
| session_id（改成tracr_id） | string  | Y    | **向推荐引擎请求列表时由推荐引擎返回的session_id**，用于A/Btesting分流和效果测试 |
| action_id              | string  | Y    | 行为发生时间戳，秒级时间戳(需要确定是请求前还是请求后曝光，event_id去确定-赵淑云) |
| pool_id                | string  | Y    | 优惠券适合的广场id（同item上报信息）                    |

#### 推荐请求服务（实时）

**接口描述**

获取给定场景下， 给特定用户的推荐结果。 获取推荐时， 需要指定场景， 用户信息及需要使用的物料池，推荐系统返回用户在当前场景下，对各个物品喜好的权重。 开发者发送http-post-json获取服务结果，服务URL：`待定`

| 参数名称        | 类型      | 必传   | 备注                                       |
| ----------- | ------- | ---- | ---------------------------------------- |
| request_id  | string  | Y    | 请求标识，格式：毫秒级时间戳_随机数，随机数建议三位以上             |
| uid         | string  | Y    | imei/idfa，手机号、openID                     |
| uid_type    | integer | N    | 0-imei/idfa，2- 手机号，3-openID              |
| scene_id    | string  | Y    | 场景ID，sc_01：首页，sc_02：详情页，sc03：支付页 ，需要跟行为上报时的ID一致 |
| request_num | Integer | N    | 返回推荐列表数量                                 |
| pool_id     | string  | Y    | 优惠券适合的广场id（同item上报信息）                    |
| cid         | string  | Y    | 详情页或支付页对应物料的id                           |
| ulocation   | string  | N    | 用户地理位置                                   |

##### 返回值

| 返回值名称      | 类型     | 备注                               |
| ---------- | ------ | -------------------------------- |
| session_id | string | 该id用于追踪算法的效果，开发者需要在用户行为上报时将该id返回 |
| scene_id   | string | 场景id                             |
| item_id    | string | 推荐物料的id                          |
| Item_wgt   | float  | 推荐物料的排序权重                        |

#### A/B Testing 请求接口（非必须）

**接口描述**

提供分流和转化两个接口，分流接口用于创建实验和用户分流到相关实验类别，转化接口用于统计实验效果及优选实验目标确定。 开发者发送http-post-json获取服务结果，服务URL：`待定`

- **分流**

| 参数名称             | 类型     | 必传   | 备注                                       |
| ---------------- | ------ | ---- | ---------------------------------------- |
| exp_id           | string | Y    | 实验名称/ID                                  |
| alternatives     | string | Y    | 实验所包含的项目，如：["红色按钮","蓝色按钮"]               |
| session_id       | string | N    | 请求时对应的标识                                 |
| user_agent       | string | N    | 用于识别是否为非法请求                              |
| ip_address       | string | N    | 用于识别是否为非法请求                              |
| force            | string | N    | 可以指定只向某个实验项目分配流量                         |
| traffic_fraction | float  | N    | 可以对实验项目进行流量比例设定，比如 `traffic_fraction=0.10` 即分配10%的流量到该实验 |

##### 返回值

| 返回值名称       | 类型     | 备注                           |
| ----------- | ------ | ---------------------------- |
| status      | string | 请求状态，‘OK’、‘error’            |
| alternative | string | 本次请求分配的实验项目                  |
| exp_id      | string | 实验名称/ID                      |
| session_id  | float  | 用于记录转化需要的标识，可以由请求要户指定或系统自动分配 |

- **转化**

| 参数名称       | 类型     | 必传   | 备注                                  |
| ---------- | ------ | ---- | ----------------------------------- |
| exp_id     | string | Y    | 实验名称/ID                             |
| session_id | string | Y    | 分流时用户指定或系统指定的id标识                   |
| kpi        | string | N    | 比如可以将同一个实验的转化细分为点击、浏览、购买等不同的kpi进行统计 |

##### 返回值

| 返回值名称       | 类型     | 备注                |
| ----------- | ------ | ----------------- |
| status      | string | 请求状态，‘OK’、‘error’ |
| alternative | string | 本次请求分配的实验项目       |
| exp_id      | string | 实验名称/ID           |
