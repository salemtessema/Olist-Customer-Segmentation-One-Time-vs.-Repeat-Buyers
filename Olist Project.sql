WITH item_totals AS(
SELECT order_id, SUM(price) AS product_value, SUM(freight_value) AS shipping_value
FROM olist_order_items_dataset
GROUP BY order_id
),

payment_totals AS(
SELECT order_id, SUM(payment_value) AS payment_value
FROM olist_order_payments_dataset
GROUP BY order_id
),

review_totals AS(
SELECT order_id, AVG(review_score) AS avg_review_score
FROM olist_order_reviews_dataset
GROUP BY order_id
)

   SELECT 
    c.customer_unique_id,
    COUNT(DISTINCT o.order_id) AS total_orders,
    MIN(o.order_purchase_timestamp) AS first_purchase,
    MAX(o.order_purchase_timestamp) AS last_purchase,
    SUM(it.product_value) AS total_product_value,
    SUM(it.shipping_value) AS total_shipping_value,
    SUM(pt.payment_value) AS total_payment_value,
    AVG(r.avg_review_score) AS average_review_score
FROM
    olist_customers_dataset c
		JOIN
    olist_orders_dataset o ON c.customer_id = o.customer_id
        LEFT JOIN
    item_totals it ON o.order_id = it.order_id
        LEFT JOIN
    payment_totals pt ON o.order_id = pt.order_id
        LEFT JOIN
    review_totals r ON o.order_id = r.order_id
GROUP BY c.customer_unique_id
ORDER BY total_orders DESC;

