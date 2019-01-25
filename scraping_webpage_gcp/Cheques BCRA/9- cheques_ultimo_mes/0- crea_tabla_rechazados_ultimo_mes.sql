
IF OBJECT_ID('tempdb..#formato_cheques') IS NOT NULL DROP TABLE #formato_cheques;
select
chq.cuil_cuit_cdi,
chq.nro_cheque,
chq.fecha_rechazo,
Convert(varchar(30),concat(SUBSTRING(CONVERT(varchar(10), chq.fecha_rechazo), 7, 2),'/',SUBSTRING(CONVERT(varchar(10), chq.fecha_rechazo), 5, 2),'/',SUBSTRING(CONVERT(varchar(10), chq.fecha_rechazo), 1, 4)),102) fecha_rechazo_formato,
Cast(Convert(varchar(30),concat(SUBSTRING(CONVERT(varchar(10), chq.fecha_rechazo), 5, 2),'/',SUBSTRING(CONVERT(varchar(10), chq.fecha_rechazo), 7, 2),'/',SUBSTRING(CONVERT(varchar(10), chq.fecha_rechazo), 1, 4)),102) as datetime) fecha_rechazo_datetime,
chq.monto,
chq.fecha_pago,
case when chq.fecha_pago is not null then
Convert(varchar(30),concat(SUBSTRING(CONVERT(varchar(10), chq.fecha_pago), 7, 2),'/',SUBSTRING(CONVERT(varchar(10), chq.fecha_pago), 5, 2),'/',SUBSTRING(CONVERT(varchar(10), chq.fecha_pago), 1, 4)),102)  
end fecha_pago_formato,
case when chq.fecha_pago is not null then
Cast(Convert(varchar(30),concat(SUBSTRING(CONVERT(varchar(10), chq.fecha_pago), 5, 2),'/',SUBSTRING(CONVERT(varchar(10), chq.fecha_pago), 7, 2),'/',SUBSTRING(CONVERT(varchar(10), chq.fecha_pago), 1, 4)),102) as datetime)
end fecha_pago_datetime,
causal,
pago_multa,
case when pago_multa like '%[0-9]%' then 
Cast(Convert(varchar(30),concat(SUBSTRING(CONVERT(varchar(10), chq.pago_multa), 4, 2),'/',SUBSTRING(CONVERT(varchar(10), chq.pago_multa), 1, 2),'/',SUBSTRING(CONVERT(varchar(10), chq.pago_multa), 7, 4))) as datetime) 
end pago_multa_datetime,
revision,
judicial,
cuit_relacionado
into #formato_cheques
from
claiun_bcra_cheques_bajada chq
;




IF OBJECT_ID('tempdb..#formato_cheques_fechas') IS NOT NULL DROP TABLE #formato_cheques_fechas;
select
cuil_cuit_cdi,
nro_cheque,
fecha_rechazo_formato fecha_rechazo,
fecha_rechazo_datetime,
monto,
fecha_pago_datetime,
case when fecha_pago_formato is null then '' else fecha_pago_formato end fecha_pago,
causal,
pago_multa,
pago_multa_datetime,
revision,
judicial,
cuit_relacionado persona_juridica_relacionada,
DATEDIFF(DAY, fecha_rechazo_datetime,fecha_pago_datetime) dias_entre_rechazo_pago_cheque,
DATEDIFF(DAY, fecha_rechazo_datetime,pago_multa_datetime) dias_entre_rechazo_pago_multa,
case when DATEDIFF(DAY, fecha_rechazo_datetime,pago_multa_datetime)  > 30 or (pago_multa_datetime is null and DATEDIFF(DAY, fecha_rechazo_datetime,cast('2017/06/01' as datetime)) > 30) then 1 else 0 end flag_in,
--DATEDIFF(DAY, fecha_rechazo_datetime,SYSDATETIME()) dif_rechazo_fechahoy
DATEDIFF(DAY, fecha_rechazo_datetime,cast('2017/02/01' as datetime)) dif_rechazo_mes_particular
into #formato_cheques_fechas
from 
#formato_cheques
;



IF OBJECT_ID('dbo.claiun_cheques_rechazados_ultimo_mes') IS NOT NULL DROP TABLE claiun_cheques_rechazados_ultimo_mes;
--
-- rechazado 6 meses
--
select
cuil_cuit_cdi,
sum(monto) monto_total_1m,
sum(1) cantidad_total_1m,
--cheque impago
sum(case when dias_entre_rechazo_pago_cheque is null then monto else 0 end ) monto_cheque_impago_1m,
sum(case when dias_entre_rechazo_pago_cheque is null then 1 else 0 end) cantidad_cheque_impago_1m,
--multa impaga
sum(case when dias_entre_rechazo_pago_multa is null then monto else 0 end) monto_multa_impago_1m,
sum(case when dias_entre_rechazo_pago_multa is null then 1 else 0 end) cantidad_multa_impago_1m,
--cheque y multa impaga
sum(case when dias_entre_rechazo_pago_cheque is null and dias_entre_rechazo_pago_multa is null then monto else 0 end) monto_multa_y_cheque_impago_1m,
sum(case when dias_entre_rechazo_pago_cheque is null and dias_entre_rechazo_pago_multa is null then 1 else 0 end) cantidad_multa_y_cheque_impago_1m,
--tiempos
max(case when dias_entre_rechazo_pago_cheque is null  then dif_rechazo_mes_particular else 0 end) maximo_tiempo_cheque_impago_1m,
max(case when dias_entre_rechazo_pago_multa is null then dif_rechazo_mes_particular else 0 end) maximo_tiempo_multa_impago_1m,
max(case when dias_entre_rechazo_pago_cheque is null and dias_entre_rechazo_pago_multa is null then dif_rechazo_mes_particular else 0 end) maximo_tiempo_multa_y_cheque_impago_1m
into claiun_cheques_rechazados_ultimo_mes
from
#formato_cheques_fechas
where 1=1
and lower(causal) like 'sin fondos'
and fecha_rechazo_datetime >= DATEADD(month, -1, GETDATE())
and fecha_rechazo_datetime < GETDATE()
and (fecha_pago_datetime <= GETDATE() or fecha_pago_datetime is null)
and (pago_multa_datetime <= GETDATE() or pago_multa_datetime is null)
group by cuil_cuit_cdi
;
