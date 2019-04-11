CREATE TABLE final_shop(
  sid varchar(255),
  name varchar(255),
  image_path varchar(255), 
  address varchar(255), 
  float_delivery_fee float,
  order_lead_time float,
  distance float,
  float_minimum_order_amount float,
  rating float, 
  recent_order_num INT,
  rating_count float,
  flavors varchar(255)
);
insert into final_shop VALUES('1','衢州土菜馆','emm','杭州市余杭区常二路永福村1号19幢101室', 2.7, 22, 1094, 20, 4.6 ,723, 256, '川湘菜');

CREATE TABLE final_food(
  fid varchar(255),
  shop_id varchar(255),
  name varchar(255),
  description varchar(255), 
  image_path varchar(255), 
  month_sales float,
  satisfy_rate float,
  price float
);
insert into final_food VALUES('1','1','emm','emm', 'emm', 22, 1094, 20);
