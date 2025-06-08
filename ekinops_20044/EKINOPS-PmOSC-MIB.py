# SNMP MIB module (EKINOPS-PmOSC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-PmOSC-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:01:48 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(EkiApiState,
 EkiMeasureType,
 EkiMode,
 EkiOnOff,
 EkiProtocol,
 EkiState,
 EkiSynchroMode,
 ekinops) = mibBuilder.importSymbols(
    "EKINOPS-MIB",
    "EkiApiState",
    "EkiMeasureType",
    "EkiMode",
    "EkiOnOff",
    "EkiProtocol",
    "EkiState",
    "EkiSynchroMode",
    "ekinops")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

modulePmOSC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14)
)
if mibBuilder.loadTexts:
    modulePmOSC.setRevisions(
        ("2006-07-03 00:00",
         "2007-05-21 00:00",
         "2007-06-28 00:00",
         "2007-11-21 00:00",
         "2009-05-18 00:00",
         "2010-02-25 00:00",
         "2010-11-04 00:00",
         "2012-07-04 00:00",
         "2014-03-27 00:00",
         "2014-12-11 00:00",
         "2016-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pmoscalarms_ObjectIdentity = ObjectIdentity
pmoscalarms = _Pmoscalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2)
)
_PmoscAlmOther_ObjectIdentity = ObjectIdentity
pmoscAlmOther = _PmoscAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 1)
)
_PmoscAlmOtherNurg_ObjectIdentity = ObjectIdentity
pmoscAlmOtherNurg = _PmoscAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 1, 1)
)
_PmoscAlmOtherUrg_ObjectIdentity = ObjectIdentity
pmoscAlmOtherUrg = _PmoscAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 1, 2)
)
_PmoscAlmOtherCrit_ObjectIdentity = ObjectIdentity
pmoscAlmOtherCrit = _PmoscAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 1, 3)
)
_PmoscAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmoscAlmsynthAlm0 = _PmoscAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 1, 3, 0)
)
_PmoscAlmModuleGlobFailure_Type = EkiOnOff
_PmoscAlmModuleGlobFailure_Object = MibScalar
pmoscAlmModuleGlobFailure = _PmoscAlmModuleGlobFailure_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 1, 3, 0, 9),
    _PmoscAlmModuleGlobFailure_Type()
)
pmoscAlmModuleGlobFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmModuleGlobFailure.setStatus("current")
_PmoscAlmDefFuseA_Type = EkiOnOff
_PmoscAlmDefFuseA_Object = MibScalar
pmoscAlmDefFuseA = _PmoscAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 1, 3, 0, 15),
    _PmoscAlmDefFuseA_Type()
)
pmoscAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmDefFuseA.setStatus("current")
_PmoscAlmDefFuseB_Type = EkiOnOff
_PmoscAlmDefFuseB_Object = MibScalar
pmoscAlmDefFuseB = _PmoscAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 1, 3, 0, 16),
    _PmoscAlmDefFuseB_Type()
)
pmoscAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmDefFuseB.setStatus("current")
_PmoscAlmClient_ObjectIdentity = ObjectIdentity
pmoscAlmClient = _PmoscAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2)
)
_PmoscAlmClientNurg_ObjectIdentity = ObjectIdentity
pmoscAlmClientNurg = _PmoscAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 1)
)
_PmoscAlmportaSfpWarnDdm_ObjectIdentity = ObjectIdentity
pmoscAlmportaSfpWarnDdm = _PmoscAlmportaSfpWarnDdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 1, 20)
)
_PmoscAlmPortaTxPwLowWng_Type = EkiOnOff
_PmoscAlmPortaTxPwLowWng_Object = MibScalar
pmoscAlmPortaTxPwLowWng = _PmoscAlmPortaTxPwLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 1, 20, 1),
    _PmoscAlmPortaTxPwLowWng_Type()
)
pmoscAlmPortaTxPwLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaTxPwLowWng.setStatus("current")
_PmoscAlmPortaTxPwrHighWng_Type = EkiOnOff
_PmoscAlmPortaTxPwrHighWng_Object = MibScalar
pmoscAlmPortaTxPwrHighWng = _PmoscAlmPortaTxPwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 1, 20, 2),
    _PmoscAlmPortaTxPwrHighWng_Type()
)
pmoscAlmPortaTxPwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaTxPwrHighWng.setStatus("current")
_PmoscAlmPortaTxBiasLowWng_Type = EkiOnOff
_PmoscAlmPortaTxBiasLowWng_Object = MibScalar
pmoscAlmPortaTxBiasLowWng = _PmoscAlmPortaTxBiasLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 1, 20, 3),
    _PmoscAlmPortaTxBiasLowWng_Type()
)
pmoscAlmPortaTxBiasLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaTxBiasLowWng.setStatus("current")
_PmoscAlmPortaTxBiasHighWng_Type = EkiOnOff
_PmoscAlmPortaTxBiasHighWng_Object = MibScalar
pmoscAlmPortaTxBiasHighWng = _PmoscAlmPortaTxBiasHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 1, 20, 4),
    _PmoscAlmPortaTxBiasHighWng_Type()
)
pmoscAlmPortaTxBiasHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaTxBiasHighWng.setStatus("current")
_PmoscAlmPortaTempLowWng_Type = EkiOnOff
_PmoscAlmPortaTempLowWng_Object = MibScalar
pmoscAlmPortaTempLowWng = _PmoscAlmPortaTempLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 1, 20, 7),
    _PmoscAlmPortaTempLowWng_Type()
)
pmoscAlmPortaTempLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaTempLowWng.setStatus("current")
_PmoscAlmPortaTempHighWng_Type = EkiOnOff
_PmoscAlmPortaTempHighWng_Object = MibScalar
pmoscAlmPortaTempHighWng = _PmoscAlmPortaTempHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 1, 20, 8),
    _PmoscAlmPortaTempHighWng_Type()
)
pmoscAlmPortaTempHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaTempHighWng.setStatus("current")
_PmoscAlmPortaRxPwrLowWng_Type = EkiOnOff
_PmoscAlmPortaRxPwrLowWng_Object = MibScalar
pmoscAlmPortaRxPwrLowWng = _PmoscAlmPortaRxPwrLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 1, 20, 15),
    _PmoscAlmPortaRxPwrLowWng_Type()
)
pmoscAlmPortaRxPwrLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaRxPwrLowWng.setStatus("current")
_PmoscAlmPortaRxPwrHighWng_Type = EkiOnOff
_PmoscAlmPortaRxPwrHighWng_Object = MibScalar
pmoscAlmPortaRxPwrHighWng = _PmoscAlmPortaRxPwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 1, 20, 16),
    _PmoscAlmPortaRxPwrHighWng_Type()
)
pmoscAlmPortaRxPwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaRxPwrHighWng.setStatus("current")
_PmoscAlmClientUrg_ObjectIdentity = ObjectIdentity
pmoscAlmClientUrg = _PmoscAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 2)
)
_PmoscAlmportaSfpAlmDdm_ObjectIdentity = ObjectIdentity
pmoscAlmportaSfpAlmDdm = _PmoscAlmportaSfpAlmDdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 2, 18)
)
_PmoscAlmPortaTxPwrLowAla_Type = EkiOnOff
_PmoscAlmPortaTxPwrLowAla_Object = MibScalar
pmoscAlmPortaTxPwrLowAla = _PmoscAlmPortaTxPwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 2, 18, 1),
    _PmoscAlmPortaTxPwrLowAla_Type()
)
pmoscAlmPortaTxPwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaTxPwrLowAla.setStatus("current")
_PmoscAlmPortaTxPwrHighAla_Type = EkiOnOff
_PmoscAlmPortaTxPwrHighAla_Object = MibScalar
pmoscAlmPortaTxPwrHighAla = _PmoscAlmPortaTxPwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 2, 18, 2),
    _PmoscAlmPortaTxPwrHighAla_Type()
)
pmoscAlmPortaTxPwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaTxPwrHighAla.setStatus("current")
_PmoscAlmPortaTxBiasLowAla_Type = EkiOnOff
_PmoscAlmPortaTxBiasLowAla_Object = MibScalar
pmoscAlmPortaTxBiasLowAla = _PmoscAlmPortaTxBiasLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 2, 18, 3),
    _PmoscAlmPortaTxBiasLowAla_Type()
)
pmoscAlmPortaTxBiasLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaTxBiasLowAla.setStatus("current")
_PmoscAlmPortaTxBiasHighAla_Type = EkiOnOff
_PmoscAlmPortaTxBiasHighAla_Object = MibScalar
pmoscAlmPortaTxBiasHighAla = _PmoscAlmPortaTxBiasHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 2, 18, 4),
    _PmoscAlmPortaTxBiasHighAla_Type()
)
pmoscAlmPortaTxBiasHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaTxBiasHighAla.setStatus("current")
_PmoscAlmPortaTempLowAla_Type = EkiOnOff
_PmoscAlmPortaTempLowAla_Object = MibScalar
pmoscAlmPortaTempLowAla = _PmoscAlmPortaTempLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 2, 18, 7),
    _PmoscAlmPortaTempLowAla_Type()
)
pmoscAlmPortaTempLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaTempLowAla.setStatus("current")
_PmoscAlmPortaTempHighAla_Type = EkiOnOff
_PmoscAlmPortaTempHighAla_Object = MibScalar
pmoscAlmPortaTempHighAla = _PmoscAlmPortaTempHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 2, 18, 8),
    _PmoscAlmPortaTempHighAla_Type()
)
pmoscAlmPortaTempHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaTempHighAla.setStatus("current")
_PmoscAlmPortaRxPwrLowAla_Type = EkiOnOff
_PmoscAlmPortaRxPwrLowAla_Object = MibScalar
pmoscAlmPortaRxPwrLowAla = _PmoscAlmPortaRxPwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 2, 18, 15),
    _PmoscAlmPortaRxPwrLowAla_Type()
)
pmoscAlmPortaRxPwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaRxPwrLowAla.setStatus("current")
_PmoscAlmPortaRxPwrHighAla_Type = EkiOnOff
_PmoscAlmPortaRxPwrHighAla_Object = MibScalar
pmoscAlmPortaRxPwrHighAla = _PmoscAlmPortaRxPwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 2, 18, 16),
    _PmoscAlmPortaRxPwrHighAla_Type()
)
pmoscAlmPortaRxPwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaRxPwrHighAla.setStatus("current")
_PmoscAlmClientCrit_ObjectIdentity = ObjectIdentity
pmoscAlmClientCrit = _PmoscAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 3)
)
_PmoscAlmsynthAlm8_ObjectIdentity = ObjectIdentity
pmoscAlmsynthAlm8 = _PmoscAlmsynthAlm8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 3, 8)
)
_PmoscAlmPortaSfpAbsent_Type = EkiOnOff
_PmoscAlmPortaSfpAbsent_Object = MibScalar
pmoscAlmPortaSfpAbsent = _PmoscAlmPortaSfpAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 3, 8, 1),
    _PmoscAlmPortaSfpAbsent_Type()
)
pmoscAlmPortaSfpAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaSfpAbsent.setStatus("current")
_PmoscAlmPortaDdmAbsent_Type = EkiOnOff
_PmoscAlmPortaDdmAbsent_Object = MibScalar
pmoscAlmPortaDdmAbsent = _PmoscAlmPortaDdmAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 3, 8, 2),
    _PmoscAlmPortaDdmAbsent_Type()
)
pmoscAlmPortaDdmAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaDdmAbsent.setStatus("current")
_PmoscAlmPortaHwFail_Type = EkiOnOff
_PmoscAlmPortaHwFail_Object = MibScalar
pmoscAlmPortaHwFail = _PmoscAlmPortaHwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 3, 8, 4),
    _PmoscAlmPortaHwFail_Type()
)
pmoscAlmPortaHwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaHwFail.setStatus("current")
_PmoscAlmPortaLsd_Type = EkiOnOff
_PmoscAlmPortaLsd_Object = MibScalar
pmoscAlmPortaLsd = _PmoscAlmPortaLsd_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 3, 8, 5),
    _PmoscAlmPortaLsd_Type()
)
pmoscAlmPortaLsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaLsd.setStatus("current")
_PmoscAlmPortaLocalOos_Type = EkiOnOff
_PmoscAlmPortaLocalOos_Object = MibScalar
pmoscAlmPortaLocalOos = _PmoscAlmPortaLocalOos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 3, 8, 6),
    _PmoscAlmPortaLocalOos_Type()
)
pmoscAlmPortaLocalOos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaLocalOos.setStatus("current")
_PmoscAlmPortaDdmWarning_Type = EkiOnOff
_PmoscAlmPortaDdmWarning_Object = MibScalar
pmoscAlmPortaDdmWarning = _PmoscAlmPortaDdmWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 3, 8, 9),
    _PmoscAlmPortaDdmWarning_Type()
)
pmoscAlmPortaDdmWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaDdmWarning.setStatus("current")
_PmoscAlmPortaDdmAlm_Type = EkiOnOff
_PmoscAlmPortaDdmAlm_Object = MibScalar
pmoscAlmPortaDdmAlm = _PmoscAlmPortaDdmAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 3, 8, 10),
    _PmoscAlmPortaDdmAlm_Type()
)
pmoscAlmPortaDdmAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaDdmAlm.setStatus("current")
_PmoscAlmPortaFail_Type = EkiOnOff
_PmoscAlmPortaFail_Object = MibScalar
pmoscAlmPortaFail = _PmoscAlmPortaFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 3, 8, 12),
    _PmoscAlmPortaFail_Type()
)
pmoscAlmPortaFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaFail.setStatus("current")
_PmoscAlmportaAccessioAlm_ObjectIdentity = ObjectIdentity
pmoscAlmportaAccessioAlm = _PmoscAlmportaAccessioAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 3, 16)
)
_PmoscAlmPortaLasFail_Type = EkiOnOff
_PmoscAlmPortaLasFail_Object = MibScalar
pmoscAlmPortaLasFail = _PmoscAlmPortaLasFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 3, 16, 1),
    _PmoscAlmPortaLasFail_Type()
)
pmoscAlmPortaLasFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaLasFail.setStatus("current")
_PmoscAlmPortaLos_Type = EkiOnOff
_PmoscAlmPortaLos_Object = MibScalar
pmoscAlmPortaLos = _PmoscAlmPortaLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 2, 3, 16, 4),
    _PmoscAlmPortaLos_Type()
)
pmoscAlmPortaLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortaLos.setStatus("current")
_PmoscAlmLine_ObjectIdentity = ObjectIdentity
pmoscAlmLine = _PmoscAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3)
)
_PmoscAlmLineNurg_ObjectIdentity = ObjectIdentity
pmoscAlmLineNurg = _PmoscAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 1)
)
_PmoscAlmportbSfpWarnDdm_ObjectIdentity = ObjectIdentity
pmoscAlmportbSfpWarnDdm = _PmoscAlmportbSfpWarnDdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 1, 28)
)
_PmoscAlmPortbTxPwLowWng_Type = EkiOnOff
_PmoscAlmPortbTxPwLowWng_Object = MibScalar
pmoscAlmPortbTxPwLowWng = _PmoscAlmPortbTxPwLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 1, 28, 1),
    _PmoscAlmPortbTxPwLowWng_Type()
)
pmoscAlmPortbTxPwLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbTxPwLowWng.setStatus("current")
_PmoscAlmPortbTxPwrHighWng_Type = EkiOnOff
_PmoscAlmPortbTxPwrHighWng_Object = MibScalar
pmoscAlmPortbTxPwrHighWng = _PmoscAlmPortbTxPwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 1, 28, 2),
    _PmoscAlmPortbTxPwrHighWng_Type()
)
pmoscAlmPortbTxPwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbTxPwrHighWng.setStatus("current")
_PmoscAlmPortbTxBiasLowWng_Type = EkiOnOff
_PmoscAlmPortbTxBiasLowWng_Object = MibScalar
pmoscAlmPortbTxBiasLowWng = _PmoscAlmPortbTxBiasLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 1, 28, 3),
    _PmoscAlmPortbTxBiasLowWng_Type()
)
pmoscAlmPortbTxBiasLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbTxBiasLowWng.setStatus("current")
_PmoscAlmPortbTxBiasHighWng_Type = EkiOnOff
_PmoscAlmPortbTxBiasHighWng_Object = MibScalar
pmoscAlmPortbTxBiasHighWng = _PmoscAlmPortbTxBiasHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 1, 28, 4),
    _PmoscAlmPortbTxBiasHighWng_Type()
)
pmoscAlmPortbTxBiasHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbTxBiasHighWng.setStatus("current")
_PmoscAlmPortbTempLowWng_Type = EkiOnOff
_PmoscAlmPortbTempLowWng_Object = MibScalar
pmoscAlmPortbTempLowWng = _PmoscAlmPortbTempLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 1, 28, 7),
    _PmoscAlmPortbTempLowWng_Type()
)
pmoscAlmPortbTempLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbTempLowWng.setStatus("current")
_PmoscAlmPortbTempHighWng_Type = EkiOnOff
_PmoscAlmPortbTempHighWng_Object = MibScalar
pmoscAlmPortbTempHighWng = _PmoscAlmPortbTempHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 1, 28, 8),
    _PmoscAlmPortbTempHighWng_Type()
)
pmoscAlmPortbTempHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbTempHighWng.setStatus("current")
_PmoscAlmPortbRxPwrLowWng_Type = EkiOnOff
_PmoscAlmPortbRxPwrLowWng_Object = MibScalar
pmoscAlmPortbRxPwrLowWng = _PmoscAlmPortbRxPwrLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 1, 28, 15),
    _PmoscAlmPortbRxPwrLowWng_Type()
)
pmoscAlmPortbRxPwrLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbRxPwrLowWng.setStatus("current")
_PmoscAlmPortbRxPwrHighWng_Type = EkiOnOff
_PmoscAlmPortbRxPwrHighWng_Object = MibScalar
pmoscAlmPortbRxPwrHighWng = _PmoscAlmPortbRxPwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 1, 28, 16),
    _PmoscAlmPortbRxPwrHighWng_Type()
)
pmoscAlmPortbRxPwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbRxPwrHighWng.setStatus("current")
_PmoscAlmLineUrg_ObjectIdentity = ObjectIdentity
pmoscAlmLineUrg = _PmoscAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 2)
)
_PmoscAlmportbSfpAlmDdm_ObjectIdentity = ObjectIdentity
pmoscAlmportbSfpAlmDdm = _PmoscAlmportbSfpAlmDdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 2, 26)
)
_PmoscAlmPortbTxPwrLowAla_Type = EkiOnOff
_PmoscAlmPortbTxPwrLowAla_Object = MibScalar
pmoscAlmPortbTxPwrLowAla = _PmoscAlmPortbTxPwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 2, 26, 1),
    _PmoscAlmPortbTxPwrLowAla_Type()
)
pmoscAlmPortbTxPwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbTxPwrLowAla.setStatus("current")
_PmoscAlmPortbTxPwrHighAla_Type = EkiOnOff
_PmoscAlmPortbTxPwrHighAla_Object = MibScalar
pmoscAlmPortbTxPwrHighAla = _PmoscAlmPortbTxPwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 2, 26, 2),
    _PmoscAlmPortbTxPwrHighAla_Type()
)
pmoscAlmPortbTxPwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbTxPwrHighAla.setStatus("current")
_PmoscAlmPortbTxBiasLowAla_Type = EkiOnOff
_PmoscAlmPortbTxBiasLowAla_Object = MibScalar
pmoscAlmPortbTxBiasLowAla = _PmoscAlmPortbTxBiasLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 2, 26, 3),
    _PmoscAlmPortbTxBiasLowAla_Type()
)
pmoscAlmPortbTxBiasLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbTxBiasLowAla.setStatus("current")
_PmoscAlmPortbTxBiasHighAla_Type = EkiOnOff
_PmoscAlmPortbTxBiasHighAla_Object = MibScalar
pmoscAlmPortbTxBiasHighAla = _PmoscAlmPortbTxBiasHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 2, 26, 4),
    _PmoscAlmPortbTxBiasHighAla_Type()
)
pmoscAlmPortbTxBiasHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbTxBiasHighAla.setStatus("current")
_PmoscAlmPortbTempLowAla_Type = EkiOnOff
_PmoscAlmPortbTempLowAla_Object = MibScalar
pmoscAlmPortbTempLowAla = _PmoscAlmPortbTempLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 2, 26, 7),
    _PmoscAlmPortbTempLowAla_Type()
)
pmoscAlmPortbTempLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbTempLowAla.setStatus("current")
_PmoscAlmPortbTempHighAla_Type = EkiOnOff
_PmoscAlmPortbTempHighAla_Object = MibScalar
pmoscAlmPortbTempHighAla = _PmoscAlmPortbTempHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 2, 26, 8),
    _PmoscAlmPortbTempHighAla_Type()
)
pmoscAlmPortbTempHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbTempHighAla.setStatus("current")
_PmoscAlmPortbRxPwrLowAla_Type = EkiOnOff
_PmoscAlmPortbRxPwrLowAla_Object = MibScalar
pmoscAlmPortbRxPwrLowAla = _PmoscAlmPortbRxPwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 2, 26, 15),
    _PmoscAlmPortbRxPwrLowAla_Type()
)
pmoscAlmPortbRxPwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbRxPwrLowAla.setStatus("current")
_PmoscAlmPortbRxPwrHighAla_Type = EkiOnOff
_PmoscAlmPortbRxPwrHighAla_Object = MibScalar
pmoscAlmPortbRxPwrHighAla = _PmoscAlmPortbRxPwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 2, 26, 16),
    _PmoscAlmPortbRxPwrHighAla_Type()
)
pmoscAlmPortbRxPwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbRxPwrHighAla.setStatus("current")
_PmoscAlmLineCrit_ObjectIdentity = ObjectIdentity
pmoscAlmLineCrit = _PmoscAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 3)
)
_PmoscAlmsynthAlm7_ObjectIdentity = ObjectIdentity
pmoscAlmsynthAlm7 = _PmoscAlmsynthAlm7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 3, 7)
)
_PmoscAlmPortbSfpAbsent_Type = EkiOnOff
_PmoscAlmPortbSfpAbsent_Object = MibScalar
pmoscAlmPortbSfpAbsent = _PmoscAlmPortbSfpAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 3, 7, 1),
    _PmoscAlmPortbSfpAbsent_Type()
)
pmoscAlmPortbSfpAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbSfpAbsent.setStatus("current")
_PmoscAlmPortbDdmAbsent_Type = EkiOnOff
_PmoscAlmPortbDdmAbsent_Object = MibScalar
pmoscAlmPortbDdmAbsent = _PmoscAlmPortbDdmAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 3, 7, 2),
    _PmoscAlmPortbDdmAbsent_Type()
)
pmoscAlmPortbDdmAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbDdmAbsent.setStatus("current")
_PmoscAlmPortbHwFail_Type = EkiOnOff
_PmoscAlmPortbHwFail_Object = MibScalar
pmoscAlmPortbHwFail = _PmoscAlmPortbHwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 3, 7, 4),
    _PmoscAlmPortbHwFail_Type()
)
pmoscAlmPortbHwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbHwFail.setStatus("current")
_PmoscAlmPortbLsd_Type = EkiOnOff
_PmoscAlmPortbLsd_Object = MibScalar
pmoscAlmPortbLsd = _PmoscAlmPortbLsd_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 3, 7, 5),
    _PmoscAlmPortbLsd_Type()
)
pmoscAlmPortbLsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbLsd.setStatus("current")
_PmoscAlmPortbLocalOos_Type = EkiOnOff
_PmoscAlmPortbLocalOos_Object = MibScalar
pmoscAlmPortbLocalOos = _PmoscAlmPortbLocalOos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 3, 7, 6),
    _PmoscAlmPortbLocalOos_Type()
)
pmoscAlmPortbLocalOos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbLocalOos.setStatus("current")
_PmoscAlmPortbDdmWarning_Type = EkiOnOff
_PmoscAlmPortbDdmWarning_Object = MibScalar
pmoscAlmPortbDdmWarning = _PmoscAlmPortbDdmWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 3, 7, 9),
    _PmoscAlmPortbDdmWarning_Type()
)
pmoscAlmPortbDdmWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbDdmWarning.setStatus("current")
_PmoscAlmPortbDdmAlm_Type = EkiOnOff
_PmoscAlmPortbDdmAlm_Object = MibScalar
pmoscAlmPortbDdmAlm = _PmoscAlmPortbDdmAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 3, 7, 10),
    _PmoscAlmPortbDdmAlm_Type()
)
pmoscAlmPortbDdmAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbDdmAlm.setStatus("current")
_PmoscAlmPortbFail_Type = EkiOnOff
_PmoscAlmPortbFail_Object = MibScalar
pmoscAlmPortbFail = _PmoscAlmPortbFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 3, 7, 12),
    _PmoscAlmPortbFail_Type()
)
pmoscAlmPortbFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbFail.setStatus("current")
_PmoscAlmportbAccessioAlm_ObjectIdentity = ObjectIdentity
pmoscAlmportbAccessioAlm = _PmoscAlmportbAccessioAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 3, 24)
)
_PmoscAlmPortbLasFail_Type = EkiOnOff
_PmoscAlmPortbLasFail_Object = MibScalar
pmoscAlmPortbLasFail = _PmoscAlmPortbLasFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 3, 24, 1),
    _PmoscAlmPortbLasFail_Type()
)
pmoscAlmPortbLasFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbLasFail.setStatus("current")
_PmoscAlmPortbLos_Type = EkiOnOff
_PmoscAlmPortbLos_Object = MibScalar
pmoscAlmPortbLos = _PmoscAlmPortbLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 2, 3, 3, 24, 4),
    _PmoscAlmPortbLos_Type()
)
pmoscAlmPortbLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscAlmPortbLos.setStatus("current")
_Pmoscmeasures_ObjectIdentity = ObjectIdentity
pmoscmeasures = _Pmoscmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 3)
)
_PmoscMesrOther_ObjectIdentity = ObjectIdentity
pmoscMesrOther = _PmoscMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 3, 1)
)
_PmoscMesrClient_ObjectIdentity = ObjectIdentity
pmoscMesrClient = _PmoscMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 3, 2)
)


class _PmoscMesrportaTemperature_Type(Unsigned32):
    """Custom type pmoscMesrportaTemperature based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoscMesrportaTemperature_Type.__name__ = "Unsigned32"
_PmoscMesrportaTemperature_Object = MibScalar
pmoscMesrportaTemperature = _PmoscMesrportaTemperature_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 3, 2, 16),
    _PmoscMesrportaTemperature_Type()
)
pmoscMesrportaTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscMesrportaTemperature.setStatus("current")


class _PmoscMesrportaVolt_Type(Unsigned32):
    """Custom type pmoscMesrportaVolt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoscMesrportaVolt_Type.__name__ = "Unsigned32"
_PmoscMesrportaVolt_Object = MibScalar
pmoscMesrportaVolt = _PmoscMesrportaVolt_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 3, 2, 17),
    _PmoscMesrportaVolt_Type()
)
pmoscMesrportaVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscMesrportaVolt.setStatus("current")


class _PmoscMesrportaTxBias_Type(Unsigned32):
    """Custom type pmoscMesrportaTxBias based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoscMesrportaTxBias_Type.__name__ = "Unsigned32"
_PmoscMesrportaTxBias_Object = MibScalar
pmoscMesrportaTxBias = _PmoscMesrportaTxBias_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 3, 2, 18),
    _PmoscMesrportaTxBias_Type()
)
pmoscMesrportaTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscMesrportaTxBias.setStatus("current")


class _PmoscMesrportaTxPower_Type(Unsigned32):
    """Custom type pmoscMesrportaTxPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoscMesrportaTxPower_Type.__name__ = "Unsigned32"
_PmoscMesrportaTxPower_Object = MibScalar
pmoscMesrportaTxPower = _PmoscMesrportaTxPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 3, 2, 19),
    _PmoscMesrportaTxPower_Type()
)
pmoscMesrportaTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscMesrportaTxPower.setStatus("current")


class _PmoscMesrportaRxPower_Type(Unsigned32):
    """Custom type pmoscMesrportaRxPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoscMesrportaRxPower_Type.__name__ = "Unsigned32"
_PmoscMesrportaRxPower_Object = MibScalar
pmoscMesrportaRxPower = _PmoscMesrportaRxPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 3, 2, 20),
    _PmoscMesrportaRxPower_Type()
)
pmoscMesrportaRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscMesrportaRxPower.setStatus("current")
_PmoscMesrLine_ObjectIdentity = ObjectIdentity
pmoscMesrLine = _PmoscMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 3, 3)
)


class _PmoscMesrportbTemperature_Type(Unsigned32):
    """Custom type pmoscMesrportbTemperature based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoscMesrportbTemperature_Type.__name__ = "Unsigned32"
_PmoscMesrportbTemperature_Object = MibScalar
pmoscMesrportbTemperature = _PmoscMesrportbTemperature_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 3, 3, 24),
    _PmoscMesrportbTemperature_Type()
)
pmoscMesrportbTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscMesrportbTemperature.setStatus("current")


class _PmoscMesrportbVolt_Type(Unsigned32):
    """Custom type pmoscMesrportbVolt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoscMesrportbVolt_Type.__name__ = "Unsigned32"
_PmoscMesrportbVolt_Object = MibScalar
pmoscMesrportbVolt = _PmoscMesrportbVolt_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 3, 3, 25),
    _PmoscMesrportbVolt_Type()
)
pmoscMesrportbVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscMesrportbVolt.setStatus("current")


class _PmoscMesrportbTxBias_Type(Unsigned32):
    """Custom type pmoscMesrportbTxBias based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoscMesrportbTxBias_Type.__name__ = "Unsigned32"
_PmoscMesrportbTxBias_Object = MibScalar
pmoscMesrportbTxBias = _PmoscMesrportbTxBias_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 3, 3, 26),
    _PmoscMesrportbTxBias_Type()
)
pmoscMesrportbTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscMesrportbTxBias.setStatus("current")


class _PmoscMesrportbTxPower_Type(Unsigned32):
    """Custom type pmoscMesrportbTxPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoscMesrportbTxPower_Type.__name__ = "Unsigned32"
_PmoscMesrportbTxPower_Object = MibScalar
pmoscMesrportbTxPower = _PmoscMesrportbTxPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 3, 3, 27),
    _PmoscMesrportbTxPower_Type()
)
pmoscMesrportbTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscMesrportbTxPower.setStatus("current")


class _PmoscMesrportbRxPower_Type(Unsigned32):
    """Custom type pmoscMesrportbRxPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoscMesrportbRxPower_Type.__name__ = "Unsigned32"
_PmoscMesrportbRxPower_Object = MibScalar
pmoscMesrportbRxPower = _PmoscMesrportbRxPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 3, 3, 28),
    _PmoscMesrportbRxPower_Type()
)
pmoscMesrportbRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscMesrportbRxPower.setStatus("current")
_PmosccontrolsWrite_ObjectIdentity = ObjectIdentity
pmosccontrolsWrite = _PmosccontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6)
)
_PmoscCtrlOther_ObjectIdentity = ObjectIdentity
pmoscCtrlOther = _PmoscCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 1)
)
_PmoscCtrlsynth0_ObjectIdentity = ObjectIdentity
pmoscCtrlsynth0 = _PmoscCtrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 1, 0)
)
_PmoscCtrlConfLoad_Type = EkiOnOff
_PmoscCtrlConfLoad_Object = MibScalar
pmoscCtrlConfLoad = _PmoscCtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 1, 0, 1),
    _PmoscCtrlConfLoad_Type()
)
pmoscCtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCtrlConfLoad.setStatus("current")
_PmoscCtrlConfFlash_Type = EkiOnOff
_PmoscCtrlConfFlash_Object = MibScalar
pmoscCtrlConfFlash = _PmoscCtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 1, 0, 9),
    _PmoscCtrlConfFlash_Type()
)
pmoscCtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCtrlConfFlash.setStatus("current")
_PmoscCtrlConfClear_Type = EkiOnOff
_PmoscCtrlConfClear_Object = MibScalar
pmoscCtrlConfClear = _PmoscCtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 1, 0, 13),
    _PmoscCtrlConfClear_Type()
)
pmoscCtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCtrlConfClear.setStatus("current")
_PmoscCtrlsynth4_ObjectIdentity = ObjectIdentity
pmoscCtrlsynth4 = _PmoscCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 1, 4)
)
_PmoscCtrlCorrelatOn_Type = EkiOnOff
_PmoscCtrlCorrelatOn_Object = MibScalar
pmoscCtrlCorrelatOn = _PmoscCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 1, 4, 1),
    _PmoscCtrlCorrelatOn_Type()
)
pmoscCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCtrlCorrelatOn.setStatus("current")
_PmoscCtrlCorrelatOff_Type = EkiOnOff
_PmoscCtrlCorrelatOff_Object = MibScalar
pmoscCtrlCorrelatOff = _PmoscCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 1, 4, 2),
    _PmoscCtrlCorrelatOff_Type()
)
pmoscCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCtrlCorrelatOff.setStatus("current")
_PmoscCtrlswMgnt_ObjectIdentity = ObjectIdentity
pmoscCtrlswMgnt = _PmoscCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 1, 5)
)
_PmoscCtrlColdReset_Type = EkiOnOff
_PmoscCtrlColdReset_Object = MibScalar
pmoscCtrlColdReset = _PmoscCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 1, 5, 2),
    _PmoscCtrlColdReset_Type()
)
pmoscCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCtrlColdReset.setStatus("current")
_PmoscCtrlWarmReset_Type = EkiOnOff
_PmoscCtrlWarmReset_Object = MibScalar
pmoscCtrlWarmReset = _PmoscCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 1, 5, 3),
    _PmoscCtrlWarmReset_Type()
)
pmoscCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCtrlWarmReset.setStatus("current")
_PmoscCtrlledTest_ObjectIdentity = ObjectIdentity
pmoscCtrlledTest = _PmoscCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 1, 64)
)
_PmoscCtrlGreenLed_Type = EkiOnOff
_PmoscCtrlGreenLed_Object = MibScalar
pmoscCtrlGreenLed = _PmoscCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 1, 64, 1),
    _PmoscCtrlGreenLed_Type()
)
pmoscCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCtrlGreenLed.setStatus("current")
_PmoscCtrlRedLed_Type = EkiOnOff
_PmoscCtrlRedLed_Object = MibScalar
pmoscCtrlRedLed = _PmoscCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 1, 64, 2),
    _PmoscCtrlRedLed_Type()
)
pmoscCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCtrlRedLed.setStatus("current")
_PmoscCtrlLedOff_Type = EkiOnOff
_PmoscCtrlLedOff_Object = MibScalar
pmoscCtrlLedOff = _PmoscCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 1, 64, 3),
    _PmoscCtrlLedOff_Type()
)
pmoscCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCtrlLedOff.setStatus("current")
_PmoscCtrlmoduleOosMode_ObjectIdentity = ObjectIdentity
pmoscCtrlmoduleOosMode = _PmoscCtrlmoduleOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 1, 65)
)
_PmoscCtrlModuleOosMode_Type = EkiOnOff
_PmoscCtrlModuleOosMode_Object = MibScalar
pmoscCtrlModuleOosMode = _PmoscCtrlModuleOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 1, 65, 1),
    _PmoscCtrlModuleOosMode_Type()
)
pmoscCtrlModuleOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCtrlModuleOosMode.setStatus("current")
_PmoscCtrlClient_ObjectIdentity = ObjectIdentity
pmoscCtrlClient = _PmoscCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 2)
)
_PmoscCtrlportaSfpOnoff_ObjectIdentity = ObjectIdentity
pmoscCtrlportaSfpOnoff = _PmoscCtrlportaSfpOnoff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 2, 16)
)
_PmoscCtrlPortaSfpOnoff_Type = EkiOnOff
_PmoscCtrlPortaSfpOnoff_Object = MibScalar
pmoscCtrlPortaSfpOnoff = _PmoscCtrlPortaSfpOnoff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 2, 16, 1),
    _PmoscCtrlPortaSfpOnoff_Type()
)
pmoscCtrlPortaSfpOnoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCtrlPortaSfpOnoff.setStatus("current")
_PmoscCtrlportaOosMode_ObjectIdentity = ObjectIdentity
pmoscCtrlportaOosMode = _PmoscCtrlportaOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 2, 17)
)
_PmoscCtrlPortaOosMode_Type = EkiOnOff
_PmoscCtrlPortaOosMode_Object = MibScalar
pmoscCtrlPortaOosMode = _PmoscCtrlPortaOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 2, 17, 1),
    _PmoscCtrlPortaOosMode_Type()
)
pmoscCtrlPortaOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCtrlPortaOosMode.setStatus("current")
_PmoscCtrlLine_ObjectIdentity = ObjectIdentity
pmoscCtrlLine = _PmoscCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 3)
)
_PmoscCtrlportbSfpOnoff_ObjectIdentity = ObjectIdentity
pmoscCtrlportbSfpOnoff = _PmoscCtrlportbSfpOnoff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 3, 24)
)
_PmoscCtrlPortbSfpOnoff_Type = EkiOnOff
_PmoscCtrlPortbSfpOnoff_Object = MibScalar
pmoscCtrlPortbSfpOnoff = _PmoscCtrlPortbSfpOnoff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 3, 24, 1),
    _PmoscCtrlPortbSfpOnoff_Type()
)
pmoscCtrlPortbSfpOnoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCtrlPortbSfpOnoff.setStatus("current")
_PmoscCtrlportbOosMode_ObjectIdentity = ObjectIdentity
pmoscCtrlportbOosMode = _PmoscCtrlportbOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 3, 25)
)
_PmoscCtrlPortbOosMode_Type = EkiOnOff
_PmoscCtrlPortbOosMode_Object = MibScalar
pmoscCtrlPortbOosMode = _PmoscCtrlPortbOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 6, 3, 25, 1),
    _PmoscCtrlPortbOosMode_Type()
)
pmoscCtrlPortbOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCtrlPortbOosMode.setStatus("current")
_Pmoscri_ObjectIdentity = ObjectIdentity
pmoscri = _Pmoscri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 7)
)
_PmoscRinvReloadInventory_Type = EkiOnOff
_PmoscRinvReloadInventory_Object = MibScalar
pmoscRinvReloadInventory = _PmoscRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 7, 2),
    _PmoscRinvReloadInventory_Type()
)
pmoscRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscRinvReloadInventory.setStatus("current")
_PmoscRinvHwPlatform_Type = DisplayString
_PmoscRinvHwPlatform_Object = MibScalar
pmoscRinvHwPlatform = _PmoscRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 7, 4),
    _PmoscRinvHwPlatform_Type()
)
pmoscRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscRinvHwPlatform.setStatus("current")
_PmoscRinvSwPlatform_Type = DisplayString
_PmoscRinvSwPlatform_Object = MibScalar
pmoscRinvSwPlatform = _PmoscRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 7, 5),
    _PmoscRinvSwPlatform_Type()
)
pmoscRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscRinvSwPlatform.setStatus("current")
_PmoscRinvPortASFP_Type = DisplayString
_PmoscRinvPortASFP_Object = MibScalar
pmoscRinvPortASFP = _PmoscRinvPortASFP_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 7, 6),
    _PmoscRinvPortASFP_Type()
)
pmoscRinvPortASFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscRinvPortASFP.setStatus("current")
_PmoscRinvPortBSFP_Type = DisplayString
_PmoscRinvPortBSFP_Object = MibScalar
pmoscRinvPortBSFP = _PmoscRinvPortBSFP_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 7, 7),
    _PmoscRinvPortBSFP_Type()
)
pmoscRinvPortBSFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscRinvPortBSFP.setStatus("current")
_PmoscConfig_ObjectIdentity = ObjectIdentity
pmoscConfig = _PmoscConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 9)
)
_PmoscCfgLsd_ObjectIdentity = ObjectIdentity
pmoscCfgLsd = _PmoscCfgLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 9, 1)
)
_PmoscCfgStartUp_ObjectIdentity = ObjectIdentity
pmoscCfgStartUp = _PmoscCfgStartUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 9, 2)
)
_PmosctableclientStartup_ObjectIdentity = ObjectIdentity
pmosctableclientStartup = _PmosctableclientStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 9, 2, 1)
)


class _PmoscCfgportaSfpCtrl_Type(Unsigned32):
    """Custom type pmoscCfgportaSfpCtrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoscCfgportaSfpCtrl_Type.__name__ = "Unsigned32"
_PmoscCfgportaSfpCtrl_Object = MibScalar
pmoscCfgportaSfpCtrl = _PmoscCfgportaSfpCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 9, 2, 1, 2),
    _PmoscCfgportaSfpCtrl_Type()
)
pmoscCfgportaSfpCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCfgportaSfpCtrl.setStatus("current")


class _PmoscCfgportaOosMode_Type(Unsigned32):
    """Custom type pmoscCfgportaOosMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoscCfgportaOosMode_Type.__name__ = "Unsigned32"
_PmoscCfgportaOosMode_Object = MibScalar
pmoscCfgportaOosMode = _PmoscCfgportaOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 9, 2, 1, 3),
    _PmoscCfgportaOosMode_Type()
)
pmoscCfgportaOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCfgportaOosMode.setStatus("current")
_PmosctablelineStartup_ObjectIdentity = ObjectIdentity
pmosctablelineStartup = _PmosctablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 9, 2, 2)
)


class _PmoscCfgportbSfpCtrl_Type(Unsigned32):
    """Custom type pmoscCfgportbSfpCtrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoscCfgportbSfpCtrl_Type.__name__ = "Unsigned32"
_PmoscCfgportbSfpCtrl_Object = MibScalar
pmoscCfgportbSfpCtrl = _PmoscCfgportbSfpCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 9, 2, 2, 2),
    _PmoscCfgportbSfpCtrl_Type()
)
pmoscCfgportbSfpCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCfgportbSfpCtrl.setStatus("current")


class _PmoscCfgportbOosMode_Type(Unsigned32):
    """Custom type pmoscCfgportbOosMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoscCfgportbOosMode_Type.__name__ = "Unsigned32"
_PmoscCfgportbOosMode_Object = MibScalar
pmoscCfgportbOosMode = _PmoscCfgportbOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 9, 2, 2, 3),
    _PmoscCfgportbOosMode_Type()
)
pmoscCfgportbOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCfgportbOosMode.setStatus("current")
_PmoscCfgLabels_ObjectIdentity = ObjectIdentity
pmoscCfgLabels = _PmoscCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 9, 3)
)
_PmoscCfgLabelclientTable_Object = MibTable
pmoscCfgLabelclientTable = _PmoscCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pmoscCfgLabelclientTable.setStatus("current")
_PmoscCfgLabelclientEntry_Object = MibTableRow
pmoscCfgLabelclientEntry = _PmoscCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 9, 3, 1, 1)
)
pmoscCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-PmOSC-MIB", "pmoscCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmoscCfgLabelclientEntry.setStatus("current")


class _PmoscCfgLabelclientIndex_Type(Integer32):
    """Custom type pmoscCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoscCfgLabelclientIndex_Type.__name__ = "Integer32"
_PmoscCfgLabelclientIndex_Object = MibTableColumn
pmoscCfgLabelclientIndex = _PmoscCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 9, 3, 1, 1, 1),
    _PmoscCfgLabelclientIndex_Type()
)
pmoscCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscCfgLabelclientIndex.setStatus("current")


class _PmoscCfgLabelclientPortn_Type(DisplayString):
    """Custom type pmoscCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmoscCfgLabelclientPortn_Type.__name__ = "DisplayString"
_PmoscCfgLabelclientPortn_Object = MibTableColumn
pmoscCfgLabelclientPortn = _PmoscCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 9, 3, 1, 1, 3),
    _PmoscCfgLabelclientPortn_Type()
)
pmoscCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCfgLabelclientPortn.setStatus("current")
_PmoscCfgLabellineTable_Object = MibTable
pmoscCfgLabellineTable = _PmoscCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pmoscCfgLabellineTable.setStatus("current")
_PmoscCfgLabellineEntry_Object = MibTableRow
pmoscCfgLabellineEntry = _PmoscCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 9, 3, 2, 1)
)
pmoscCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-PmOSC-MIB", "pmoscCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmoscCfgLabellineEntry.setStatus("current")


class _PmoscCfgLabellineIndex_Type(Integer32):
    """Custom type pmoscCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoscCfgLabellineIndex_Type.__name__ = "Integer32"
_PmoscCfgLabellineIndex_Object = MibTableColumn
pmoscCfgLabellineIndex = _PmoscCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 9, 3, 2, 1, 1),
    _PmoscCfgLabellineIndex_Type()
)
pmoscCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoscCfgLabellineIndex.setStatus("current")


class _PmoscCfgLabellinePortn_Type(DisplayString):
    """Custom type pmoscCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmoscCfgLabellinePortn_Type.__name__ = "DisplayString"
_PmoscCfgLabellinePortn_Object = MibTableColumn
pmoscCfgLabellinePortn = _PmoscCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 9, 3, 2, 1, 3),
    _PmoscCfgLabellinePortn_Type()
)
pmoscCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCfgLabellinePortn.setStatus("current")
_PmoscCfgWriteConfiguration_Type = EkiOnOff
_PmoscCfgWriteConfiguration_Object = MibScalar
pmoscCfgWriteConfiguration = _PmoscCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 9, 257),
    _PmoscCfgWriteConfiguration_Type()
)
pmoscCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoscCfgWriteConfiguration.setStatus("current")
_Pmosctraps_ObjectIdentity = ObjectIdentity
pmosctraps = _Pmosctraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 14, 10)
)


class _PmosctrapBoardNumber_Type(Integer32):
    """Custom type pmosctrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PmosctrapBoardNumber_Type.__name__ = "Integer32"
_PmosctrapBoardNumber_Object = MibScalar
pmosctrapBoardNumber = _PmosctrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 14, 10, 4),
    _PmosctrapBoardNumber_Type()
)
pmosctrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmosctrapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pmoscPortaTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 14, 10, 30)
)
pmoscPortaTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOSC-MIB", "pmoscAlmPortaDdmWarning"),
        ("EKINOPS-PmOSC-MIB", "pmosctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoscPortaTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmoscPortaTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 14, 10, 31)
)
pmoscPortaTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOSC-MIB", "pmoscAlmPortaDdmWarning"),
        ("EKINOPS-PmOSC-MIB", "pmosctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoscPortaTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmoscPortaTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 14, 10, 32)
)
pmoscPortaTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOSC-MIB", "pmoscAlmPortaDdmAlm"),
        ("EKINOPS-PmOSC-MIB", "pmosctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoscPortaTrapUrgentGoesOn.setStatus(
        "current"
    )

pmoscPortaTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 14, 10, 33)
)
pmoscPortaTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOSC-MIB", "pmoscAlmPortaDdmAlm"),
        ("EKINOPS-PmOSC-MIB", "pmosctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoscPortaTrapUrgentGoesOff.setStatus(
        "current"
    )

pmoscPortaTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 14, 10, 34)
)
pmoscPortaTrapCritGoesOn.setObjects(
      *(("EKINOPS-PmOSC-MIB", "pmoscAlmPortaFail"),
        ("EKINOPS-PmOSC-MIB", "pmoscAlmPortaHwFail"),
        ("EKINOPS-PmOSC-MIB", "pmosctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoscPortaTrapCritGoesOn.setStatus(
        "current"
    )

pmoscPortaTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 14, 10, 35)
)
pmoscPortaTrapCritGoesOff.setObjects(
      *(("EKINOPS-PmOSC-MIB", "pmoscAlmPortaFail"),
        ("EKINOPS-PmOSC-MIB", "pmoscAlmPortaHwFail"),
        ("EKINOPS-PmOSC-MIB", "pmosctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoscPortaTrapCritGoesOff.setStatus(
        "current"
    )

pmoscPortbNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 14, 10, 40)
)
pmoscPortbNotUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOSC-MIB", "pmoscAlmPortbDdmWarning"),
        ("EKINOPS-PmOSC-MIB", "pmosctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoscPortbNotUrgentGoesOn.setStatus(
        "current"
    )

pmoscPortbNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 14, 10, 41)
)
pmoscPortbNotUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOSC-MIB", "pmoscAlmPortbDdmWarning"),
        ("EKINOPS-PmOSC-MIB", "pmosctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoscPortbNotUrgentGoesOff.setStatus(
        "current"
    )

pmoscPortbUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 14, 10, 42)
)
pmoscPortbUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOSC-MIB", "pmoscAlmPortbDdmAlm"),
        ("EKINOPS-PmOSC-MIB", "pmosctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoscPortbUrgentGoesOn.setStatus(
        "current"
    )

pmoscPortbUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 14, 10, 43)
)
pmoscPortbUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOSC-MIB", "pmoscAlmPortbDdmAlm"),
        ("EKINOPS-PmOSC-MIB", "pmosctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoscPortbUrgentGoesOff.setStatus(
        "current"
    )

pmoscPortbCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 14, 10, 44)
)
pmoscPortbCritGoesOn.setObjects(
      *(("EKINOPS-PmOSC-MIB", "pmoscAlmPortbFail"),
        ("EKINOPS-PmOSC-MIB", "pmoscAlmPortbHwFail"),
        ("EKINOPS-PmOSC-MIB", "pmosctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoscPortbCritGoesOn.setStatus(
        "current"
    )

pmoscPortbCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 14, 10, 45)
)
pmoscPortbCritGoesOff.setObjects(
      *(("EKINOPS-PmOSC-MIB", "pmoscAlmPortbFail"),
        ("EKINOPS-PmOSC-MIB", "pmoscAlmPortbHwFail"),
        ("EKINOPS-PmOSC-MIB", "pmosctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoscPortbCritGoesOff.setStatus(
        "current"
    )

pmoscPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 14, 10, 50)
)
pmoscPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOSC-MIB", "pmoscAlmDefFuseB"),
        ("EKINOPS-PmOSC-MIB", "pmoscAlmDefFuseA"),
        ("EKINOPS-PmOSC-MIB", "pmosctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoscPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmoscPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 14, 10, 51)
)
pmoscPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOSC-MIB", "pmoscAlmDefFuseB"),
        ("EKINOPS-PmOSC-MIB", "pmoscAlmDefFuseA"),
        ("EKINOPS-PmOSC-MIB", "pmosctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoscPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-PmOSC-MIB",
    **{"modulePmOSC": modulePmOSC,
       "pmoscalarms": pmoscalarms,
       "pmoscAlmOther": pmoscAlmOther,
       "pmoscAlmOtherNurg": pmoscAlmOtherNurg,
       "pmoscAlmOtherUrg": pmoscAlmOtherUrg,
       "pmoscAlmOtherCrit": pmoscAlmOtherCrit,
       "pmoscAlmsynthAlm0": pmoscAlmsynthAlm0,
       "pmoscAlmModuleGlobFailure": pmoscAlmModuleGlobFailure,
       "pmoscAlmDefFuseA": pmoscAlmDefFuseA,
       "pmoscAlmDefFuseB": pmoscAlmDefFuseB,
       "pmoscAlmClient": pmoscAlmClient,
       "pmoscAlmClientNurg": pmoscAlmClientNurg,
       "pmoscAlmportaSfpWarnDdm": pmoscAlmportaSfpWarnDdm,
       "pmoscAlmPortaTxPwLowWng": pmoscAlmPortaTxPwLowWng,
       "pmoscAlmPortaTxPwrHighWng": pmoscAlmPortaTxPwrHighWng,
       "pmoscAlmPortaTxBiasLowWng": pmoscAlmPortaTxBiasLowWng,
       "pmoscAlmPortaTxBiasHighWng": pmoscAlmPortaTxBiasHighWng,
       "pmoscAlmPortaTempLowWng": pmoscAlmPortaTempLowWng,
       "pmoscAlmPortaTempHighWng": pmoscAlmPortaTempHighWng,
       "pmoscAlmPortaRxPwrLowWng": pmoscAlmPortaRxPwrLowWng,
       "pmoscAlmPortaRxPwrHighWng": pmoscAlmPortaRxPwrHighWng,
       "pmoscAlmClientUrg": pmoscAlmClientUrg,
       "pmoscAlmportaSfpAlmDdm": pmoscAlmportaSfpAlmDdm,
       "pmoscAlmPortaTxPwrLowAla": pmoscAlmPortaTxPwrLowAla,
       "pmoscAlmPortaTxPwrHighAla": pmoscAlmPortaTxPwrHighAla,
       "pmoscAlmPortaTxBiasLowAla": pmoscAlmPortaTxBiasLowAla,
       "pmoscAlmPortaTxBiasHighAla": pmoscAlmPortaTxBiasHighAla,
       "pmoscAlmPortaTempLowAla": pmoscAlmPortaTempLowAla,
       "pmoscAlmPortaTempHighAla": pmoscAlmPortaTempHighAla,
       "pmoscAlmPortaRxPwrLowAla": pmoscAlmPortaRxPwrLowAla,
       "pmoscAlmPortaRxPwrHighAla": pmoscAlmPortaRxPwrHighAla,
       "pmoscAlmClientCrit": pmoscAlmClientCrit,
       "pmoscAlmsynthAlm8": pmoscAlmsynthAlm8,
       "pmoscAlmPortaSfpAbsent": pmoscAlmPortaSfpAbsent,
       "pmoscAlmPortaDdmAbsent": pmoscAlmPortaDdmAbsent,
       "pmoscAlmPortaHwFail": pmoscAlmPortaHwFail,
       "pmoscAlmPortaLsd": pmoscAlmPortaLsd,
       "pmoscAlmPortaLocalOos": pmoscAlmPortaLocalOos,
       "pmoscAlmPortaDdmWarning": pmoscAlmPortaDdmWarning,
       "pmoscAlmPortaDdmAlm": pmoscAlmPortaDdmAlm,
       "pmoscAlmPortaFail": pmoscAlmPortaFail,
       "pmoscAlmportaAccessioAlm": pmoscAlmportaAccessioAlm,
       "pmoscAlmPortaLasFail": pmoscAlmPortaLasFail,
       "pmoscAlmPortaLos": pmoscAlmPortaLos,
       "pmoscAlmLine": pmoscAlmLine,
       "pmoscAlmLineNurg": pmoscAlmLineNurg,
       "pmoscAlmportbSfpWarnDdm": pmoscAlmportbSfpWarnDdm,
       "pmoscAlmPortbTxPwLowWng": pmoscAlmPortbTxPwLowWng,
       "pmoscAlmPortbTxPwrHighWng": pmoscAlmPortbTxPwrHighWng,
       "pmoscAlmPortbTxBiasLowWng": pmoscAlmPortbTxBiasLowWng,
       "pmoscAlmPortbTxBiasHighWng": pmoscAlmPortbTxBiasHighWng,
       "pmoscAlmPortbTempLowWng": pmoscAlmPortbTempLowWng,
       "pmoscAlmPortbTempHighWng": pmoscAlmPortbTempHighWng,
       "pmoscAlmPortbRxPwrLowWng": pmoscAlmPortbRxPwrLowWng,
       "pmoscAlmPortbRxPwrHighWng": pmoscAlmPortbRxPwrHighWng,
       "pmoscAlmLineUrg": pmoscAlmLineUrg,
       "pmoscAlmportbSfpAlmDdm": pmoscAlmportbSfpAlmDdm,
       "pmoscAlmPortbTxPwrLowAla": pmoscAlmPortbTxPwrLowAla,
       "pmoscAlmPortbTxPwrHighAla": pmoscAlmPortbTxPwrHighAla,
       "pmoscAlmPortbTxBiasLowAla": pmoscAlmPortbTxBiasLowAla,
       "pmoscAlmPortbTxBiasHighAla": pmoscAlmPortbTxBiasHighAla,
       "pmoscAlmPortbTempLowAla": pmoscAlmPortbTempLowAla,
       "pmoscAlmPortbTempHighAla": pmoscAlmPortbTempHighAla,
       "pmoscAlmPortbRxPwrLowAla": pmoscAlmPortbRxPwrLowAla,
       "pmoscAlmPortbRxPwrHighAla": pmoscAlmPortbRxPwrHighAla,
       "pmoscAlmLineCrit": pmoscAlmLineCrit,
       "pmoscAlmsynthAlm7": pmoscAlmsynthAlm7,
       "pmoscAlmPortbSfpAbsent": pmoscAlmPortbSfpAbsent,
       "pmoscAlmPortbDdmAbsent": pmoscAlmPortbDdmAbsent,
       "pmoscAlmPortbHwFail": pmoscAlmPortbHwFail,
       "pmoscAlmPortbLsd": pmoscAlmPortbLsd,
       "pmoscAlmPortbLocalOos": pmoscAlmPortbLocalOos,
       "pmoscAlmPortbDdmWarning": pmoscAlmPortbDdmWarning,
       "pmoscAlmPortbDdmAlm": pmoscAlmPortbDdmAlm,
       "pmoscAlmPortbFail": pmoscAlmPortbFail,
       "pmoscAlmportbAccessioAlm": pmoscAlmportbAccessioAlm,
       "pmoscAlmPortbLasFail": pmoscAlmPortbLasFail,
       "pmoscAlmPortbLos": pmoscAlmPortbLos,
       "pmoscmeasures": pmoscmeasures,
       "pmoscMesrOther": pmoscMesrOther,
       "pmoscMesrClient": pmoscMesrClient,
       "pmoscMesrportaTemperature": pmoscMesrportaTemperature,
       "pmoscMesrportaVolt": pmoscMesrportaVolt,
       "pmoscMesrportaTxBias": pmoscMesrportaTxBias,
       "pmoscMesrportaTxPower": pmoscMesrportaTxPower,
       "pmoscMesrportaRxPower": pmoscMesrportaRxPower,
       "pmoscMesrLine": pmoscMesrLine,
       "pmoscMesrportbTemperature": pmoscMesrportbTemperature,
       "pmoscMesrportbVolt": pmoscMesrportbVolt,
       "pmoscMesrportbTxBias": pmoscMesrportbTxBias,
       "pmoscMesrportbTxPower": pmoscMesrportbTxPower,
       "pmoscMesrportbRxPower": pmoscMesrportbRxPower,
       "pmosccontrolsWrite": pmosccontrolsWrite,
       "pmoscCtrlOther": pmoscCtrlOther,
       "pmoscCtrlsynth0": pmoscCtrlsynth0,
       "pmoscCtrlConfLoad": pmoscCtrlConfLoad,
       "pmoscCtrlConfFlash": pmoscCtrlConfFlash,
       "pmoscCtrlConfClear": pmoscCtrlConfClear,
       "pmoscCtrlsynth4": pmoscCtrlsynth4,
       "pmoscCtrlCorrelatOn": pmoscCtrlCorrelatOn,
       "pmoscCtrlCorrelatOff": pmoscCtrlCorrelatOff,
       "pmoscCtrlswMgnt": pmoscCtrlswMgnt,
       "pmoscCtrlColdReset": pmoscCtrlColdReset,
       "pmoscCtrlWarmReset": pmoscCtrlWarmReset,
       "pmoscCtrlledTest": pmoscCtrlledTest,
       "pmoscCtrlGreenLed": pmoscCtrlGreenLed,
       "pmoscCtrlRedLed": pmoscCtrlRedLed,
       "pmoscCtrlLedOff": pmoscCtrlLedOff,
       "pmoscCtrlmoduleOosMode": pmoscCtrlmoduleOosMode,
       "pmoscCtrlModuleOosMode": pmoscCtrlModuleOosMode,
       "pmoscCtrlClient": pmoscCtrlClient,
       "pmoscCtrlportaSfpOnoff": pmoscCtrlportaSfpOnoff,
       "pmoscCtrlPortaSfpOnoff": pmoscCtrlPortaSfpOnoff,
       "pmoscCtrlportaOosMode": pmoscCtrlportaOosMode,
       "pmoscCtrlPortaOosMode": pmoscCtrlPortaOosMode,
       "pmoscCtrlLine": pmoscCtrlLine,
       "pmoscCtrlportbSfpOnoff": pmoscCtrlportbSfpOnoff,
       "pmoscCtrlPortbSfpOnoff": pmoscCtrlPortbSfpOnoff,
       "pmoscCtrlportbOosMode": pmoscCtrlportbOosMode,
       "pmoscCtrlPortbOosMode": pmoscCtrlPortbOosMode,
       "pmoscri": pmoscri,
       "pmoscRinvReloadInventory": pmoscRinvReloadInventory,
       "pmoscRinvHwPlatform": pmoscRinvHwPlatform,
       "pmoscRinvSwPlatform": pmoscRinvSwPlatform,
       "pmoscRinvPortASFP": pmoscRinvPortASFP,
       "pmoscRinvPortBSFP": pmoscRinvPortBSFP,
       "pmoscConfig": pmoscConfig,
       "pmoscCfgLsd": pmoscCfgLsd,
       "pmoscCfgStartUp": pmoscCfgStartUp,
       "pmosctableclientStartup": pmosctableclientStartup,
       "pmoscCfgportaSfpCtrl": pmoscCfgportaSfpCtrl,
       "pmoscCfgportaOosMode": pmoscCfgportaOosMode,
       "pmosctablelineStartup": pmosctablelineStartup,
       "pmoscCfgportbSfpCtrl": pmoscCfgportbSfpCtrl,
       "pmoscCfgportbOosMode": pmoscCfgportbOosMode,
       "pmoscCfgLabels": pmoscCfgLabels,
       "pmoscCfgLabelclientTable": pmoscCfgLabelclientTable,
       "pmoscCfgLabelclientEntry": pmoscCfgLabelclientEntry,
       "pmoscCfgLabelclientIndex": pmoscCfgLabelclientIndex,
       "pmoscCfgLabelclientPortn": pmoscCfgLabelclientPortn,
       "pmoscCfgLabellineTable": pmoscCfgLabellineTable,
       "pmoscCfgLabellineEntry": pmoscCfgLabellineEntry,
       "pmoscCfgLabellineIndex": pmoscCfgLabellineIndex,
       "pmoscCfgLabellinePortn": pmoscCfgLabellinePortn,
       "pmoscCfgWriteConfiguration": pmoscCfgWriteConfiguration,
       "pmosctraps": pmosctraps,
       "pmosctrapBoardNumber": pmosctrapBoardNumber,
       "pmoscPortaTrapNotUrgentGoesOn": pmoscPortaTrapNotUrgentGoesOn,
       "pmoscPortaTrapNotUrgentGoesOff": pmoscPortaTrapNotUrgentGoesOff,
       "pmoscPortaTrapUrgentGoesOn": pmoscPortaTrapUrgentGoesOn,
       "pmoscPortaTrapUrgentGoesOff": pmoscPortaTrapUrgentGoesOff,
       "pmoscPortaTrapCritGoesOn": pmoscPortaTrapCritGoesOn,
       "pmoscPortaTrapCritGoesOff": pmoscPortaTrapCritGoesOff,
       "pmoscPortbNotUrgentGoesOn": pmoscPortbNotUrgentGoesOn,
       "pmoscPortbNotUrgentGoesOff": pmoscPortbNotUrgentGoesOff,
       "pmoscPortbUrgentGoesOn": pmoscPortbUrgentGoesOn,
       "pmoscPortbUrgentGoesOff": pmoscPortbUrgentGoesOff,
       "pmoscPortbCritGoesOn": pmoscPortbCritGoesOn,
       "pmoscPortbCritGoesOff": pmoscPortbCritGoesOff,
       "pmoscPowerTrapUrgentGoesOn": pmoscPowerTrapUrgentGoesOn,
       "pmoscPowerTrapUrgentGoesOff": pmoscPowerTrapUrgentGoesOff}
)
