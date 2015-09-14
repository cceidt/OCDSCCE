SELECT 
-- id
  ADJUDICACION.ID_ADJUDICACION AS id,
-- status
  CASE PROCESO.ESTADO_PROCESO
    WHEN '3' THEN 'active'
    WHEN '4' THEN 'active'
    WHEN '5' THEN 'active'
    WHEN '7' THEN 'unsuccessful'
    WHEN '8' THEN 'active'
    ELSE NULL
  END status,
-- date
  (  
    SELECT MAX(NOVEDAD.FECHA_NOVEDAD)
    FROM T_PTC_NOVEDADES NOVEDAD 
    WHERE 
    NOVEDAD.NUMERO_CONSTANCIA = ADJUDICACION.ID_PROCESO
    AND NOVEDAD.OID_TIPO_NOVEDAD = 3
    GROUP BY NOVEDAD.NUMERO_CONSTANCIA
  ) AS datea,
-- value - amount
  ADJUDICACION.VALOR_CONTRATO AS amount,
  CASE ADJUDICACION.ID_MONEDA_PAGO 
    WHEN '1' THEN 'COP'
    WHEN '2' THEN 'USD'
    WHEN '4' THEN 'EUR'
    WHEN '5' THEN 'GBP'
    WHEN '6' THEN 'AFN'
    WHEN '10' THEN 'VEF'
    WHEN '11' THEN 'BOB'
    WHEN '20' THEN 'CZK'
    ELSE NULL
  END currency,

-- suppliers
-- suppliers _ identifier - scheme
  TRIM(TIPODOC.DESCRIPCION) AS identifier_scheme,
-- suppliers _ identifier - id
  ADJUDICACION.NUMERO_DOC AS identifier_id,
-- suppliers _ identifier - legalName
  TRIM(ADJUDICACION.RAZON_SOCIAL) AS identifier_legalName,
-- suppliers - name
  TRIM(ADJUDICACION.RAZON_SOCIAL) AS name,
-- suppliers _ address - streetAddress
  ADJUDICACION.DIR_CONTRATISTA AS streetAddress,
-- suppliers _ address - region
  GEO.DESCRIPCION AS region,
-- suppliers _ address - countryName
  'Colombia' AS countryName,
-- suppliers _ contactPoint - name
  ADJUDICACION.NOMBRE_REPRESENTANTE AS contactName,
  
-- Items
-- Items - id
  CASE 
    WHEN PROCESO.UNSPSC_CLASE IS NULL THEN PROCESO.ID_OBJETO_CONTRATO
    ELSE PROCESO.UNSPSC_CLASE
  END item_id,
-- Items - description
  CASE 
    WHEN PROCESO.UNSPSC_CLASE IS NULL THEN OBJETO.DESC_OBJE
    ELSE ITEM.NOM_CLASE
  END item_description,
-- Item _ Classification  
-- Item _ Classification - scheme
  'UNSPSC' AS item_classi_scheme,
-- Item _ Classification - id
  CASE 
    WHEN PROCESO.UNSPSC_CLASE IS NULL THEN PROCESO.ID_OBJETO_CONTRATO
    ELSE PROCESO.UNSPSC_CLASE
  END item_classi_id, 
-- Item _ Classification - description
  CASE 
    WHEN PROCESO.UNSPSC_CLASE IS NULL THEN OBJETO.DESC_OBJE
    ELSE ITEM.NOM_CLASE
  END item_classi_description,
-- Item _ Classification - uri
  'http://www.colombiacompra.gov.co/es/clasificacion' AS item_classi_uri,

-- contractPeriod
-- contractPeriod - startDate
  ADJUDICACION.FECHA_INICIO_EJECUCION AS startDate,
-- contractPeriod - endDate
  CASE ADJUDICACION.RANGO_PLAZO_EJECUCION
    WHEN 'M'
      THEN
        ADD_MONTHS(ADJUDICACION.fecha_inicio_ejecucion, NVL(ADJUDICACION.plazo_ejecucion, 0))
    WHEN 'D'
      THEN
        ADJUDICACION.fecha_inicio_ejecucion + NVL(ADJUDICACION.plazo_ejecucion, 0)
    ELSE NULL
  END endDate,
  PROCESO.NUM_CONSTANCIA AS num_constancia 
FROM T_PTC_ADJUDICACIONES ADJUDICACION
LEFT JOIN T_PTC_PROCESOS PROCESO
  ON ADJUDICACION.ID_PROCESO = PROCESO.NUM_CONSTANCIA
LEFT JOIN TB_USUARIOLDAP USRLDAP
  ON PROCESO.USUARIO = USRLDAP.USUARIO
LEFT JOIN T_PTC_TIPOS_DOCUMENTOS TIPODOC
  ON TIPODOC.IDENTIFICACION = ADJUDICACION.TIPO_DOC_CONTRATISTA
LEFT JOIN T_PTC_UBICACIONES_GEO GEO
  ON ADJUDICACION.ID_MUNICIPIO_CONTRATISTA = GEO.IDENTIFICADOR
LEFT JOIN UNSPSC_CLASES ITEM
  ON PROCESO.UNSPSC_CLASE = ITEM.COD_CLASE
LEFT JOIN TPOR_OBJE OBJETO
  ON PROCESO.ID_OBJETO_CONTRATO = OBJETO.CODI_OBJE
WHERE 
  USRLDAP.IDENTIDAD <> '199999999'
  AND TRUNC(PROCESO.FECHA_CARGUE) BETWEEN TO_DATE('01/01/2015','DD/MM/YYYY') AND TO_DATE('19/08/2015','DD/MM/YYYY')
;