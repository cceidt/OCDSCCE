SELECT
-- id
  PROCESO.NUM_CONSTANCIA AS id,
-- title
  PROCESO.NUMERO_PROCESO AS title,
-- Description
  PROCESO.DETALLE_OBJETO AS description,
-- status
  CASE PROCESO.ESTADO_PROCESO
    WHEN '1' THEN 'planned'
    WHEN '2' THEN 'active'
    WHEN '3' THEN 'complete'
    WHEN '4' THEN 'complete'
    WHEN '5' THEN 'complete'
    WHEN '6' THEN 'cancelled'
    WHEN '7' THEN 'unsuccessful'
    WHEN '8' THEN 'complete'
    WHEN '9' THEN 'active'
    WHEN '10' THEN 'active'
    WHEN '11' THEN 'active'
    WHEN '12' THEN 'complete'
    WHEN '13' THEN 'active'
    WHEN '14' THEN 'active'
    WHEN '15' THEN 'active'
    WHEN '16' THEN 'active'
    WHEN '17' THEN 'active'
    WHEN '18' THEN 'active'
    ELSE NULL
  END status,

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

-- value
-- value - amount
  PROCESO.CUANTIA AS value,
-- value - currency
  'COP' AS currency,
-- procurementMethod
  CASE PROCESO.ID_TIPO_PROCESO
    WHEN '1' THEN 'open'
    WHEN '2' THEN 'limited'
    WHEN '3' THEN 'limited'
    WHEN '5' THEN 'selective'
    WHEN '6' THEN 'open'
    WHEN '7' THEN 'selective'
    WHEN '8' THEN 'open'
    WHEN '9' THEN 'open'
    WHEN '10' THEN 'selective'
    WHEN '18' THEN 'open'
    WHEN '19' THEN 'selective'
    WHEN '20' THEN 'selective'
    WHEN '12' THEN 'limited'
    WHEN '11' THEN 'open'
    WHEN '13' THEN 'open'
    WHEN '17' THEN 'open'
    WHEN '16' THEN 'selective'
    WHEN '15' THEN 'open'
    WHEN '14' THEN 'selective' 
    ELSE NULL
  END procurementMethod,
-- procurementMethodRationale
C_DIRECTA.DESCRIPCION AS procurementMethodRationale,

-- tenderPeriod
-- tenderPeriod - startDate
PROCESO.FECHA_APERTURA AS tenderPeriod_startDate,
-- tenderPeriod - endDate
PROCESO.FECHA_CIERRE AS tenderPeriod_endDate,

-- enquiryPeriod
-- enquiryPeriod - startDate
PROCESO.FECHA_ACLARACION AS enquiryPeriod_startDate,
-- enquiryPeriod - endDate
PROCESO.FECHA_ACLARACION AS enquiryPeriod_endDate,

-- hasEnquiries
CASE 
  WHEN (SELECT COUNT (1)
    FROM TB_ARCHIVO
    WHERE NUMERO_CONSTANCIA = PROCESO.NUM_CONSTANCIA
    AND OID_CLASE_ARCHIVO = 7) > 0 THEN 1
  ELSE 0
END hasEnquiries,

-- documents and milestones  is a distinct process into pentaho

-- amendment
MODIFICACIONES.FECHA_MODIFICACION AS amendment_date,
-- amendment _ changes
-- amendment _ changes - property
MODIFICACIONES.CAMPO AS amendment_changes_property,
-- amendment _ changes - former_value
MODIFICACIONES.VALOR_ANTERIOR AS amendment_changes_former_value,
-- amendment - rationale
MODIFICACIONES.COMENTARIOS AS amendment_rationale

-- deliveryAddressh is a distinct process into pentaho


FROM T_PTC_PROCESOS PROCESO
LEFT JOIN UNSPSC_CLASES ITEM
  ON PROCESO.UNSPSC_CLASE = ITEM.COD_CLASE
LEFT JOIN T_PTC_CAUSALES_DIRECTA C_DIRECTA
  ON C_DIRECTA.IDENTIFICADOR = PROCESO.ID_CAUSAL_DIRECTA
LEFT JOIN TPOR_OBJE OBJETO
  ON PROCESO.ID_OBJETO_CONTRATO = OBJETO.CODI_OBJE
LEFT JOIN (
  SELECT 
    SOPORTES_MODIFICACIONES.FECHA_MODIFICACION,
    SOPORTES_MODIFICACIONES.CAMPO,
    SOPORTES_MODIFICACIONES.VALOR_ANTERIOR,
    SOPORTES_MODIFICACIONES.COMENTARIOS,
    SOPORTES_MODIFICACIONES.ID_PROCESO
  FROM T_PTC_SOPORTES_MODIFICACIONES SOPORTES_MODIFICACIONES
  WHERE 
    (SOPORTES_MODIFICACIONES.ID_ADJUDICACION IS NULL
    OR SOPORTES_MODIFICACIONES.ID_ADJUDICACION = 0)
    AND 
      SOPORTES_MODIFICACIONES.ID_MODIFICACION IN (SELECT MAX(ID_MODIFICACION) FROM T_PTC_SOPORTES_MODIFICACIONES GROUP BY ID_PROCESO)
  ) MODIFICACIONES
  ON PROCESO.NUM_CONSTANCIA = MODIFICACIONES.ID_PROCESO
LEFT JOIN TB_USUARIOLDAP USRLDAP
  ON PROCESO.USUARIO = USRLDAP.USUARIO
WHERE 
  TRUNC(PROCESO.FECHA_CARGUE) BETWEEN TO_DATE('01/01/2015','DD/MM/YYYY') AND TO_DATE('19/08/2015','DD/MM/YYYY')
  AND USRLDAP.IDENTIDAD <> '199999999';