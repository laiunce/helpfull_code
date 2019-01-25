
select distinct
CUIT_CUIL_Prospecto
into #tmp_distinct_prospectos
from
claiun_tmp_prospectos_melicard mc
;

select 
mc.CUIT_CUIL_Prospecto,
max(pro.Ingreso_Inferido) Ingreso_inferido,
sum(case when mes = 20170816 and fecha_pago is null then monto else 0 end) monto_20170816,
sum(case when mes = 20170815 and fecha_pago is null then monto else 0 end) monto_20170815,
sum(case when mes = 20170814 and fecha_pago is null then monto else 0 end) monto_20170814,
sum(case when mes = 20170811 and fecha_pago is null then monto else 0 end) monto_20170811,
sum(case when mes = 20170810 and fecha_pago is null then monto else 0 end) monto_20170810,
sum(case when mes = 20170809 and fecha_pago is null then monto else 0 end) monto_20170809,
sum(case when mes = 20170808 and fecha_pago is null then monto else 0 end) monto_20170808,
sum(case when mes = 20170807 and fecha_pago is null then monto else 0 end) monto_20170807,
sum(case when mes = 20170804 and fecha_pago is null then monto else 0 end) monto_20170804,
sum(case when mes = 20170803 and fecha_pago is null then monto else 0 end) monto_20170803,
sum(case when mes = 20170802 and fecha_pago is null then monto else 0 end) monto_20170802,
sum(case when mes = 20170801 and fecha_pago is null then monto else 0 end) monto_20170801,
sum(case when mes = 20170731 and fecha_pago is null then monto else 0 end) monto_20170731,
sum(case when mes = 20170728 and fecha_pago is null then monto else 0 end) monto_20170728,
sum(case when mes = 20170727 and fecha_pago is null then monto else 0 end) monto_20170727,
sum(case when mes = 20170726 and fecha_pago is null then monto else 0 end) monto_20170726,
sum(case when mes = 20170725 and fecha_pago is null then monto else 0 end) monto_20170725,
sum(case when mes = 20170724 and fecha_pago is null then monto else 0 end) monto_20170724,
sum(case when mes = 20170721 and fecha_pago is null then monto else 0 end) monto_20170721,
sum(case when mes = 20170720 and fecha_pago is null then monto else 0 end) monto_20170720,
sum(case when mes = 20170719 and fecha_pago is null then monto else 0 end) monto_20170719,
sum(case when mes = 20170718 and fecha_pago is null then monto else 0 end) monto_20170718,
sum(case when mes = 20170717 and fecha_pago is null then monto else 0 end) monto_20170717,
sum(case when mes = 20170714 and fecha_pago is null then monto else 0 end) monto_20170714,
sum(case when mes = 20170713 and fecha_pago is null then monto else 0 end) monto_20170713,
sum(case when mes = 20170712 and fecha_pago is null then monto else 0 end) monto_20170712,
sum(case when mes = 20170711 and fecha_pago is null then monto else 0 end) monto_20170711,
sum(case when mes = 20170710 and fecha_pago is null then monto else 0 end) monto_20170710,
sum(case when mes = 20170707 and fecha_pago is null then monto else 0 end) monto_20170707,
sum(case when mes = 20170706 and fecha_pago is null then monto else 0 end) monto_20170706,
sum(case when mes = 20170705 and fecha_pago is null then monto else 0 end) monto_20170705,
sum(case when mes = 20170704 and fecha_pago is null then monto else 0 end) monto_20170704,
sum(case when mes = 20170703 and fecha_pago is null then monto else 0 end) monto_20170703,
sum(case when mes = 20170630 and fecha_pago is null then monto else 0 end) monto_20170630,
sum(case when mes = 20170629 and fecha_pago is null then monto else 0 end) monto_20170629,
sum(case when mes = 20170628 and fecha_pago is null then monto else 0 end) monto_20170628,
sum(case when mes = 20170627 and fecha_pago is null then monto else 0 end) monto_20170627,
sum(case when mes = 20170626 and fecha_pago is null then monto else 0 end) monto_20170626,
sum(case when mes = 20170623 and fecha_pago is null then monto else 0 end) monto_20170623,
sum(case when mes = 20170622 and fecha_pago is null then monto else 0 end) monto_20170622,
sum(case when mes = 20170621 and fecha_pago is null then monto else 0 end) monto_20170621,
sum(case when mes = 20170619 and fecha_pago is null then monto else 0 end) monto_20170619,
sum(case when mes = 20170616 and fecha_pago is null then monto else 0 end) monto_20170616,
sum(case when mes = 20170615 and fecha_pago is null then monto else 0 end) monto_20170615
from
claiun_bcra_cheques_al_format chq