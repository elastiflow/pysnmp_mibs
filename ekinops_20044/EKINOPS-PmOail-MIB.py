# SNMP MIB module (EKINOPS-PmOail-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-PmOail-MIB.mib
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

modulepmoail = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36)
)
if mibBuilder.loadTexts:
    modulepmoail.setRevisions(
        ("2009-03-23 00:00",
         "2009-04-08 00:00",
         "2009-09-24 00:00",
         "2009-12-14 00:00",
         "2010-02-24 00:00",
         "2010-07-15 00:00",
         "2010-10-29 00:00",
         "2010-11-03 00:00",
         "2012-07-04 00:00",
         "2012-10-05 00:00",
         "2014-03-26 00:00",
         "2014-12-10 00:00",
         "2016-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PmoailpreampMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oapreampdefaultmode", 0),
          ("oapreampconstantcurrentmode", 1),
          ("oapreampconstantpowermode", 2))
    )



class PmoailboosterMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oaboosterdefaultmode", 0),
          ("oaboosterconstantcurrentmode", 1),
          ("oaboosterconstantpowermode", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Pmoailalarms_ObjectIdentity = ObjectIdentity
pmoailalarms = _Pmoailalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2)
)
_PmoailAlmOther_ObjectIdentity = ObjectIdentity
pmoailAlmOther = _PmoailAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1)
)
_PmoailAlmOtherNurg_ObjectIdentity = ObjectIdentity
pmoailAlmOtherNurg = _PmoailAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 1)
)
_PmoailAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pmoailAlmsynthAlm2 = _PmoailAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 1, 2)
)
_PmoailAlmConfTableSave_Type = EkiOnOff
_PmoailAlmConfTableSave_Object = MibScalar
pmoailAlmConfTableSave = _PmoailAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 1, 2, 1),
    _PmoailAlmConfTableSave_Type()
)
pmoailAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmConfTableSave.setStatus("current")
_PmoailAlmInvUpload_Type = EkiOnOff
_PmoailAlmInvUpload_Object = MibScalar
pmoailAlmInvUpload = _PmoailAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 1, 2, 2),
    _PmoailAlmInvUpload_Type()
)
pmoailAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmInvUpload.setStatus("current")
_PmoailAlmConfTableLoad_Type = EkiOnOff
_PmoailAlmConfTableLoad_Object = MibScalar
pmoailAlmConfTableLoad = _PmoailAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 1, 2, 3),
    _PmoailAlmConfTableLoad_Type()
)
pmoailAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmConfTableLoad.setStatus("current")
_PmoailAlmfoaWarnings_ObjectIdentity = ObjectIdentity
pmoailAlmfoaWarnings = _PmoailAlmfoaWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 1, 75)
)
_PmoailAlm3v3LowWarning_Type = EkiOnOff
_PmoailAlm3v3LowWarning_Object = MibScalar
pmoailAlm3v3LowWarning = _PmoailAlm3v3LowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 1, 75, 5),
    _PmoailAlm3v3LowWarning_Type()
)
pmoailAlm3v3LowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlm3v3LowWarning.setStatus("current")
_PmoailAlm3v3HighWarning_Type = EkiOnOff
_PmoailAlm3v3HighWarning_Object = MibScalar
pmoailAlm3v3HighWarning = _PmoailAlm3v3HighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 1, 75, 6),
    _PmoailAlm3v3HighWarning_Type()
)
pmoailAlm3v3HighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlm3v3HighWarning.setStatus("current")
_PmoailAlmTermpLowWarning_Type = EkiOnOff
_PmoailAlmTermpLowWarning_Object = MibScalar
pmoailAlmTermpLowWarning = _PmoailAlmTermpLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 1, 75, 7),
    _PmoailAlmTermpLowWarning_Type()
)
pmoailAlmTermpLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmTermpLowWarning.setStatus("current")
_PmoailAlmTempHighWarning_Type = EkiOnOff
_PmoailAlmTempHighWarning_Object = MibScalar
pmoailAlmTempHighWarning = _PmoailAlmTempHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 1, 75, 8),
    _PmoailAlmTempHighWarning_Type()
)
pmoailAlmTempHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmTempHighWarning.setStatus("current")
_PmoailAlmOtherUrg_ObjectIdentity = ObjectIdentity
pmoailAlmOtherUrg = _PmoailAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 2)
)
_PmoailAlmfoaAlarms_ObjectIdentity = ObjectIdentity
pmoailAlmfoaAlarms = _PmoailAlmfoaAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 2, 74)
)
_PmoailAlm3v3LowAlarm_Type = EkiOnOff
_PmoailAlm3v3LowAlarm_Object = MibScalar
pmoailAlm3v3LowAlarm = _PmoailAlm3v3LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 2, 74, 5),
    _PmoailAlm3v3LowAlarm_Type()
)
pmoailAlm3v3LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlm3v3LowAlarm.setStatus("current")
_PmoailAlm3v3HighAlarm_Type = EkiOnOff
_PmoailAlm3v3HighAlarm_Object = MibScalar
pmoailAlm3v3HighAlarm = _PmoailAlm3v3HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 2, 74, 6),
    _PmoailAlm3v3HighAlarm_Type()
)
pmoailAlm3v3HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlm3v3HighAlarm.setStatus("current")
_PmoailAlmTermpLowAlarm_Type = EkiOnOff
_PmoailAlmTermpLowAlarm_Object = MibScalar
pmoailAlmTermpLowAlarm = _PmoailAlmTermpLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 2, 74, 7),
    _PmoailAlmTermpLowAlarm_Type()
)
pmoailAlmTermpLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmTermpLowAlarm.setStatus("current")
_PmoailAlmTempHighAlarm_Type = EkiOnOff
_PmoailAlmTempHighAlarm_Object = MibScalar
pmoailAlmTempHighAlarm = _PmoailAlmTempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 2, 74, 8),
    _PmoailAlmTempHighAlarm_Type()
)
pmoailAlmTempHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmTempHighAlarm.setStatus("current")
_PmoailAlmOtherCrit_ObjectIdentity = ObjectIdentity
pmoailAlmOtherCrit = _PmoailAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 3)
)
_PmoailAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmoailAlmsynthAlm0 = _PmoailAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 3, 0)
)
_PmoailAlmMaintenanceMode_Type = EkiOnOff
_PmoailAlmMaintenanceMode_Object = MibScalar
pmoailAlmMaintenanceMode = _PmoailAlmMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 3, 0, 1),
    _PmoailAlmMaintenanceMode_Type()
)
pmoailAlmMaintenanceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmMaintenanceMode.setStatus("current")
_PmoailAlmModGlobFail_Type = EkiOnOff
_PmoailAlmModGlobFail_Object = MibScalar
pmoailAlmModGlobFail = _PmoailAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 3, 0, 9),
    _PmoailAlmModGlobFail_Type()
)
pmoailAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmModGlobFail.setStatus("current")
_PmoailAlmUpEdfaInitNotCompl_Type = EkiOnOff
_PmoailAlmUpEdfaInitNotCompl_Object = MibScalar
pmoailAlmUpEdfaInitNotCompl = _PmoailAlmUpEdfaInitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 3, 0, 10),
    _PmoailAlmUpEdfaInitNotCompl_Type()
)
pmoailAlmUpEdfaInitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmUpEdfaInitNotCompl.setStatus("current")
_PmoailAlmDwEdfaInitNotCompl_Type = EkiOnOff
_PmoailAlmDwEdfaInitNotCompl_Object = MibScalar
pmoailAlmDwEdfaInitNotCompl = _PmoailAlmDwEdfaInitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 3, 0, 11),
    _PmoailAlmDwEdfaInitNotCompl_Type()
)
pmoailAlmDwEdfaInitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmDwEdfaInitNotCompl.setStatus("current")
_PmoailAlmExtPumpNotLocked_Type = EkiOnOff
_PmoailAlmExtPumpNotLocked_Object = MibScalar
pmoailAlmExtPumpNotLocked = _PmoailAlmExtPumpNotLocked_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 3, 0, 12),
    _PmoailAlmExtPumpNotLocked_Type()
)
pmoailAlmExtPumpNotLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmExtPumpNotLocked.setStatus("current")
_PmoailAlmDefFuseA_Type = EkiOnOff
_PmoailAlmDefFuseA_Object = MibScalar
pmoailAlmDefFuseA = _PmoailAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 3, 0, 15),
    _PmoailAlmDefFuseA_Type()
)
pmoailAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmDefFuseA.setStatus("current")
_PmoailAlmDefFuseB_Type = EkiOnOff
_PmoailAlmDefFuseB_Object = MibScalar
pmoailAlmDefFuseB = _PmoailAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 1, 3, 0, 16),
    _PmoailAlmDefFuseB_Type()
)
pmoailAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmDefFuseB.setStatus("current")
_PmoailAlmClient_ObjectIdentity = ObjectIdentity
pmoailAlmClient = _PmoailAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2)
)
_PmoailAlmClientNurg_ObjectIdentity = ObjectIdentity
pmoailAlmClientNurg = _PmoailAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 1)
)
_PmoailAlmclientEdfaWarnings_ObjectIdentity = ObjectIdentity
pmoailAlmclientEdfaWarnings = _PmoailAlmclientEdfaWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 1, 33)
)
_PmoailAlmClientGainLowWarning_Type = EkiOnOff
_PmoailAlmClientGainLowWarning_Object = MibScalar
pmoailAlmClientGainLowWarning = _PmoailAlmClientGainLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 1, 33, 1),
    _PmoailAlmClientGainLowWarning_Type()
)
pmoailAlmClientGainLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientGainLowWarning.setStatus("current")
_PmoailAlmClientGainHighWarning_Type = EkiOnOff
_PmoailAlmClientGainHighWarning_Object = MibScalar
pmoailAlmClientGainHighWarning = _PmoailAlmClientGainHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 1, 33, 2),
    _PmoailAlmClientGainHighWarning_Type()
)
pmoailAlmClientGainHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientGainHighWarning.setStatus("current")
_PmoailAlmClientInputPwrLowWarning_Type = EkiOnOff
_PmoailAlmClientInputPwrLowWarning_Object = MibScalar
pmoailAlmClientInputPwrLowWarning = _PmoailAlmClientInputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 1, 33, 3),
    _PmoailAlmClientInputPwrLowWarning_Type()
)
pmoailAlmClientInputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientInputPwrLowWarning.setStatus("current")
_PmoailAlmClientInputPwrHighWarning_Type = EkiOnOff
_PmoailAlmClientInputPwrHighWarning_Object = MibScalar
pmoailAlmClientInputPwrHighWarning = _PmoailAlmClientInputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 1, 33, 4),
    _PmoailAlmClientInputPwrHighWarning_Type()
)
pmoailAlmClientInputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientInputPwrHighWarning.setStatus("current")
_PmoailAlmClientOutputPwrLowWarning_Type = EkiOnOff
_PmoailAlmClientOutputPwrLowWarning_Object = MibScalar
pmoailAlmClientOutputPwrLowWarning = _PmoailAlmClientOutputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 1, 33, 5),
    _PmoailAlmClientOutputPwrLowWarning_Type()
)
pmoailAlmClientOutputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientOutputPwrLowWarning.setStatus("current")
_PmoailAlmClientOutputPwrHighWarning_Type = EkiOnOff
_PmoailAlmClientOutputPwrHighWarning_Object = MibScalar
pmoailAlmClientOutputPwrHighWarning = _PmoailAlmClientOutputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 1, 33, 6),
    _PmoailAlmClientOutputPwrHighWarning_Type()
)
pmoailAlmClientOutputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientOutputPwrHighWarning.setStatus("current")
_PmoailAlmClientBiasLowWarning_Type = EkiOnOff
_PmoailAlmClientBiasLowWarning_Object = MibScalar
pmoailAlmClientBiasLowWarning = _PmoailAlmClientBiasLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 1, 33, 7),
    _PmoailAlmClientBiasLowWarning_Type()
)
pmoailAlmClientBiasLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientBiasLowWarning.setStatus("current")
_PmoailAlmClientBiasHighWarning_Type = EkiOnOff
_PmoailAlmClientBiasHighWarning_Object = MibScalar
pmoailAlmClientBiasHighWarning = _PmoailAlmClientBiasHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 1, 33, 8),
    _PmoailAlmClientBiasHighWarning_Type()
)
pmoailAlmClientBiasHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientBiasHighWarning.setStatus("current")
_PmoailAlmClientUrg_ObjectIdentity = ObjectIdentity
pmoailAlmClientUrg = _PmoailAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 2)
)
_PmoailAlmclientEdfaAlarms1_ObjectIdentity = ObjectIdentity
pmoailAlmclientEdfaAlarms1 = _PmoailAlmclientEdfaAlarms1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 2, 32)
)
_PmoailAlmClientGainLowAlarm_Type = EkiOnOff
_PmoailAlmClientGainLowAlarm_Object = MibScalar
pmoailAlmClientGainLowAlarm = _PmoailAlmClientGainLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 2, 32, 1),
    _PmoailAlmClientGainLowAlarm_Type()
)
pmoailAlmClientGainLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientGainLowAlarm.setStatus("current")
_PmoailAlmClientGainHighAlarm_Type = EkiOnOff
_PmoailAlmClientGainHighAlarm_Object = MibScalar
pmoailAlmClientGainHighAlarm = _PmoailAlmClientGainHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 2, 32, 2),
    _PmoailAlmClientGainHighAlarm_Type()
)
pmoailAlmClientGainHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientGainHighAlarm.setStatus("current")
_PmoailAlmClientInputPwrLowAlarm_Type = EkiOnOff
_PmoailAlmClientInputPwrLowAlarm_Object = MibScalar
pmoailAlmClientInputPwrLowAlarm = _PmoailAlmClientInputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 2, 32, 3),
    _PmoailAlmClientInputPwrLowAlarm_Type()
)
pmoailAlmClientInputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientInputPwrLowAlarm.setStatus("current")
_PmoailAlmClientInputPwrHighAlarm_Type = EkiOnOff
_PmoailAlmClientInputPwrHighAlarm_Object = MibScalar
pmoailAlmClientInputPwrHighAlarm = _PmoailAlmClientInputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 2, 32, 4),
    _PmoailAlmClientInputPwrHighAlarm_Type()
)
pmoailAlmClientInputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientInputPwrHighAlarm.setStatus("current")
_PmoailAlmClientOutputPwrLowAlarm_Type = EkiOnOff
_PmoailAlmClientOutputPwrLowAlarm_Object = MibScalar
pmoailAlmClientOutputPwrLowAlarm = _PmoailAlmClientOutputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 2, 32, 5),
    _PmoailAlmClientOutputPwrLowAlarm_Type()
)
pmoailAlmClientOutputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientOutputPwrLowAlarm.setStatus("current")
_PmoailAlmClientOutputPwrHighAlarm_Type = EkiOnOff
_PmoailAlmClientOutputPwrHighAlarm_Object = MibScalar
pmoailAlmClientOutputPwrHighAlarm = _PmoailAlmClientOutputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 2, 32, 6),
    _PmoailAlmClientOutputPwrHighAlarm_Type()
)
pmoailAlmClientOutputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientOutputPwrHighAlarm.setStatus("current")
_PmoailAlmClientBiasLowAlarm_Type = EkiOnOff
_PmoailAlmClientBiasLowAlarm_Object = MibScalar
pmoailAlmClientBiasLowAlarm = _PmoailAlmClientBiasLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 2, 32, 7),
    _PmoailAlmClientBiasLowAlarm_Type()
)
pmoailAlmClientBiasLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientBiasLowAlarm.setStatus("current")
_PmoailAlmClientBiasHighAlarm_Type = EkiOnOff
_PmoailAlmClientBiasHighAlarm_Object = MibScalar
pmoailAlmClientBiasHighAlarm = _PmoailAlmClientBiasHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 2, 32, 8),
    _PmoailAlmClientBiasHighAlarm_Type()
)
pmoailAlmClientBiasHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientBiasHighAlarm.setStatus("current")
_PmoailAlmClientCrit_ObjectIdentity = ObjectIdentity
pmoailAlmClientCrit = _PmoailAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 3)
)
_PmoailAlmsynthAlm8_ObjectIdentity = ObjectIdentity
pmoailAlmsynthAlm8 = _PmoailAlmsynthAlm8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 3, 8)
)
_PmoailAlmClientHwFail_Type = EkiOnOff
_PmoailAlmClientHwFail_Object = MibScalar
pmoailAlmClientHwFail = _PmoailAlmClientHwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 3, 8, 4),
    _PmoailAlmClientHwFail_Type()
)
pmoailAlmClientHwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientHwFail.setStatus("current")
_PmoailAlmClientTxOff_Type = EkiOnOff
_PmoailAlmClientTxOff_Object = MibScalar
pmoailAlmClientTxOff = _PmoailAlmClientTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 3, 8, 5),
    _PmoailAlmClientTxOff_Type()
)
pmoailAlmClientTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientTxOff.setStatus("current")
_PmoailAlmClientDdmWarning_Type = EkiOnOff
_PmoailAlmClientDdmWarning_Object = MibScalar
pmoailAlmClientDdmWarning = _PmoailAlmClientDdmWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 3, 8, 9),
    _PmoailAlmClientDdmWarning_Type()
)
pmoailAlmClientDdmWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientDdmWarning.setStatus("current")
_PmoailAlmClientDdmAlm_Type = EkiOnOff
_PmoailAlmClientDdmAlm_Object = MibScalar
pmoailAlmClientDdmAlm = _PmoailAlmClientDdmAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 3, 8, 10),
    _PmoailAlmClientDdmAlm_Type()
)
pmoailAlmClientDdmAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientDdmAlm.setStatus("current")
_PmoailAlmClientFail_Type = EkiOnOff
_PmoailAlmClientFail_Object = MibScalar
pmoailAlmClientFail = _PmoailAlmClientFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 3, 8, 12),
    _PmoailAlmClientFail_Type()
)
pmoailAlmClientFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientFail.setStatus("current")
_PmoailAlmclientEdfaAlarms2_ObjectIdentity = ObjectIdentity
pmoailAlmclientEdfaAlarms2 = _PmoailAlmclientEdfaAlarms2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 3, 35)
)
_PmoailAlmClientEdfaNr_Type = EkiOnOff
_PmoailAlmClientEdfaNr_Object = MibScalar
pmoailAlmClientEdfaNr = _PmoailAlmClientEdfaNr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 3, 35, 1),
    _PmoailAlmClientEdfaNr_Type()
)
pmoailAlmClientEdfaNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientEdfaNr.setStatus("current")
_PmoailAlmClientEdfaTecFail_Type = EkiOnOff
_PmoailAlmClientEdfaTecFail_Object = MibScalar
pmoailAlmClientEdfaTecFail = _PmoailAlmClientEdfaTecFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 3, 35, 2),
    _PmoailAlmClientEdfaTecFail_Type()
)
pmoailAlmClientEdfaTecFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientEdfaTecFail.setStatus("current")
_PmoailAlmClientEdfaLaserFail_Type = EkiOnOff
_PmoailAlmClientEdfaLaserFail_Object = MibScalar
pmoailAlmClientEdfaLaserFail = _PmoailAlmClientEdfaLaserFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 3, 35, 3),
    _PmoailAlmClientEdfaLaserFail_Type()
)
pmoailAlmClientEdfaLaserFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientEdfaLaserFail.setStatus("current")
_PmoailAlmClientEdfaLos_Type = EkiOnOff
_PmoailAlmClientEdfaLos_Object = MibScalar
pmoailAlmClientEdfaLos = _PmoailAlmClientEdfaLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 3, 35, 4),
    _PmoailAlmClientEdfaLos_Type()
)
pmoailAlmClientEdfaLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientEdfaLos.setStatus("current")
_PmoailAlmClientExtPumpEdfaLowCurrent_Type = EkiOnOff
_PmoailAlmClientExtPumpEdfaLowCurrent_Object = MibScalar
pmoailAlmClientExtPumpEdfaLowCurrent = _PmoailAlmClientExtPumpEdfaLowCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 2, 3, 35, 5),
    _PmoailAlmClientExtPumpEdfaLowCurrent_Type()
)
pmoailAlmClientExtPumpEdfaLowCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmClientExtPumpEdfaLowCurrent.setStatus("current")
_PmoailAlmLine_ObjectIdentity = ObjectIdentity
pmoailAlmLine = _PmoailAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3)
)
_PmoailAlmLineNurg_ObjectIdentity = ObjectIdentity
pmoailAlmLineNurg = _PmoailAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 1)
)
_PmoailAlmlineEdfaWarnings_ObjectIdentity = ObjectIdentity
pmoailAlmlineEdfaWarnings = _PmoailAlmlineEdfaWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 1, 41)
)
_PmoailAlmLineGainLowWarning_Type = EkiOnOff
_PmoailAlmLineGainLowWarning_Object = MibScalar
pmoailAlmLineGainLowWarning = _PmoailAlmLineGainLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 1, 41, 1),
    _PmoailAlmLineGainLowWarning_Type()
)
pmoailAlmLineGainLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineGainLowWarning.setStatus("current")
_PmoailAlmLineGainHighWarning_Type = EkiOnOff
_PmoailAlmLineGainHighWarning_Object = MibScalar
pmoailAlmLineGainHighWarning = _PmoailAlmLineGainHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 1, 41, 2),
    _PmoailAlmLineGainHighWarning_Type()
)
pmoailAlmLineGainHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineGainHighWarning.setStatus("current")
_PmoailAlmLineInputPwrLowWarning_Type = EkiOnOff
_PmoailAlmLineInputPwrLowWarning_Object = MibScalar
pmoailAlmLineInputPwrLowWarning = _PmoailAlmLineInputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 1, 41, 3),
    _PmoailAlmLineInputPwrLowWarning_Type()
)
pmoailAlmLineInputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineInputPwrLowWarning.setStatus("current")
_PmoailAlmLineInputPwrHighWarning_Type = EkiOnOff
_PmoailAlmLineInputPwrHighWarning_Object = MibScalar
pmoailAlmLineInputPwrHighWarning = _PmoailAlmLineInputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 1, 41, 4),
    _PmoailAlmLineInputPwrHighWarning_Type()
)
pmoailAlmLineInputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineInputPwrHighWarning.setStatus("current")
_PmoailAlmLineOutputPwrLowWarning_Type = EkiOnOff
_PmoailAlmLineOutputPwrLowWarning_Object = MibScalar
pmoailAlmLineOutputPwrLowWarning = _PmoailAlmLineOutputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 1, 41, 5),
    _PmoailAlmLineOutputPwrLowWarning_Type()
)
pmoailAlmLineOutputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineOutputPwrLowWarning.setStatus("current")
_PmoailAlmLineOutputPwrHighWarning_Type = EkiOnOff
_PmoailAlmLineOutputPwrHighWarning_Object = MibScalar
pmoailAlmLineOutputPwrHighWarning = _PmoailAlmLineOutputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 1, 41, 6),
    _PmoailAlmLineOutputPwrHighWarning_Type()
)
pmoailAlmLineOutputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineOutputPwrHighWarning.setStatus("current")
_PmoailAlmLineBiasLowWarning_Type = EkiOnOff
_PmoailAlmLineBiasLowWarning_Object = MibScalar
pmoailAlmLineBiasLowWarning = _PmoailAlmLineBiasLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 1, 41, 7),
    _PmoailAlmLineBiasLowWarning_Type()
)
pmoailAlmLineBiasLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineBiasLowWarning.setStatus("current")
_PmoailAlmLineBiasHighWarning_Type = EkiOnOff
_PmoailAlmLineBiasHighWarning_Object = MibScalar
pmoailAlmLineBiasHighWarning = _PmoailAlmLineBiasHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 1, 41, 8),
    _PmoailAlmLineBiasHighWarning_Type()
)
pmoailAlmLineBiasHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineBiasHighWarning.setStatus("current")
_PmoailAlmLineUrg_ObjectIdentity = ObjectIdentity
pmoailAlmLineUrg = _PmoailAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 2)
)
_PmoailAlmlineEdfaAlarms1_ObjectIdentity = ObjectIdentity
pmoailAlmlineEdfaAlarms1 = _PmoailAlmlineEdfaAlarms1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 2, 40)
)
_PmoailAlmLineGainLowAlarm_Type = EkiOnOff
_PmoailAlmLineGainLowAlarm_Object = MibScalar
pmoailAlmLineGainLowAlarm = _PmoailAlmLineGainLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 2, 40, 1),
    _PmoailAlmLineGainLowAlarm_Type()
)
pmoailAlmLineGainLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineGainLowAlarm.setStatus("current")
_PmoailAlmLineGainHighAlarm_Type = EkiOnOff
_PmoailAlmLineGainHighAlarm_Object = MibScalar
pmoailAlmLineGainHighAlarm = _PmoailAlmLineGainHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 2, 40, 2),
    _PmoailAlmLineGainHighAlarm_Type()
)
pmoailAlmLineGainHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineGainHighAlarm.setStatus("current")
_PmoailAlmLineInputPwrLowAlarm_Type = EkiOnOff
_PmoailAlmLineInputPwrLowAlarm_Object = MibScalar
pmoailAlmLineInputPwrLowAlarm = _PmoailAlmLineInputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 2, 40, 3),
    _PmoailAlmLineInputPwrLowAlarm_Type()
)
pmoailAlmLineInputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineInputPwrLowAlarm.setStatus("current")
_PmoailAlmLineInputPwrHighAlarm_Type = EkiOnOff
_PmoailAlmLineInputPwrHighAlarm_Object = MibScalar
pmoailAlmLineInputPwrHighAlarm = _PmoailAlmLineInputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 2, 40, 4),
    _PmoailAlmLineInputPwrHighAlarm_Type()
)
pmoailAlmLineInputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineInputPwrHighAlarm.setStatus("current")
_PmoailAlmLineOutputPwrLowAlarm_Type = EkiOnOff
_PmoailAlmLineOutputPwrLowAlarm_Object = MibScalar
pmoailAlmLineOutputPwrLowAlarm = _PmoailAlmLineOutputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 2, 40, 5),
    _PmoailAlmLineOutputPwrLowAlarm_Type()
)
pmoailAlmLineOutputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineOutputPwrLowAlarm.setStatus("current")
_PmoailAlmLineOutputPwrHighAlarm_Type = EkiOnOff
_PmoailAlmLineOutputPwrHighAlarm_Object = MibScalar
pmoailAlmLineOutputPwrHighAlarm = _PmoailAlmLineOutputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 2, 40, 6),
    _PmoailAlmLineOutputPwrHighAlarm_Type()
)
pmoailAlmLineOutputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineOutputPwrHighAlarm.setStatus("current")
_PmoailAlmLineBiasLowAlarm_Type = EkiOnOff
_PmoailAlmLineBiasLowAlarm_Object = MibScalar
pmoailAlmLineBiasLowAlarm = _PmoailAlmLineBiasLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 2, 40, 7),
    _PmoailAlmLineBiasLowAlarm_Type()
)
pmoailAlmLineBiasLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineBiasLowAlarm.setStatus("current")
_PmoailAlmLineBiasHighAlarm_Type = EkiOnOff
_PmoailAlmLineBiasHighAlarm_Object = MibScalar
pmoailAlmLineBiasHighAlarm = _PmoailAlmLineBiasHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 2, 40, 8),
    _PmoailAlmLineBiasHighAlarm_Type()
)
pmoailAlmLineBiasHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineBiasHighAlarm.setStatus("current")
_PmoailAlmLineCrit_ObjectIdentity = ObjectIdentity
pmoailAlmLineCrit = _PmoailAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 3)
)
_PmoailAlmsynthAlm7_ObjectIdentity = ObjectIdentity
pmoailAlmsynthAlm7 = _PmoailAlmsynthAlm7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 3, 7)
)
_PmoailAlmLineHwFail_Type = EkiOnOff
_PmoailAlmLineHwFail_Object = MibScalar
pmoailAlmLineHwFail = _PmoailAlmLineHwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 3, 7, 4),
    _PmoailAlmLineHwFail_Type()
)
pmoailAlmLineHwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineHwFail.setStatus("current")
_PmoailAlmLineTxOff_Type = EkiOnOff
_PmoailAlmLineTxOff_Object = MibScalar
pmoailAlmLineTxOff = _PmoailAlmLineTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 3, 7, 5),
    _PmoailAlmLineTxOff_Type()
)
pmoailAlmLineTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineTxOff.setStatus("current")
_PmoailAlmLineDdmWarning_Type = EkiOnOff
_PmoailAlmLineDdmWarning_Object = MibScalar
pmoailAlmLineDdmWarning = _PmoailAlmLineDdmWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 3, 7, 9),
    _PmoailAlmLineDdmWarning_Type()
)
pmoailAlmLineDdmWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineDdmWarning.setStatus("current")
_PmoailAlmLineDdmAlm_Type = EkiOnOff
_PmoailAlmLineDdmAlm_Object = MibScalar
pmoailAlmLineDdmAlm = _PmoailAlmLineDdmAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 3, 7, 10),
    _PmoailAlmLineDdmAlm_Type()
)
pmoailAlmLineDdmAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineDdmAlm.setStatus("current")
_PmoailAlmLineFail_Type = EkiOnOff
_PmoailAlmLineFail_Object = MibScalar
pmoailAlmLineFail = _PmoailAlmLineFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 3, 7, 12),
    _PmoailAlmLineFail_Type()
)
pmoailAlmLineFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineFail.setStatus("current")
_PmoailAlmlineEdfaAlarms2_ObjectIdentity = ObjectIdentity
pmoailAlmlineEdfaAlarms2 = _PmoailAlmlineEdfaAlarms2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 3, 43)
)
_PmoailAlmLineEdfaNr_Type = EkiOnOff
_PmoailAlmLineEdfaNr_Object = MibScalar
pmoailAlmLineEdfaNr = _PmoailAlmLineEdfaNr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 3, 43, 1),
    _PmoailAlmLineEdfaNr_Type()
)
pmoailAlmLineEdfaNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineEdfaNr.setStatus("current")
_PmoailAlmLineEdfaTecFail_Type = EkiOnOff
_PmoailAlmLineEdfaTecFail_Object = MibScalar
pmoailAlmLineEdfaTecFail = _PmoailAlmLineEdfaTecFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 3, 43, 2),
    _PmoailAlmLineEdfaTecFail_Type()
)
pmoailAlmLineEdfaTecFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineEdfaTecFail.setStatus("current")
_PmoailAlmLineEdfaLaserFail_Type = EkiOnOff
_PmoailAlmLineEdfaLaserFail_Object = MibScalar
pmoailAlmLineEdfaLaserFail = _PmoailAlmLineEdfaLaserFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 3, 43, 3),
    _PmoailAlmLineEdfaLaserFail_Type()
)
pmoailAlmLineEdfaLaserFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineEdfaLaserFail.setStatus("current")
_PmoailAlmLineEdfaLos_Type = EkiOnOff
_PmoailAlmLineEdfaLos_Object = MibScalar
pmoailAlmLineEdfaLos = _PmoailAlmLineEdfaLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 3, 43, 4),
    _PmoailAlmLineEdfaLos_Type()
)
pmoailAlmLineEdfaLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineEdfaLos.setStatus("current")
_PmoailAlmLineExtPumpEdfaLowCurrent_Type = EkiOnOff
_PmoailAlmLineExtPumpEdfaLowCurrent_Object = MibScalar
pmoailAlmLineExtPumpEdfaLowCurrent = _PmoailAlmLineExtPumpEdfaLowCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 2, 3, 3, 43, 5),
    _PmoailAlmLineExtPumpEdfaLowCurrent_Type()
)
pmoailAlmLineExtPumpEdfaLowCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailAlmLineExtPumpEdfaLowCurrent.setStatus("current")
_Pmoailmeasures_ObjectIdentity = ObjectIdentity
pmoailmeasures = _Pmoailmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 3)
)
_PmoailMesrOther_ObjectIdentity = ObjectIdentity
pmoailMesrOther = _PmoailMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 3, 1)
)


class _PmoailMesrtempMeas_Type(Integer32):
    """Custom type pmoailMesrtempMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailMesrtempMeas_Type.__name__ = "Integer32"
_PmoailMesrtempMeas_Object = MibScalar
pmoailMesrtempMeas = _PmoailMesrtempMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 3, 1, 72),
    _PmoailMesrtempMeas_Type()
)
pmoailMesrtempMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailMesrtempMeas.setStatus("current")


class _PmoailMesr3v3Meas_Type(Integer32):
    """Custom type pmoailMesr3v3Meas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailMesr3v3Meas_Type.__name__ = "Integer32"
_PmoailMesr3v3Meas_Object = MibScalar
pmoailMesr3v3Meas = _PmoailMesr3v3Meas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 3, 1, 73),
    _PmoailMesr3v3Meas_Type()
)
pmoailMesr3v3Meas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailMesr3v3Meas.setStatus("current")
_PmoailMesrClient_ObjectIdentity = ObjectIdentity
pmoailMesrClient = _PmoailMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 3, 2)
)


class _PmoailMesrclientEdfaBiasMeas_Type(Integer32):
    """Custom type pmoailMesrclientEdfaBiasMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailMesrclientEdfaBiasMeas_Type.__name__ = "Integer32"
_PmoailMesrclientEdfaBiasMeas_Object = MibScalar
pmoailMesrclientEdfaBiasMeas = _PmoailMesrclientEdfaBiasMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 3, 2, 32),
    _PmoailMesrclientEdfaBiasMeas_Type()
)
pmoailMesrclientEdfaBiasMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailMesrclientEdfaBiasMeas.setStatus("current")


class _PmoailMesrclientEdfaTxpwrMeas_Type(Integer32):
    """Custom type pmoailMesrclientEdfaTxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailMesrclientEdfaTxpwrMeas_Type.__name__ = "Integer32"
_PmoailMesrclientEdfaTxpwrMeas_Object = MibScalar
pmoailMesrclientEdfaTxpwrMeas = _PmoailMesrclientEdfaTxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 3, 2, 33),
    _PmoailMesrclientEdfaTxpwrMeas_Type()
)
pmoailMesrclientEdfaTxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailMesrclientEdfaTxpwrMeas.setStatus("current")


class _PmoailMesrclientEdfaRxpwrMeas_Type(Integer32):
    """Custom type pmoailMesrclientEdfaRxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailMesrclientEdfaRxpwrMeas_Type.__name__ = "Integer32"
_PmoailMesrclientEdfaRxpwrMeas_Object = MibScalar
pmoailMesrclientEdfaRxpwrMeas = _PmoailMesrclientEdfaRxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 3, 2, 34),
    _PmoailMesrclientEdfaRxpwrMeas_Type()
)
pmoailMesrclientEdfaRxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailMesrclientEdfaRxpwrMeas.setStatus("current")


class _PmoailMesrclientEdfaGainMeas_Type(Integer32):
    """Custom type pmoailMesrclientEdfaGainMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailMesrclientEdfaGainMeas_Type.__name__ = "Integer32"
_PmoailMesrclientEdfaGainMeas_Object = MibScalar
pmoailMesrclientEdfaGainMeas = _PmoailMesrclientEdfaGainMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 3, 2, 35),
    _PmoailMesrclientEdfaGainMeas_Type()
)
pmoailMesrclientEdfaGainMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailMesrclientEdfaGainMeas.setStatus("current")
_PmoailMesrLine_ObjectIdentity = ObjectIdentity
pmoailMesrLine = _PmoailMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 3, 3)
)


class _PmoailMesrlineEdfaBiasMeas_Type(Integer32):
    """Custom type pmoailMesrlineEdfaBiasMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailMesrlineEdfaBiasMeas_Type.__name__ = "Integer32"
_PmoailMesrlineEdfaBiasMeas_Object = MibScalar
pmoailMesrlineEdfaBiasMeas = _PmoailMesrlineEdfaBiasMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 3, 3, 40),
    _PmoailMesrlineEdfaBiasMeas_Type()
)
pmoailMesrlineEdfaBiasMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailMesrlineEdfaBiasMeas.setStatus("current")


class _PmoailMesrlineEdfaTxpwrMeas_Type(Integer32):
    """Custom type pmoailMesrlineEdfaTxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailMesrlineEdfaTxpwrMeas_Type.__name__ = "Integer32"
_PmoailMesrlineEdfaTxpwrMeas_Object = MibScalar
pmoailMesrlineEdfaTxpwrMeas = _PmoailMesrlineEdfaTxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 3, 3, 41),
    _PmoailMesrlineEdfaTxpwrMeas_Type()
)
pmoailMesrlineEdfaTxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailMesrlineEdfaTxpwrMeas.setStatus("current")


class _PmoailMesrlineEdfaRxpwrMeas_Type(Integer32):
    """Custom type pmoailMesrlineEdfaRxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailMesrlineEdfaRxpwrMeas_Type.__name__ = "Integer32"
_PmoailMesrlineEdfaRxpwrMeas_Object = MibScalar
pmoailMesrlineEdfaRxpwrMeas = _PmoailMesrlineEdfaRxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 3, 3, 42),
    _PmoailMesrlineEdfaRxpwrMeas_Type()
)
pmoailMesrlineEdfaRxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailMesrlineEdfaRxpwrMeas.setStatus("current")


class _PmoailMesrlineEdfaGainMeas_Type(Integer32):
    """Custom type pmoailMesrlineEdfaGainMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailMesrlineEdfaGainMeas_Type.__name__ = "Integer32"
_PmoailMesrlineEdfaGainMeas_Object = MibScalar
pmoailMesrlineEdfaGainMeas = _PmoailMesrlineEdfaGainMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 3, 3, 43),
    _PmoailMesrlineEdfaGainMeas_Type()
)
pmoailMesrlineEdfaGainMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailMesrlineEdfaGainMeas.setStatus("current")
_PmoailcontrolsWrite_ObjectIdentity = ObjectIdentity
pmoailcontrolsWrite = _PmoailcontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6)
)
_PmoailCtrlOther_ObjectIdentity = ObjectIdentity
pmoailCtrlOther = _PmoailCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 1)
)
_PmoailCtrlsynth0_ObjectIdentity = ObjectIdentity
pmoailCtrlsynth0 = _PmoailCtrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 1, 0)
)
_PmoailCtrlConfLoad_Type = EkiOnOff
_PmoailCtrlConfLoad_Object = MibScalar
pmoailCtrlConfLoad = _PmoailCtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 1, 0, 1),
    _PmoailCtrlConfLoad_Type()
)
pmoailCtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrlConfLoad.setStatus("current")
_PmoailCtrlConfFlash_Type = EkiOnOff
_PmoailCtrlConfFlash_Object = MibScalar
pmoailCtrlConfFlash = _PmoailCtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 1, 0, 9),
    _PmoailCtrlConfFlash_Type()
)
pmoailCtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrlConfFlash.setStatus("current")
_PmoailCtrlConfClear_Type = EkiOnOff
_PmoailCtrlConfClear_Object = MibScalar
pmoailCtrlConfClear = _PmoailCtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 1, 0, 13),
    _PmoailCtrlConfClear_Type()
)
pmoailCtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrlConfClear.setStatus("current")
_PmoailCtrlswMgnt_ObjectIdentity = ObjectIdentity
pmoailCtrlswMgnt = _PmoailCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 1, 5)
)
_PmoailCtrlColdReset_Type = EkiOnOff
_PmoailCtrlColdReset_Object = MibScalar
pmoailCtrlColdReset = _PmoailCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 1, 5, 2),
    _PmoailCtrlColdReset_Type()
)
pmoailCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrlColdReset.setStatus("current")
_PmoailCtrlWarmReset_Type = EkiOnOff
_PmoailCtrlWarmReset_Object = MibScalar
pmoailCtrlWarmReset = _PmoailCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 1, 5, 3),
    _PmoailCtrlWarmReset_Type()
)
pmoailCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrlWarmReset.setStatus("current")
_PmoailCtrlpowerDown_ObjectIdentity = ObjectIdentity
pmoailCtrlpowerDown = _PmoailCtrlpowerDown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 1, 72)
)
_PmoailCtrlSoftPowerDown_Type = EkiOnOff
_PmoailCtrlSoftPowerDown_Object = MibScalar
pmoailCtrlSoftPowerDown = _PmoailCtrlSoftPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 1, 72, 1),
    _PmoailCtrlSoftPowerDown_Type()
)
pmoailCtrlSoftPowerDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrlSoftPowerDown.setStatus("current")
_PmoailCtrlledTest_ObjectIdentity = ObjectIdentity
pmoailCtrlledTest = _PmoailCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 1, 73)
)
_PmoailCtrlGreenLed_Type = EkiOnOff
_PmoailCtrlGreenLed_Object = MibScalar
pmoailCtrlGreenLed = _PmoailCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 1, 73, 1),
    _PmoailCtrlGreenLed_Type()
)
pmoailCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrlGreenLed.setStatus("current")
_PmoailCtrlRedLed_Type = EkiOnOff
_PmoailCtrlRedLed_Object = MibScalar
pmoailCtrlRedLed = _PmoailCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 1, 73, 2),
    _PmoailCtrlRedLed_Type()
)
pmoailCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrlRedLed.setStatus("current")
_PmoailCtrlLedOff_Type = EkiOnOff
_PmoailCtrlLedOff_Object = MibScalar
pmoailCtrlLedOff = _PmoailCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 1, 73, 3),
    _PmoailCtrlLedOff_Type()
)
pmoailCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrlLedOff.setStatus("current")
_PmoailCtrlmaintMode_ObjectIdentity = ObjectIdentity
pmoailCtrlmaintMode = _PmoailCtrlmaintMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 1, 75)
)
_PmoailCtrlMaintenance_Type = EkiOnOff
_PmoailCtrlMaintenance_Object = MibScalar
pmoailCtrlMaintenance = _PmoailCtrlMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 1, 75, 1),
    _PmoailCtrlMaintenance_Type()
)
pmoailCtrlMaintenance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrlMaintenance.setStatus("current")
_PmoailCtrlClient_ObjectIdentity = ObjectIdentity
pmoailCtrlClient = _PmoailCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 2)
)
_PmoailCtrlclientEdfaLaserOff_ObjectIdentity = ObjectIdentity
pmoailCtrlclientEdfaLaserOff = _PmoailCtrlclientEdfaLaserOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 2, 32)
)
_PmoailCtrlClientEdfaLaserOff_Type = EkiOnOff
_PmoailCtrlClientEdfaLaserOff_Object = MibScalar
pmoailCtrlClientEdfaLaserOff = _PmoailCtrlClientEdfaLaserOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 2, 32, 1),
    _PmoailCtrlClientEdfaLaserOff_Type()
)
pmoailCtrlClientEdfaLaserOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrlClientEdfaLaserOff.setStatus("current")
_PmoailCtrlclientEdfaMode_Type = PmoailpreampMode
_PmoailCtrlclientEdfaMode_Object = MibScalar
pmoailCtrlclientEdfaMode = _PmoailCtrlclientEdfaMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 2, 33),
    _PmoailCtrlclientEdfaMode_Type()
)
pmoailCtrlclientEdfaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrlclientEdfaMode.setStatus("current")


class _PmoailCtrlclientIlasSettingValue_Type(Integer32):
    """Custom type pmoailCtrlclientIlasSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailCtrlclientIlasSettingValue_Type.__name__ = "Integer32"
_PmoailCtrlclientIlasSettingValue_Object = MibScalar
pmoailCtrlclientIlasSettingValue = _PmoailCtrlclientIlasSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 2, 34),
    _PmoailCtrlclientIlasSettingValue_Type()
)
pmoailCtrlclientIlasSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrlclientIlasSettingValue.setStatus("current")


class _PmoailCtrlclientPlasSettingValue_Type(Integer32):
    """Custom type pmoailCtrlclientPlasSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailCtrlclientPlasSettingValue_Type.__name__ = "Integer32"
_PmoailCtrlclientPlasSettingValue_Object = MibScalar
pmoailCtrlclientPlasSettingValue = _PmoailCtrlclientPlasSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 2, 35),
    _PmoailCtrlclientPlasSettingValue_Type()
)
pmoailCtrlclientPlasSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrlclientPlasSettingValue.setStatus("current")


class _PmoailCtrlclientGainSettingValue_Type(Integer32):
    """Custom type pmoailCtrlclientGainSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailCtrlclientGainSettingValue_Type.__name__ = "Integer32"
_PmoailCtrlclientGainSettingValue_Object = MibScalar
pmoailCtrlclientGainSettingValue = _PmoailCtrlclientGainSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 2, 36),
    _PmoailCtrlclientGainSettingValue_Type()
)
pmoailCtrlclientGainSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrlclientGainSettingValue.setStatus("current")


class _PmoailCtrlclientEffPwrOutSettingValue_Type(Integer32):
    """Custom type pmoailCtrlclientEffPwrOutSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailCtrlclientEffPwrOutSettingValue_Type.__name__ = "Integer32"
_PmoailCtrlclientEffPwrOutSettingValue_Object = MibScalar
pmoailCtrlclientEffPwrOutSettingValue = _PmoailCtrlclientEffPwrOutSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 2, 37),
    _PmoailCtrlclientEffPwrOutSettingValue_Type()
)
pmoailCtrlclientEffPwrOutSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrlclientEffPwrOutSettingValue.setStatus("current")
_PmoailCtrlLine_ObjectIdentity = ObjectIdentity
pmoailCtrlLine = _PmoailCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 3)
)
_PmoailCtrllineEdfaLaserOff_ObjectIdentity = ObjectIdentity
pmoailCtrllineEdfaLaserOff = _PmoailCtrllineEdfaLaserOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 3, 40)
)
_PmoailCtrlLineEdfaLaserOff_Type = EkiOnOff
_PmoailCtrlLineEdfaLaserOff_Object = MibScalar
pmoailCtrlLineEdfaLaserOff = _PmoailCtrlLineEdfaLaserOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 3, 40, 1),
    _PmoailCtrlLineEdfaLaserOff_Type()
)
pmoailCtrlLineEdfaLaserOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrlLineEdfaLaserOff.setStatus("current")
_PmoailCtrllineEdfaMode_Type = PmoailboosterMode
_PmoailCtrllineEdfaMode_Object = MibScalar
pmoailCtrllineEdfaMode = _PmoailCtrllineEdfaMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 3, 41),
    _PmoailCtrllineEdfaMode_Type()
)
pmoailCtrllineEdfaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrllineEdfaMode.setStatus("current")


class _PmoailCtrllineIlasSettingValue_Type(Integer32):
    """Custom type pmoailCtrllineIlasSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailCtrllineIlasSettingValue_Type.__name__ = "Integer32"
_PmoailCtrllineIlasSettingValue_Object = MibScalar
pmoailCtrllineIlasSettingValue = _PmoailCtrllineIlasSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 3, 42),
    _PmoailCtrllineIlasSettingValue_Type()
)
pmoailCtrllineIlasSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrllineIlasSettingValue.setStatus("current")


class _PmoailCtrllinePlasSettingValue_Type(Integer32):
    """Custom type pmoailCtrllinePlasSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailCtrllinePlasSettingValue_Type.__name__ = "Integer32"
_PmoailCtrllinePlasSettingValue_Object = MibScalar
pmoailCtrllinePlasSettingValue = _PmoailCtrllinePlasSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 3, 43),
    _PmoailCtrllinePlasSettingValue_Type()
)
pmoailCtrllinePlasSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrllinePlasSettingValue.setStatus("current")


class _PmoailCtrllineGainSettingValue_Type(Integer32):
    """Custom type pmoailCtrllineGainSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailCtrllineGainSettingValue_Type.__name__ = "Integer32"
_PmoailCtrllineGainSettingValue_Object = MibScalar
pmoailCtrllineGainSettingValue = _PmoailCtrllineGainSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 3, 44),
    _PmoailCtrllineGainSettingValue_Type()
)
pmoailCtrllineGainSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrllineGainSettingValue.setStatus("current")


class _PmoailCtrllineEffPwrOutSettingValue_Type(Integer32):
    """Custom type pmoailCtrllineEffPwrOutSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailCtrllineEffPwrOutSettingValue_Type.__name__ = "Integer32"
_PmoailCtrllineEffPwrOutSettingValue_Object = MibScalar
pmoailCtrllineEffPwrOutSettingValue = _PmoailCtrllineEffPwrOutSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 6, 3, 45),
    _PmoailCtrllineEffPwrOutSettingValue_Type()
)
pmoailCtrllineEffPwrOutSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCtrllineEffPwrOutSettingValue.setStatus("current")
_Pmoailri_ObjectIdentity = ObjectIdentity
pmoailri = _Pmoailri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 7)
)
_PmoailRinvReloadInventory_Type = EkiOnOff
_PmoailRinvReloadInventory_Object = MibScalar
pmoailRinvReloadInventory = _PmoailRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 7, 2),
    _PmoailRinvReloadInventory_Type()
)
pmoailRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailRinvReloadInventory.setStatus("current")
_PmoailRinvModulePlatform_Type = DisplayString
_PmoailRinvModulePlatform_Object = MibScalar
pmoailRinvModulePlatform = _PmoailRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 7, 3),
    _PmoailRinvModulePlatform_Type()
)
pmoailRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailRinvModulePlatform.setStatus("current")
_PmoailRinvSwPlatform_Type = DisplayString
_PmoailRinvSwPlatform_Object = MibScalar
pmoailRinvSwPlatform = _PmoailRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 7, 4),
    _PmoailRinvSwPlatform_Type()
)
pmoailRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailRinvSwPlatform.setStatus("current")
_PmoailRinvSwFoa_Type = DisplayString
_PmoailRinvSwFoa_Object = MibScalar
pmoailRinvSwFoa = _PmoailRinvSwFoa_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 7, 5),
    _PmoailRinvSwFoa_Type()
)
pmoailRinvSwFoa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailRinvSwFoa.setStatus("current")
_PmoailRinvInLine1Table_Object = MibTable
pmoailRinvInLine1Table = _PmoailRinvInLine1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 7, 6)
)
if mibBuilder.loadTexts:
    pmoailRinvInLine1Table.setStatus("current")
_PmoailRinvInLine1Entry_Object = MibTableRow
pmoailRinvInLine1Entry = _PmoailRinvInLine1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 7, 6, 1)
)
pmoailRinvInLine1Entry.setIndexNames(
    (0, "EKINOPS-PmOail-MIB", "pmoailRinvInLine1Index"),
)
if mibBuilder.loadTexts:
    pmoailRinvInLine1Entry.setStatus("current")


class _PmoailRinvInLine1Index_Type(Integer32):
    """Custom type pmoailRinvInLine1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PmoailRinvInLine1Index_Type.__name__ = "Integer32"
_PmoailRinvInLine1Index_Object = MibTableColumn
pmoailRinvInLine1Index = _PmoailRinvInLine1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 7, 6, 1, 1),
    _PmoailRinvInLine1Index_Type()
)
pmoailRinvInLine1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailRinvInLine1Index.setStatus("current")
_PmoailRinvInLine1_Type = DisplayString
_PmoailRinvInLine1_Object = MibTableColumn
pmoailRinvInLine1 = _PmoailRinvInLine1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 7, 6, 1, 2),
    _PmoailRinvInLine1_Type()
)
pmoailRinvInLine1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailRinvInLine1.setStatus("current")
_PmoailRinvInLine2Table_Object = MibTable
pmoailRinvInLine2Table = _PmoailRinvInLine2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 7, 7)
)
if mibBuilder.loadTexts:
    pmoailRinvInLine2Table.setStatus("current")
_PmoailRinvInLine2Entry_Object = MibTableRow
pmoailRinvInLine2Entry = _PmoailRinvInLine2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 7, 7, 1)
)
pmoailRinvInLine2Entry.setIndexNames(
    (0, "EKINOPS-PmOail-MIB", "pmoailRinvInLine2Index"),
)
if mibBuilder.loadTexts:
    pmoailRinvInLine2Entry.setStatus("current")


class _PmoailRinvInLine2Index_Type(Integer32):
    """Custom type pmoailRinvInLine2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PmoailRinvInLine2Index_Type.__name__ = "Integer32"
_PmoailRinvInLine2Index_Object = MibTableColumn
pmoailRinvInLine2Index = _PmoailRinvInLine2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 7, 7, 1, 1),
    _PmoailRinvInLine2Index_Type()
)
pmoailRinvInLine2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailRinvInLine2Index.setStatus("current")
_PmoailRinvInLine2_Type = DisplayString
_PmoailRinvInLine2_Object = MibTableColumn
pmoailRinvInLine2 = _PmoailRinvInLine2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 7, 7, 1, 2),
    _PmoailRinvInLine2_Type()
)
pmoailRinvInLine2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailRinvInLine2.setStatus("current")
_PmoailConfig_ObjectIdentity = ObjectIdentity
pmoailConfig = _PmoailConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 9)
)
_PmoailCfgNoValue_ObjectIdentity = ObjectIdentity
pmoailCfgNoValue = _PmoailCfgNoValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 9, 1)
)
_PmoailtableclientStartup_ObjectIdentity = ObjectIdentity
pmoailtableclientStartup = _PmoailtableclientStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 9, 1, 1)
)


class _PmoailCfgclientEdfaLaserCtrl_Type(Unsigned32):
    """Custom type pmoailCfgclientEdfaLaserCtrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoailCfgclientEdfaLaserCtrl_Type.__name__ = "Unsigned32"
_PmoailCfgclientEdfaLaserCtrl_Object = MibScalar
pmoailCfgclientEdfaLaserCtrl = _PmoailCfgclientEdfaLaserCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 9, 1, 1, 2),
    _PmoailCfgclientEdfaLaserCtrl_Type()
)
pmoailCfgclientEdfaLaserCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCfgclientEdfaLaserCtrl.setStatus("current")


class _PmoailCfgclientEdfaLaserMode_Type(Unsigned32):
    """Custom type pmoailCfgclientEdfaLaserMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoailCfgclientEdfaLaserMode_Type.__name__ = "Unsigned32"
_PmoailCfgclientEdfaLaserMode_Object = MibScalar
pmoailCfgclientEdfaLaserMode = _PmoailCfgclientEdfaLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 9, 1, 1, 3),
    _PmoailCfgclientEdfaLaserMode_Type()
)
pmoailCfgclientEdfaLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCfgclientEdfaLaserMode.setStatus("current")
_PmoailCfgLineStartUp_ObjectIdentity = ObjectIdentity
pmoailCfgLineStartUp = _PmoailCfgLineStartUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 9, 2)
)
_PmoailtablelineStartup_ObjectIdentity = ObjectIdentity
pmoailtablelineStartup = _PmoailtablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 9, 2, 1)
)


class _PmoailCfglineEdfaLaserCtrl_Type(Unsigned32):
    """Custom type pmoailCfglineEdfaLaserCtrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoailCfglineEdfaLaserCtrl_Type.__name__ = "Unsigned32"
_PmoailCfglineEdfaLaserCtrl_Object = MibScalar
pmoailCfglineEdfaLaserCtrl = _PmoailCfglineEdfaLaserCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 9, 2, 1, 2),
    _PmoailCfglineEdfaLaserCtrl_Type()
)
pmoailCfglineEdfaLaserCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCfglineEdfaLaserCtrl.setStatus("current")


class _PmoailCfglineEdfaLaserMode_Type(Unsigned32):
    """Custom type pmoailCfglineEdfaLaserMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoailCfglineEdfaLaserMode_Type.__name__ = "Unsigned32"
_PmoailCfglineEdfaLaserMode_Object = MibScalar
pmoailCfglineEdfaLaserMode = _PmoailCfglineEdfaLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 9, 2, 1, 3),
    _PmoailCfglineEdfaLaserMode_Type()
)
pmoailCfglineEdfaLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCfglineEdfaLaserMode.setStatus("current")
_PmoailCfgLabels_ObjectIdentity = ObjectIdentity
pmoailCfgLabels = _PmoailCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 9, 3)
)
_PmoailCfgLabelclientTable_Object = MibTable
pmoailCfgLabelclientTable = _PmoailCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pmoailCfgLabelclientTable.setStatus("current")
_PmoailCfgLabelclientEntry_Object = MibTableRow
pmoailCfgLabelclientEntry = _PmoailCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 9, 3, 1, 1)
)
pmoailCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-PmOail-MIB", "pmoailCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmoailCfgLabelclientEntry.setStatus("current")


class _PmoailCfgLabelclientIndex_Type(Integer32):
    """Custom type pmoailCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoailCfgLabelclientIndex_Type.__name__ = "Integer32"
_PmoailCfgLabelclientIndex_Object = MibTableColumn
pmoailCfgLabelclientIndex = _PmoailCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 9, 3, 1, 1, 1),
    _PmoailCfgLabelclientIndex_Type()
)
pmoailCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailCfgLabelclientIndex.setStatus("current")


class _PmoailCfgLabelclientPortn_Type(DisplayString):
    """Custom type pmoailCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmoailCfgLabelclientPortn_Type.__name__ = "DisplayString"
_PmoailCfgLabelclientPortn_Object = MibTableColumn
pmoailCfgLabelclientPortn = _PmoailCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 9, 3, 1, 1, 3),
    _PmoailCfgLabelclientPortn_Type()
)
pmoailCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCfgLabelclientPortn.setStatus("current")
_PmoailCfgLabellineTable_Object = MibTable
pmoailCfgLabellineTable = _PmoailCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pmoailCfgLabellineTable.setStatus("current")
_PmoailCfgLabellineEntry_Object = MibTableRow
pmoailCfgLabellineEntry = _PmoailCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 9, 3, 2, 1)
)
pmoailCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-PmOail-MIB", "pmoailCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmoailCfgLabellineEntry.setStatus("current")


class _PmoailCfgLabellineIndex_Type(Integer32):
    """Custom type pmoailCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoailCfgLabellineIndex_Type.__name__ = "Integer32"
_PmoailCfgLabellineIndex_Object = MibTableColumn
pmoailCfgLabellineIndex = _PmoailCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 9, 3, 2, 1, 1),
    _PmoailCfgLabellineIndex_Type()
)
pmoailCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailCfgLabellineIndex.setStatus("current")


class _PmoailCfgLabellinePortn_Type(DisplayString):
    """Custom type pmoailCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmoailCfgLabellinePortn_Type.__name__ = "DisplayString"
_PmoailCfgLabellinePortn_Object = MibTableColumn
pmoailCfgLabellinePortn = _PmoailCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 9, 3, 2, 1, 3),
    _PmoailCfgLabellinePortn_Type()
)
pmoailCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCfgLabellinePortn.setStatus("current")
_PmoailCfgWriteConfiguration_Type = EkiOnOff
_PmoailCfgWriteConfiguration_Object = MibScalar
pmoailCfgWriteConfiguration = _PmoailCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 9, 257),
    _PmoailCfgWriteConfiguration_Type()
)
pmoailCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailCfgWriteConfiguration.setStatus("current")
_Pmoailtraps_ObjectIdentity = ObjectIdentity
pmoailtraps = _Pmoailtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 36, 10)
)


class _PmoailtrapBoardNumber_Type(Integer32):
    """Custom type pmoailtrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PmoailtrapBoardNumber_Type.__name__ = "Integer32"
_PmoailtrapBoardNumber_Object = MibScalar
pmoailtrapBoardNumber = _PmoailtrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 36, 10, 4),
    _PmoailtrapBoardNumber_Type()
)
pmoailtrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailtrapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pmoailLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 36, 10, 30)
)
pmoailLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOail-MIB", "pmoailAlmLineDdmWarning"),
        ("EKINOPS-PmOail-MIB", "pmoailtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmoailLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 36, 10, 31)
)
pmoailLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOail-MIB", "pmoailAlmLineDdmWarning"),
        ("EKINOPS-PmOail-MIB", "pmoailtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmoailLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 36, 10, 32)
)
pmoailLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOail-MIB", "pmoailAlmLineDdmAlm"),
        ("EKINOPS-PmOail-MIB", "pmoailtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pmoailLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 36, 10, 33)
)
pmoailLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOail-MIB", "pmoailAlmLineDdmAlm"),
        ("EKINOPS-PmOail-MIB", "pmoailtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pmoailLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 36, 10, 34)
)
pmoailLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-PmOail-MIB", "pmoailAlmLineFail"),
        ("EKINOPS-PmOail-MIB", "pmoailAlmLineHwFail"),
        ("EKINOPS-PmOail-MIB", "pmoailtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailLineTrapCritGoesOn.setStatus(
        "current"
    )

pmoailLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 36, 10, 35)
)
pmoailLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-PmOail-MIB", "pmoailAlmLineFail"),
        ("EKINOPS-PmOail-MIB", "pmoailAlmLineHwFail"),
        ("EKINOPS-PmOail-MIB", "pmoailtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailLineTrapCritGoesOff.setStatus(
        "current"
    )

pmoailClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 36, 10, 40)
)
pmoailClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOail-MIB", "pmoailAlmClientDdmWarning"),
        ("EKINOPS-PmOail-MIB", "pmoailtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmoailClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 36, 10, 41)
)
pmoailClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOail-MIB", "pmoailAlmClientDdmWarning"),
        ("EKINOPS-PmOail-MIB", "pmoailtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmoailClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 36, 10, 42)
)
pmoailClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOail-MIB", "pmoailAlmClientDdmAlm"),
        ("EKINOPS-PmOail-MIB", "pmoailtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pmoailClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 36, 10, 43)
)
pmoailClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOail-MIB", "pmoailAlmClientDdmAlm"),
        ("EKINOPS-PmOail-MIB", "pmoailtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pmoailClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 36, 10, 44)
)
pmoailClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-PmOail-MIB", "pmoailAlmClientFail"),
        ("EKINOPS-PmOail-MIB", "pmoailAlmClientHwFail"),
        ("EKINOPS-PmOail-MIB", "pmoailtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailClientTrapCritGoesOn.setStatus(
        "current"
    )

pmoailClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 36, 10, 45)
)
pmoailClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-PmOail-MIB", "pmoailAlmClientFail"),
        ("EKINOPS-PmOail-MIB", "pmoailAlmClientHwFail"),
        ("EKINOPS-PmOail-MIB", "pmoailtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailClientTrapCritGoesOff.setStatus(
        "current"
    )

pmoailPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 36, 10, 50)
)
pmoailPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOail-MIB", "pmoailAlmDefFuseB"),
        ("EKINOPS-PmOail-MIB", "pmoailAlmDefFuseA"),
        ("EKINOPS-PmOail-MIB", "pmoailtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmoailPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 36, 10, 51)
)
pmoailPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOail-MIB", "pmoailAlmDefFuseB"),
        ("EKINOPS-PmOail-MIB", "pmoailAlmDefFuseA"),
        ("EKINOPS-PmOail-MIB", "pmoailtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-PmOail-MIB",
    **{"PmoailpreampMode": PmoailpreampMode,
       "PmoailboosterMode": PmoailboosterMode,
       "modulepmoail": modulepmoail,
       "pmoailalarms": pmoailalarms,
       "pmoailAlmOther": pmoailAlmOther,
       "pmoailAlmOtherNurg": pmoailAlmOtherNurg,
       "pmoailAlmsynthAlm2": pmoailAlmsynthAlm2,
       "pmoailAlmConfTableSave": pmoailAlmConfTableSave,
       "pmoailAlmInvUpload": pmoailAlmInvUpload,
       "pmoailAlmConfTableLoad": pmoailAlmConfTableLoad,
       "pmoailAlmfoaWarnings": pmoailAlmfoaWarnings,
       "pmoailAlm3v3LowWarning": pmoailAlm3v3LowWarning,
       "pmoailAlm3v3HighWarning": pmoailAlm3v3HighWarning,
       "pmoailAlmTermpLowWarning": pmoailAlmTermpLowWarning,
       "pmoailAlmTempHighWarning": pmoailAlmTempHighWarning,
       "pmoailAlmOtherUrg": pmoailAlmOtherUrg,
       "pmoailAlmfoaAlarms": pmoailAlmfoaAlarms,
       "pmoailAlm3v3LowAlarm": pmoailAlm3v3LowAlarm,
       "pmoailAlm3v3HighAlarm": pmoailAlm3v3HighAlarm,
       "pmoailAlmTermpLowAlarm": pmoailAlmTermpLowAlarm,
       "pmoailAlmTempHighAlarm": pmoailAlmTempHighAlarm,
       "pmoailAlmOtherCrit": pmoailAlmOtherCrit,
       "pmoailAlmsynthAlm0": pmoailAlmsynthAlm0,
       "pmoailAlmMaintenanceMode": pmoailAlmMaintenanceMode,
       "pmoailAlmModGlobFail": pmoailAlmModGlobFail,
       "pmoailAlmUpEdfaInitNotCompl": pmoailAlmUpEdfaInitNotCompl,
       "pmoailAlmDwEdfaInitNotCompl": pmoailAlmDwEdfaInitNotCompl,
       "pmoailAlmExtPumpNotLocked": pmoailAlmExtPumpNotLocked,
       "pmoailAlmDefFuseA": pmoailAlmDefFuseA,
       "pmoailAlmDefFuseB": pmoailAlmDefFuseB,
       "pmoailAlmClient": pmoailAlmClient,
       "pmoailAlmClientNurg": pmoailAlmClientNurg,
       "pmoailAlmclientEdfaWarnings": pmoailAlmclientEdfaWarnings,
       "pmoailAlmClientGainLowWarning": pmoailAlmClientGainLowWarning,
       "pmoailAlmClientGainHighWarning": pmoailAlmClientGainHighWarning,
       "pmoailAlmClientInputPwrLowWarning": pmoailAlmClientInputPwrLowWarning,
       "pmoailAlmClientInputPwrHighWarning": pmoailAlmClientInputPwrHighWarning,
       "pmoailAlmClientOutputPwrLowWarning": pmoailAlmClientOutputPwrLowWarning,
       "pmoailAlmClientOutputPwrHighWarning": pmoailAlmClientOutputPwrHighWarning,
       "pmoailAlmClientBiasLowWarning": pmoailAlmClientBiasLowWarning,
       "pmoailAlmClientBiasHighWarning": pmoailAlmClientBiasHighWarning,
       "pmoailAlmClientUrg": pmoailAlmClientUrg,
       "pmoailAlmclientEdfaAlarms1": pmoailAlmclientEdfaAlarms1,
       "pmoailAlmClientGainLowAlarm": pmoailAlmClientGainLowAlarm,
       "pmoailAlmClientGainHighAlarm": pmoailAlmClientGainHighAlarm,
       "pmoailAlmClientInputPwrLowAlarm": pmoailAlmClientInputPwrLowAlarm,
       "pmoailAlmClientInputPwrHighAlarm": pmoailAlmClientInputPwrHighAlarm,
       "pmoailAlmClientOutputPwrLowAlarm": pmoailAlmClientOutputPwrLowAlarm,
       "pmoailAlmClientOutputPwrHighAlarm": pmoailAlmClientOutputPwrHighAlarm,
       "pmoailAlmClientBiasLowAlarm": pmoailAlmClientBiasLowAlarm,
       "pmoailAlmClientBiasHighAlarm": pmoailAlmClientBiasHighAlarm,
       "pmoailAlmClientCrit": pmoailAlmClientCrit,
       "pmoailAlmsynthAlm8": pmoailAlmsynthAlm8,
       "pmoailAlmClientHwFail": pmoailAlmClientHwFail,
       "pmoailAlmClientTxOff": pmoailAlmClientTxOff,
       "pmoailAlmClientDdmWarning": pmoailAlmClientDdmWarning,
       "pmoailAlmClientDdmAlm": pmoailAlmClientDdmAlm,
       "pmoailAlmClientFail": pmoailAlmClientFail,
       "pmoailAlmclientEdfaAlarms2": pmoailAlmclientEdfaAlarms2,
       "pmoailAlmClientEdfaNr": pmoailAlmClientEdfaNr,
       "pmoailAlmClientEdfaTecFail": pmoailAlmClientEdfaTecFail,
       "pmoailAlmClientEdfaLaserFail": pmoailAlmClientEdfaLaserFail,
       "pmoailAlmClientEdfaLos": pmoailAlmClientEdfaLos,
       "pmoailAlmClientExtPumpEdfaLowCurrent": pmoailAlmClientExtPumpEdfaLowCurrent,
       "pmoailAlmLine": pmoailAlmLine,
       "pmoailAlmLineNurg": pmoailAlmLineNurg,
       "pmoailAlmlineEdfaWarnings": pmoailAlmlineEdfaWarnings,
       "pmoailAlmLineGainLowWarning": pmoailAlmLineGainLowWarning,
       "pmoailAlmLineGainHighWarning": pmoailAlmLineGainHighWarning,
       "pmoailAlmLineInputPwrLowWarning": pmoailAlmLineInputPwrLowWarning,
       "pmoailAlmLineInputPwrHighWarning": pmoailAlmLineInputPwrHighWarning,
       "pmoailAlmLineOutputPwrLowWarning": pmoailAlmLineOutputPwrLowWarning,
       "pmoailAlmLineOutputPwrHighWarning": pmoailAlmLineOutputPwrHighWarning,
       "pmoailAlmLineBiasLowWarning": pmoailAlmLineBiasLowWarning,
       "pmoailAlmLineBiasHighWarning": pmoailAlmLineBiasHighWarning,
       "pmoailAlmLineUrg": pmoailAlmLineUrg,
       "pmoailAlmlineEdfaAlarms1": pmoailAlmlineEdfaAlarms1,
       "pmoailAlmLineGainLowAlarm": pmoailAlmLineGainLowAlarm,
       "pmoailAlmLineGainHighAlarm": pmoailAlmLineGainHighAlarm,
       "pmoailAlmLineInputPwrLowAlarm": pmoailAlmLineInputPwrLowAlarm,
       "pmoailAlmLineInputPwrHighAlarm": pmoailAlmLineInputPwrHighAlarm,
       "pmoailAlmLineOutputPwrLowAlarm": pmoailAlmLineOutputPwrLowAlarm,
       "pmoailAlmLineOutputPwrHighAlarm": pmoailAlmLineOutputPwrHighAlarm,
       "pmoailAlmLineBiasLowAlarm": pmoailAlmLineBiasLowAlarm,
       "pmoailAlmLineBiasHighAlarm": pmoailAlmLineBiasHighAlarm,
       "pmoailAlmLineCrit": pmoailAlmLineCrit,
       "pmoailAlmsynthAlm7": pmoailAlmsynthAlm7,
       "pmoailAlmLineHwFail": pmoailAlmLineHwFail,
       "pmoailAlmLineTxOff": pmoailAlmLineTxOff,
       "pmoailAlmLineDdmWarning": pmoailAlmLineDdmWarning,
       "pmoailAlmLineDdmAlm": pmoailAlmLineDdmAlm,
       "pmoailAlmLineFail": pmoailAlmLineFail,
       "pmoailAlmlineEdfaAlarms2": pmoailAlmlineEdfaAlarms2,
       "pmoailAlmLineEdfaNr": pmoailAlmLineEdfaNr,
       "pmoailAlmLineEdfaTecFail": pmoailAlmLineEdfaTecFail,
       "pmoailAlmLineEdfaLaserFail": pmoailAlmLineEdfaLaserFail,
       "pmoailAlmLineEdfaLos": pmoailAlmLineEdfaLos,
       "pmoailAlmLineExtPumpEdfaLowCurrent": pmoailAlmLineExtPumpEdfaLowCurrent,
       "pmoailmeasures": pmoailmeasures,
       "pmoailMesrOther": pmoailMesrOther,
       "pmoailMesrtempMeas": pmoailMesrtempMeas,
       "pmoailMesr3v3Meas": pmoailMesr3v3Meas,
       "pmoailMesrClient": pmoailMesrClient,
       "pmoailMesrclientEdfaBiasMeas": pmoailMesrclientEdfaBiasMeas,
       "pmoailMesrclientEdfaTxpwrMeas": pmoailMesrclientEdfaTxpwrMeas,
       "pmoailMesrclientEdfaRxpwrMeas": pmoailMesrclientEdfaRxpwrMeas,
       "pmoailMesrclientEdfaGainMeas": pmoailMesrclientEdfaGainMeas,
       "pmoailMesrLine": pmoailMesrLine,
       "pmoailMesrlineEdfaBiasMeas": pmoailMesrlineEdfaBiasMeas,
       "pmoailMesrlineEdfaTxpwrMeas": pmoailMesrlineEdfaTxpwrMeas,
       "pmoailMesrlineEdfaRxpwrMeas": pmoailMesrlineEdfaRxpwrMeas,
       "pmoailMesrlineEdfaGainMeas": pmoailMesrlineEdfaGainMeas,
       "pmoailcontrolsWrite": pmoailcontrolsWrite,
       "pmoailCtrlOther": pmoailCtrlOther,
       "pmoailCtrlsynth0": pmoailCtrlsynth0,
       "pmoailCtrlConfLoad": pmoailCtrlConfLoad,
       "pmoailCtrlConfFlash": pmoailCtrlConfFlash,
       "pmoailCtrlConfClear": pmoailCtrlConfClear,
       "pmoailCtrlswMgnt": pmoailCtrlswMgnt,
       "pmoailCtrlColdReset": pmoailCtrlColdReset,
       "pmoailCtrlWarmReset": pmoailCtrlWarmReset,
       "pmoailCtrlpowerDown": pmoailCtrlpowerDown,
       "pmoailCtrlSoftPowerDown": pmoailCtrlSoftPowerDown,
       "pmoailCtrlledTest": pmoailCtrlledTest,
       "pmoailCtrlGreenLed": pmoailCtrlGreenLed,
       "pmoailCtrlRedLed": pmoailCtrlRedLed,
       "pmoailCtrlLedOff": pmoailCtrlLedOff,
       "pmoailCtrlmaintMode": pmoailCtrlmaintMode,
       "pmoailCtrlMaintenance": pmoailCtrlMaintenance,
       "pmoailCtrlClient": pmoailCtrlClient,
       "pmoailCtrlclientEdfaLaserOff": pmoailCtrlclientEdfaLaserOff,
       "pmoailCtrlClientEdfaLaserOff": pmoailCtrlClientEdfaLaserOff,
       "pmoailCtrlclientEdfaMode": pmoailCtrlclientEdfaMode,
       "pmoailCtrlclientIlasSettingValue": pmoailCtrlclientIlasSettingValue,
       "pmoailCtrlclientPlasSettingValue": pmoailCtrlclientPlasSettingValue,
       "pmoailCtrlclientGainSettingValue": pmoailCtrlclientGainSettingValue,
       "pmoailCtrlclientEffPwrOutSettingValue": pmoailCtrlclientEffPwrOutSettingValue,
       "pmoailCtrlLine": pmoailCtrlLine,
       "pmoailCtrllineEdfaLaserOff": pmoailCtrllineEdfaLaserOff,
       "pmoailCtrlLineEdfaLaserOff": pmoailCtrlLineEdfaLaserOff,
       "pmoailCtrllineEdfaMode": pmoailCtrllineEdfaMode,
       "pmoailCtrllineIlasSettingValue": pmoailCtrllineIlasSettingValue,
       "pmoailCtrllinePlasSettingValue": pmoailCtrllinePlasSettingValue,
       "pmoailCtrllineGainSettingValue": pmoailCtrllineGainSettingValue,
       "pmoailCtrllineEffPwrOutSettingValue": pmoailCtrllineEffPwrOutSettingValue,
       "pmoailri": pmoailri,
       "pmoailRinvReloadInventory": pmoailRinvReloadInventory,
       "pmoailRinvModulePlatform": pmoailRinvModulePlatform,
       "pmoailRinvSwPlatform": pmoailRinvSwPlatform,
       "pmoailRinvSwFoa": pmoailRinvSwFoa,
       "pmoailRinvInLine1Table": pmoailRinvInLine1Table,
       "pmoailRinvInLine1Entry": pmoailRinvInLine1Entry,
       "pmoailRinvInLine1Index": pmoailRinvInLine1Index,
       "pmoailRinvInLine1": pmoailRinvInLine1,
       "pmoailRinvInLine2Table": pmoailRinvInLine2Table,
       "pmoailRinvInLine2Entry": pmoailRinvInLine2Entry,
       "pmoailRinvInLine2Index": pmoailRinvInLine2Index,
       "pmoailRinvInLine2": pmoailRinvInLine2,
       "pmoailConfig": pmoailConfig,
       "pmoailCfgNoValue": pmoailCfgNoValue,
       "pmoailtableclientStartup": pmoailtableclientStartup,
       "pmoailCfgclientEdfaLaserCtrl": pmoailCfgclientEdfaLaserCtrl,
       "pmoailCfgclientEdfaLaserMode": pmoailCfgclientEdfaLaserMode,
       "pmoailCfgLineStartUp": pmoailCfgLineStartUp,
       "pmoailtablelineStartup": pmoailtablelineStartup,
       "pmoailCfglineEdfaLaserCtrl": pmoailCfglineEdfaLaserCtrl,
       "pmoailCfglineEdfaLaserMode": pmoailCfglineEdfaLaserMode,
       "pmoailCfgLabels": pmoailCfgLabels,
       "pmoailCfgLabelclientTable": pmoailCfgLabelclientTable,
       "pmoailCfgLabelclientEntry": pmoailCfgLabelclientEntry,
       "pmoailCfgLabelclientIndex": pmoailCfgLabelclientIndex,
       "pmoailCfgLabelclientPortn": pmoailCfgLabelclientPortn,
       "pmoailCfgLabellineTable": pmoailCfgLabellineTable,
       "pmoailCfgLabellineEntry": pmoailCfgLabellineEntry,
       "pmoailCfgLabellineIndex": pmoailCfgLabellineIndex,
       "pmoailCfgLabellinePortn": pmoailCfgLabellinePortn,
       "pmoailCfgWriteConfiguration": pmoailCfgWriteConfiguration,
       "pmoailtraps": pmoailtraps,
       "pmoailtrapBoardNumber": pmoailtrapBoardNumber,
       "pmoailLineTrapNotUrgentGoesOn": pmoailLineTrapNotUrgentGoesOn,
       "pmoailLineTrapNotUrgentGoesOff": pmoailLineTrapNotUrgentGoesOff,
       "pmoailLineTrapUrgentGoesOn": pmoailLineTrapUrgentGoesOn,
       "pmoailLineTrapUrgentGoesOff": pmoailLineTrapUrgentGoesOff,
       "pmoailLineTrapCritGoesOn": pmoailLineTrapCritGoesOn,
       "pmoailLineTrapCritGoesOff": pmoailLineTrapCritGoesOff,
       "pmoailClientTrapNotUrgentGoesOn": pmoailClientTrapNotUrgentGoesOn,
       "pmoailClientTrapNotUrgentGoesOff": pmoailClientTrapNotUrgentGoesOff,
       "pmoailClientTrapUrgentGoesOn": pmoailClientTrapUrgentGoesOn,
       "pmoailClientTrapUrgentGoesOff": pmoailClientTrapUrgentGoesOff,
       "pmoailClientTrapCritGoesOn": pmoailClientTrapCritGoesOn,
       "pmoailClientTrapCritGoesOff": pmoailClientTrapCritGoesOff,
       "pmoailPowerTrapUrgentGoesOn": pmoailPowerTrapUrgentGoesOn,
       "pmoailPowerTrapUrgentGoesOff": pmoailPowerTrapUrgentGoesOff}
)
