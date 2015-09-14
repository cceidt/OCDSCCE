SELECT 
NUMERO_CONSTANCIA AS n_constancia,
OID as id,

CASE OID_CLASE_ARCHIVO
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

NOMBRE AS title,
DESCRIPCION AS description,
'/consultas/VerDocumentoPublic?ruta=' || RUTA_SERVIDOR AS url,
FECHA_CREACION AS datePublished,
FECHA_ULTIMA_MODIFICACION AS dateModified,
TIPO AS format
FROM TB_ARCHIVO
WHERE
  OID_ESTADO_PROCESO IN (2,9,10,11,13,14,15,16,17,18)
  AND TRUNC(FECHA_CREACION)  BETWEEN TO_DATE('01/03/2015','DD/MM/YYYY') AND TO_DATE('31/08/2015','DD/MM/YYYY')