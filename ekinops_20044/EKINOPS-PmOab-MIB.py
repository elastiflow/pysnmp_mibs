# SNMP MIB module (EKINOPS-PmOab-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-PmOab-MIB.mib
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

modulepmoab = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23)
)
if mibBuilder.loadTexts:
    modulepmoab.setRevisions(
        ("2007-02-07 00:00",
         "2007-07-06 00:00",
         "2007-11-21 00:00",
         "2009-04-15 00:00",
         "2009-09-21 00:00",
         "2009-12-14 00:00",
         "2010-02-25 00:00",
         "2010-07-15 00:00",
         "2010-10-29 00:00",
         "2010-11-03 00:00",
         "2012-07-04 00:00",
         "2014-03-26 00:00",
         "2014-12-10 00:00",
         "2016-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PmoabboosterMode(TextualConvention, Integer32):
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

_Pmoabalarms_ObjectIdentity = ObjectIdentity
pmoabalarms = _Pmoabalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2)
)
_PmoabAlmOther_ObjectIdentity = ObjectIdentity
pmoabAlmOther = _PmoabAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1)
)
_PmoabAlmOtherNurg_ObjectIdentity = ObjectIdentity
pmoabAlmOtherNurg = _PmoabAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 1)
)
_PmoabAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pmoabAlmsynthAlm2 = _PmoabAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 1, 2)
)
_PmoabAlmConfTableSave_Type = EkiOnOff
_PmoabAlmConfTableSave_Object = MibScalar
pmoabAlmConfTableSave = _PmoabAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 1, 2, 1),
    _PmoabAlmConfTableSave_Type()
)
pmoabAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmConfTableSave.setStatus("current")
_PmoabAlmInvUpload_Type = EkiOnOff
_PmoabAlmInvUpload_Object = MibScalar
pmoabAlmInvUpload = _PmoabAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 1, 2, 2),
    _PmoabAlmInvUpload_Type()
)
pmoabAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmInvUpload.setStatus("current")
_PmoabAlmConfTableLoad_Type = EkiOnOff
_PmoabAlmConfTableLoad_Object = MibScalar
pmoabAlmConfTableLoad = _PmoabAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 1, 2, 3),
    _PmoabAlmConfTableLoad_Type()
)
pmoabAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmConfTableLoad.setStatus("current")
_PmoabAlmfoaWarnings_ObjectIdentity = ObjectIdentity
pmoabAlmfoaWarnings = _PmoabAlmfoaWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 1, 75)
)
_PmoabAlm3v3LowWarning_Type = EkiOnOff
_PmoabAlm3v3LowWarning_Object = MibScalar
pmoabAlm3v3LowWarning = _PmoabAlm3v3LowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 1, 75, 5),
    _PmoabAlm3v3LowWarning_Type()
)
pmoabAlm3v3LowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlm3v3LowWarning.setStatus("current")
_PmoabAlm3v3HighWarning_Type = EkiOnOff
_PmoabAlm3v3HighWarning_Object = MibScalar
pmoabAlm3v3HighWarning = _PmoabAlm3v3HighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 1, 75, 6),
    _PmoabAlm3v3HighWarning_Type()
)
pmoabAlm3v3HighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlm3v3HighWarning.setStatus("current")
_PmoabAlmTermpLowWarning_Type = EkiOnOff
_PmoabAlmTermpLowWarning_Object = MibScalar
pmoabAlmTermpLowWarning = _PmoabAlmTermpLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 1, 75, 7),
    _PmoabAlmTermpLowWarning_Type()
)
pmoabAlmTermpLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmTermpLowWarning.setStatus("current")
_PmoabAlmTempHighWarning_Type = EkiOnOff
_PmoabAlmTempHighWarning_Object = MibScalar
pmoabAlmTempHighWarning = _PmoabAlmTempHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 1, 75, 8),
    _PmoabAlmTempHighWarning_Type()
)
pmoabAlmTempHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmTempHighWarning.setStatus("current")
_PmoabAlmOtherUrg_ObjectIdentity = ObjectIdentity
pmoabAlmOtherUrg = _PmoabAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 2)
)
_PmoabAlmfoaAlarms_ObjectIdentity = ObjectIdentity
pmoabAlmfoaAlarms = _PmoabAlmfoaAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 2, 74)
)
_PmoabAlm3v3LowAlarm_Type = EkiOnOff
_PmoabAlm3v3LowAlarm_Object = MibScalar
pmoabAlm3v3LowAlarm = _PmoabAlm3v3LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 2, 74, 5),
    _PmoabAlm3v3LowAlarm_Type()
)
pmoabAlm3v3LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlm3v3LowAlarm.setStatus("current")
_PmoabAlm3v3HighAlarm_Type = EkiOnOff
_PmoabAlm3v3HighAlarm_Object = MibScalar
pmoabAlm3v3HighAlarm = _PmoabAlm3v3HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 2, 74, 6),
    _PmoabAlm3v3HighAlarm_Type()
)
pmoabAlm3v3HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlm3v3HighAlarm.setStatus("current")
_PmoabAlmTermpLowAlarm_Type = EkiOnOff
_PmoabAlmTermpLowAlarm_Object = MibScalar
pmoabAlmTermpLowAlarm = _PmoabAlmTermpLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 2, 74, 7),
    _PmoabAlmTermpLowAlarm_Type()
)
pmoabAlmTermpLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmTermpLowAlarm.setStatus("current")
_PmoabAlmTempHighAlarm_Type = EkiOnOff
_PmoabAlmTempHighAlarm_Object = MibScalar
pmoabAlmTempHighAlarm = _PmoabAlmTempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 2, 74, 8),
    _PmoabAlmTempHighAlarm_Type()
)
pmoabAlmTempHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmTempHighAlarm.setStatus("current")
_PmoabAlmOtherCrit_ObjectIdentity = ObjectIdentity
pmoabAlmOtherCrit = _PmoabAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 3)
)
_PmoabAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmoabAlmsynthAlm0 = _PmoabAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 3, 0)
)
_PmoabAlmMaintenanceMode_Type = EkiOnOff
_PmoabAlmMaintenanceMode_Object = MibScalar
pmoabAlmMaintenanceMode = _PmoabAlmMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 3, 0, 1),
    _PmoabAlmMaintenanceMode_Type()
)
pmoabAlmMaintenanceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmMaintenanceMode.setStatus("current")
_PmoabAlmModGlobFail_Type = EkiOnOff
_PmoabAlmModGlobFail_Object = MibScalar
pmoabAlmModGlobFail = _PmoabAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 3, 0, 9),
    _PmoabAlmModGlobFail_Type()
)
pmoabAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmModGlobFail.setStatus("current")
_PmoabAlmUpEdfaInitNotCompl_Type = EkiOnOff
_PmoabAlmUpEdfaInitNotCompl_Object = MibScalar
pmoabAlmUpEdfaInitNotCompl = _PmoabAlmUpEdfaInitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 3, 0, 10),
    _PmoabAlmUpEdfaInitNotCompl_Type()
)
pmoabAlmUpEdfaInitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmUpEdfaInitNotCompl.setStatus("current")
_PmoabAlmDwEdfaInitNotCompl_Type = EkiOnOff
_PmoabAlmDwEdfaInitNotCompl_Object = MibScalar
pmoabAlmDwEdfaInitNotCompl = _PmoabAlmDwEdfaInitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 3, 0, 11),
    _PmoabAlmDwEdfaInitNotCompl_Type()
)
pmoabAlmDwEdfaInitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmDwEdfaInitNotCompl.setStatus("current")
_PmoabAlmExtPumpNotLocked_Type = EkiOnOff
_PmoabAlmExtPumpNotLocked_Object = MibScalar
pmoabAlmExtPumpNotLocked = _PmoabAlmExtPumpNotLocked_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 3, 0, 12),
    _PmoabAlmExtPumpNotLocked_Type()
)
pmoabAlmExtPumpNotLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmExtPumpNotLocked.setStatus("current")
_PmoabAlmDefFuseA_Type = EkiOnOff
_PmoabAlmDefFuseA_Object = MibScalar
pmoabAlmDefFuseA = _PmoabAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 3, 0, 15),
    _PmoabAlmDefFuseA_Type()
)
pmoabAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmDefFuseA.setStatus("current")
_PmoabAlmDefFuseB_Type = EkiOnOff
_PmoabAlmDefFuseB_Object = MibScalar
pmoabAlmDefFuseB = _PmoabAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 1, 3, 0, 16),
    _PmoabAlmDefFuseB_Type()
)
pmoabAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmDefFuseB.setStatus("current")
_PmoabAlmClient_ObjectIdentity = ObjectIdentity
pmoabAlmClient = _PmoabAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 2)
)
_PmoabAlmClientNurg_ObjectIdentity = ObjectIdentity
pmoabAlmClientNurg = _PmoabAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 2, 1)
)
_PmoabAlmclientEdfaWarnings_ObjectIdentity = ObjectIdentity
pmoabAlmclientEdfaWarnings = _PmoabAlmclientEdfaWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 2, 1, 33)
)
_PmoabAlmClientInputPwrLowWarning_Type = EkiOnOff
_PmoabAlmClientInputPwrLowWarning_Object = MibScalar
pmoabAlmClientInputPwrLowWarning = _PmoabAlmClientInputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 2, 1, 33, 3),
    _PmoabAlmClientInputPwrLowWarning_Type()
)
pmoabAlmClientInputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmClientInputPwrLowWarning.setStatus("current")
_PmoabAlmClientInputPwrHighWarning_Type = EkiOnOff
_PmoabAlmClientInputPwrHighWarning_Object = MibScalar
pmoabAlmClientInputPwrHighWarning = _PmoabAlmClientInputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 2, 1, 33, 4),
    _PmoabAlmClientInputPwrHighWarning_Type()
)
pmoabAlmClientInputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmClientInputPwrHighWarning.setStatus("current")
_PmoabAlmClientUrg_ObjectIdentity = ObjectIdentity
pmoabAlmClientUrg = _PmoabAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 2, 2)
)
_PmoabAlmclientEdfaAlarms1_ObjectIdentity = ObjectIdentity
pmoabAlmclientEdfaAlarms1 = _PmoabAlmclientEdfaAlarms1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 2, 2, 32)
)
_PmoabAlmClientInputPwrLowAlarm_Type = EkiOnOff
_PmoabAlmClientInputPwrLowAlarm_Object = MibScalar
pmoabAlmClientInputPwrLowAlarm = _PmoabAlmClientInputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 2, 2, 32, 3),
    _PmoabAlmClientInputPwrLowAlarm_Type()
)
pmoabAlmClientInputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmClientInputPwrLowAlarm.setStatus("current")
_PmoabAlmClientInputPwrHighAlarm_Type = EkiOnOff
_PmoabAlmClientInputPwrHighAlarm_Object = MibScalar
pmoabAlmClientInputPwrHighAlarm = _PmoabAlmClientInputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 2, 2, 32, 4),
    _PmoabAlmClientInputPwrHighAlarm_Type()
)
pmoabAlmClientInputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmClientInputPwrHighAlarm.setStatus("current")
_PmoabAlmClientCrit_ObjectIdentity = ObjectIdentity
pmoabAlmClientCrit = _PmoabAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 2, 3)
)
_PmoabAlmsynthAlm8_ObjectIdentity = ObjectIdentity
pmoabAlmsynthAlm8 = _PmoabAlmsynthAlm8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 2, 3, 8)
)
_PmoabAlmClientHwFail_Type = EkiOnOff
_PmoabAlmClientHwFail_Object = MibScalar
pmoabAlmClientHwFail = _PmoabAlmClientHwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 2, 3, 8, 4),
    _PmoabAlmClientHwFail_Type()
)
pmoabAlmClientHwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmClientHwFail.setStatus("current")
_PmoabAlmClientDdmWarning_Type = EkiOnOff
_PmoabAlmClientDdmWarning_Object = MibScalar
pmoabAlmClientDdmWarning = _PmoabAlmClientDdmWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 2, 3, 8, 9),
    _PmoabAlmClientDdmWarning_Type()
)
pmoabAlmClientDdmWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmClientDdmWarning.setStatus("current")
_PmoabAlmClientDdmAlm_Type = EkiOnOff
_PmoabAlmClientDdmAlm_Object = MibScalar
pmoabAlmClientDdmAlm = _PmoabAlmClientDdmAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 2, 3, 8, 10),
    _PmoabAlmClientDdmAlm_Type()
)
pmoabAlmClientDdmAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmClientDdmAlm.setStatus("current")
_PmoabAlmClientFail_Type = EkiOnOff
_PmoabAlmClientFail_Object = MibScalar
pmoabAlmClientFail = _PmoabAlmClientFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 2, 3, 8, 12),
    _PmoabAlmClientFail_Type()
)
pmoabAlmClientFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmClientFail.setStatus("current")
_PmoabAlmclientEdfaAlarms2_ObjectIdentity = ObjectIdentity
pmoabAlmclientEdfaAlarms2 = _PmoabAlmclientEdfaAlarms2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 2, 3, 35)
)
_PmoabAlmClientEdfaLos_Type = EkiOnOff
_PmoabAlmClientEdfaLos_Object = MibScalar
pmoabAlmClientEdfaLos = _PmoabAlmClientEdfaLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 2, 3, 35, 4),
    _PmoabAlmClientEdfaLos_Type()
)
pmoabAlmClientEdfaLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmClientEdfaLos.setStatus("current")
_PmoabAlmLine_ObjectIdentity = ObjectIdentity
pmoabAlmLine = _PmoabAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3)
)
_PmoabAlmLineNurg_ObjectIdentity = ObjectIdentity
pmoabAlmLineNurg = _PmoabAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 1)
)
_PmoabAlmlineEdfaWarnings_ObjectIdentity = ObjectIdentity
pmoabAlmlineEdfaWarnings = _PmoabAlmlineEdfaWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 1, 41)
)
_PmoabAlmLineGainLowWarning_Type = EkiOnOff
_PmoabAlmLineGainLowWarning_Object = MibScalar
pmoabAlmLineGainLowWarning = _PmoabAlmLineGainLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 1, 41, 1),
    _PmoabAlmLineGainLowWarning_Type()
)
pmoabAlmLineGainLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineGainLowWarning.setStatus("current")
_PmoabAlmLineGainHighWarning_Type = EkiOnOff
_PmoabAlmLineGainHighWarning_Object = MibScalar
pmoabAlmLineGainHighWarning = _PmoabAlmLineGainHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 1, 41, 2),
    _PmoabAlmLineGainHighWarning_Type()
)
pmoabAlmLineGainHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineGainHighWarning.setStatus("current")
_PmoabAlmLineOutputPwrLowWarning_Type = EkiOnOff
_PmoabAlmLineOutputPwrLowWarning_Object = MibScalar
pmoabAlmLineOutputPwrLowWarning = _PmoabAlmLineOutputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 1, 41, 5),
    _PmoabAlmLineOutputPwrLowWarning_Type()
)
pmoabAlmLineOutputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineOutputPwrLowWarning.setStatus("current")
_PmoabAlmLineOutputPwrHighWarning_Type = EkiOnOff
_PmoabAlmLineOutputPwrHighWarning_Object = MibScalar
pmoabAlmLineOutputPwrHighWarning = _PmoabAlmLineOutputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 1, 41, 6),
    _PmoabAlmLineOutputPwrHighWarning_Type()
)
pmoabAlmLineOutputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineOutputPwrHighWarning.setStatus("current")
_PmoabAlmLineBiasLowWarning_Type = EkiOnOff
_PmoabAlmLineBiasLowWarning_Object = MibScalar
pmoabAlmLineBiasLowWarning = _PmoabAlmLineBiasLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 1, 41, 7),
    _PmoabAlmLineBiasLowWarning_Type()
)
pmoabAlmLineBiasLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineBiasLowWarning.setStatus("current")
_PmoabAlmLineBiasHighWarning_Type = EkiOnOff
_PmoabAlmLineBiasHighWarning_Object = MibScalar
pmoabAlmLineBiasHighWarning = _PmoabAlmLineBiasHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 1, 41, 8),
    _PmoabAlmLineBiasHighWarning_Type()
)
pmoabAlmLineBiasHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineBiasHighWarning.setStatus("current")
_PmoabAlmLineUrg_ObjectIdentity = ObjectIdentity
pmoabAlmLineUrg = _PmoabAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 2)
)
_PmoabAlmlineEdfaAlarms1_ObjectIdentity = ObjectIdentity
pmoabAlmlineEdfaAlarms1 = _PmoabAlmlineEdfaAlarms1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 2, 40)
)
_PmoabAlmLineGainLowAlarm_Type = EkiOnOff
_PmoabAlmLineGainLowAlarm_Object = MibScalar
pmoabAlmLineGainLowAlarm = _PmoabAlmLineGainLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 2, 40, 1),
    _PmoabAlmLineGainLowAlarm_Type()
)
pmoabAlmLineGainLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineGainLowAlarm.setStatus("current")
_PmoabAlmLineGainHighAlarm_Type = EkiOnOff
_PmoabAlmLineGainHighAlarm_Object = MibScalar
pmoabAlmLineGainHighAlarm = _PmoabAlmLineGainHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 2, 40, 2),
    _PmoabAlmLineGainHighAlarm_Type()
)
pmoabAlmLineGainHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineGainHighAlarm.setStatus("current")
_PmoabAlmLineOutputPwrLowAlarm_Type = EkiOnOff
_PmoabAlmLineOutputPwrLowAlarm_Object = MibScalar
pmoabAlmLineOutputPwrLowAlarm = _PmoabAlmLineOutputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 2, 40, 5),
    _PmoabAlmLineOutputPwrLowAlarm_Type()
)
pmoabAlmLineOutputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineOutputPwrLowAlarm.setStatus("current")
_PmoabAlmLineOutputPwrHighAlarm_Type = EkiOnOff
_PmoabAlmLineOutputPwrHighAlarm_Object = MibScalar
pmoabAlmLineOutputPwrHighAlarm = _PmoabAlmLineOutputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 2, 40, 6),
    _PmoabAlmLineOutputPwrHighAlarm_Type()
)
pmoabAlmLineOutputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineOutputPwrHighAlarm.setStatus("current")
_PmoabAlmLineBiasLowAlarm_Type = EkiOnOff
_PmoabAlmLineBiasLowAlarm_Object = MibScalar
pmoabAlmLineBiasLowAlarm = _PmoabAlmLineBiasLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 2, 40, 7),
    _PmoabAlmLineBiasLowAlarm_Type()
)
pmoabAlmLineBiasLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineBiasLowAlarm.setStatus("current")
_PmoabAlmLineBiasHighAlarm_Type = EkiOnOff
_PmoabAlmLineBiasHighAlarm_Object = MibScalar
pmoabAlmLineBiasHighAlarm = _PmoabAlmLineBiasHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 2, 40, 8),
    _PmoabAlmLineBiasHighAlarm_Type()
)
pmoabAlmLineBiasHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineBiasHighAlarm.setStatus("current")
_PmoabAlmLineCrit_ObjectIdentity = ObjectIdentity
pmoabAlmLineCrit = _PmoabAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 3)
)
_PmoabAlmsynthAlm7_ObjectIdentity = ObjectIdentity
pmoabAlmsynthAlm7 = _PmoabAlmsynthAlm7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 3, 7)
)
_PmoabAlmLineHwFail_Type = EkiOnOff
_PmoabAlmLineHwFail_Object = MibScalar
pmoabAlmLineHwFail = _PmoabAlmLineHwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 3, 7, 4),
    _PmoabAlmLineHwFail_Type()
)
pmoabAlmLineHwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineHwFail.setStatus("current")
_PmoabAlmLineTxOff_Type = EkiOnOff
_PmoabAlmLineTxOff_Object = MibScalar
pmoabAlmLineTxOff = _PmoabAlmLineTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 3, 7, 5),
    _PmoabAlmLineTxOff_Type()
)
pmoabAlmLineTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineTxOff.setStatus("current")
_PmoabAlmLineDdmWarning_Type = EkiOnOff
_PmoabAlmLineDdmWarning_Object = MibScalar
pmoabAlmLineDdmWarning = _PmoabAlmLineDdmWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 3, 7, 9),
    _PmoabAlmLineDdmWarning_Type()
)
pmoabAlmLineDdmWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineDdmWarning.setStatus("current")
_PmoabAlmLineDdmAlm_Type = EkiOnOff
_PmoabAlmLineDdmAlm_Object = MibScalar
pmoabAlmLineDdmAlm = _PmoabAlmLineDdmAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 3, 7, 10),
    _PmoabAlmLineDdmAlm_Type()
)
pmoabAlmLineDdmAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineDdmAlm.setStatus("current")
_PmoabAlmLineFail_Type = EkiOnOff
_PmoabAlmLineFail_Object = MibScalar
pmoabAlmLineFail = _PmoabAlmLineFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 3, 7, 12),
    _PmoabAlmLineFail_Type()
)
pmoabAlmLineFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineFail.setStatus("current")
_PmoabAlmlineEdfaAlarms2_ObjectIdentity = ObjectIdentity
pmoabAlmlineEdfaAlarms2 = _PmoabAlmlineEdfaAlarms2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 3, 43)
)
_PmoabAlmLineEdfaNr_Type = EkiOnOff
_PmoabAlmLineEdfaNr_Object = MibScalar
pmoabAlmLineEdfaNr = _PmoabAlmLineEdfaNr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 3, 43, 1),
    _PmoabAlmLineEdfaNr_Type()
)
pmoabAlmLineEdfaNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineEdfaNr.setStatus("current")
_PmoabAlmLineEdfaTecFail_Type = EkiOnOff
_PmoabAlmLineEdfaTecFail_Object = MibScalar
pmoabAlmLineEdfaTecFail = _PmoabAlmLineEdfaTecFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 3, 43, 2),
    _PmoabAlmLineEdfaTecFail_Type()
)
pmoabAlmLineEdfaTecFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineEdfaTecFail.setStatus("current")
_PmoabAlmLineEdfaLaserFail_Type = EkiOnOff
_PmoabAlmLineEdfaLaserFail_Object = MibScalar
pmoabAlmLineEdfaLaserFail = _PmoabAlmLineEdfaLaserFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 3, 43, 3),
    _PmoabAlmLineEdfaLaserFail_Type()
)
pmoabAlmLineEdfaLaserFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineEdfaLaserFail.setStatus("current")
_PmoabAlmLineExtPumpEdfaLowCurrent_Type = EkiOnOff
_PmoabAlmLineExtPumpEdfaLowCurrent_Object = MibScalar
pmoabAlmLineExtPumpEdfaLowCurrent = _PmoabAlmLineExtPumpEdfaLowCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 2, 3, 3, 43, 5),
    _PmoabAlmLineExtPumpEdfaLowCurrent_Type()
)
pmoabAlmLineExtPumpEdfaLowCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabAlmLineExtPumpEdfaLowCurrent.setStatus("current")
_Pmoabmeasures_ObjectIdentity = ObjectIdentity
pmoabmeasures = _Pmoabmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 3)
)
_PmoabMesrOther_ObjectIdentity = ObjectIdentity
pmoabMesrOther = _PmoabMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 3, 1)
)


class _PmoabMesrtempMeas_Type(Integer32):
    """Custom type pmoabMesrtempMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabMesrtempMeas_Type.__name__ = "Integer32"
_PmoabMesrtempMeas_Object = MibScalar
pmoabMesrtempMeas = _PmoabMesrtempMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 3, 1, 72),
    _PmoabMesrtempMeas_Type()
)
pmoabMesrtempMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabMesrtempMeas.setStatus("current")


class _PmoabMesr3v3Meas_Type(Integer32):
    """Custom type pmoabMesr3v3Meas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabMesr3v3Meas_Type.__name__ = "Integer32"
_PmoabMesr3v3Meas_Object = MibScalar
pmoabMesr3v3Meas = _PmoabMesr3v3Meas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 3, 1, 73),
    _PmoabMesr3v3Meas_Type()
)
pmoabMesr3v3Meas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabMesr3v3Meas.setStatus("current")
_PmoabMesrClient_ObjectIdentity = ObjectIdentity
pmoabMesrClient = _PmoabMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 3, 2)
)


class _PmoabMesrclientEdfaRxpwrMeas_Type(Integer32):
    """Custom type pmoabMesrclientEdfaRxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabMesrclientEdfaRxpwrMeas_Type.__name__ = "Integer32"
_PmoabMesrclientEdfaRxpwrMeas_Object = MibScalar
pmoabMesrclientEdfaRxpwrMeas = _PmoabMesrclientEdfaRxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 3, 2, 34),
    _PmoabMesrclientEdfaRxpwrMeas_Type()
)
pmoabMesrclientEdfaRxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabMesrclientEdfaRxpwrMeas.setStatus("current")
_PmoabMesrLine_ObjectIdentity = ObjectIdentity
pmoabMesrLine = _PmoabMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 3, 3)
)


class _PmoabMesrlineEdfaBiasMeas_Type(Integer32):
    """Custom type pmoabMesrlineEdfaBiasMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabMesrlineEdfaBiasMeas_Type.__name__ = "Integer32"
_PmoabMesrlineEdfaBiasMeas_Object = MibScalar
pmoabMesrlineEdfaBiasMeas = _PmoabMesrlineEdfaBiasMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 3, 3, 40),
    _PmoabMesrlineEdfaBiasMeas_Type()
)
pmoabMesrlineEdfaBiasMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabMesrlineEdfaBiasMeas.setStatus("current")


class _PmoabMesrlineEdfaTxpwrMeas_Type(Integer32):
    """Custom type pmoabMesrlineEdfaTxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabMesrlineEdfaTxpwrMeas_Type.__name__ = "Integer32"
_PmoabMesrlineEdfaTxpwrMeas_Object = MibScalar
pmoabMesrlineEdfaTxpwrMeas = _PmoabMesrlineEdfaTxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 3, 3, 41),
    _PmoabMesrlineEdfaTxpwrMeas_Type()
)
pmoabMesrlineEdfaTxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabMesrlineEdfaTxpwrMeas.setStatus("current")


class _PmoabMesrlineEdfaGainMeas_Type(Integer32):
    """Custom type pmoabMesrlineEdfaGainMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabMesrlineEdfaGainMeas_Type.__name__ = "Integer32"
_PmoabMesrlineEdfaGainMeas_Object = MibScalar
pmoabMesrlineEdfaGainMeas = _PmoabMesrlineEdfaGainMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 3, 3, 43),
    _PmoabMesrlineEdfaGainMeas_Type()
)
pmoabMesrlineEdfaGainMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabMesrlineEdfaGainMeas.setStatus("current")
_PmoabcontrolsWrite_ObjectIdentity = ObjectIdentity
pmoabcontrolsWrite = _PmoabcontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6)
)
_PmoabCtrlOther_ObjectIdentity = ObjectIdentity
pmoabCtrlOther = _PmoabCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 1)
)
_PmoabCtrlsynth0_ObjectIdentity = ObjectIdentity
pmoabCtrlsynth0 = _PmoabCtrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 1, 0)
)
_PmoabCtrlConfLoad_Type = EkiOnOff
_PmoabCtrlConfLoad_Object = MibScalar
pmoabCtrlConfLoad = _PmoabCtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 1, 0, 1),
    _PmoabCtrlConfLoad_Type()
)
pmoabCtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCtrlConfLoad.setStatus("current")
_PmoabCtrlConfFlash_Type = EkiOnOff
_PmoabCtrlConfFlash_Object = MibScalar
pmoabCtrlConfFlash = _PmoabCtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 1, 0, 9),
    _PmoabCtrlConfFlash_Type()
)
pmoabCtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCtrlConfFlash.setStatus("current")
_PmoabCtrlConfClear_Type = EkiOnOff
_PmoabCtrlConfClear_Object = MibScalar
pmoabCtrlConfClear = _PmoabCtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 1, 0, 13),
    _PmoabCtrlConfClear_Type()
)
pmoabCtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCtrlConfClear.setStatus("current")
_PmoabCtrlswMgnt_ObjectIdentity = ObjectIdentity
pmoabCtrlswMgnt = _PmoabCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 1, 5)
)
_PmoabCtrlColdReset_Type = EkiOnOff
_PmoabCtrlColdReset_Object = MibScalar
pmoabCtrlColdReset = _PmoabCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 1, 5, 2),
    _PmoabCtrlColdReset_Type()
)
pmoabCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCtrlColdReset.setStatus("current")
_PmoabCtrlWarmReset_Type = EkiOnOff
_PmoabCtrlWarmReset_Object = MibScalar
pmoabCtrlWarmReset = _PmoabCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 1, 5, 3),
    _PmoabCtrlWarmReset_Type()
)
pmoabCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCtrlWarmReset.setStatus("current")
_PmoabCtrlpowerDown_ObjectIdentity = ObjectIdentity
pmoabCtrlpowerDown = _PmoabCtrlpowerDown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 1, 72)
)
_PmoabCtrlSoftPowerDown_Type = EkiOnOff
_PmoabCtrlSoftPowerDown_Object = MibScalar
pmoabCtrlSoftPowerDown = _PmoabCtrlSoftPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 1, 72, 1),
    _PmoabCtrlSoftPowerDown_Type()
)
pmoabCtrlSoftPowerDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCtrlSoftPowerDown.setStatus("current")
_PmoabCtrlledTest_ObjectIdentity = ObjectIdentity
pmoabCtrlledTest = _PmoabCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 1, 73)
)
_PmoabCtrlGreenLed_Type = EkiOnOff
_PmoabCtrlGreenLed_Object = MibScalar
pmoabCtrlGreenLed = _PmoabCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 1, 73, 1),
    _PmoabCtrlGreenLed_Type()
)
pmoabCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCtrlGreenLed.setStatus("current")
_PmoabCtrlRedLed_Type = EkiOnOff
_PmoabCtrlRedLed_Object = MibScalar
pmoabCtrlRedLed = _PmoabCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 1, 73, 2),
    _PmoabCtrlRedLed_Type()
)
pmoabCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCtrlRedLed.setStatus("current")
_PmoabCtrlLedOff_Type = EkiOnOff
_PmoabCtrlLedOff_Object = MibScalar
pmoabCtrlLedOff = _PmoabCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 1, 73, 3),
    _PmoabCtrlLedOff_Type()
)
pmoabCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCtrlLedOff.setStatus("current")
_PmoabCtrlmaintMode_ObjectIdentity = ObjectIdentity
pmoabCtrlmaintMode = _PmoabCtrlmaintMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 1, 75)
)
_PmoabCtrlMaintenance_Type = EkiOnOff
_PmoabCtrlMaintenance_Object = MibScalar
pmoabCtrlMaintenance = _PmoabCtrlMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 1, 75, 1),
    _PmoabCtrlMaintenance_Type()
)
pmoabCtrlMaintenance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCtrlMaintenance.setStatus("current")
_PmoabCtrlClient_ObjectIdentity = ObjectIdentity
pmoabCtrlClient = _PmoabCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 2)
)
_PmoabCtrlLine_ObjectIdentity = ObjectIdentity
pmoabCtrlLine = _PmoabCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 3)
)
_PmoabCtrllineEdfaLaserOff_ObjectIdentity = ObjectIdentity
pmoabCtrllineEdfaLaserOff = _PmoabCtrllineEdfaLaserOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 3, 40)
)
_PmoabCtrlLineEdfaLaserOff_Type = EkiOnOff
_PmoabCtrlLineEdfaLaserOff_Object = MibScalar
pmoabCtrlLineEdfaLaserOff = _PmoabCtrlLineEdfaLaserOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 3, 40, 1),
    _PmoabCtrlLineEdfaLaserOff_Type()
)
pmoabCtrlLineEdfaLaserOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCtrlLineEdfaLaserOff.setStatus("current")
_PmoabCtrllineEdfaMode_Type = PmoabboosterMode
_PmoabCtrllineEdfaMode_Object = MibScalar
pmoabCtrllineEdfaMode = _PmoabCtrllineEdfaMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 3, 41),
    _PmoabCtrllineEdfaMode_Type()
)
pmoabCtrllineEdfaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCtrllineEdfaMode.setStatus("current")


class _PmoabCtrllineIlasSettingValue_Type(Integer32):
    """Custom type pmoabCtrllineIlasSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabCtrllineIlasSettingValue_Type.__name__ = "Integer32"
_PmoabCtrllineIlasSettingValue_Object = MibScalar
pmoabCtrllineIlasSettingValue = _PmoabCtrllineIlasSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 3, 42),
    _PmoabCtrllineIlasSettingValue_Type()
)
pmoabCtrllineIlasSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCtrllineIlasSettingValue.setStatus("current")


class _PmoabCtrllinePlasSettingValue_Type(Integer32):
    """Custom type pmoabCtrllinePlasSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabCtrllinePlasSettingValue_Type.__name__ = "Integer32"
_PmoabCtrllinePlasSettingValue_Object = MibScalar
pmoabCtrllinePlasSettingValue = _PmoabCtrllinePlasSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 3, 43),
    _PmoabCtrllinePlasSettingValue_Type()
)
pmoabCtrllinePlasSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCtrllinePlasSettingValue.setStatus("current")


class _PmoabCtrllineGainSettingValue_Type(Integer32):
    """Custom type pmoabCtrllineGainSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabCtrllineGainSettingValue_Type.__name__ = "Integer32"
_PmoabCtrllineGainSettingValue_Object = MibScalar
pmoabCtrllineGainSettingValue = _PmoabCtrllineGainSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 3, 44),
    _PmoabCtrllineGainSettingValue_Type()
)
pmoabCtrllineGainSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCtrllineGainSettingValue.setStatus("current")


class _PmoabCtrllineEffPwrOutSettingValue_Type(Integer32):
    """Custom type pmoabCtrllineEffPwrOutSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabCtrllineEffPwrOutSettingValue_Type.__name__ = "Integer32"
_PmoabCtrllineEffPwrOutSettingValue_Object = MibScalar
pmoabCtrllineEffPwrOutSettingValue = _PmoabCtrllineEffPwrOutSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 6, 3, 45),
    _PmoabCtrllineEffPwrOutSettingValue_Type()
)
pmoabCtrllineEffPwrOutSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCtrllineEffPwrOutSettingValue.setStatus("current")
_Pmoabri_ObjectIdentity = ObjectIdentity
pmoabri = _Pmoabri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 7)
)
_PmoabRinvReloadInventory_Type = EkiOnOff
_PmoabRinvReloadInventory_Object = MibScalar
pmoabRinvReloadInventory = _PmoabRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 7, 2),
    _PmoabRinvReloadInventory_Type()
)
pmoabRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabRinvReloadInventory.setStatus("current")
_PmoabRinvModulePlatform_Type = DisplayString
_PmoabRinvModulePlatform_Object = MibScalar
pmoabRinvModulePlatform = _PmoabRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 7, 3),
    _PmoabRinvModulePlatform_Type()
)
pmoabRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabRinvModulePlatform.setStatus("current")
_PmoabRinvSwPlatform_Type = DisplayString
_PmoabRinvSwPlatform_Object = MibScalar
pmoabRinvSwPlatform = _PmoabRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 7, 4),
    _PmoabRinvSwPlatform_Type()
)
pmoabRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabRinvSwPlatform.setStatus("current")
_PmoabRinvSwFoa_Type = DisplayString
_PmoabRinvSwFoa_Object = MibScalar
pmoabRinvSwFoa = _PmoabRinvSwFoa_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 7, 5),
    _PmoabRinvSwFoa_Type()
)
pmoabRinvSwFoa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabRinvSwFoa.setStatus("current")
_PmoabRinvBoosterTable_Object = MibTable
pmoabRinvBoosterTable = _PmoabRinvBoosterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 7, 6)
)
if mibBuilder.loadTexts:
    pmoabRinvBoosterTable.setStatus("current")
_PmoabRinvBoosterEntry_Object = MibTableRow
pmoabRinvBoosterEntry = _PmoabRinvBoosterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 7, 6, 1)
)
pmoabRinvBoosterEntry.setIndexNames(
    (0, "EKINOPS-PmOab-MIB", "pmoabRinvBoosterIndex"),
)
if mibBuilder.loadTexts:
    pmoabRinvBoosterEntry.setStatus("current")


class _PmoabRinvBoosterIndex_Type(Integer32):
    """Custom type pmoabRinvBoosterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PmoabRinvBoosterIndex_Type.__name__ = "Integer32"
_PmoabRinvBoosterIndex_Object = MibTableColumn
pmoabRinvBoosterIndex = _PmoabRinvBoosterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 7, 6, 1, 1),
    _PmoabRinvBoosterIndex_Type()
)
pmoabRinvBoosterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabRinvBoosterIndex.setStatus("current")
_PmoabRinvBooster_Type = DisplayString
_PmoabRinvBooster_Object = MibTableColumn
pmoabRinvBooster = _PmoabRinvBooster_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 7, 6, 1, 2),
    _PmoabRinvBooster_Type()
)
pmoabRinvBooster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabRinvBooster.setStatus("current")
_PmoabConfig_ObjectIdentity = ObjectIdentity
pmoabConfig = _PmoabConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 9)
)
_PmoabCfgNoValue_ObjectIdentity = ObjectIdentity
pmoabCfgNoValue = _PmoabCfgNoValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 9, 1)
)
_PmoabtableclientStartup_ObjectIdentity = ObjectIdentity
pmoabtableclientStartup = _PmoabtableclientStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 9, 1, 1)
)
_PmoabCfgLineStartUp_ObjectIdentity = ObjectIdentity
pmoabCfgLineStartUp = _PmoabCfgLineStartUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 9, 2)
)
_PmoabtablelineStartup_ObjectIdentity = ObjectIdentity
pmoabtablelineStartup = _PmoabtablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 9, 2, 1)
)


class _PmoabCfglineEdfaLaserCtrl_Type(Unsigned32):
    """Custom type pmoabCfglineEdfaLaserCtrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabCfglineEdfaLaserCtrl_Type.__name__ = "Unsigned32"
_PmoabCfglineEdfaLaserCtrl_Object = MibScalar
pmoabCfglineEdfaLaserCtrl = _PmoabCfglineEdfaLaserCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 9, 2, 1, 2),
    _PmoabCfglineEdfaLaserCtrl_Type()
)
pmoabCfglineEdfaLaserCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCfglineEdfaLaserCtrl.setStatus("current")


class _PmoabCfglineEdfaLaserMode_Type(Unsigned32):
    """Custom type pmoabCfglineEdfaLaserMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabCfglineEdfaLaserMode_Type.__name__ = "Unsigned32"
_PmoabCfglineEdfaLaserMode_Object = MibScalar
pmoabCfglineEdfaLaserMode = _PmoabCfglineEdfaLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 9, 2, 1, 3),
    _PmoabCfglineEdfaLaserMode_Type()
)
pmoabCfglineEdfaLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCfglineEdfaLaserMode.setStatus("current")
_PmoabCfgLabels_ObjectIdentity = ObjectIdentity
pmoabCfgLabels = _PmoabCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 9, 3)
)
_PmoabCfgLabelclientTable_Object = MibTable
pmoabCfgLabelclientTable = _PmoabCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pmoabCfgLabelclientTable.setStatus("current")
_PmoabCfgLabelclientEntry_Object = MibTableRow
pmoabCfgLabelclientEntry = _PmoabCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 9, 3, 1, 1)
)
pmoabCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-PmOab-MIB", "pmoabCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmoabCfgLabelclientEntry.setStatus("current")


class _PmoabCfgLabelclientIndex_Type(Integer32):
    """Custom type pmoabCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoabCfgLabelclientIndex_Type.__name__ = "Integer32"
_PmoabCfgLabelclientIndex_Object = MibTableColumn
pmoabCfgLabelclientIndex = _PmoabCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 9, 3, 1, 1, 1),
    _PmoabCfgLabelclientIndex_Type()
)
pmoabCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabCfgLabelclientIndex.setStatus("current")


class _PmoabCfgLabelclientPortn_Type(DisplayString):
    """Custom type pmoabCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmoabCfgLabelclientPortn_Type.__name__ = "DisplayString"
_PmoabCfgLabelclientPortn_Object = MibTableColumn
pmoabCfgLabelclientPortn = _PmoabCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 9, 3, 1, 1, 3),
    _PmoabCfgLabelclientPortn_Type()
)
pmoabCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCfgLabelclientPortn.setStatus("current")
_PmoabCfgLabellineTable_Object = MibTable
pmoabCfgLabellineTable = _PmoabCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pmoabCfgLabellineTable.setStatus("current")
_PmoabCfgLabellineEntry_Object = MibTableRow
pmoabCfgLabellineEntry = _PmoabCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 9, 3, 2, 1)
)
pmoabCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-PmOab-MIB", "pmoabCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmoabCfgLabellineEntry.setStatus("current")


class _PmoabCfgLabellineIndex_Type(Integer32):
    """Custom type pmoabCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoabCfgLabellineIndex_Type.__name__ = "Integer32"
_PmoabCfgLabellineIndex_Object = MibTableColumn
pmoabCfgLabellineIndex = _PmoabCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 9, 3, 2, 1, 1),
    _PmoabCfgLabellineIndex_Type()
)
pmoabCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabCfgLabellineIndex.setStatus("current")


class _PmoabCfgLabellinePortn_Type(DisplayString):
    """Custom type pmoabCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmoabCfgLabellinePortn_Type.__name__ = "DisplayString"
_PmoabCfgLabellinePortn_Object = MibTableColumn
pmoabCfgLabellinePortn = _PmoabCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 9, 3, 2, 1, 3),
    _PmoabCfgLabellinePortn_Type()
)
pmoabCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCfgLabellinePortn.setStatus("current")
_PmoabCfgWriteConfiguration_Type = EkiOnOff
_PmoabCfgWriteConfiguration_Object = MibScalar
pmoabCfgWriteConfiguration = _PmoabCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 9, 257),
    _PmoabCfgWriteConfiguration_Type()
)
pmoabCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabCfgWriteConfiguration.setStatus("current")
_Pmoabtraps_ObjectIdentity = ObjectIdentity
pmoabtraps = _Pmoabtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 23, 10)
)


class _PmoabtrapBoardNumber_Type(Integer32):
    """Custom type pmoabtrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PmoabtrapBoardNumber_Type.__name__ = "Integer32"
_PmoabtrapBoardNumber_Object = MibScalar
pmoabtrapBoardNumber = _PmoabtrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 23, 10, 4),
    _PmoabtrapBoardNumber_Type()
)
pmoabtrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabtrapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pmoabLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 23, 10, 30)
)
pmoabLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOab-MIB", "pmoabAlmLineDdmWarning"),
        ("EKINOPS-PmOab-MIB", "pmoabtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmoabLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 23, 10, 31)
)
pmoabLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOab-MIB", "pmoabAlmLineDdmWarning"),
        ("EKINOPS-PmOab-MIB", "pmoabtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmoabLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 23, 10, 32)
)
pmoabLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOab-MIB", "pmoabAlmLineDdmAlm"),
        ("EKINOPS-PmOab-MIB", "pmoabtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pmoabLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 23, 10, 33)
)
pmoabLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOab-MIB", "pmoabAlmLineDdmAlm"),
        ("EKINOPS-PmOab-MIB", "pmoabtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pmoabLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 23, 10, 34)
)
pmoabLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-PmOab-MIB", "pmoabAlmLineFail"),
        ("EKINOPS-PmOab-MIB", "pmoabAlmLineHwFail"),
        ("EKINOPS-PmOab-MIB", "pmoabtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabLineTrapCritGoesOn.setStatus(
        "current"
    )

pmoabLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 23, 10, 35)
)
pmoabLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-PmOab-MIB", "pmoabAlmLineFail"),
        ("EKINOPS-PmOab-MIB", "pmoabAlmLineHwFail"),
        ("EKINOPS-PmOab-MIB", "pmoabtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabLineTrapCritGoesOff.setStatus(
        "current"
    )

pmoabClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 23, 10, 40)
)
pmoabClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOab-MIB", "pmoabAlmClientDdmWarning"),
        ("EKINOPS-PmOab-MIB", "pmoabtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmoabClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 23, 10, 41)
)
pmoabClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOab-MIB", "pmoabAlmClientDdmWarning"),
        ("EKINOPS-PmOab-MIB", "pmoabtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmoabClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 23, 10, 42)
)
pmoabClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOab-MIB", "pmoabAlmClientDdmAlm"),
        ("EKINOPS-PmOab-MIB", "pmoabtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pmoabClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 23, 10, 43)
)
pmoabClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOab-MIB", "pmoabAlmClientDdmAlm"),
        ("EKINOPS-PmOab-MIB", "pmoabtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pmoabClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 23, 10, 44)
)
pmoabClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-PmOab-MIB", "pmoabAlmClientFail"),
        ("EKINOPS-PmOab-MIB", "pmoabAlmClientHwFail"),
        ("EKINOPS-PmOab-MIB", "pmoabtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabClientTrapCritGoesOn.setStatus(
        "current"
    )

pmoabClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 23, 10, 45)
)
pmoabClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-PmOab-MIB", "pmoabAlmClientFail"),
        ("EKINOPS-PmOab-MIB", "pmoabAlmClientHwFail"),
        ("EKINOPS-PmOab-MIB", "pmoabtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabClientTrapCritGoesOff.setStatus(
        "current"
    )

pmoabPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 23, 10, 50)
)
pmoabPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOab-MIB", "pmoabAlmDefFuseB"),
        ("EKINOPS-PmOab-MIB", "pmoabAlmDefFuseA"),
        ("EKINOPS-PmOab-MIB", "pmoabtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmoabPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 23, 10, 51)
)
pmoabPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOab-MIB", "pmoabAlmDefFuseB"),
        ("EKINOPS-PmOab-MIB", "pmoabAlmDefFuseA"),
        ("EKINOPS-PmOab-MIB", "pmoabtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-PmOab-MIB",
    **{"PmoabboosterMode": PmoabboosterMode,
       "modulepmoab": modulepmoab,
       "pmoabalarms": pmoabalarms,
       "pmoabAlmOther": pmoabAlmOther,
       "pmoabAlmOtherNurg": pmoabAlmOtherNurg,
       "pmoabAlmsynthAlm2": pmoabAlmsynthAlm2,
       "pmoabAlmConfTableSave": pmoabAlmConfTableSave,
       "pmoabAlmInvUpload": pmoabAlmInvUpload,
       "pmoabAlmConfTableLoad": pmoabAlmConfTableLoad,
       "pmoabAlmfoaWarnings": pmoabAlmfoaWarnings,
       "pmoabAlm3v3LowWarning": pmoabAlm3v3LowWarning,
       "pmoabAlm3v3HighWarning": pmoabAlm3v3HighWarning,
       "pmoabAlmTermpLowWarning": pmoabAlmTermpLowWarning,
       "pmoabAlmTempHighWarning": pmoabAlmTempHighWarning,
       "pmoabAlmOtherUrg": pmoabAlmOtherUrg,
       "pmoabAlmfoaAlarms": pmoabAlmfoaAlarms,
       "pmoabAlm3v3LowAlarm": pmoabAlm3v3LowAlarm,
       "pmoabAlm3v3HighAlarm": pmoabAlm3v3HighAlarm,
       "pmoabAlmTermpLowAlarm": pmoabAlmTermpLowAlarm,
       "pmoabAlmTempHighAlarm": pmoabAlmTempHighAlarm,
       "pmoabAlmOtherCrit": pmoabAlmOtherCrit,
       "pmoabAlmsynthAlm0": pmoabAlmsynthAlm0,
       "pmoabAlmMaintenanceMode": pmoabAlmMaintenanceMode,
       "pmoabAlmModGlobFail": pmoabAlmModGlobFail,
       "pmoabAlmUpEdfaInitNotCompl": pmoabAlmUpEdfaInitNotCompl,
       "pmoabAlmDwEdfaInitNotCompl": pmoabAlmDwEdfaInitNotCompl,
       "pmoabAlmExtPumpNotLocked": pmoabAlmExtPumpNotLocked,
       "pmoabAlmDefFuseA": pmoabAlmDefFuseA,
       "pmoabAlmDefFuseB": pmoabAlmDefFuseB,
       "pmoabAlmClient": pmoabAlmClient,
       "pmoabAlmClientNurg": pmoabAlmClientNurg,
       "pmoabAlmclientEdfaWarnings": pmoabAlmclientEdfaWarnings,
       "pmoabAlmClientInputPwrLowWarning": pmoabAlmClientInputPwrLowWarning,
       "pmoabAlmClientInputPwrHighWarning": pmoabAlmClientInputPwrHighWarning,
       "pmoabAlmClientUrg": pmoabAlmClientUrg,
       "pmoabAlmclientEdfaAlarms1": pmoabAlmclientEdfaAlarms1,
       "pmoabAlmClientInputPwrLowAlarm": pmoabAlmClientInputPwrLowAlarm,
       "pmoabAlmClientInputPwrHighAlarm": pmoabAlmClientInputPwrHighAlarm,
       "pmoabAlmClientCrit": pmoabAlmClientCrit,
       "pmoabAlmsynthAlm8": pmoabAlmsynthAlm8,
       "pmoabAlmClientHwFail": pmoabAlmClientHwFail,
       "pmoabAlmClientDdmWarning": pmoabAlmClientDdmWarning,
       "pmoabAlmClientDdmAlm": pmoabAlmClientDdmAlm,
       "pmoabAlmClientFail": pmoabAlmClientFail,
       "pmoabAlmclientEdfaAlarms2": pmoabAlmclientEdfaAlarms2,
       "pmoabAlmClientEdfaLos": pmoabAlmClientEdfaLos,
       "pmoabAlmLine": pmoabAlmLine,
       "pmoabAlmLineNurg": pmoabAlmLineNurg,
       "pmoabAlmlineEdfaWarnings": pmoabAlmlineEdfaWarnings,
       "pmoabAlmLineGainLowWarning": pmoabAlmLineGainLowWarning,
       "pmoabAlmLineGainHighWarning": pmoabAlmLineGainHighWarning,
       "pmoabAlmLineOutputPwrLowWarning": pmoabAlmLineOutputPwrLowWarning,
       "pmoabAlmLineOutputPwrHighWarning": pmoabAlmLineOutputPwrHighWarning,
       "pmoabAlmLineBiasLowWarning": pmoabAlmLineBiasLowWarning,
       "pmoabAlmLineBiasHighWarning": pmoabAlmLineBiasHighWarning,
       "pmoabAlmLineUrg": pmoabAlmLineUrg,
       "pmoabAlmlineEdfaAlarms1": pmoabAlmlineEdfaAlarms1,
       "pmoabAlmLineGainLowAlarm": pmoabAlmLineGainLowAlarm,
       "pmoabAlmLineGainHighAlarm": pmoabAlmLineGainHighAlarm,
       "pmoabAlmLineOutputPwrLowAlarm": pmoabAlmLineOutputPwrLowAlarm,
       "pmoabAlmLineOutputPwrHighAlarm": pmoabAlmLineOutputPwrHighAlarm,
       "pmoabAlmLineBiasLowAlarm": pmoabAlmLineBiasLowAlarm,
       "pmoabAlmLineBiasHighAlarm": pmoabAlmLineBiasHighAlarm,
       "pmoabAlmLineCrit": pmoabAlmLineCrit,
       "pmoabAlmsynthAlm7": pmoabAlmsynthAlm7,
       "pmoabAlmLineHwFail": pmoabAlmLineHwFail,
       "pmoabAlmLineTxOff": pmoabAlmLineTxOff,
       "pmoabAlmLineDdmWarning": pmoabAlmLineDdmWarning,
       "pmoabAlmLineDdmAlm": pmoabAlmLineDdmAlm,
       "pmoabAlmLineFail": pmoabAlmLineFail,
       "pmoabAlmlineEdfaAlarms2": pmoabAlmlineEdfaAlarms2,
       "pmoabAlmLineEdfaNr": pmoabAlmLineEdfaNr,
       "pmoabAlmLineEdfaTecFail": pmoabAlmLineEdfaTecFail,
       "pmoabAlmLineEdfaLaserFail": pmoabAlmLineEdfaLaserFail,
       "pmoabAlmLineExtPumpEdfaLowCurrent": pmoabAlmLineExtPumpEdfaLowCurrent,
       "pmoabmeasures": pmoabmeasures,
       "pmoabMesrOther": pmoabMesrOther,
       "pmoabMesrtempMeas": pmoabMesrtempMeas,
       "pmoabMesr3v3Meas": pmoabMesr3v3Meas,
       "pmoabMesrClient": pmoabMesrClient,
       "pmoabMesrclientEdfaRxpwrMeas": pmoabMesrclientEdfaRxpwrMeas,
       "pmoabMesrLine": pmoabMesrLine,
       "pmoabMesrlineEdfaBiasMeas": pmoabMesrlineEdfaBiasMeas,
       "pmoabMesrlineEdfaTxpwrMeas": pmoabMesrlineEdfaTxpwrMeas,
       "pmoabMesrlineEdfaGainMeas": pmoabMesrlineEdfaGainMeas,
       "pmoabcontrolsWrite": pmoabcontrolsWrite,
       "pmoabCtrlOther": pmoabCtrlOther,
       "pmoabCtrlsynth0": pmoabCtrlsynth0,
       "pmoabCtrlConfLoad": pmoabCtrlConfLoad,
       "pmoabCtrlConfFlash": pmoabCtrlConfFlash,
       "pmoabCtrlConfClear": pmoabCtrlConfClear,
       "pmoabCtrlswMgnt": pmoabCtrlswMgnt,
       "pmoabCtrlColdReset": pmoabCtrlColdReset,
       "pmoabCtrlWarmReset": pmoabCtrlWarmReset,
       "pmoabCtrlpowerDown": pmoabCtrlpowerDown,
       "pmoabCtrlSoftPowerDown": pmoabCtrlSoftPowerDown,
       "pmoabCtrlledTest": pmoabCtrlledTest,
       "pmoabCtrlGreenLed": pmoabCtrlGreenLed,
       "pmoabCtrlRedLed": pmoabCtrlRedLed,
       "pmoabCtrlLedOff": pmoabCtrlLedOff,
       "pmoabCtrlmaintMode": pmoabCtrlmaintMode,
       "pmoabCtrlMaintenance": pmoabCtrlMaintenance,
       "pmoabCtrlClient": pmoabCtrlClient,
       "pmoabCtrlLine": pmoabCtrlLine,
       "pmoabCtrllineEdfaLaserOff": pmoabCtrllineEdfaLaserOff,
       "pmoabCtrlLineEdfaLaserOff": pmoabCtrlLineEdfaLaserOff,
       "pmoabCtrllineEdfaMode": pmoabCtrllineEdfaMode,
       "pmoabCtrllineIlasSettingValue": pmoabCtrllineIlasSettingValue,
       "pmoabCtrllinePlasSettingValue": pmoabCtrllinePlasSettingValue,
       "pmoabCtrllineGainSettingValue": pmoabCtrllineGainSettingValue,
       "pmoabCtrllineEffPwrOutSettingValue": pmoabCtrllineEffPwrOutSettingValue,
       "pmoabri": pmoabri,
       "pmoabRinvReloadInventory": pmoabRinvReloadInventory,
       "pmoabRinvModulePlatform": pmoabRinvModulePlatform,
       "pmoabRinvSwPlatform": pmoabRinvSwPlatform,
       "pmoabRinvSwFoa": pmoabRinvSwFoa,
       "pmoabRinvBoosterTable": pmoabRinvBoosterTable,
       "pmoabRinvBoosterEntry": pmoabRinvBoosterEntry,
       "pmoabRinvBoosterIndex": pmoabRinvBoosterIndex,
       "pmoabRinvBooster": pmoabRinvBooster,
       "pmoabConfig": pmoabConfig,
       "pmoabCfgNoValue": pmoabCfgNoValue,
       "pmoabtableclientStartup": pmoabtableclientStartup,
       "pmoabCfgLineStartUp": pmoabCfgLineStartUp,
       "pmoabtablelineStartup": pmoabtablelineStartup,
       "pmoabCfglineEdfaLaserCtrl": pmoabCfglineEdfaLaserCtrl,
       "pmoabCfglineEdfaLaserMode": pmoabCfglineEdfaLaserMode,
       "pmoabCfgLabels": pmoabCfgLabels,
       "pmoabCfgLabelclientTable": pmoabCfgLabelclientTable,
       "pmoabCfgLabelclientEntry": pmoabCfgLabelclientEntry,
       "pmoabCfgLabelclientIndex": pmoabCfgLabelclientIndex,
       "pmoabCfgLabelclientPortn": pmoabCfgLabelclientPortn,
       "pmoabCfgLabellineTable": pmoabCfgLabellineTable,
       "pmoabCfgLabellineEntry": pmoabCfgLabellineEntry,
       "pmoabCfgLabellineIndex": pmoabCfgLabellineIndex,
       "pmoabCfgLabellinePortn": pmoabCfgLabellinePortn,
       "pmoabCfgWriteConfiguration": pmoabCfgWriteConfiguration,
       "pmoabtraps": pmoabtraps,
       "pmoabtrapBoardNumber": pmoabtrapBoardNumber,
       "pmoabLineTrapNotUrgentGoesOn": pmoabLineTrapNotUrgentGoesOn,
       "pmoabLineTrapNotUrgentGoesOff": pmoabLineTrapNotUrgentGoesOff,
       "pmoabLineTrapUrgentGoesOn": pmoabLineTrapUrgentGoesOn,
       "pmoabLineTrapUrgentGoesOff": pmoabLineTrapUrgentGoesOff,
       "pmoabLineTrapCritGoesOn": pmoabLineTrapCritGoesOn,
       "pmoabLineTrapCritGoesOff": pmoabLineTrapCritGoesOff,
       "pmoabClientTrapNotUrgentGoesOn": pmoabClientTrapNotUrgentGoesOn,
       "pmoabClientTrapNotUrgentGoesOff": pmoabClientTrapNotUrgentGoesOff,
       "pmoabClientTrapUrgentGoesOn": pmoabClientTrapUrgentGoesOn,
       "pmoabClientTrapUrgentGoesOff": pmoabClientTrapUrgentGoesOff,
       "pmoabClientTrapCritGoesOn": pmoabClientTrapCritGoesOn,
       "pmoabClientTrapCritGoesOff": pmoabClientTrapCritGoesOff,
       "pmoabPowerTrapUrgentGoesOn": pmoabPowerTrapUrgentGoesOn,
       "pmoabPowerTrapUrgentGoesOff": pmoabPowerTrapUrgentGoesOff}
)
