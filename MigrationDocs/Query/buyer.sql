SELECT 
--identifier
--identifier - id
ENTIDAD.NIT_ENTI AS id,
--identifier - legalName
ENTIDAD.NOMB_ENTI AS legalName,
--name
ENTIDAD.NOMB_ENTI AS name,
--address - streetAddress
ENTIDAD.DIRE_ENTI AS streetAddress,
--address - locality
GEO.DESCRIPCION AS locality,
--address - region
GEO_TWO.DESCRIPCION AS region,
--address - countryName
'Colombia' AS countryName
FROM TPOR_ENTI ENTIDAD
LEFT JOIN T_PTC_UBICACIONES_GEO GEO
  ON ENTIDAD.UBICACION_GEO = GEO.IDENTIFICADOR
LEFT JOIN T_PTC_UBICACIONES_GEO GEO_TWO
  ON GEO.IDENTIFICADOR_PADRE = GEO_TWO.IDENTIFICADOR
;