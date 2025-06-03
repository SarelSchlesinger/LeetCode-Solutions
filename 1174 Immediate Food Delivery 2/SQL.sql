DECLARE @customers int = (SELECT COUNT(DISTINCT customer_id) FROM Delivery);

SELECT ROUND(100.0 * count(*) / @customers, 2) AS 'immediate_percentage'
FROM Delivery d1 JOIN (SELECT customer_id, MIN(order_date) AS 'first_order'
                       FROM Delivery
                       GROUP BY customer_id) d2
ON d1.customer_pref_delivery_date = d2.first_order
AND d1.customer_id = d2.customer_id