delete
from
claiun_bcra_cheques_bajada_201601_2017
where anio_mes_dia in (select anio_mes_dia from claiun_tmp_intermedio_meses_borrar);
