#https://es.investing.com/equities/pampa-energia-historical-data
#http://www.mdpbursatil.com.ar/especie.aspx?especie=PAMP
#claiun_tmp_evolucion_pmp

#hacer scraping con investing
#hacer en python todo el calculo de metricas y desp en sql o con mining o Analaisis correspondencia buscar patrones demas de la query

#tutorial time series
#https://www.analyticsvidhya.com/blog/2015/12/complete-tutorial-time-series-modeling/



IF OBJECT_ID('tempdb..#tmp_pmp') IS NOT NULL DROP TABLE #tmp_pmp;
select 
fecha,
ultimo,
lag(ultimo,1) over (order by fecha) as cierre_lag1,
lag(ultimo,2) over (order by fecha) as cierre_lag2,
lag(ultimo,3) over (order by fecha) as cierre_lag3,
lag(ultimo,4) over (order by fecha) as cierre_lag4,
lag(ultimo,5) over (order by fecha) as cierre_lag5,
lead(ultimo,1) over (order by fecha) as cierre_lead1,
lead(ultimo,2) over (order by fecha) as cierre_lead2,
lead(ultimo,3) over (order by fecha) as cierre_lead3,
lead(ultimo,4) over (order by fecha) as cierre_lead4,
lead(ultimo,5) over (order by fecha) as cierre_lead5,
(avg(ultimo) OVER(ORDER BY fecha ROWS BETWEEN 1 FOLLOWING AND 1 FOLLOWING)*1.0) siguientes_1,
(avg(ultimo) OVER(ORDER BY fecha ROWS BETWEEN 30 PRECEDING  AND 1 PRECEDING )*1.0) anteriores_30,
(avg(ultimo) OVER(ORDER BY fecha ROWS BETWEEN 15 PRECEDING  AND 1 PRECEDING )*1.0) anteriores_15,
(avg(ultimo) OVER(ORDER BY fecha ROWS BETWEEN 10 PRECEDING  AND 1 PRECEDING )*1.0) anteriores_10,
(avg(ultimo) OVER(ORDER BY fecha ROWS BETWEEN 5 PRECEDING  AND 1 PRECEDING )*1.0) anteriores_5
into #tmp_pmp
from
claiun_tmp_evolucion_pmp c
where fecha > 20160000
order by fecha asc
;




IF OBJECT_ID('tempdb..#tmp_pmp_2') IS NOT NULL DROP TABLE #tmp_pmp_2;
select
fecha,
ultimo,
ultimo/anteriores_5 dif_15prom_anterior,
case when cierre_lag1 >= ultimo and cierre_lag2 > cierre_lag1 and cierre_lag3 > cierre_lag2 then 1 else 0 end tendencia_negativa,
cierre_lead1/ultimo dif_lead1,
cierre_lead2/ultimo dif_lead2,
cierre_lead3/ultimo dif_lead3,
cierre_lead4/ultimo dif_lead4,
cierre_lead5/ultimo dif_lead5
into #tmp_pmp_2
from
#tmp_pmp
--order by dif_15prom desc




IF OBJECT_ID('tempdb..#tmp_pmp_3') IS NOT NULL DROP TABLE #tmp_pmp_3;
select
fecha,
case when dif_15prom_anterior < 0.97 and tendencia_negativa = 1 then 1 else 0 end dif_15prom_anterior,
--case when tendencia_negativa = 1 then 1 else 0 end dif_15prom_anterior,
case when dif_lead1 > 1.02 or dif_lead2 > 1.02  or dif_lead3 > 1.02  or dif_lead4 > 1.02 or dif_lead5 > 1.02  then 1 else 0 end dif_siguiente
--case when dif_15prom_anterior < 0.95 and dif_siguiente > 1 then 1 else 0 end metrica
into #tmp_pmp_3
from
#tmp_pmp_2



select
dif_siguiente,
count(*)
from
#tmp_pmp_3
where
dif_15prom_anterior = 1
group by dif_siguiente


---------------- CONTROL 

select
*
from
#tmp_pmp_3
where
dif_15prom_anterior = 1
order by fecha desc

select
*
from
#tmp_pmp
where fecha = '20170717'

select
*
from
#tmp_pmp_2
where fecha = '20170717'