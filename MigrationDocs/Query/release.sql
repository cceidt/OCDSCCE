SELECT
-- id
  PROCESO.NUM_CONSTANCIA AS id,
-- date
  NOVEDAD.dueDate AS R_date,
-- tag
  CASE PROCESO.ESTADO_PROCESO
    WHEN '1' THEN 'planning'
    WHEN '2' THEN 'tender'
    WHEN '3' THEN 'award'
    WHEN '4' THEN 'contract'
    WHEN '5' THEN 'contractTermination'
    WHEN '6' THEN 'awardCancellation'
    WHEN '7' THEN 'awardCancellation'
    WHEN '8' THEN 'contractTermination'
    WHEN '9' THEN 'tender'
    WHEN '10' THEN 'tender'
    WHEN '11' THEN 'tender'
    WHEN '12' THEN 'award'
    WHEN '13' THEN 'tender'
    WHEN '14' THEN 'tender'
    WHEN '15' THEN 'tender'
    WHEN '16' THEN 'tender'
    WHEN '17' THEN 'tender'
    WHEN '18' THEN 'tender'
    ELSE NULL
  END tag,
-- initiationType
  'tender' as initiationType,
  
-- planning and tender are another transformation Pentaho

-- buyer
-- buyer _ identifier
-- buyer _ identifier - id
  ENTIDAD.NIT_ENTI AS ident,
-- buyer _ identifier - legalName
  ENTIDAD.NOMB_ENTI AS legalName,
-- buyer - name
  ENTIDAD.NOMB_ENTI AS name,
-- buyer _ address - streetAddress
  ENTIDAD.DIRE_ENTI AS streetAddress,
-- buyer _ address - locality
  GEO.DESCRIPCION AS locality,
-- buyer _ address - region
  GEO_TWO.DESCRIPCION AS region,
-- buyer _ address - region
  'Colombia' AS countryName,
-- buyer _ contactPoint - name
  USRLDAP.NOMBREUSUARIO AS usrname,
-- buyer _ contactPoint - email
  USRLDAP.EMAILUSUARIO AS usremail,
-- buyer _ contactPoint - telephone
  USRLDAP.TELEFONO AS usrtelephone,
-- language  
  'es' as language,
  
  PROCESO.NUM_CONSTANCIA AS num_constancia
  
FROM T_PTC_PROCESOS PROCESO
LEFT JOIN (
  SELECT 
    NOVEDAD.FECHA_NOVEDAD AS dueDate,
    NOVEDAD.NUMERO_CONSTANCIA AS NUM_CONSTANCIA
  FROM T_PTC_NOVEDADES NOVEDAD
  WHERE 
    NOVEDAD.OID IN (SELECT MAX(OID) FROM T_PTC_NOVEDADES GROUP BY NUMERO_CONSTANCIA)
  ) NOVEDAD
  ON PROCESO.NUM_CONSTANCIA = NOVEDAD.NUM_CONSTANCIA
LEFT JOIN TB_USUARIOLDAP USRLDAP
  ON PROCESO.USUARIO = USRLDAP.USUARIO
LEFT JOIN TPOR_ENTI ENTIDAD
  ON USRLDAP.IDENTIDAD = ENTIDAD.CODI_ENTI
LEFT JOIN T_PTC_UBICACIONES_GEO GEO
  ON ENTIDAD.UBICACION_GEO = GEO.IDENTIFICADOR
LEFT JOIN T_PTC_UBICACIONES_GEO GEO_TWO
  ON GEO.IDENTIFICADOR_PADRE = GEO_TWO.IDENTIFICADOR
WHERE 
  TRUNC(PROCESO.fecha_cargue) BETWEEN TO_DATE('01/01/2015','DD/MM/YYYY') AND TO_DATE('19/08/2015','DD/MM/YYYY')
AND USRLDAP.IDENTIDAD <> '199999999'
;