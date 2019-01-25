
IF OBJECT_ID('tempdb..#formato_cheques') IS NOT NULL DROP TABLE #formato_cheques;
select
chq.cuil,
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
persona_juridica_relacionada,
mes
into #formato_cheques
from
claiun_bcra_cheques_al_format chq
;


IF OBJECT_ID('tempdb..#formato_cheques_fechas') IS NOT NULL DROP TABLE #formato_cheques_fechas;
select
mes,
cuil,
nro_cheque,
fecha_rechazo_formato fecha_rechazo,
monto,
case when fecha_pago_formato is null then '' else fecha_pago_formato end fecha_pago,
causal,
pago_multa,
persona_juridica_relacionada,
DATEDIFF(DAY, fecha_rechazo_datetime,fecha_pago_datetime) dias_entre_rechazo_pago_cheque,
DATEDIFF(DAY, fecha_rechazo_datetime,pago_multa_datetime) dias_entre_rechazo_pago_multa
into #formato_cheques_fechas
from 
#formato_cheques
;



drop table claiun_tmp_tabla_clientes_cheques_rechazados;
select
mes,
cuil,
nro_cheque,
fecha_rechazo,
monto,
fecha_pago,
causal,
pago_multa,
persona_juridica_relacionada,
dias_entre_rechazo_pago_cheque,
dias_entre_rechazo_pago_multa,
case when dias_entre_rechazo_pago_cheque is not null then 'Si' else 'No' end pago_cheque_flag,
case when dias_entre_rechazo_pago_multa is not null then 'Si' else 'No' end pago_multa_flag,
case when dias_entre_rechazo_pago_cheque is not null and dias_entre_rechazo_pago_multa is not null then 'Si' else 'No' end pago_cheque_y_multa_flag
into claiun_tmp_tabla_clientes_cheques_rechazados
from 
#formato_cheques_fechas fchq
;
