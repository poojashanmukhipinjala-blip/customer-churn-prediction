use project;
show tables;

---checking for null values------------------------------------------------------------------------------------------

select *
from customers
where customer_id is NULL
OR customer_name is NULL
OR age is NULL
OR gender is NULL
OR city is NULL
OR signup_date is NULL;

select *
from customer_behavior
where customer_id is NULL
OR total_orders is NULL
OR total_spending is NULL
OR average_order_value is NULL
OR last_order_days is NULL
OR churn_flag is NULL;

select *
from delivery_partners
where partner_id is NULL
OR partner_name is NULL
OR vehicle_type is NULL
OR joining_date is NULL;


SELECT *
FROM orders
WHERE order_id IS NULL
OR customer_id IS NULL
OR restaurant_id IS NULL
OR partner_id IS NULL
OR order_time IS NULL
OR order_amount IS NULL
OR delivery_fee IS NULL
OR status IS NULL;

select *
from payments
where payment_id is NULL
 OR order_id is NULL
 OR payment_mode is NULL
 OR amount is NULL;
 
select *
from ratings
where rating_id is NULL
OR order_id is NULL
OR customer_rating is NULL
OR feedback is NULL;

select *
FROM restaurants
WHERE restaurant_id IS NUll
OR restaurant_name IS NULL
OR cuisine_type is NULL
OR city IS NULL
OR rating IS NULL;

----checking for duplicates------------------------------------------------------------------------------------------

select customer_id, count(*) as duplicate_count
from customer_behavior
group by customer_id
having count(*) > 1;

select customer_id, count(*) as duplicate_count
from customers
group by customer_id
having count(*) > 1;

select partner_id, count(*) as duplicate_count
from delivery_partners
group by partner_id
having count(*) > 1;

select order_id, count(*) as duplicate_count
from orders
group by order_id
having count(*) > 1;

select payment_id, count(*) as duplicate_count
from payments
group by payment_id
having count(*) > 1;

select rating_id, count(*) as duplicate_count
from ratings
group by rating_id
having count(*) > 1;

select restaurant_id, count(*) as duplicate_count
from restaurants
group by restaurant_id
having count(*) > 1;

select order_time, delivered_time
from orders
limit 10;

---modifing varchar to DATETIME--------------------------------------------------------------------------------------

DESC orders;
alter table orders
modify column order_time DATETIME;

SELECT delivered_time
FROM orders
WHERE STR_TO_DATE(delivered_time, '%Y-%m-%d %H:%i:%s') IS NULL
AND delivered_time IS NOT NULL;
  
SELECT delivered_time
FROM orders
WHERE STR_TO_DATE(delivered_time, '%Y-%m-%d %H:%i:%s') IS NULL
AND delivered_time IS NOT NULL
LIMIT 50;

select count(*)
from orders
where delivered_time is null;


ALTER TABLE orders
MODIFY COLUMN delivered_time DATETIME;
  
  SELECT order_id,
       LENGTH(delivered_time) AS len,
       HEX(delivered_time) AS hex_value
FROM orders
WHERE delivered_time = ''
   OR TRIM(delivered_time) = ''
LIMIT 20;

UPDATE orders
SET delivered_time = NULL
WHERE delivered_time = ''
   OR TRIM(delivered_time) = '';
   
   SELECT COUNT(*)
FROM orders
WHERE delivered_time = ''
   OR TRIM(delivered_time) = '';
   
   ALTER TABLE orders
MODIFY COLUMN delivered_time DATETIME NULL;

---Business Rule Validation------------------------------------------------------------------------------------------
  select * from orders
  where order_amount < 0;
  
select * from orders
where delivery_fee < 0;

select distinct status
from orders;

select * from restaurants
where rating < 1 or rating > 5;

select * from ratings
where customer_rating < 1 or customer_rating > 5;

select  distinct payment_mode from payments; 

select distinct vehicle_type
from delivery_partners;

select distinct churn_flag
from customer_behavior;

select distinct gender
from customers;

--Referential Integrity Check -to verify that every foreign key references an existing record.----------------------

SELECT COUNT(*) AS invalid_customer_ids
FROM orders o
LEFT JOIN restaurants r
ON o.restaurant_id = r.restaurant_id
WHERE r.restaurant_id IS NULL;

SELECT COUNT(*) AS invalid_customer_ids
FROM orders o
LEFT JOIN customers c
ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

SELECT COUNT(*) AS invalid_customer_ids
FROM ratings r
LEFT JOIN orders o
ON r.order_id = o.order_id
WHERE o.order_id IS NULL;









  
  





 
