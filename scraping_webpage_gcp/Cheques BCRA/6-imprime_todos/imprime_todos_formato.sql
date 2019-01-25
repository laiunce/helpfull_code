
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
cuit_relacionado,
anio_mes_dia
into #formato_cheques
from
claiun_bcra_cheques_bajada chq
;


IF OBJECT_ID('tempdb..#formato_cheques_fechas') IS NOT NULL DROP TABLE #formato_cheques_fechas;
select
anio_mes_dia,
cuil_cuit_cdi,
nro_cheque,
fecha_rechazo_formato fecha_rechazo,
monto,
case when fecha_pago_formato is null then '' else fecha_pago_formato end fecha_pago,
causal,
pago_multa,
revision,
judicial,
cuit_relacionado persona_juridica_relacionada,
DATEDIFF(DAY, fecha_rechazo_datetime,fecha_pago_datetime) dias_entre_rechazo_pago_cheque,
DATEDIFF(DAY, fecha_rechazo_datetime,pago_multa_datetime) dias_entre_rechazo_pago_multa
into #formato_cheques_fechas
from 
#formato_cheques
;

IF OBJECT_ID('claiun_tmp_formato_nosis_cheques_fechas') IS NOT NULL DROP TABLE claiun_tmp_formato_nosis_cheques_fechas;
select
cuil_cuit_cdi,
nro_cheque,
fecha_rechazo,
round(monto,0) monto,
fecha_pago,
causal,
pago_multa,
revision,
judicial,
persona_juridica_relacionada,
case when dias_entre_rechazo_pago_cheque is null then '' else Convert(varchar(30),dias_entre_rechazo_pago_cheque) end dias_entre_rechazo_pago_cheque,
case when dias_entre_rechazo_pago_multa is null then '' else Convert(varchar(30),dias_entre_rechazo_pago_multa) end dias_entre_rechazo_pago_multa
into claiun_tmp_formato_nosis_cheques_fechas
from 
#formato_cheques_fechas
where anio_mes_dia = (select max(anio_mes_dia) from claiun_bcra_cheques_bajada)
order by cuil_cuit_cdi desc
;