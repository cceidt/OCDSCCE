SELECT 
  CONCAT('/consultas/detalleProceso.do?numConstancia=', PROCESO.NUM_CONSTANCIA) AS uri,
  PROCESO.FECHA_ULT_ACTUALIZACION AS publishedDate,

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

  PROCESO.NUM_CONSTANCIA AS num_constancia

FROM T_PTC_PROCESOS PROCESO
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
  AND USRLDAP.IDENTIDAD <> '199999999';