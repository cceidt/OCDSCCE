--  Query for budget package
SELECT
-- budget - source
  'http://www.minhacienda.gov.co/HomeMinhacienda/siif' AS source,
-- budget - id
  RESPALDO.NUMERO_RESPALDO AS id,
-- budget - description
  RESPALDO.TIPO_RESPALDO AS description,
-- budget - amount
  RESPALDO.CUANTIA_RESPALDO AS amount,
-- Numero de constancia
  RESPALDO.ID_PROCESO AS num_constancia
FROM T_PTC_RESPALDO RESPALDO
LEFT JOIN T_PTC_PROCESOS PROCESO
  ON RESPALDO.ID_PROCESO = PROCESO.NUM_CONSTANCIA
LEFT JOIN TB_USUARIOLDAP USRLDAP
  ON PROCESO.USUARIO = USRLDAP.USUARIO
WHERE 
  TRUNC(PROCESO.fecha_cargue) BETWEEN TO_DATE('01/01/2015','DD/MM/YYYY') AND TO_DATE('19/08/2015','DD/MM/YYYY')
AND USRLDAP.IDENTIDAD <> '199999999'
;