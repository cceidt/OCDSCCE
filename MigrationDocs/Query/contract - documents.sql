SELECT 
ARCHIVO.NUMERO_CONSTANCIA AS id_release,
OID as id,

CASE ARCHIVO.OID_CLASE_ARCHIVO
  WHEN 3 THEN 'clarifications'
  WHEN 6 THEN 'hearingNotice'
  WHEN 9 THEN 'winningBid'
  WHEN 10 THEN 'evaluationReports'
  WHEN 11 THEN 'Contract notice'
  WHEN 13 THEN 'contractSigned'
  WHEN 17 THEN 'completionCertificate'
  WHEN 18 THEN 'completionCertificate'
  WHEN 19 THEN 'contractAnnexe'
  WHEN 21 THEN 'technicalSpecifications'
  WHEN 26 THEN 'Award notice'
  WHEN 29 THEN 'assetAndLiabilityAssessment'
  WHEN 30 THEN 'shortlistedFirms'
  WHEN 32 THEN 'winningBid'
  WHEN 34 THEN 'biddingDocuments'
  WHEN 36 THEN 'shortlistedFirms'
  WHEN 37 THEN 'Tender notice'
  WHEN 39 THEN 'technicalSpecifications'
  WHEN 40 THEN 'riskProvisions'
  WHEN 42 THEN 'Tender notice'
  WHEN 44 THEN 'Tender notice'
  WHEN 47 THEN 'technicalSpecifications'  
  ELSE NULL
END documentType,

ARCHIVO.NOMBRE AS title,
ARCHIVO.DESCRIPCION AS description,
'/consultas/VerDocumentoPublic?ruta=' || RUTA_SERVIDOR AS url,
ARCHIVO.FECHA_CREACION AS datePublished,
ARCHIVO.FECHA_ULTIMA_MODIFICACION AS dateModified,
ARCHIVO.TIPO AS format
FROM TB_ARCHIVO ARCHIVO
LEFT JOIN T_PTC_PROCESOS PROCESO
  ON ARCHIVO.NUMERO_CONSTANCIA = PROCESO.NUM_CONSTANCIA
LEFT JOIN TB_USUARIOLDAP USRLDAP
  ON PROCESO.USUARIO = USRLDAP.USUARIO
WHERE
  ARCHIVO.OID_ESTADO_PROCESO IN (5, 8)
  AND  TRUNC(PROCESO.FECHA_CARGUE) BETWEEN TO_DATE('01/01/2015','DD/MM/YYYY') AND TO_DATE('10/12/2015','DD/MM/YYYY')
AND USRLDAP.IDENTIDAD <> '199999999';