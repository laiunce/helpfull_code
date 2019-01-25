-- crea registros unicos actualizando estados de pago con la novedad
IF OBJECT_ID('dbo.claiun_bcra_cheques_bajada_tmp') IS NOT NULL DROP TABLE claiun_bcra_cheques_bajada_tmp;
select
cuil_cuit_cdi,
nro_cheque,
fecha_rechazo,
monto,
causal,
revision,
judicial,
cuit_relacionado,
max(fecha_pago) fecha_pago,
min(pago_multa) pago_multa
into claiun_bcra_cheques_bajada_tmp
from
claiun_bcra_cheques_bajada_201601_2017
where 1=1
and lower(causal)='sin fondos'
group by
cuil_cuit_cdi,
nro_cheque,
fecha_rechazo,
monto,
causal,
revision,
judicial,
cuit_relacionado
;


IF OBJECT_ID('dbo.claiun_bcra_cheques_bajada') IS NOT NULL DROP TABLE claiun_bcra_cheques_bajada;
select
*
into claiun_bcra_cheques_bajada
from
claiun_bcra_cheques_bajada_tmp
;


IF OBJECT_ID('dbo.claiun_bcra_cheques_bajada_tmp') IS NOT NULL DROP TABLE claiun_bcra_cheques_bajada_tmp;
