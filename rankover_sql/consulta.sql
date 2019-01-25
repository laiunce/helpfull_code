select 
*
from
claiun_prueba

--obtengo usuario y su gasto
select
usr,
sum(gasto) gasto_suma
into #tmp_gasto_por_usuario
from
claiun_prueba
group by 
usr

--obtengo usuario y share de gasto
select 
usr,
100*(1.1*gasto_suma/sum(gasto_suma) OVER ()) porc
into #temp_us_prc
from
#tmp_gasto_por_usuario
order by porc desc

--le asigno rowid en base al monto descendente
select 
usr,
porc,
ROW_NUMBER() over(order by porc desc) RowId
into #tmp_ordenado_share
from
#temp_us_prc

--hago suma acumulada
select
usr,
porc,
SUM(porc) OVER(ORDER BY RowId ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS acumulado
into #tmp_acumulados
from
#tmp_ordenado_share

--selecciono los que acumulan el 50% de compras
select 
*
from
#tmp_acumulados
where 
acumulado < 50


