########################################### EJERCICIO 2. 1  ###########################################

SELECT country, `status`, count(`status`) as "total operaciones", ROUND(avg(amount), 2) as "importe promedio"
FROM operaciones_ucm.orders
WHERE created_at > 2015-07-01
AND country IN ("Francia", "Portugal", "España")
AND amount BETWEEN 100 AND 1500
GROUP BY country, status
ORDER BY country, avg(amount) DESC ;

########################################### EJERCICIO 2. 2  ###########################################

	SELECT country, count(status) AS "numero de operaciones", max(amount) AS "transacción maxima",
		min(amount) AS "transacción mínima"
	FROM operaciones_ucm.orders
	WHERE status <> "DELINQUENT" AND amount > 100
	GROUP BY country 
	ORDER BY count(status) DESC
	LIMIT 3;
    

########################################### 3.1 ###########################################

SELECT country, merchants.name, merchants.merchant_id, count(orders.order_id) as "total_operaciones", ROUND(avg(orders.amount),2) AS "venta_promedio", 
		SUM(r.conteo_devoluciones) as "total_devoluciones",
	(CASE
		WHEN SUM(r.conteo_devoluciones) != 0 THEN "SI" ELSE "NO" END) AS "acepta_devoluciones"
FROM operaciones_ucm.orders
	INNER JOIN operaciones_ucm.merchants 
		ON operaciones_ucm.orders.merchant_id = operaciones_ucm.merchants.merchant_id
	LEFT JOIN (SELECT refunds.order_id, count(refunds.order_id ) as "conteo_devoluciones", sum(amount) as "suma_devoluciones"
					FROM operaciones_ucm.refunds
					GROUP BY order_id) AS r
		ON orders.order_id = r.order_id

GROUP BY merchants.name, merchants.merchant_id, country
HAVING count(orders.order_id) > 10 AND country IN ("Marruecos","Italia", "España", "Portugal")
ORDER BY count(orders.order_id) ASC;



########################################### 3.2 #############################################


CREATE VIEW operaciones_ucm.orders_view AS
SELECT o.order_id, o.created_at, o.status, o.amount, o.merchant_id, o.country, m.name , r.conteo_devoluciones, r.suma_devoluciones
FROM operaciones_ucm.orders as o
	LEFT JOIN (SELECT refunds.order_id, count(refunds.order_id ) as "conteo_devoluciones", sum(amount) as "suma_devoluciones"
					FROM operaciones_ucm.refunds
					GROUP BY order_id) AS r
		ON o.order_id = r.order_id
	INNER JOIN operaciones_ucm.merchants as m
		ON o.merchant_id = m.merchant_id;


############################################# EJERCICIO 4 #############################################

SELECT DISTINCT country, 
	ROUND(SUM(amount) OVER(PARTITION BY country), 2) as `suma_por_pais`,
	ROUND(AVG(amount) OVER(PARTITION BY country), 2)  as `prestamo_promedio_pais`,
	ROUND(AVG(amount) OVER(), 2)  as `prestamo_promedio_general`,
	(CASE 
	WHEN AVG(amount) OVER(PARTITION BY country) > AVG(amount) OVER() THEN "ENCIMA"
    ELSE "DEBAJO" END) AS `comportamiento_de_prestamos` 
FROM operaciones_ucm.orders
ORDER BY `suma_por_pais` DESC;



SELECT  distinct country, 
		count(order_id) OVER (partition by country) as `recuento_de_operaciones`,
		ROUND(sum(amount) OVER(partition by country), 2) as `suma_total_pais`,
        CONCAT(ROUND(((sum(amount) OVER(partition by country)/sum(amount) OVER())*100), 2), "%") AS `Porcentaje_prestamo`
FROM operaciones_ucm.orders
ORDER BY `suma_total_pais` DESC;