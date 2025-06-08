# SNMP MIB module (EKINOPS-PmOa-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-PmOa-MIB.mib
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

modulepmoa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9)
)
if mibBuilder.loadTexts:
    modulepmoa.setRevisions(
        ("2006-01-05 00:00",
         "2007-11-21 00:00",
         "2009-02-05 00:00",
         "2009-04-08 00:00",
         "2009-09-14 00:00",
         "2009-12-14 00:00",
         "2010-02-24 00:00",
         "2010-07-15 00:00",
         "2010-10-29 00:00",
         "2010-11-03 00:00",
         "2012-07-04 00:00",
         "2012-10-05 00:00",
         "2014-03-26 00:00",
         "2014-11-24 00:00",
         "2016-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PmoapreampMode(TextualConvention, Integer32):
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



class PmoaboosterMode(TextualConvention, Integer32):
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

_Pmoaalarms_ObjectIdentity = ObjectIdentity
pmoaalarms = _Pmoaalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2)
)
_PmoaAlmOther_ObjectIdentity = ObjectIdentity
pmoaAlmOther = _PmoaAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1)
)
_PmoaAlmOtherNurg_ObjectIdentity = ObjectIdentity
pmoaAlmOtherNurg = _PmoaAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 1)
)
_PmoaAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pmoaAlmsynthAlm2 = _PmoaAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 1, 2)
)
_PmoaAlmConfTableSave_Type = EkiOnOff
_PmoaAlmConfTableSave_Object = MibScalar
pmoaAlmConfTableSave = _PmoaAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 1, 2, 1),
    _PmoaAlmConfTableSave_Type()
)
pmoaAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmConfTableSave.setStatus("current")
_PmoaAlmInvUpload_Type = EkiOnOff
_PmoaAlmInvUpload_Object = MibScalar
pmoaAlmInvUpload = _PmoaAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 1, 2, 2),
    _PmoaAlmInvUpload_Type()
)
pmoaAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmInvUpload.setStatus("current")
_PmoaAlmConfTableLoad_Type = EkiOnOff
_PmoaAlmConfTableLoad_Object = MibScalar
pmoaAlmConfTableLoad = _PmoaAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 1, 2, 3),
    _PmoaAlmConfTableLoad_Type()
)
pmoaAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmConfTableLoad.setStatus("current")
_PmoaAlmfoaWarnings_ObjectIdentity = ObjectIdentity
pmoaAlmfoaWarnings = _PmoaAlmfoaWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 1, 75)
)
_PmoaAlm3v3LowWarning_Type = EkiOnOff
_PmoaAlm3v3LowWarning_Object = MibScalar
pmoaAlm3v3LowWarning = _PmoaAlm3v3LowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 1, 75, 5),
    _PmoaAlm3v3LowWarning_Type()
)
pmoaAlm3v3LowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlm3v3LowWarning.setStatus("current")
_PmoaAlm3v3HighWarning_Type = EkiOnOff
_PmoaAlm3v3HighWarning_Object = MibScalar
pmoaAlm3v3HighWarning = _PmoaAlm3v3HighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 1, 75, 6),
    _PmoaAlm3v3HighWarning_Type()
)
pmoaAlm3v3HighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlm3v3HighWarning.setStatus("current")
_PmoaAlmTermpLowWarning_Type = EkiOnOff
_PmoaAlmTermpLowWarning_Object = MibScalar
pmoaAlmTermpLowWarning = _PmoaAlmTermpLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 1, 75, 7),
    _PmoaAlmTermpLowWarning_Type()
)
pmoaAlmTermpLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmTermpLowWarning.setStatus("current")
_PmoaAlmTempHighWarning_Type = EkiOnOff
_PmoaAlmTempHighWarning_Object = MibScalar
pmoaAlmTempHighWarning = _PmoaAlmTempHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 1, 75, 8),
    _PmoaAlmTempHighWarning_Type()
)
pmoaAlmTempHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmTempHighWarning.setStatus("current")
_PmoaAlmOtherUrg_ObjectIdentity = ObjectIdentity
pmoaAlmOtherUrg = _PmoaAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 2)
)
_PmoaAlmfoaAlarms_ObjectIdentity = ObjectIdentity
pmoaAlmfoaAlarms = _PmoaAlmfoaAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 2, 74)
)
_PmoaAlm3v3LowAlarm_Type = EkiOnOff
_PmoaAlm3v3LowAlarm_Object = MibScalar
pmoaAlm3v3LowAlarm = _PmoaAlm3v3LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 2, 74, 5),
    _PmoaAlm3v3LowAlarm_Type()
)
pmoaAlm3v3LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlm3v3LowAlarm.setStatus("current")
_PmoaAlm3v3HighAlarm_Type = EkiOnOff
_PmoaAlm3v3HighAlarm_Object = MibScalar
pmoaAlm3v3HighAlarm = _PmoaAlm3v3HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 2, 74, 6),
    _PmoaAlm3v3HighAlarm_Type()
)
pmoaAlm3v3HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlm3v3HighAlarm.setStatus("current")
_PmoaAlmTermpLowAlarm_Type = EkiOnOff
_PmoaAlmTermpLowAlarm_Object = MibScalar
pmoaAlmTermpLowAlarm = _PmoaAlmTermpLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 2, 74, 7),
    _PmoaAlmTermpLowAlarm_Type()
)
pmoaAlmTermpLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmTermpLowAlarm.setStatus("current")
_PmoaAlmTempHighAlarm_Type = EkiOnOff
_PmoaAlmTempHighAlarm_Object = MibScalar
pmoaAlmTempHighAlarm = _PmoaAlmTempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 2, 74, 8),
    _PmoaAlmTempHighAlarm_Type()
)
pmoaAlmTempHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmTempHighAlarm.setStatus("current")
_PmoaAlmOtherCrit_ObjectIdentity = ObjectIdentity
pmoaAlmOtherCrit = _PmoaAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 3)
)
_PmoaAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmoaAlmsynthAlm0 = _PmoaAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 3, 0)
)
_PmoaAlmMaintenanceMode_Type = EkiOnOff
_PmoaAlmMaintenanceMode_Object = MibScalar
pmoaAlmMaintenanceMode = _PmoaAlmMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 3, 0, 1),
    _PmoaAlmMaintenanceMode_Type()
)
pmoaAlmMaintenanceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmMaintenanceMode.setStatus("current")
_PmoaAlmModGlobFail_Type = EkiOnOff
_PmoaAlmModGlobFail_Object = MibScalar
pmoaAlmModGlobFail = _PmoaAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 3, 0, 9),
    _PmoaAlmModGlobFail_Type()
)
pmoaAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmModGlobFail.setStatus("current")
_PmoaAlmUpEdfaInitNotCompl_Type = EkiOnOff
_PmoaAlmUpEdfaInitNotCompl_Object = MibScalar
pmoaAlmUpEdfaInitNotCompl = _PmoaAlmUpEdfaInitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 3, 0, 10),
    _PmoaAlmUpEdfaInitNotCompl_Type()
)
pmoaAlmUpEdfaInitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmUpEdfaInitNotCompl.setStatus("current")
_PmoaAlmDwEdfaInitNotCompl_Type = EkiOnOff
_PmoaAlmDwEdfaInitNotCompl_Object = MibScalar
pmoaAlmDwEdfaInitNotCompl = _PmoaAlmDwEdfaInitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 3, 0, 11),
    _PmoaAlmDwEdfaInitNotCompl_Type()
)
pmoaAlmDwEdfaInitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmDwEdfaInitNotCompl.setStatus("current")
_PmoaAlmExtPumpNotLocked_Type = EkiOnOff
_PmoaAlmExtPumpNotLocked_Object = MibScalar
pmoaAlmExtPumpNotLocked = _PmoaAlmExtPumpNotLocked_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 3, 0, 12),
    _PmoaAlmExtPumpNotLocked_Type()
)
pmoaAlmExtPumpNotLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmExtPumpNotLocked.setStatus("current")
_PmoaAlmDefFuseA_Type = EkiOnOff
_PmoaAlmDefFuseA_Object = MibScalar
pmoaAlmDefFuseA = _PmoaAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 3, 0, 15),
    _PmoaAlmDefFuseA_Type()
)
pmoaAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmDefFuseA.setStatus("current")
_PmoaAlmDefFuseB_Type = EkiOnOff
_PmoaAlmDefFuseB_Object = MibScalar
pmoaAlmDefFuseB = _PmoaAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 1, 3, 0, 16),
    _PmoaAlmDefFuseB_Type()
)
pmoaAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmDefFuseB.setStatus("current")
_PmoaAlmClient_ObjectIdentity = ObjectIdentity
pmoaAlmClient = _PmoaAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2)
)
_PmoaAlmClientNurg_ObjectIdentity = ObjectIdentity
pmoaAlmClientNurg = _PmoaAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 1)
)
_PmoaAlmclientEdfaWarnings_ObjectIdentity = ObjectIdentity
pmoaAlmclientEdfaWarnings = _PmoaAlmclientEdfaWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 1, 33)
)
_PmoaAlmClientGainLowWarning_Type = EkiOnOff
_PmoaAlmClientGainLowWarning_Object = MibScalar
pmoaAlmClientGainLowWarning = _PmoaAlmClientGainLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 1, 33, 1),
    _PmoaAlmClientGainLowWarning_Type()
)
pmoaAlmClientGainLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientGainLowWarning.setStatus("current")
_PmoaAlmClientGainHighWarning_Type = EkiOnOff
_PmoaAlmClientGainHighWarning_Object = MibScalar
pmoaAlmClientGainHighWarning = _PmoaAlmClientGainHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 1, 33, 2),
    _PmoaAlmClientGainHighWarning_Type()
)
pmoaAlmClientGainHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientGainHighWarning.setStatus("current")
_PmoaAlmClientInputPwrLowWarning_Type = EkiOnOff
_PmoaAlmClientInputPwrLowWarning_Object = MibScalar
pmoaAlmClientInputPwrLowWarning = _PmoaAlmClientInputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 1, 33, 3),
    _PmoaAlmClientInputPwrLowWarning_Type()
)
pmoaAlmClientInputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientInputPwrLowWarning.setStatus("current")
_PmoaAlmClientInputPwrHighWarning_Type = EkiOnOff
_PmoaAlmClientInputPwrHighWarning_Object = MibScalar
pmoaAlmClientInputPwrHighWarning = _PmoaAlmClientInputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 1, 33, 4),
    _PmoaAlmClientInputPwrHighWarning_Type()
)
pmoaAlmClientInputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientInputPwrHighWarning.setStatus("current")
_PmoaAlmClientOutputPwrLowWarning_Type = EkiOnOff
_PmoaAlmClientOutputPwrLowWarning_Object = MibScalar
pmoaAlmClientOutputPwrLowWarning = _PmoaAlmClientOutputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 1, 33, 5),
    _PmoaAlmClientOutputPwrLowWarning_Type()
)
pmoaAlmClientOutputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientOutputPwrLowWarning.setStatus("current")
_PmoaAlmClientOutputPwrHighWarning_Type = EkiOnOff
_PmoaAlmClientOutputPwrHighWarning_Object = MibScalar
pmoaAlmClientOutputPwrHighWarning = _PmoaAlmClientOutputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 1, 33, 6),
    _PmoaAlmClientOutputPwrHighWarning_Type()
)
pmoaAlmClientOutputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientOutputPwrHighWarning.setStatus("current")
_PmoaAlmClientBiasLowWarning_Type = EkiOnOff
_PmoaAlmClientBiasLowWarning_Object = MibScalar
pmoaAlmClientBiasLowWarning = _PmoaAlmClientBiasLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 1, 33, 7),
    _PmoaAlmClientBiasLowWarning_Type()
)
pmoaAlmClientBiasLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientBiasLowWarning.setStatus("current")
_PmoaAlmClientBiasHighWarning_Type = EkiOnOff
_PmoaAlmClientBiasHighWarning_Object = MibScalar
pmoaAlmClientBiasHighWarning = _PmoaAlmClientBiasHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 1, 33, 8),
    _PmoaAlmClientBiasHighWarning_Type()
)
pmoaAlmClientBiasHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientBiasHighWarning.setStatus("current")
_PmoaAlmClientUrg_ObjectIdentity = ObjectIdentity
pmoaAlmClientUrg = _PmoaAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 2)
)
_PmoaAlmclientEdfaAlarms1_ObjectIdentity = ObjectIdentity
pmoaAlmclientEdfaAlarms1 = _PmoaAlmclientEdfaAlarms1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 2, 32)
)
_PmoaAlmClientGainLowAlarm_Type = EkiOnOff
_PmoaAlmClientGainLowAlarm_Object = MibScalar
pmoaAlmClientGainLowAlarm = _PmoaAlmClientGainLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 2, 32, 1),
    _PmoaAlmClientGainLowAlarm_Type()
)
pmoaAlmClientGainLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientGainLowAlarm.setStatus("current")
_PmoaAlmClientGainHighAlarm_Type = EkiOnOff
_PmoaAlmClientGainHighAlarm_Object = MibScalar
pmoaAlmClientGainHighAlarm = _PmoaAlmClientGainHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 2, 32, 2),
    _PmoaAlmClientGainHighAlarm_Type()
)
pmoaAlmClientGainHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientGainHighAlarm.setStatus("current")
_PmoaAlmClientInputPwrLowAlarm_Type = EkiOnOff
_PmoaAlmClientInputPwrLowAlarm_Object = MibScalar
pmoaAlmClientInputPwrLowAlarm = _PmoaAlmClientInputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 2, 32, 3),
    _PmoaAlmClientInputPwrLowAlarm_Type()
)
pmoaAlmClientInputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientInputPwrLowAlarm.setStatus("current")
_PmoaAlmClientInputPwrHighAlarm_Type = EkiOnOff
_PmoaAlmClientInputPwrHighAlarm_Object = MibScalar
pmoaAlmClientInputPwrHighAlarm = _PmoaAlmClientInputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 2, 32, 4),
    _PmoaAlmClientInputPwrHighAlarm_Type()
)
pmoaAlmClientInputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientInputPwrHighAlarm.setStatus("current")
_PmoaAlmClientOutputPwrLowAlarm_Type = EkiOnOff
_PmoaAlmClientOutputPwrLowAlarm_Object = MibScalar
pmoaAlmClientOutputPwrLowAlarm = _PmoaAlmClientOutputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 2, 32, 5),
    _PmoaAlmClientOutputPwrLowAlarm_Type()
)
pmoaAlmClientOutputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientOutputPwrLowAlarm.setStatus("current")
_PmoaAlmClientOutputPwrHighAlarm_Type = EkiOnOff
_PmoaAlmClientOutputPwrHighAlarm_Object = MibScalar
pmoaAlmClientOutputPwrHighAlarm = _PmoaAlmClientOutputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 2, 32, 6),
    _PmoaAlmClientOutputPwrHighAlarm_Type()
)
pmoaAlmClientOutputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientOutputPwrHighAlarm.setStatus("current")
_PmoaAlmClientBiasLowAlarm_Type = EkiOnOff
_PmoaAlmClientBiasLowAlarm_Object = MibScalar
pmoaAlmClientBiasLowAlarm = _PmoaAlmClientBiasLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 2, 32, 7),
    _PmoaAlmClientBiasLowAlarm_Type()
)
pmoaAlmClientBiasLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientBiasLowAlarm.setStatus("current")
_PmoaAlmClientBiasHighAlarm_Type = EkiOnOff
_PmoaAlmClientBiasHighAlarm_Object = MibScalar
pmoaAlmClientBiasHighAlarm = _PmoaAlmClientBiasHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 2, 32, 8),
    _PmoaAlmClientBiasHighAlarm_Type()
)
pmoaAlmClientBiasHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientBiasHighAlarm.setStatus("current")
_PmoaAlmClientCrit_ObjectIdentity = ObjectIdentity
pmoaAlmClientCrit = _PmoaAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 3)
)
_PmoaAlmsynthAlm8_ObjectIdentity = ObjectIdentity
pmoaAlmsynthAlm8 = _PmoaAlmsynthAlm8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 3, 8)
)
_PmoaAlmClientHwFail_Type = EkiOnOff
_PmoaAlmClientHwFail_Object = MibScalar
pmoaAlmClientHwFail = _PmoaAlmClientHwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 3, 8, 4),
    _PmoaAlmClientHwFail_Type()
)
pmoaAlmClientHwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientHwFail.setStatus("current")
_PmoaAlmClientTxOff_Type = EkiOnOff
_PmoaAlmClientTxOff_Object = MibScalar
pmoaAlmClientTxOff = _PmoaAlmClientTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 3, 8, 5),
    _PmoaAlmClientTxOff_Type()
)
pmoaAlmClientTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientTxOff.setStatus("current")
_PmoaAlmClientDdmWarning_Type = EkiOnOff
_PmoaAlmClientDdmWarning_Object = MibScalar
pmoaAlmClientDdmWarning = _PmoaAlmClientDdmWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 3, 8, 9),
    _PmoaAlmClientDdmWarning_Type()
)
pmoaAlmClientDdmWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientDdmWarning.setStatus("current")
_PmoaAlmClientDdmAlm_Type = EkiOnOff
_PmoaAlmClientDdmAlm_Object = MibScalar
pmoaAlmClientDdmAlm = _PmoaAlmClientDdmAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 3, 8, 10),
    _PmoaAlmClientDdmAlm_Type()
)
pmoaAlmClientDdmAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientDdmAlm.setStatus("current")
_PmoaAlmClientFail_Type = EkiOnOff
_PmoaAlmClientFail_Object = MibScalar
pmoaAlmClientFail = _PmoaAlmClientFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 3, 8, 12),
    _PmoaAlmClientFail_Type()
)
pmoaAlmClientFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientFail.setStatus("current")
_PmoaAlmclientEdfaAlarms2_ObjectIdentity = ObjectIdentity
pmoaAlmclientEdfaAlarms2 = _PmoaAlmclientEdfaAlarms2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 3, 35)
)
_PmoaAlmClientEdfaNr_Type = EkiOnOff
_PmoaAlmClientEdfaNr_Object = MibScalar
pmoaAlmClientEdfaNr = _PmoaAlmClientEdfaNr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 3, 35, 1),
    _PmoaAlmClientEdfaNr_Type()
)
pmoaAlmClientEdfaNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientEdfaNr.setStatus("current")
_PmoaAlmClientEdfaTecFail_Type = EkiOnOff
_PmoaAlmClientEdfaTecFail_Object = MibScalar
pmoaAlmClientEdfaTecFail = _PmoaAlmClientEdfaTecFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 3, 35, 2),
    _PmoaAlmClientEdfaTecFail_Type()
)
pmoaAlmClientEdfaTecFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientEdfaTecFail.setStatus("current")
_PmoaAlmClientEdfaLaserFail_Type = EkiOnOff
_PmoaAlmClientEdfaLaserFail_Object = MibScalar
pmoaAlmClientEdfaLaserFail = _PmoaAlmClientEdfaLaserFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 3, 35, 3),
    _PmoaAlmClientEdfaLaserFail_Type()
)
pmoaAlmClientEdfaLaserFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientEdfaLaserFail.setStatus("current")
_PmoaAlmClientEdfaLos_Type = EkiOnOff
_PmoaAlmClientEdfaLos_Object = MibScalar
pmoaAlmClientEdfaLos = _PmoaAlmClientEdfaLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 3, 35, 4),
    _PmoaAlmClientEdfaLos_Type()
)
pmoaAlmClientEdfaLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientEdfaLos.setStatus("current")
_PmoaAlmClientExtPumpEdfaLowCurrent_Type = EkiOnOff
_PmoaAlmClientExtPumpEdfaLowCurrent_Object = MibScalar
pmoaAlmClientExtPumpEdfaLowCurrent = _PmoaAlmClientExtPumpEdfaLowCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 2, 3, 35, 5),
    _PmoaAlmClientExtPumpEdfaLowCurrent_Type()
)
pmoaAlmClientExtPumpEdfaLowCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmClientExtPumpEdfaLowCurrent.setStatus("current")
_PmoaAlmLine_ObjectIdentity = ObjectIdentity
pmoaAlmLine = _PmoaAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3)
)
_PmoaAlmLineNurg_ObjectIdentity = ObjectIdentity
pmoaAlmLineNurg = _PmoaAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 1)
)
_PmoaAlmlineEdfaWarnings_ObjectIdentity = ObjectIdentity
pmoaAlmlineEdfaWarnings = _PmoaAlmlineEdfaWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 1, 41)
)
_PmoaAlmLineGainLowWarning_Type = EkiOnOff
_PmoaAlmLineGainLowWarning_Object = MibScalar
pmoaAlmLineGainLowWarning = _PmoaAlmLineGainLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 1, 41, 1),
    _PmoaAlmLineGainLowWarning_Type()
)
pmoaAlmLineGainLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineGainLowWarning.setStatus("current")
_PmoaAlmLineGainHighWarning_Type = EkiOnOff
_PmoaAlmLineGainHighWarning_Object = MibScalar
pmoaAlmLineGainHighWarning = _PmoaAlmLineGainHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 1, 41, 2),
    _PmoaAlmLineGainHighWarning_Type()
)
pmoaAlmLineGainHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineGainHighWarning.setStatus("current")
_PmoaAlmLineInputPwrLowWarning_Type = EkiOnOff
_PmoaAlmLineInputPwrLowWarning_Object = MibScalar
pmoaAlmLineInputPwrLowWarning = _PmoaAlmLineInputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 1, 41, 3),
    _PmoaAlmLineInputPwrLowWarning_Type()
)
pmoaAlmLineInputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineInputPwrLowWarning.setStatus("current")
_PmoaAlmLineInputPwrHighWarning_Type = EkiOnOff
_PmoaAlmLineInputPwrHighWarning_Object = MibScalar
pmoaAlmLineInputPwrHighWarning = _PmoaAlmLineInputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 1, 41, 4),
    _PmoaAlmLineInputPwrHighWarning_Type()
)
pmoaAlmLineInputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineInputPwrHighWarning.setStatus("current")
_PmoaAlmLineOutputPwrLowWarning_Type = EkiOnOff
_PmoaAlmLineOutputPwrLowWarning_Object = MibScalar
pmoaAlmLineOutputPwrLowWarning = _PmoaAlmLineOutputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 1, 41, 5),
    _PmoaAlmLineOutputPwrLowWarning_Type()
)
pmoaAlmLineOutputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineOutputPwrLowWarning.setStatus("current")
_PmoaAlmLineOutputPwrHighWarning_Type = EkiOnOff
_PmoaAlmLineOutputPwrHighWarning_Object = MibScalar
pmoaAlmLineOutputPwrHighWarning = _PmoaAlmLineOutputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 1, 41, 6),
    _PmoaAlmLineOutputPwrHighWarning_Type()
)
pmoaAlmLineOutputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineOutputPwrHighWarning.setStatus("current")
_PmoaAlmLineBiasLowWarning_Type = EkiOnOff
_PmoaAlmLineBiasLowWarning_Object = MibScalar
pmoaAlmLineBiasLowWarning = _PmoaAlmLineBiasLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 1, 41, 7),
    _PmoaAlmLineBiasLowWarning_Type()
)
pmoaAlmLineBiasLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineBiasLowWarning.setStatus("current")
_PmoaAlmLineBiasHighWarning_Type = EkiOnOff
_PmoaAlmLineBiasHighWarning_Object = MibScalar
pmoaAlmLineBiasHighWarning = _PmoaAlmLineBiasHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 1, 41, 8),
    _PmoaAlmLineBiasHighWarning_Type()
)
pmoaAlmLineBiasHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineBiasHighWarning.setStatus("current")
_PmoaAlmLineUrg_ObjectIdentity = ObjectIdentity
pmoaAlmLineUrg = _PmoaAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 2)
)
_PmoaAlmlineEdfaAlarms1_ObjectIdentity = ObjectIdentity
pmoaAlmlineEdfaAlarms1 = _PmoaAlmlineEdfaAlarms1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 2, 40)
)
_PmoaAlmLineGainLowAlarm_Type = EkiOnOff
_PmoaAlmLineGainLowAlarm_Object = MibScalar
pmoaAlmLineGainLowAlarm = _PmoaAlmLineGainLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 2, 40, 1),
    _PmoaAlmLineGainLowAlarm_Type()
)
pmoaAlmLineGainLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineGainLowAlarm.setStatus("current")
_PmoaAlmLineGainHighAlarm_Type = EkiOnOff
_PmoaAlmLineGainHighAlarm_Object = MibScalar
pmoaAlmLineGainHighAlarm = _PmoaAlmLineGainHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 2, 40, 2),
    _PmoaAlmLineGainHighAlarm_Type()
)
pmoaAlmLineGainHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineGainHighAlarm.setStatus("current")
_PmoaAlmLineInputPwrLowAlarm_Type = EkiOnOff
_PmoaAlmLineInputPwrLowAlarm_Object = MibScalar
pmoaAlmLineInputPwrLowAlarm = _PmoaAlmLineInputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 2, 40, 3),
    _PmoaAlmLineInputPwrLowAlarm_Type()
)
pmoaAlmLineInputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineInputPwrLowAlarm.setStatus("current")
_PmoaAlmLineInputPwrHighAlarm_Type = EkiOnOff
_PmoaAlmLineInputPwrHighAlarm_Object = MibScalar
pmoaAlmLineInputPwrHighAlarm = _PmoaAlmLineInputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 2, 40, 4),
    _PmoaAlmLineInputPwrHighAlarm_Type()
)
pmoaAlmLineInputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineInputPwrHighAlarm.setStatus("current")
_PmoaAlmLineOutputPwrLowAlarm_Type = EkiOnOff
_PmoaAlmLineOutputPwrLowAlarm_Object = MibScalar
pmoaAlmLineOutputPwrLowAlarm = _PmoaAlmLineOutputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 2, 40, 5),
    _PmoaAlmLineOutputPwrLowAlarm_Type()
)
pmoaAlmLineOutputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineOutputPwrLowAlarm.setStatus("current")
_PmoaAlmLineOutputPwrHighAlarm_Type = EkiOnOff
_PmoaAlmLineOutputPwrHighAlarm_Object = MibScalar
pmoaAlmLineOutputPwrHighAlarm = _PmoaAlmLineOutputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 2, 40, 6),
    _PmoaAlmLineOutputPwrHighAlarm_Type()
)
pmoaAlmLineOutputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineOutputPwrHighAlarm.setStatus("current")
_PmoaAlmLineBiasLowAlarm_Type = EkiOnOff
_PmoaAlmLineBiasLowAlarm_Object = MibScalar
pmoaAlmLineBiasLowAlarm = _PmoaAlmLineBiasLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 2, 40, 7),
    _PmoaAlmLineBiasLowAlarm_Type()
)
pmoaAlmLineBiasLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineBiasLowAlarm.setStatus("current")
_PmoaAlmLineBiasHighAlarm_Type = EkiOnOff
_PmoaAlmLineBiasHighAlarm_Object = MibScalar
pmoaAlmLineBiasHighAlarm = _PmoaAlmLineBiasHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 2, 40, 8),
    _PmoaAlmLineBiasHighAlarm_Type()
)
pmoaAlmLineBiasHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineBiasHighAlarm.setStatus("current")
_PmoaAlmLineCrit_ObjectIdentity = ObjectIdentity
pmoaAlmLineCrit = _PmoaAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 3)
)
_PmoaAlmsynthAlm7_ObjectIdentity = ObjectIdentity
pmoaAlmsynthAlm7 = _PmoaAlmsynthAlm7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 3, 7)
)
_PmoaAlmLineHwFail_Type = EkiOnOff
_PmoaAlmLineHwFail_Object = MibScalar
pmoaAlmLineHwFail = _PmoaAlmLineHwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 3, 7, 4),
    _PmoaAlmLineHwFail_Type()
)
pmoaAlmLineHwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineHwFail.setStatus("current")
_PmoaAlmLineTxOff_Type = EkiOnOff
_PmoaAlmLineTxOff_Object = MibScalar
pmoaAlmLineTxOff = _PmoaAlmLineTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 3, 7, 5),
    _PmoaAlmLineTxOff_Type()
)
pmoaAlmLineTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineTxOff.setStatus("current")
_PmoaAlmLineDdmWarning_Type = EkiOnOff
_PmoaAlmLineDdmWarning_Object = MibScalar
pmoaAlmLineDdmWarning = _PmoaAlmLineDdmWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 3, 7, 9),
    _PmoaAlmLineDdmWarning_Type()
)
pmoaAlmLineDdmWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineDdmWarning.setStatus("current")
_PmoaAlmLineDdmAlm_Type = EkiOnOff
_PmoaAlmLineDdmAlm_Object = MibScalar
pmoaAlmLineDdmAlm = _PmoaAlmLineDdmAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 3, 7, 10),
    _PmoaAlmLineDdmAlm_Type()
)
pmoaAlmLineDdmAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineDdmAlm.setStatus("current")
_PmoaAlmLineFail_Type = EkiOnOff
_PmoaAlmLineFail_Object = MibScalar
pmoaAlmLineFail = _PmoaAlmLineFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 3, 7, 12),
    _PmoaAlmLineFail_Type()
)
pmoaAlmLineFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineFail.setStatus("current")
_PmoaAlmlineEdfaAlarms2_ObjectIdentity = ObjectIdentity
pmoaAlmlineEdfaAlarms2 = _PmoaAlmlineEdfaAlarms2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 3, 43)
)
_PmoaAlmLineEdfaNr_Type = EkiOnOff
_PmoaAlmLineEdfaNr_Object = MibScalar
pmoaAlmLineEdfaNr = _PmoaAlmLineEdfaNr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 3, 43, 1),
    _PmoaAlmLineEdfaNr_Type()
)
pmoaAlmLineEdfaNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineEdfaNr.setStatus("current")
_PmoaAlmLineEdfaTecFail_Type = EkiOnOff
_PmoaAlmLineEdfaTecFail_Object = MibScalar
pmoaAlmLineEdfaTecFail = _PmoaAlmLineEdfaTecFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 3, 43, 2),
    _PmoaAlmLineEdfaTecFail_Type()
)
pmoaAlmLineEdfaTecFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineEdfaTecFail.setStatus("current")
_PmoaAlmLineEdfaLaserFail_Type = EkiOnOff
_PmoaAlmLineEdfaLaserFail_Object = MibScalar
pmoaAlmLineEdfaLaserFail = _PmoaAlmLineEdfaLaserFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 3, 43, 3),
    _PmoaAlmLineEdfaLaserFail_Type()
)
pmoaAlmLineEdfaLaserFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineEdfaLaserFail.setStatus("current")
_PmoaAlmLineEdfaLos_Type = EkiOnOff
_PmoaAlmLineEdfaLos_Object = MibScalar
pmoaAlmLineEdfaLos = _PmoaAlmLineEdfaLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 3, 43, 4),
    _PmoaAlmLineEdfaLos_Type()
)
pmoaAlmLineEdfaLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineEdfaLos.setStatus("current")
_PmoaAlmLineExtPumpEdfaLowCurrent_Type = EkiOnOff
_PmoaAlmLineExtPumpEdfaLowCurrent_Object = MibScalar
pmoaAlmLineExtPumpEdfaLowCurrent = _PmoaAlmLineExtPumpEdfaLowCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 2, 3, 3, 43, 5),
    _PmoaAlmLineExtPumpEdfaLowCurrent_Type()
)
pmoaAlmLineExtPumpEdfaLowCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaAlmLineExtPumpEdfaLowCurrent.setStatus("current")
_Pmoameasures_ObjectIdentity = ObjectIdentity
pmoameasures = _Pmoameasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 3)
)
_PmoaMesrOther_ObjectIdentity = ObjectIdentity
pmoaMesrOther = _PmoaMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 3, 1)
)


class _PmoaMesrtempMeas_Type(Integer32):
    """Custom type pmoaMesrtempMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoaMesrtempMeas_Type.__name__ = "Integer32"
_PmoaMesrtempMeas_Object = MibScalar
pmoaMesrtempMeas = _PmoaMesrtempMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 3, 1, 72),
    _PmoaMesrtempMeas_Type()
)
pmoaMesrtempMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaMesrtempMeas.setStatus("current")


class _PmoaMesr3v3Meas_Type(Integer32):
    """Custom type pmoaMesr3v3Meas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoaMesr3v3Meas_Type.__name__ = "Integer32"
_PmoaMesr3v3Meas_Object = MibScalar
pmoaMesr3v3Meas = _PmoaMesr3v3Meas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 3, 1, 73),
    _PmoaMesr3v3Meas_Type()
)
pmoaMesr3v3Meas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaMesr3v3Meas.setStatus("current")
_PmoaMesrClient_ObjectIdentity = ObjectIdentity
pmoaMesrClient = _PmoaMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 3, 2)
)


class _PmoaMesrclientEdfaBiasMeas_Type(Integer32):
    """Custom type pmoaMesrclientEdfaBiasMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoaMesrclientEdfaBiasMeas_Type.__name__ = "Integer32"
_PmoaMesrclientEdfaBiasMeas_Object = MibScalar
pmoaMesrclientEdfaBiasMeas = _PmoaMesrclientEdfaBiasMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 3, 2, 32),
    _PmoaMesrclientEdfaBiasMeas_Type()
)
pmoaMesrclientEdfaBiasMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaMesrclientEdfaBiasMeas.setStatus("current")


class _PmoaMesrclientEdfaTxpwrMeas_Type(Integer32):
    """Custom type pmoaMesrclientEdfaTxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoaMesrclientEdfaTxpwrMeas_Type.__name__ = "Integer32"
_PmoaMesrclientEdfaTxpwrMeas_Object = MibScalar
pmoaMesrclientEdfaTxpwrMeas = _PmoaMesrclientEdfaTxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 3, 2, 33),
    _PmoaMesrclientEdfaTxpwrMeas_Type()
)
pmoaMesrclientEdfaTxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaMesrclientEdfaTxpwrMeas.setStatus("current")


class _PmoaMesrclientEdfaRxpwrMeas_Type(Integer32):
    """Custom type pmoaMesrclientEdfaRxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoaMesrclientEdfaRxpwrMeas_Type.__name__ = "Integer32"
_PmoaMesrclientEdfaRxpwrMeas_Object = MibScalar
pmoaMesrclientEdfaRxpwrMeas = _PmoaMesrclientEdfaRxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 3, 2, 34),
    _PmoaMesrclientEdfaRxpwrMeas_Type()
)
pmoaMesrclientEdfaRxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaMesrclientEdfaRxpwrMeas.setStatus("current")


class _PmoaMesrclientEdfaGainMeas_Type(Integer32):
    """Custom type pmoaMesrclientEdfaGainMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoaMesrclientEdfaGainMeas_Type.__name__ = "Integer32"
_PmoaMesrclientEdfaGainMeas_Object = MibScalar
pmoaMesrclientEdfaGainMeas = _PmoaMesrclientEdfaGainMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 3, 2, 35),
    _PmoaMesrclientEdfaGainMeas_Type()
)
pmoaMesrclientEdfaGainMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaMesrclientEdfaGainMeas.setStatus("current")
_PmoaMesrLine_ObjectIdentity = ObjectIdentity
pmoaMesrLine = _PmoaMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 3, 3)
)


class _PmoaMesrlineEdfaBiasMeas_Type(Integer32):
    """Custom type pmoaMesrlineEdfaBiasMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoaMesrlineEdfaBiasMeas_Type.__name__ = "Integer32"
_PmoaMesrlineEdfaBiasMeas_Object = MibScalar
pmoaMesrlineEdfaBiasMeas = _PmoaMesrlineEdfaBiasMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 3, 3, 40),
    _PmoaMesrlineEdfaBiasMeas_Type()
)
pmoaMesrlineEdfaBiasMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaMesrlineEdfaBiasMeas.setStatus("current")


class _PmoaMesrlineEdfaTxpwrMeas_Type(Integer32):
    """Custom type pmoaMesrlineEdfaTxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoaMesrlineEdfaTxpwrMeas_Type.__name__ = "Integer32"
_PmoaMesrlineEdfaTxpwrMeas_Object = MibScalar
pmoaMesrlineEdfaTxpwrMeas = _PmoaMesrlineEdfaTxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 3, 3, 41),
    _PmoaMesrlineEdfaTxpwrMeas_Type()
)
pmoaMesrlineEdfaTxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaMesrlineEdfaTxpwrMeas.setStatus("current")


class _PmoaMesrlineEdfaRxpwrMeas_Type(Integer32):
    """Custom type pmoaMesrlineEdfaRxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoaMesrlineEdfaRxpwrMeas_Type.__name__ = "Integer32"
_PmoaMesrlineEdfaRxpwrMeas_Object = MibScalar
pmoaMesrlineEdfaRxpwrMeas = _PmoaMesrlineEdfaRxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 3, 3, 42),
    _PmoaMesrlineEdfaRxpwrMeas_Type()
)
pmoaMesrlineEdfaRxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaMesrlineEdfaRxpwrMeas.setStatus("current")


class _PmoaMesrlineEdfaGainMeas_Type(Integer32):
    """Custom type pmoaMesrlineEdfaGainMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoaMesrlineEdfaGainMeas_Type.__name__ = "Integer32"
_PmoaMesrlineEdfaGainMeas_Object = MibScalar
pmoaMesrlineEdfaGainMeas = _PmoaMesrlineEdfaGainMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 3, 3, 43),
    _PmoaMesrlineEdfaGainMeas_Type()
)
pmoaMesrlineEdfaGainMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaMesrlineEdfaGainMeas.setStatus("current")
_PmoacontrolsWrite_ObjectIdentity = ObjectIdentity
pmoacontrolsWrite = _PmoacontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6)
)
_PmoaCtrlOther_ObjectIdentity = ObjectIdentity
pmoaCtrlOther = _PmoaCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 1)
)
_PmoaCtrlsynth0_ObjectIdentity = ObjectIdentity
pmoaCtrlsynth0 = _PmoaCtrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 1, 0)
)
_PmoaCtrlConfLoad_Type = EkiOnOff
_PmoaCtrlConfLoad_Object = MibScalar
pmoaCtrlConfLoad = _PmoaCtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 1, 0, 1),
    _PmoaCtrlConfLoad_Type()
)
pmoaCtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrlConfLoad.setStatus("current")
_PmoaCtrlConfFlash_Type = EkiOnOff
_PmoaCtrlConfFlash_Object = MibScalar
pmoaCtrlConfFlash = _PmoaCtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 1, 0, 9),
    _PmoaCtrlConfFlash_Type()
)
pmoaCtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrlConfFlash.setStatus("current")
_PmoaCtrlConfClear_Type = EkiOnOff
_PmoaCtrlConfClear_Object = MibScalar
pmoaCtrlConfClear = _PmoaCtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 1, 0, 13),
    _PmoaCtrlConfClear_Type()
)
pmoaCtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrlConfClear.setStatus("current")
_PmoaCtrlswMgnt_ObjectIdentity = ObjectIdentity
pmoaCtrlswMgnt = _PmoaCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 1, 5)
)
_PmoaCtrlColdReset_Type = EkiOnOff
_PmoaCtrlColdReset_Object = MibScalar
pmoaCtrlColdReset = _PmoaCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 1, 5, 2),
    _PmoaCtrlColdReset_Type()
)
pmoaCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrlColdReset.setStatus("current")
_PmoaCtrlWarmReset_Type = EkiOnOff
_PmoaCtrlWarmReset_Object = MibScalar
pmoaCtrlWarmReset = _PmoaCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 1, 5, 3),
    _PmoaCtrlWarmReset_Type()
)
pmoaCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrlWarmReset.setStatus("current")
_PmoaCtrlpowerDown_ObjectIdentity = ObjectIdentity
pmoaCtrlpowerDown = _PmoaCtrlpowerDown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 1, 72)
)
_PmoaCtrlSoftPowerDown_Type = EkiOnOff
_PmoaCtrlSoftPowerDown_Object = MibScalar
pmoaCtrlSoftPowerDown = _PmoaCtrlSoftPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 1, 72, 1),
    _PmoaCtrlSoftPowerDown_Type()
)
pmoaCtrlSoftPowerDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrlSoftPowerDown.setStatus("current")
_PmoaCtrlledTest_ObjectIdentity = ObjectIdentity
pmoaCtrlledTest = _PmoaCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 1, 73)
)
_PmoaCtrlGreenLed_Type = EkiOnOff
_PmoaCtrlGreenLed_Object = MibScalar
pmoaCtrlGreenLed = _PmoaCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 1, 73, 1),
    _PmoaCtrlGreenLed_Type()
)
pmoaCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrlGreenLed.setStatus("current")
_PmoaCtrlRedLed_Type = EkiOnOff
_PmoaCtrlRedLed_Object = MibScalar
pmoaCtrlRedLed = _PmoaCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 1, 73, 2),
    _PmoaCtrlRedLed_Type()
)
pmoaCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrlRedLed.setStatus("current")
_PmoaCtrlLedOff_Type = EkiOnOff
_PmoaCtrlLedOff_Object = MibScalar
pmoaCtrlLedOff = _PmoaCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 1, 73, 3),
    _PmoaCtrlLedOff_Type()
)
pmoaCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrlLedOff.setStatus("current")
_PmoaCtrlmaintMode_ObjectIdentity = ObjectIdentity
pmoaCtrlmaintMode = _PmoaCtrlmaintMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 1, 75)
)
_PmoaCtrlMaintenance_Type = EkiOnOff
_PmoaCtrlMaintenance_Object = MibScalar
pmoaCtrlMaintenance = _PmoaCtrlMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 1, 75, 1),
    _PmoaCtrlMaintenance_Type()
)
pmoaCtrlMaintenance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrlMaintenance.setStatus("current")
_PmoaCtrlClient_ObjectIdentity = ObjectIdentity
pmoaCtrlClient = _PmoaCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 2)
)
_PmoaCtrlclientEdfaLaserOff_ObjectIdentity = ObjectIdentity
pmoaCtrlclientEdfaLaserOff = _PmoaCtrlclientEdfaLaserOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 2, 32)
)
_PmoaCtrlClientEdfaLaserOff_Type = EkiOnOff
_PmoaCtrlClientEdfaLaserOff_Object = MibScalar
pmoaCtrlClientEdfaLaserOff = _PmoaCtrlClientEdfaLaserOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 2, 32, 1),
    _PmoaCtrlClientEdfaLaserOff_Type()
)
pmoaCtrlClientEdfaLaserOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrlClientEdfaLaserOff.setStatus("current")
_PmoaCtrlclientEdfaMode_Type = PmoapreampMode
_PmoaCtrlclientEdfaMode_Object = MibScalar
pmoaCtrlclientEdfaMode = _PmoaCtrlclientEdfaMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 2, 33),
    _PmoaCtrlclientEdfaMode_Type()
)
pmoaCtrlclientEdfaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrlclientEdfaMode.setStatus("current")


class _PmoaCtrlclientIlasSettingValue_Type(Integer32):
    """Custom type pmoaCtrlclientIlasSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoaCtrlclientIlasSettingValue_Type.__name__ = "Integer32"
_PmoaCtrlclientIlasSettingValue_Object = MibScalar
pmoaCtrlclientIlasSettingValue = _PmoaCtrlclientIlasSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 2, 34),
    _PmoaCtrlclientIlasSettingValue_Type()
)
pmoaCtrlclientIlasSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrlclientIlasSettingValue.setStatus("current")


class _PmoaCtrlclientPlasSettingValue_Type(Integer32):
    """Custom type pmoaCtrlclientPlasSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoaCtrlclientPlasSettingValue_Type.__name__ = "Integer32"
_PmoaCtrlclientPlasSettingValue_Object = MibScalar
pmoaCtrlclientPlasSettingValue = _PmoaCtrlclientPlasSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 2, 35),
    _PmoaCtrlclientPlasSettingValue_Type()
)
pmoaCtrlclientPlasSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrlclientPlasSettingValue.setStatus("current")


class _PmoaCtrlclientGainSettingValue_Type(Integer32):
    """Custom type pmoaCtrlclientGainSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoaCtrlclientGainSettingValue_Type.__name__ = "Integer32"
_PmoaCtrlclientGainSettingValue_Object = MibScalar
pmoaCtrlclientGainSettingValue = _PmoaCtrlclientGainSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 2, 36),
    _PmoaCtrlclientGainSettingValue_Type()
)
pmoaCtrlclientGainSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrlclientGainSettingValue.setStatus("current")


class _PmoaCtrlclientEffPwrOutSettingValue_Type(Integer32):
    """Custom type pmoaCtrlclientEffPwrOutSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoaCtrlclientEffPwrOutSettingValue_Type.__name__ = "Integer32"
_PmoaCtrlclientEffPwrOutSettingValue_Object = MibScalar
pmoaCtrlclientEffPwrOutSettingValue = _PmoaCtrlclientEffPwrOutSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 2, 37),
    _PmoaCtrlclientEffPwrOutSettingValue_Type()
)
pmoaCtrlclientEffPwrOutSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrlclientEffPwrOutSettingValue.setStatus("current")
_PmoaCtrlLine_ObjectIdentity = ObjectIdentity
pmoaCtrlLine = _PmoaCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 3)
)
_PmoaCtrllineEdfaLaserOff_ObjectIdentity = ObjectIdentity
pmoaCtrllineEdfaLaserOff = _PmoaCtrllineEdfaLaserOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 3, 40)
)
_PmoaCtrlLineEdfaLaserOff_Type = EkiOnOff
_PmoaCtrlLineEdfaLaserOff_Object = MibScalar
pmoaCtrlLineEdfaLaserOff = _PmoaCtrlLineEdfaLaserOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 3, 40, 1),
    _PmoaCtrlLineEdfaLaserOff_Type()
)
pmoaCtrlLineEdfaLaserOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrlLineEdfaLaserOff.setStatus("current")
_PmoaCtrllineEdfaMode_Type = PmoaboosterMode
_PmoaCtrllineEdfaMode_Object = MibScalar
pmoaCtrllineEdfaMode = _PmoaCtrllineEdfaMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 3, 41),
    _PmoaCtrllineEdfaMode_Type()
)
pmoaCtrllineEdfaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrllineEdfaMode.setStatus("current")


class _PmoaCtrllineIlasSettingValue_Type(Integer32):
    """Custom type pmoaCtrllineIlasSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoaCtrllineIlasSettingValue_Type.__name__ = "Integer32"
_PmoaCtrllineIlasSettingValue_Object = MibScalar
pmoaCtrllineIlasSettingValue = _PmoaCtrllineIlasSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 3, 42),
    _PmoaCtrllineIlasSettingValue_Type()
)
pmoaCtrllineIlasSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrllineIlasSettingValue.setStatus("current")


class _PmoaCtrllinePlasSettingValue_Type(Integer32):
    """Custom type pmoaCtrllinePlasSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoaCtrllinePlasSettingValue_Type.__name__ = "Integer32"
_PmoaCtrllinePlasSettingValue_Object = MibScalar
pmoaCtrllinePlasSettingValue = _PmoaCtrllinePlasSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 3, 43),
    _PmoaCtrllinePlasSettingValue_Type()
)
pmoaCtrllinePlasSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrllinePlasSettingValue.setStatus("current")


class _PmoaCtrllineGainSettingValue_Type(Integer32):
    """Custom type pmoaCtrllineGainSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoaCtrllineGainSettingValue_Type.__name__ = "Integer32"
_PmoaCtrllineGainSettingValue_Object = MibScalar
pmoaCtrllineGainSettingValue = _PmoaCtrllineGainSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 3, 44),
    _PmoaCtrllineGainSettingValue_Type()
)
pmoaCtrllineGainSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrllineGainSettingValue.setStatus("current")


class _PmoaCtrllineEffPwrOutSettingValue_Type(Integer32):
    """Custom type pmoaCtrllineEffPwrOutSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoaCtrllineEffPwrOutSettingValue_Type.__name__ = "Integer32"
_PmoaCtrllineEffPwrOutSettingValue_Object = MibScalar
pmoaCtrllineEffPwrOutSettingValue = _PmoaCtrllineEffPwrOutSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 6, 3, 45),
    _PmoaCtrllineEffPwrOutSettingValue_Type()
)
pmoaCtrllineEffPwrOutSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCtrllineEffPwrOutSettingValue.setStatus("current")
_Pmoari_ObjectIdentity = ObjectIdentity
pmoari = _Pmoari_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 7)
)
_PmoaRinvReloadInventory_Type = EkiOnOff
_PmoaRinvReloadInventory_Object = MibScalar
pmoaRinvReloadInventory = _PmoaRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 7, 2),
    _PmoaRinvReloadInventory_Type()
)
pmoaRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaRinvReloadInventory.setStatus("current")
_PmoaRinvModulePlatform_Type = DisplayString
_PmoaRinvModulePlatform_Object = MibScalar
pmoaRinvModulePlatform = _PmoaRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 7, 3),
    _PmoaRinvModulePlatform_Type()
)
pmoaRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaRinvModulePlatform.setStatus("current")
_PmoaRinvSwPlatform_Type = DisplayString
_PmoaRinvSwPlatform_Object = MibScalar
pmoaRinvSwPlatform = _PmoaRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 7, 4),
    _PmoaRinvSwPlatform_Type()
)
pmoaRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaRinvSwPlatform.setStatus("current")
_PmoaRinvSwFoa_Type = DisplayString
_PmoaRinvSwFoa_Object = MibScalar
pmoaRinvSwFoa = _PmoaRinvSwFoa_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 7, 5),
    _PmoaRinvSwFoa_Type()
)
pmoaRinvSwFoa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaRinvSwFoa.setStatus("current")
_PmoaRinvBoosterTable_Object = MibTable
pmoaRinvBoosterTable = _PmoaRinvBoosterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 7, 6)
)
if mibBuilder.loadTexts:
    pmoaRinvBoosterTable.setStatus("current")
_PmoaRinvBoosterEntry_Object = MibTableRow
pmoaRinvBoosterEntry = _PmoaRinvBoosterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 7, 6, 1)
)
pmoaRinvBoosterEntry.setIndexNames(
    (0, "EKINOPS-PmOa-MIB", "pmoaRinvBoosterIndex"),
)
if mibBuilder.loadTexts:
    pmoaRinvBoosterEntry.setStatus("current")


class _PmoaRinvBoosterIndex_Type(Integer32):
    """Custom type pmoaRinvBoosterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PmoaRinvBoosterIndex_Type.__name__ = "Integer32"
_PmoaRinvBoosterIndex_Object = MibTableColumn
pmoaRinvBoosterIndex = _PmoaRinvBoosterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 7, 6, 1, 1),
    _PmoaRinvBoosterIndex_Type()
)
pmoaRinvBoosterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaRinvBoosterIndex.setStatus("current")
_PmoaRinvBooster_Type = DisplayString
_PmoaRinvBooster_Object = MibTableColumn
pmoaRinvBooster = _PmoaRinvBooster_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 7, 6, 1, 2),
    _PmoaRinvBooster_Type()
)
pmoaRinvBooster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaRinvBooster.setStatus("current")
_PmoaRinvPreAmpTable_Object = MibTable
pmoaRinvPreAmpTable = _PmoaRinvPreAmpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 7, 7)
)
if mibBuilder.loadTexts:
    pmoaRinvPreAmpTable.setStatus("current")
_PmoaRinvPreAmpEntry_Object = MibTableRow
pmoaRinvPreAmpEntry = _PmoaRinvPreAmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 7, 7, 1)
)
pmoaRinvPreAmpEntry.setIndexNames(
    (0, "EKINOPS-PmOa-MIB", "pmoaRinvPreAmpIndex"),
)
if mibBuilder.loadTexts:
    pmoaRinvPreAmpEntry.setStatus("current")


class _PmoaRinvPreAmpIndex_Type(Integer32):
    """Custom type pmoaRinvPreAmpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PmoaRinvPreAmpIndex_Type.__name__ = "Integer32"
_PmoaRinvPreAmpIndex_Object = MibTableColumn
pmoaRinvPreAmpIndex = _PmoaRinvPreAmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 7, 7, 1, 1),
    _PmoaRinvPreAmpIndex_Type()
)
pmoaRinvPreAmpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaRinvPreAmpIndex.setStatus("current")
_PmoaRinvPreAmp_Type = DisplayString
_PmoaRinvPreAmp_Object = MibTableColumn
pmoaRinvPreAmp = _PmoaRinvPreAmp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 7, 7, 1, 2),
    _PmoaRinvPreAmp_Type()
)
pmoaRinvPreAmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaRinvPreAmp.setStatus("current")
_PmoaConfig_ObjectIdentity = ObjectIdentity
pmoaConfig = _PmoaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 9)
)
_PmoaCfgNoValue_ObjectIdentity = ObjectIdentity
pmoaCfgNoValue = _PmoaCfgNoValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 9, 1)
)
_PmoatableclientStartup_ObjectIdentity = ObjectIdentity
pmoatableclientStartup = _PmoatableclientStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 9, 1, 1)
)


class _PmoaCfgclientEdfaLaserCtrl_Type(Unsigned32):
    """Custom type pmoaCfgclientEdfaLaserCtrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoaCfgclientEdfaLaserCtrl_Type.__name__ = "Unsigned32"
_PmoaCfgclientEdfaLaserCtrl_Object = MibScalar
pmoaCfgclientEdfaLaserCtrl = _PmoaCfgclientEdfaLaserCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 9, 1, 1, 2),
    _PmoaCfgclientEdfaLaserCtrl_Type()
)
pmoaCfgclientEdfaLaserCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCfgclientEdfaLaserCtrl.setStatus("current")


class _PmoaCfgclientEdfaLaserMode_Type(Unsigned32):
    """Custom type pmoaCfgclientEdfaLaserMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoaCfgclientEdfaLaserMode_Type.__name__ = "Unsigned32"
_PmoaCfgclientEdfaLaserMode_Object = MibScalar
pmoaCfgclientEdfaLaserMode = _PmoaCfgclientEdfaLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 9, 1, 1, 3),
    _PmoaCfgclientEdfaLaserMode_Type()
)
pmoaCfgclientEdfaLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCfgclientEdfaLaserMode.setStatus("current")
_PmoaCfgLineStartUp_ObjectIdentity = ObjectIdentity
pmoaCfgLineStartUp = _PmoaCfgLineStartUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 9, 2)
)
_PmoatablelineStartup_ObjectIdentity = ObjectIdentity
pmoatablelineStartup = _PmoatablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 9, 2, 1)
)


class _PmoaCfglineEdfaLaserCtrl_Type(Unsigned32):
    """Custom type pmoaCfglineEdfaLaserCtrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoaCfglineEdfaLaserCtrl_Type.__name__ = "Unsigned32"
_PmoaCfglineEdfaLaserCtrl_Object = MibScalar
pmoaCfglineEdfaLaserCtrl = _PmoaCfglineEdfaLaserCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 9, 2, 1, 2),
    _PmoaCfglineEdfaLaserCtrl_Type()
)
pmoaCfglineEdfaLaserCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCfglineEdfaLaserCtrl.setStatus("current")


class _PmoaCfglineEdfaLaserMode_Type(Unsigned32):
    """Custom type pmoaCfglineEdfaLaserMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoaCfglineEdfaLaserMode_Type.__name__ = "Unsigned32"
_PmoaCfglineEdfaLaserMode_Object = MibScalar
pmoaCfglineEdfaLaserMode = _PmoaCfglineEdfaLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 9, 2, 1, 3),
    _PmoaCfglineEdfaLaserMode_Type()
)
pmoaCfglineEdfaLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCfglineEdfaLaserMode.setStatus("current")
_PmoaCfgLabels_ObjectIdentity = ObjectIdentity
pmoaCfgLabels = _PmoaCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 9, 3)
)
_PmoaCfgLabelclientTable_Object = MibTable
pmoaCfgLabelclientTable = _PmoaCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pmoaCfgLabelclientTable.setStatus("current")
_PmoaCfgLabelclientEntry_Object = MibTableRow
pmoaCfgLabelclientEntry = _PmoaCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 9, 3, 1, 1)
)
pmoaCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-PmOa-MIB", "pmoaCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmoaCfgLabelclientEntry.setStatus("current")


class _PmoaCfgLabelclientIndex_Type(Integer32):
    """Custom type pmoaCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoaCfgLabelclientIndex_Type.__name__ = "Integer32"
_PmoaCfgLabelclientIndex_Object = MibTableColumn
pmoaCfgLabelclientIndex = _PmoaCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 9, 3, 1, 1, 1),
    _PmoaCfgLabelclientIndex_Type()
)
pmoaCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaCfgLabelclientIndex.setStatus("current")


class _PmoaCfgLabelclientPortn_Type(DisplayString):
    """Custom type pmoaCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmoaCfgLabelclientPortn_Type.__name__ = "DisplayString"
_PmoaCfgLabelclientPortn_Object = MibTableColumn
pmoaCfgLabelclientPortn = _PmoaCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 9, 3, 1, 1, 3),
    _PmoaCfgLabelclientPortn_Type()
)
pmoaCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCfgLabelclientPortn.setStatus("current")
_PmoaCfgLabellineTable_Object = MibTable
pmoaCfgLabellineTable = _PmoaCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pmoaCfgLabellineTable.setStatus("current")
_PmoaCfgLabellineEntry_Object = MibTableRow
pmoaCfgLabellineEntry = _PmoaCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 9, 3, 2, 1)
)
pmoaCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-PmOa-MIB", "pmoaCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmoaCfgLabellineEntry.setStatus("current")


class _PmoaCfgLabellineIndex_Type(Integer32):
    """Custom type pmoaCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoaCfgLabellineIndex_Type.__name__ = "Integer32"
_PmoaCfgLabellineIndex_Object = MibTableColumn
pmoaCfgLabellineIndex = _PmoaCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 9, 3, 2, 1, 1),
    _PmoaCfgLabellineIndex_Type()
)
pmoaCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoaCfgLabellineIndex.setStatus("current")


class _PmoaCfgLabellinePortn_Type(DisplayString):
    """Custom type pmoaCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmoaCfgLabellinePortn_Type.__name__ = "DisplayString"
_PmoaCfgLabellinePortn_Object = MibTableColumn
pmoaCfgLabellinePortn = _PmoaCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 9, 3, 2, 1, 3),
    _PmoaCfgLabellinePortn_Type()
)
pmoaCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCfgLabellinePortn.setStatus("current")
_PmoaCfgWriteConfiguration_Type = EkiOnOff
_PmoaCfgWriteConfiguration_Object = MibScalar
pmoaCfgWriteConfiguration = _PmoaCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 9, 257),
    _PmoaCfgWriteConfiguration_Type()
)
pmoaCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoaCfgWriteConfiguration.setStatus("current")
_Pmoatraps_ObjectIdentity = ObjectIdentity
pmoatraps = _Pmoatraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 9, 10)
)


class _PmoatrapBoardNumber_Type(Integer32):
    """Custom type pmoatrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PmoatrapBoardNumber_Type.__name__ = "Integer32"
_PmoatrapBoardNumber_Object = MibScalar
pmoatrapBoardNumber = _PmoatrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 9, 10, 4),
    _PmoatrapBoardNumber_Type()
)
pmoatrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoatrapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pmoaLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 9, 10, 30)
)
pmoaLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOa-MIB", "pmoaAlmLineDdmWarning"),
        ("EKINOPS-PmOa-MIB", "pmoatrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoaLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmoaLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 9, 10, 31)
)
pmoaLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOa-MIB", "pmoaAlmLineDdmWarning"),
        ("EKINOPS-PmOa-MIB", "pmoatrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoaLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmoaLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 9, 10, 32)
)
pmoaLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOa-MIB", "pmoaAlmLineDdmAlm"),
        ("EKINOPS-PmOa-MIB", "pmoatrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoaLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pmoaLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 9, 10, 33)
)
pmoaLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOa-MIB", "pmoaAlmLineDdmAlm"),
        ("EKINOPS-PmOa-MIB", "pmoatrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoaLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pmoaLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 9, 10, 34)
)
pmoaLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-PmOa-MIB", "pmoaAlmLineFail"),
        ("EKINOPS-PmOa-MIB", "pmoaAlmLineHwFail"),
        ("EKINOPS-PmOa-MIB", "pmoatrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoaLineTrapCritGoesOn.setStatus(
        "current"
    )

pmoaLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 9, 10, 35)
)
pmoaLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-PmOa-MIB", "pmoaAlmLineFail"),
        ("EKINOPS-PmOa-MIB", "pmoaAlmLineHwFail"),
        ("EKINOPS-PmOa-MIB", "pmoatrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoaLineTrapCritGoesOff.setStatus(
        "current"
    )

pmoaClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 9, 10, 40)
)
pmoaClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOa-MIB", "pmoaAlmClientDdmWarning"),
        ("EKINOPS-PmOa-MIB", "pmoatrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoaClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmoaClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 9, 10, 41)
)
pmoaClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOa-MIB", "pmoaAlmClientDdmWarning"),
        ("EKINOPS-PmOa-MIB", "pmoatrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoaClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmoaClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 9, 10, 42)
)
pmoaClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOa-MIB", "pmoaAlmClientDdmAlm"),
        ("EKINOPS-PmOa-MIB", "pmoatrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoaClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pmoaClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 9, 10, 43)
)
pmoaClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOa-MIB", "pmoaAlmClientDdmAlm"),
        ("EKINOPS-PmOa-MIB", "pmoatrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoaClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pmoaClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 9, 10, 44)
)
pmoaClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-PmOa-MIB", "pmoaAlmClientFail"),
        ("EKINOPS-PmOa-MIB", "pmoaAlmClientHwFail"),
        ("EKINOPS-PmOa-MIB", "pmoatrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoaClientTrapCritGoesOn.setStatus(
        "current"
    )

pmoaClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 9, 10, 45)
)
pmoaClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-PmOa-MIB", "pmoaAlmClientFail"),
        ("EKINOPS-PmOa-MIB", "pmoaAlmClientHwFail"),
        ("EKINOPS-PmOa-MIB", "pmoatrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoaClientTrapCritGoesOff.setStatus(
        "current"
    )

pmoaPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 9, 10, 50)
)
pmoaPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOa-MIB", "pmoaAlmDefFuseB"),
        ("EKINOPS-PmOa-MIB", "pmoaAlmDefFuseA"),
        ("EKINOPS-PmOa-MIB", "pmoatrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoaPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmoaPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 9, 10, 51)
)
pmoaPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOa-MIB", "pmoaAlmDefFuseB"),
        ("EKINOPS-PmOa-MIB", "pmoaAlmDefFuseA"),
        ("EKINOPS-PmOa-MIB", "pmoatrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoaPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-PmOa-MIB",
    **{"PmoapreampMode": PmoapreampMode,
       "PmoaboosterMode": PmoaboosterMode,
       "modulepmoa": modulepmoa,
       "pmoaalarms": pmoaalarms,
       "pmoaAlmOther": pmoaAlmOther,
       "pmoaAlmOtherNurg": pmoaAlmOtherNurg,
       "pmoaAlmsynthAlm2": pmoaAlmsynthAlm2,
       "pmoaAlmConfTableSave": pmoaAlmConfTableSave,
       "pmoaAlmInvUpload": pmoaAlmInvUpload,
       "pmoaAlmConfTableLoad": pmoaAlmConfTableLoad,
       "pmoaAlmfoaWarnings": pmoaAlmfoaWarnings,
       "pmoaAlm3v3LowWarning": pmoaAlm3v3LowWarning,
       "pmoaAlm3v3HighWarning": pmoaAlm3v3HighWarning,
       "pmoaAlmTermpLowWarning": pmoaAlmTermpLowWarning,
       "pmoaAlmTempHighWarning": pmoaAlmTempHighWarning,
       "pmoaAlmOtherUrg": pmoaAlmOtherUrg,
       "pmoaAlmfoaAlarms": pmoaAlmfoaAlarms,
       "pmoaAlm3v3LowAlarm": pmoaAlm3v3LowAlarm,
       "pmoaAlm3v3HighAlarm": pmoaAlm3v3HighAlarm,
       "pmoaAlmTermpLowAlarm": pmoaAlmTermpLowAlarm,
       "pmoaAlmTempHighAlarm": pmoaAlmTempHighAlarm,
       "pmoaAlmOtherCrit": pmoaAlmOtherCrit,
       "pmoaAlmsynthAlm0": pmoaAlmsynthAlm0,
       "pmoaAlmMaintenanceMode": pmoaAlmMaintenanceMode,
       "pmoaAlmModGlobFail": pmoaAlmModGlobFail,
       "pmoaAlmUpEdfaInitNotCompl": pmoaAlmUpEdfaInitNotCompl,
       "pmoaAlmDwEdfaInitNotCompl": pmoaAlmDwEdfaInitNotCompl,
       "pmoaAlmExtPumpNotLocked": pmoaAlmExtPumpNotLocked,
       "pmoaAlmDefFuseA": pmoaAlmDefFuseA,
       "pmoaAlmDefFuseB": pmoaAlmDefFuseB,
       "pmoaAlmClient": pmoaAlmClient,
       "pmoaAlmClientNurg": pmoaAlmClientNurg,
       "pmoaAlmclientEdfaWarnings": pmoaAlmclientEdfaWarnings,
       "pmoaAlmClientGainLowWarning": pmoaAlmClientGainLowWarning,
       "pmoaAlmClientGainHighWarning": pmoaAlmClientGainHighWarning,
       "pmoaAlmClientInputPwrLowWarning": pmoaAlmClientInputPwrLowWarning,
       "pmoaAlmClientInputPwrHighWarning": pmoaAlmClientInputPwrHighWarning,
       "pmoaAlmClientOutputPwrLowWarning": pmoaAlmClientOutputPwrLowWarning,
       "pmoaAlmClientOutputPwrHighWarning": pmoaAlmClientOutputPwrHighWarning,
       "pmoaAlmClientBiasLowWarning": pmoaAlmClientBiasLowWarning,
       "pmoaAlmClientBiasHighWarning": pmoaAlmClientBiasHighWarning,
       "pmoaAlmClientUrg": pmoaAlmClientUrg,
       "pmoaAlmclientEdfaAlarms1": pmoaAlmclientEdfaAlarms1,
       "pmoaAlmClientGainLowAlarm": pmoaAlmClientGainLowAlarm,
       "pmoaAlmClientGainHighAlarm": pmoaAlmClientGainHighAlarm,
       "pmoaAlmClientInputPwrLowAlarm": pmoaAlmClientInputPwrLowAlarm,
       "pmoaAlmClientInputPwrHighAlarm": pmoaAlmClientInputPwrHighAlarm,
       "pmoaAlmClientOutputPwrLowAlarm": pmoaAlmClientOutputPwrLowAlarm,
       "pmoaAlmClientOutputPwrHighAlarm": pmoaAlmClientOutputPwrHighAlarm,
       "pmoaAlmClientBiasLowAlarm": pmoaAlmClientBiasLowAlarm,
       "pmoaAlmClientBiasHighAlarm": pmoaAlmClientBiasHighAlarm,
       "pmoaAlmClientCrit": pmoaAlmClientCrit,
       "pmoaAlmsynthAlm8": pmoaAlmsynthAlm8,
       "pmoaAlmClientHwFail": pmoaAlmClientHwFail,
       "pmoaAlmClientTxOff": pmoaAlmClientTxOff,
       "pmoaAlmClientDdmWarning": pmoaAlmClientDdmWarning,
       "pmoaAlmClientDdmAlm": pmoaAlmClientDdmAlm,
       "pmoaAlmClientFail": pmoaAlmClientFail,
       "pmoaAlmclientEdfaAlarms2": pmoaAlmclientEdfaAlarms2,
       "pmoaAlmClientEdfaNr": pmoaAlmClientEdfaNr,
       "pmoaAlmClientEdfaTecFail": pmoaAlmClientEdfaTecFail,
       "pmoaAlmClientEdfaLaserFail": pmoaAlmClientEdfaLaserFail,
       "pmoaAlmClientEdfaLos": pmoaAlmClientEdfaLos,
       "pmoaAlmClientExtPumpEdfaLowCurrent": pmoaAlmClientExtPumpEdfaLowCurrent,
       "pmoaAlmLine": pmoaAlmLine,
       "pmoaAlmLineNurg": pmoaAlmLineNurg,
       "pmoaAlmlineEdfaWarnings": pmoaAlmlineEdfaWarnings,
       "pmoaAlmLineGainLowWarning": pmoaAlmLineGainLowWarning,
       "pmoaAlmLineGainHighWarning": pmoaAlmLineGainHighWarning,
       "pmoaAlmLineInputPwrLowWarning": pmoaAlmLineInputPwrLowWarning,
       "pmoaAlmLineInputPwrHighWarning": pmoaAlmLineInputPwrHighWarning,
       "pmoaAlmLineOutputPwrLowWarning": pmoaAlmLineOutputPwrLowWarning,
       "pmoaAlmLineOutputPwrHighWarning": pmoaAlmLineOutputPwrHighWarning,
       "pmoaAlmLineBiasLowWarning": pmoaAlmLineBiasLowWarning,
       "pmoaAlmLineBiasHighWarning": pmoaAlmLineBiasHighWarning,
       "pmoaAlmLineUrg": pmoaAlmLineUrg,
       "pmoaAlmlineEdfaAlarms1": pmoaAlmlineEdfaAlarms1,
       "pmoaAlmLineGainLowAlarm": pmoaAlmLineGainLowAlarm,
       "pmoaAlmLineGainHighAlarm": pmoaAlmLineGainHighAlarm,
       "pmoaAlmLineInputPwrLowAlarm": pmoaAlmLineInputPwrLowAlarm,
       "pmoaAlmLineInputPwrHighAlarm": pmoaAlmLineInputPwrHighAlarm,
       "pmoaAlmLineOutputPwrLowAlarm": pmoaAlmLineOutputPwrLowAlarm,
       "pmoaAlmLineOutputPwrHighAlarm": pmoaAlmLineOutputPwrHighAlarm,
       "pmoaAlmLineBiasLowAlarm": pmoaAlmLineBiasLowAlarm,
       "pmoaAlmLineBiasHighAlarm": pmoaAlmLineBiasHighAlarm,
       "pmoaAlmLineCrit": pmoaAlmLineCrit,
       "pmoaAlmsynthAlm7": pmoaAlmsynthAlm7,
       "pmoaAlmLineHwFail": pmoaAlmLineHwFail,
       "pmoaAlmLineTxOff": pmoaAlmLineTxOff,
       "pmoaAlmLineDdmWarning": pmoaAlmLineDdmWarning,
       "pmoaAlmLineDdmAlm": pmoaAlmLineDdmAlm,
       "pmoaAlmLineFail": pmoaAlmLineFail,
       "pmoaAlmlineEdfaAlarms2": pmoaAlmlineEdfaAlarms2,
       "pmoaAlmLineEdfaNr": pmoaAlmLineEdfaNr,
       "pmoaAlmLineEdfaTecFail": pmoaAlmLineEdfaTecFail,
       "pmoaAlmLineEdfaLaserFail": pmoaAlmLineEdfaLaserFail,
       "pmoaAlmLineEdfaLos": pmoaAlmLineEdfaLos,
       "pmoaAlmLineExtPumpEdfaLowCurrent": pmoaAlmLineExtPumpEdfaLowCurrent,
       "pmoameasures": pmoameasures,
       "pmoaMesrOther": pmoaMesrOther,
       "pmoaMesrtempMeas": pmoaMesrtempMeas,
       "pmoaMesr3v3Meas": pmoaMesr3v3Meas,
       "pmoaMesrClient": pmoaMesrClient,
       "pmoaMesrclientEdfaBiasMeas": pmoaMesrclientEdfaBiasMeas,
       "pmoaMesrclientEdfaTxpwrMeas": pmoaMesrclientEdfaTxpwrMeas,
       "pmoaMesrclientEdfaRxpwrMeas": pmoaMesrclientEdfaRxpwrMeas,
       "pmoaMesrclientEdfaGainMeas": pmoaMesrclientEdfaGainMeas,
       "pmoaMesrLine": pmoaMesrLine,
       "pmoaMesrlineEdfaBiasMeas": pmoaMesrlineEdfaBiasMeas,
       "pmoaMesrlineEdfaTxpwrMeas": pmoaMesrlineEdfaTxpwrMeas,
       "pmoaMesrlineEdfaRxpwrMeas": pmoaMesrlineEdfaRxpwrMeas,
       "pmoaMesrlineEdfaGainMeas": pmoaMesrlineEdfaGainMeas,
       "pmoacontrolsWrite": pmoacontrolsWrite,
       "pmoaCtrlOther": pmoaCtrlOther,
       "pmoaCtrlsynth0": pmoaCtrlsynth0,
       "pmoaCtrlConfLoad": pmoaCtrlConfLoad,
       "pmoaCtrlConfFlash": pmoaCtrlConfFlash,
       "pmoaCtrlConfClear": pmoaCtrlConfClear,
       "pmoaCtrlswMgnt": pmoaCtrlswMgnt,
       "pmoaCtrlColdReset": pmoaCtrlColdReset,
       "pmoaCtrlWarmReset": pmoaCtrlWarmReset,
       "pmoaCtrlpowerDown": pmoaCtrlpowerDown,
       "pmoaCtrlSoftPowerDown": pmoaCtrlSoftPowerDown,
       "pmoaCtrlledTest": pmoaCtrlledTest,
       "pmoaCtrlGreenLed": pmoaCtrlGreenLed,
       "pmoaCtrlRedLed": pmoaCtrlRedLed,
       "pmoaCtrlLedOff": pmoaCtrlLedOff,
       "pmoaCtrlmaintMode": pmoaCtrlmaintMode,
       "pmoaCtrlMaintenance": pmoaCtrlMaintenance,
       "pmoaCtrlClient": pmoaCtrlClient,
       "pmoaCtrlclientEdfaLaserOff": pmoaCtrlclientEdfaLaserOff,
       "pmoaCtrlClientEdfaLaserOff": pmoaCtrlClientEdfaLaserOff,
       "pmoaCtrlclientEdfaMode": pmoaCtrlclientEdfaMode,
       "pmoaCtrlclientIlasSettingValue": pmoaCtrlclientIlasSettingValue,
       "pmoaCtrlclientPlasSettingValue": pmoaCtrlclientPlasSettingValue,
       "pmoaCtrlclientGainSettingValue": pmoaCtrlclientGainSettingValue,
       "pmoaCtrlclientEffPwrOutSettingValue": pmoaCtrlclientEffPwrOutSettingValue,
       "pmoaCtrlLine": pmoaCtrlLine,
       "pmoaCtrllineEdfaLaserOff": pmoaCtrllineEdfaLaserOff,
       "pmoaCtrlLineEdfaLaserOff": pmoaCtrlLineEdfaLaserOff,
       "pmoaCtrllineEdfaMode": pmoaCtrllineEdfaMode,
       "pmoaCtrllineIlasSettingValue": pmoaCtrllineIlasSettingValue,
       "pmoaCtrllinePlasSettingValue": pmoaCtrllinePlasSettingValue,
       "pmoaCtrllineGainSettingValue": pmoaCtrllineGainSettingValue,
       "pmoaCtrllineEffPwrOutSettingValue": pmoaCtrllineEffPwrOutSettingValue,
       "pmoari": pmoari,
       "pmoaRinvReloadInventory": pmoaRinvReloadInventory,
       "pmoaRinvModulePlatform": pmoaRinvModulePlatform,
       "pmoaRinvSwPlatform": pmoaRinvSwPlatform,
       "pmoaRinvSwFoa": pmoaRinvSwFoa,
       "pmoaRinvBoosterTable": pmoaRinvBoosterTable,
       "pmoaRinvBoosterEntry": pmoaRinvBoosterEntry,
       "pmoaRinvBoosterIndex": pmoaRinvBoosterIndex,
       "pmoaRinvBooster": pmoaRinvBooster,
       "pmoaRinvPreAmpTable": pmoaRinvPreAmpTable,
       "pmoaRinvPreAmpEntry": pmoaRinvPreAmpEntry,
       "pmoaRinvPreAmpIndex": pmoaRinvPreAmpIndex,
       "pmoaRinvPreAmp": pmoaRinvPreAmp,
       "pmoaConfig": pmoaConfig,
       "pmoaCfgNoValue": pmoaCfgNoValue,
       "pmoatableclientStartup": pmoatableclientStartup,
       "pmoaCfgclientEdfaLaserCtrl": pmoaCfgclientEdfaLaserCtrl,
       "pmoaCfgclientEdfaLaserMode": pmoaCfgclientEdfaLaserMode,
       "pmoaCfgLineStartUp": pmoaCfgLineStartUp,
       "pmoatablelineStartup": pmoatablelineStartup,
       "pmoaCfglineEdfaLaserCtrl": pmoaCfglineEdfaLaserCtrl,
       "pmoaCfglineEdfaLaserMode": pmoaCfglineEdfaLaserMode,
       "pmoaCfgLabels": pmoaCfgLabels,
       "pmoaCfgLabelclientTable": pmoaCfgLabelclientTable,
       "pmoaCfgLabelclientEntry": pmoaCfgLabelclientEntry,
       "pmoaCfgLabelclientIndex": pmoaCfgLabelclientIndex,
       "pmoaCfgLabelclientPortn": pmoaCfgLabelclientPortn,
       "pmoaCfgLabellineTable": pmoaCfgLabellineTable,
       "pmoaCfgLabellineEntry": pmoaCfgLabellineEntry,
       "pmoaCfgLabellineIndex": pmoaCfgLabellineIndex,
       "pmoaCfgLabellinePortn": pmoaCfgLabellinePortn,
       "pmoaCfgWriteConfiguration": pmoaCfgWriteConfiguration,
       "pmoatraps": pmoatraps,
       "pmoatrapBoardNumber": pmoatrapBoardNumber,
       "pmoaLineTrapNotUrgentGoesOn": pmoaLineTrapNotUrgentGoesOn,
       "pmoaLineTrapNotUrgentGoesOff": pmoaLineTrapNotUrgentGoesOff,
       "pmoaLineTrapUrgentGoesOn": pmoaLineTrapUrgentGoesOn,
       "pmoaLineTrapUrgentGoesOff": pmoaLineTrapUrgentGoesOff,
       "pmoaLineTrapCritGoesOn": pmoaLineTrapCritGoesOn,
       "pmoaLineTrapCritGoesOff": pmoaLineTrapCritGoesOff,
       "pmoaClientTrapNotUrgentGoesOn": pmoaClientTrapNotUrgentGoesOn,
       "pmoaClientTrapNotUrgentGoesOff": pmoaClientTrapNotUrgentGoesOff,
       "pmoaClientTrapUrgentGoesOn": pmoaClientTrapUrgentGoesOn,
       "pmoaClientTrapUrgentGoesOff": pmoaClientTrapUrgentGoesOff,
       "pmoaClientTrapCritGoesOn": pmoaClientTrapCritGoesOn,
       "pmoaClientTrapCritGoesOff": pmoaClientTrapCritGoesOff,
       "pmoaPowerTrapUrgentGoesOn": pmoaPowerTrapUrgentGoesOn,
       "pmoaPowerTrapUrgentGoesOff": pmoaPowerTrapUrgentGoesOff}
)
