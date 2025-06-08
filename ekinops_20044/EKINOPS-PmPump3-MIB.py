# SNMP MIB module (EKINOPS-PmPump3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-PmPump3-MIB.mib
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

modulepmpump3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49)
)
if mibBuilder.loadTexts:
    modulepmpump3.setRevisions(
        ("2010-09-01 00:00",
         "2010-12-15 00:00",
         "2011-09-20 00:00",
         "2012-07-04 00:00",
         "2014-03-26 00:00",
         "2014-11-25 00:00",
         "2016-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pmpump3alarms_ObjectIdentity = ObjectIdentity
pmpump3alarms = _Pmpump3alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2)
)
_Pmpump3AlmOther_ObjectIdentity = ObjectIdentity
pmpump3AlmOther = _Pmpump3AlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 1)
)
_Pmpump3AlmOtherNurg_ObjectIdentity = ObjectIdentity
pmpump3AlmOtherNurg = _Pmpump3AlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 1, 1)
)
_Pmpump3AlmsynthAlm2_ObjectIdentity = ObjectIdentity
pmpump3AlmsynthAlm2 = _Pmpump3AlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 1, 1, 2)
)
_Pmpump3AlmConfTableSave_Type = EkiOnOff
_Pmpump3AlmConfTableSave_Object = MibScalar
pmpump3AlmConfTableSave = _Pmpump3AlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 1, 1, 2, 1),
    _Pmpump3AlmConfTableSave_Type()
)
pmpump3AlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmConfTableSave.setStatus("current")
_Pmpump3AlmInvUpload_Type = EkiOnOff
_Pmpump3AlmInvUpload_Object = MibScalar
pmpump3AlmInvUpload = _Pmpump3AlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 1, 1, 2, 2),
    _Pmpump3AlmInvUpload_Type()
)
pmpump3AlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmInvUpload.setStatus("current")
_Pmpump3AlmConfTableLoad_Type = EkiOnOff
_Pmpump3AlmConfTableLoad_Object = MibScalar
pmpump3AlmConfTableLoad = _Pmpump3AlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 1, 1, 2, 3),
    _Pmpump3AlmConfTableLoad_Type()
)
pmpump3AlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmConfTableLoad.setStatus("current")
_Pmpump3AlmpmWarnings_ObjectIdentity = ObjectIdentity
pmpump3AlmpmWarnings = _Pmpump3AlmpmWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 1, 1, 75)
)
_Pmpump3AlmTermpLowWarning_Type = EkiOnOff
_Pmpump3AlmTermpLowWarning_Object = MibScalar
pmpump3AlmTermpLowWarning = _Pmpump3AlmTermpLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 1, 1, 75, 1),
    _Pmpump3AlmTermpLowWarning_Type()
)
pmpump3AlmTermpLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmTermpLowWarning.setStatus("current")
_Pmpump3AlmTempHighWarning_Type = EkiOnOff
_Pmpump3AlmTempHighWarning_Object = MibScalar
pmpump3AlmTempHighWarning = _Pmpump3AlmTempHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 1, 1, 75, 2),
    _Pmpump3AlmTempHighWarning_Type()
)
pmpump3AlmTempHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmTempHighWarning.setStatus("current")
_Pmpump3AlmOtherUrg_ObjectIdentity = ObjectIdentity
pmpump3AlmOtherUrg = _Pmpump3AlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 1, 2)
)
_Pmpump3AlmpmAlarms_ObjectIdentity = ObjectIdentity
pmpump3AlmpmAlarms = _Pmpump3AlmpmAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 1, 2, 74)
)
_Pmpump3AlmTermpLowAlarm_Type = EkiOnOff
_Pmpump3AlmTermpLowAlarm_Object = MibScalar
pmpump3AlmTermpLowAlarm = _Pmpump3AlmTermpLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 1, 2, 74, 1),
    _Pmpump3AlmTermpLowAlarm_Type()
)
pmpump3AlmTermpLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmTermpLowAlarm.setStatus("current")
_Pmpump3AlmTempHighAlarm_Type = EkiOnOff
_Pmpump3AlmTempHighAlarm_Object = MibScalar
pmpump3AlmTempHighAlarm = _Pmpump3AlmTempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 1, 2, 74, 2),
    _Pmpump3AlmTempHighAlarm_Type()
)
pmpump3AlmTempHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmTempHighAlarm.setStatus("current")
_Pmpump3AlmOtherCrit_ObjectIdentity = ObjectIdentity
pmpump3AlmOtherCrit = _Pmpump3AlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 1, 3)
)
_Pmpump3AlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmpump3AlmsynthAlm0 = _Pmpump3AlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 1, 3, 0)
)
_Pmpump3AlmModGlobFail_Type = EkiOnOff
_Pmpump3AlmModGlobFail_Object = MibScalar
pmpump3AlmModGlobFail = _Pmpump3AlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 1, 3, 0, 9),
    _Pmpump3AlmModGlobFail_Type()
)
pmpump3AlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmModGlobFail.setStatus("current")
_Pmpump3AlmDefFuseA_Type = EkiOnOff
_Pmpump3AlmDefFuseA_Object = MibScalar
pmpump3AlmDefFuseA = _Pmpump3AlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 1, 3, 0, 15),
    _Pmpump3AlmDefFuseA_Type()
)
pmpump3AlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmDefFuseA.setStatus("current")
_Pmpump3AlmDefFuseB_Type = EkiOnOff
_Pmpump3AlmDefFuseB_Object = MibScalar
pmpump3AlmDefFuseB = _Pmpump3AlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 1, 3, 0, 16),
    _Pmpump3AlmDefFuseB_Type()
)
pmpump3AlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmDefFuseB.setStatus("current")
_Pmpump3AlmClient_ObjectIdentity = ObjectIdentity
pmpump3AlmClient = _Pmpump3AlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2)
)
_Pmpump3AlmClientNurg_ObjectIdentity = ObjectIdentity
pmpump3AlmClientNurg = _Pmpump3AlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 1)
)
_Pmpump3Almlaser1Warnings_ObjectIdentity = ObjectIdentity
pmpump3Almlaser1Warnings = _Pmpump3Almlaser1Warnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 1, 17)
)
_Pmpump3AlmLaser1TempLowWarning_Type = EkiOnOff
_Pmpump3AlmLaser1TempLowWarning_Object = MibScalar
pmpump3AlmLaser1TempLowWarning = _Pmpump3AlmLaser1TempLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 1, 17, 1),
    _Pmpump3AlmLaser1TempLowWarning_Type()
)
pmpump3AlmLaser1TempLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1TempLowWarning.setStatus("current")
_Pmpump3AlmLaser1TempHighWarning_Type = EkiOnOff
_Pmpump3AlmLaser1TempHighWarning_Object = MibScalar
pmpump3AlmLaser1TempHighWarning = _Pmpump3AlmLaser1TempHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 1, 17, 2),
    _Pmpump3AlmLaser1TempHighWarning_Type()
)
pmpump3AlmLaser1TempHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1TempHighWarning.setStatus("current")
_Pmpump3AlmLaser1VthLowWarning_Type = EkiOnOff
_Pmpump3AlmLaser1VthLowWarning_Object = MibScalar
pmpump3AlmLaser1VthLowWarning = _Pmpump3AlmLaser1VthLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 1, 17, 3),
    _Pmpump3AlmLaser1VthLowWarning_Type()
)
pmpump3AlmLaser1VthLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1VthLowWarning.setStatus("current")
_Pmpump3AlmLaser1VthHighWarning_Type = EkiOnOff
_Pmpump3AlmLaser1VthHighWarning_Object = MibScalar
pmpump3AlmLaser1VthHighWarning = _Pmpump3AlmLaser1VthHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 1, 17, 4),
    _Pmpump3AlmLaser1VthHighWarning_Type()
)
pmpump3AlmLaser1VthHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1VthHighWarning.setStatus("current")
_Pmpump3AlmLaser1OutputPwrLowWarning_Type = EkiOnOff
_Pmpump3AlmLaser1OutputPwrLowWarning_Object = MibScalar
pmpump3AlmLaser1OutputPwrLowWarning = _Pmpump3AlmLaser1OutputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 1, 17, 5),
    _Pmpump3AlmLaser1OutputPwrLowWarning_Type()
)
pmpump3AlmLaser1OutputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1OutputPwrLowWarning.setStatus("current")
_Pmpump3AlmLaser1OutputPwrHighWarning_Type = EkiOnOff
_Pmpump3AlmLaser1OutputPwrHighWarning_Object = MibScalar
pmpump3AlmLaser1OutputPwrHighWarning = _Pmpump3AlmLaser1OutputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 1, 17, 6),
    _Pmpump3AlmLaser1OutputPwrHighWarning_Type()
)
pmpump3AlmLaser1OutputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1OutputPwrHighWarning.setStatus("current")
_Pmpump3AlmLaser1BiasLowWarning_Type = EkiOnOff
_Pmpump3AlmLaser1BiasLowWarning_Object = MibScalar
pmpump3AlmLaser1BiasLowWarning = _Pmpump3AlmLaser1BiasLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 1, 17, 7),
    _Pmpump3AlmLaser1BiasLowWarning_Type()
)
pmpump3AlmLaser1BiasLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1BiasLowWarning.setStatus("current")
_Pmpump3AlmLaser1BiasHighWarning_Type = EkiOnOff
_Pmpump3AlmLaser1BiasHighWarning_Object = MibScalar
pmpump3AlmLaser1BiasHighWarning = _Pmpump3AlmLaser1BiasHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 1, 17, 8),
    _Pmpump3AlmLaser1BiasHighWarning_Type()
)
pmpump3AlmLaser1BiasHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1BiasHighWarning.setStatus("current")
_Pmpump3AlmClientUrg_ObjectIdentity = ObjectIdentity
pmpump3AlmClientUrg = _Pmpump3AlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 2)
)
_Pmpump3Almlaser1Alarms1_ObjectIdentity = ObjectIdentity
pmpump3Almlaser1Alarms1 = _Pmpump3Almlaser1Alarms1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 2, 16)
)
_Pmpump3AlmLaser1TempLowAlarm_Type = EkiOnOff
_Pmpump3AlmLaser1TempLowAlarm_Object = MibScalar
pmpump3AlmLaser1TempLowAlarm = _Pmpump3AlmLaser1TempLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 2, 16, 1),
    _Pmpump3AlmLaser1TempLowAlarm_Type()
)
pmpump3AlmLaser1TempLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1TempLowAlarm.setStatus("current")
_Pmpump3AlmLaser1TempHighAlarm_Type = EkiOnOff
_Pmpump3AlmLaser1TempHighAlarm_Object = MibScalar
pmpump3AlmLaser1TempHighAlarm = _Pmpump3AlmLaser1TempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 2, 16, 2),
    _Pmpump3AlmLaser1TempHighAlarm_Type()
)
pmpump3AlmLaser1TempHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1TempHighAlarm.setStatus("current")
_Pmpump3AlmLaser1VthLowAlarm_Type = EkiOnOff
_Pmpump3AlmLaser1VthLowAlarm_Object = MibScalar
pmpump3AlmLaser1VthLowAlarm = _Pmpump3AlmLaser1VthLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 2, 16, 3),
    _Pmpump3AlmLaser1VthLowAlarm_Type()
)
pmpump3AlmLaser1VthLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1VthLowAlarm.setStatus("current")
_Pmpump3AlmLaser1VthHighAlarm_Type = EkiOnOff
_Pmpump3AlmLaser1VthHighAlarm_Object = MibScalar
pmpump3AlmLaser1VthHighAlarm = _Pmpump3AlmLaser1VthHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 2, 16, 4),
    _Pmpump3AlmLaser1VthHighAlarm_Type()
)
pmpump3AlmLaser1VthHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1VthHighAlarm.setStatus("current")
_Pmpump3AlmLaser1OutputPwrLowAlarm_Type = EkiOnOff
_Pmpump3AlmLaser1OutputPwrLowAlarm_Object = MibScalar
pmpump3AlmLaser1OutputPwrLowAlarm = _Pmpump3AlmLaser1OutputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 2, 16, 5),
    _Pmpump3AlmLaser1OutputPwrLowAlarm_Type()
)
pmpump3AlmLaser1OutputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1OutputPwrLowAlarm.setStatus("current")
_Pmpump3AlmLaser1OutputPwrHighAlarm_Type = EkiOnOff
_Pmpump3AlmLaser1OutputPwrHighAlarm_Object = MibScalar
pmpump3AlmLaser1OutputPwrHighAlarm = _Pmpump3AlmLaser1OutputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 2, 16, 6),
    _Pmpump3AlmLaser1OutputPwrHighAlarm_Type()
)
pmpump3AlmLaser1OutputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1OutputPwrHighAlarm.setStatus("current")
_Pmpump3AlmLaser1BiasLowAlarm_Type = EkiOnOff
_Pmpump3AlmLaser1BiasLowAlarm_Object = MibScalar
pmpump3AlmLaser1BiasLowAlarm = _Pmpump3AlmLaser1BiasLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 2, 16, 7),
    _Pmpump3AlmLaser1BiasLowAlarm_Type()
)
pmpump3AlmLaser1BiasLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1BiasLowAlarm.setStatus("current")
_Pmpump3AlmLaser1BiasHighAlarm_Type = EkiOnOff
_Pmpump3AlmLaser1BiasHighAlarm_Object = MibScalar
pmpump3AlmLaser1BiasHighAlarm = _Pmpump3AlmLaser1BiasHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 2, 16, 8),
    _Pmpump3AlmLaser1BiasHighAlarm_Type()
)
pmpump3AlmLaser1BiasHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1BiasHighAlarm.setStatus("current")
_Pmpump3AlmClientCrit_ObjectIdentity = ObjectIdentity
pmpump3AlmClientCrit = _Pmpump3AlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3)
)
_Pmpump3AlmsynthAlmLaser1_ObjectIdentity = ObjectIdentity
pmpump3AlmsynthAlmLaser1 = _Pmpump3AlmsynthAlmLaser1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 8)
)
_Pmpump3AlmLaser1InitNotCompl_Type = EkiOnOff
_Pmpump3AlmLaser1InitNotCompl_Object = MibScalar
pmpump3AlmLaser1InitNotCompl = _Pmpump3AlmLaser1InitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 8, 2),
    _Pmpump3AlmLaser1InitNotCompl_Type()
)
pmpump3AlmLaser1InitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1InitNotCompl.setStatus("current")
_Pmpump3AlmLaser1HwFail_Type = EkiOnOff
_Pmpump3AlmLaser1HwFail_Object = MibScalar
pmpump3AlmLaser1HwFail = _Pmpump3AlmLaser1HwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 8, 4),
    _Pmpump3AlmLaser1HwFail_Type()
)
pmpump3AlmLaser1HwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1HwFail.setStatus("current")
_Pmpump3AlmLaser1TxOff_Type = EkiOnOff
_Pmpump3AlmLaser1TxOff_Object = MibScalar
pmpump3AlmLaser1TxOff = _Pmpump3AlmLaser1TxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 8, 5),
    _Pmpump3AlmLaser1TxOff_Type()
)
pmpump3AlmLaser1TxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1TxOff.setStatus("current")
_Pmpump3AlmLaser1Oos_Type = EkiOnOff
_Pmpump3AlmLaser1Oos_Object = MibScalar
pmpump3AlmLaser1Oos = _Pmpump3AlmLaser1Oos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 8, 6),
    _Pmpump3AlmLaser1Oos_Type()
)
pmpump3AlmLaser1Oos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1Oos.setStatus("current")
_Pmpump3AlmLaser1Warning_Type = EkiOnOff
_Pmpump3AlmLaser1Warning_Object = MibScalar
pmpump3AlmLaser1Warning = _Pmpump3AlmLaser1Warning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 8, 9),
    _Pmpump3AlmLaser1Warning_Type()
)
pmpump3AlmLaser1Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1Warning.setStatus("current")
_Pmpump3AlmLaser1Alm_Type = EkiOnOff
_Pmpump3AlmLaser1Alm_Object = MibScalar
pmpump3AlmLaser1Alm = _Pmpump3AlmLaser1Alm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 8, 10),
    _Pmpump3AlmLaser1Alm_Type()
)
pmpump3AlmLaser1Alm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1Alm.setStatus("current")
_Pmpump3AlmLaser1Fail_Type = EkiOnOff
_Pmpump3AlmLaser1Fail_Object = MibScalar
pmpump3AlmLaser1Fail = _Pmpump3AlmLaser1Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 8, 12),
    _Pmpump3AlmLaser1Fail_Type()
)
pmpump3AlmLaser1Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1Fail.setStatus("current")
_Pmpump3AlmsynthAlmLaser2_ObjectIdentity = ObjectIdentity
pmpump3AlmsynthAlmLaser2 = _Pmpump3AlmsynthAlmLaser2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 9)
)
_Pmpump3AlmLaser2InitNotCompl_Type = EkiOnOff
_Pmpump3AlmLaser2InitNotCompl_Object = MibScalar
pmpump3AlmLaser2InitNotCompl = _Pmpump3AlmLaser2InitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 9, 2),
    _Pmpump3AlmLaser2InitNotCompl_Type()
)
pmpump3AlmLaser2InitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2InitNotCompl.setStatus("current")
_Pmpump3AlmLaser2HwFail_Type = EkiOnOff
_Pmpump3AlmLaser2HwFail_Object = MibScalar
pmpump3AlmLaser2HwFail = _Pmpump3AlmLaser2HwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 9, 4),
    _Pmpump3AlmLaser2HwFail_Type()
)
pmpump3AlmLaser2HwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2HwFail.setStatus("current")
_Pmpump3AlmLaser2TxOff_Type = EkiOnOff
_Pmpump3AlmLaser2TxOff_Object = MibScalar
pmpump3AlmLaser2TxOff = _Pmpump3AlmLaser2TxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 9, 5),
    _Pmpump3AlmLaser2TxOff_Type()
)
pmpump3AlmLaser2TxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2TxOff.setStatus("current")
_Pmpump3AlmLaser2Oos_Type = EkiOnOff
_Pmpump3AlmLaser2Oos_Object = MibScalar
pmpump3AlmLaser2Oos = _Pmpump3AlmLaser2Oos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 9, 6),
    _Pmpump3AlmLaser2Oos_Type()
)
pmpump3AlmLaser2Oos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2Oos.setStatus("current")
_Pmpump3AlmLaser2Warning_Type = EkiOnOff
_Pmpump3AlmLaser2Warning_Object = MibScalar
pmpump3AlmLaser2Warning = _Pmpump3AlmLaser2Warning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 9, 9),
    _Pmpump3AlmLaser2Warning_Type()
)
pmpump3AlmLaser2Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2Warning.setStatus("current")
_Pmpump3AlmLaser2Alm_Type = EkiOnOff
_Pmpump3AlmLaser2Alm_Object = MibScalar
pmpump3AlmLaser2Alm = _Pmpump3AlmLaser2Alm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 9, 10),
    _Pmpump3AlmLaser2Alm_Type()
)
pmpump3AlmLaser2Alm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2Alm.setStatus("current")
_Pmpump3AlmLaser2Fail_Type = EkiOnOff
_Pmpump3AlmLaser2Fail_Object = MibScalar
pmpump3AlmLaser2Fail = _Pmpump3AlmLaser2Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 9, 12),
    _Pmpump3AlmLaser2Fail_Type()
)
pmpump3AlmLaser2Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2Fail.setStatus("current")
_Pmpump3Almlaser1Alarms2_ObjectIdentity = ObjectIdentity
pmpump3Almlaser1Alarms2 = _Pmpump3Almlaser1Alarms2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 19)
)
_Pmpump3AlmLaser1AlmCurrent_Type = EkiOnOff
_Pmpump3AlmLaser1AlmCurrent_Object = MibScalar
pmpump3AlmLaser1AlmCurrent = _Pmpump3AlmLaser1AlmCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 19, 1),
    _Pmpump3AlmLaser1AlmCurrent_Type()
)
pmpump3AlmLaser1AlmCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1AlmCurrent.setStatus("current")
_Pmpump3AlmLaser1AlmTemp_Type = EkiOnOff
_Pmpump3AlmLaser1AlmTemp_Object = MibScalar
pmpump3AlmLaser1AlmTemp = _Pmpump3AlmLaser1AlmTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 19, 2),
    _Pmpump3AlmLaser1AlmTemp_Type()
)
pmpump3AlmLaser1AlmTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1AlmTemp.setStatus("current")
_Pmpump3AlmLaser1AlmTecPower_Type = EkiOnOff
_Pmpump3AlmLaser1AlmTecPower_Object = MibScalar
pmpump3AlmLaser1AlmTecPower = _Pmpump3AlmLaser1AlmTecPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 19, 3),
    _Pmpump3AlmLaser1AlmTecPower_Type()
)
pmpump3AlmLaser1AlmTecPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1AlmTecPower.setStatus("current")
_Pmpump3AlmLaser1AlmTecDev_Type = EkiOnOff
_Pmpump3AlmLaser1AlmTecDev_Object = MibScalar
pmpump3AlmLaser1AlmTecDev = _Pmpump3AlmLaser1AlmTecDev_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 19, 4),
    _Pmpump3AlmLaser1AlmTecDev_Type()
)
pmpump3AlmLaser1AlmTecDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1AlmTecDev.setStatus("current")
_Pmpump3AlmLaser1OaDisconnectedLsd_Type = EkiOnOff
_Pmpump3AlmLaser1OaDisconnectedLsd_Object = MibScalar
pmpump3AlmLaser1OaDisconnectedLsd = _Pmpump3AlmLaser1OaDisconnectedLsd_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 19, 5),
    _Pmpump3AlmLaser1OaDisconnectedLsd_Type()
)
pmpump3AlmLaser1OaDisconnectedLsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1OaDisconnectedLsd.setStatus("current")
_Pmpump3AlmLaser1ExtLsd_Type = EkiOnOff
_Pmpump3AlmLaser1ExtLsd_Object = MibScalar
pmpump3AlmLaser1ExtLsd = _Pmpump3AlmLaser1ExtLsd_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 2, 3, 19, 6),
    _Pmpump3AlmLaser1ExtLsd_Type()
)
pmpump3AlmLaser1ExtLsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser1ExtLsd.setStatus("current")
_Pmpump3AlmLine_ObjectIdentity = ObjectIdentity
pmpump3AlmLine = _Pmpump3AlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3)
)
_Pmpump3AlmLineNurg_ObjectIdentity = ObjectIdentity
pmpump3AlmLineNurg = _Pmpump3AlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 1)
)
_Pmpump3Almlaser2Warnings_ObjectIdentity = ObjectIdentity
pmpump3Almlaser2Warnings = _Pmpump3Almlaser2Warnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 1, 25)
)
_Pmpump3AlmLaser2TempLowWarning_Type = EkiOnOff
_Pmpump3AlmLaser2TempLowWarning_Object = MibScalar
pmpump3AlmLaser2TempLowWarning = _Pmpump3AlmLaser2TempLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 1, 25, 1),
    _Pmpump3AlmLaser2TempLowWarning_Type()
)
pmpump3AlmLaser2TempLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2TempLowWarning.setStatus("current")
_Pmpump3AlmLaser2TempHighWarning_Type = EkiOnOff
_Pmpump3AlmLaser2TempHighWarning_Object = MibScalar
pmpump3AlmLaser2TempHighWarning = _Pmpump3AlmLaser2TempHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 1, 25, 2),
    _Pmpump3AlmLaser2TempHighWarning_Type()
)
pmpump3AlmLaser2TempHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2TempHighWarning.setStatus("current")
_Pmpump3AlmLaser2VthLowWarning_Type = EkiOnOff
_Pmpump3AlmLaser2VthLowWarning_Object = MibScalar
pmpump3AlmLaser2VthLowWarning = _Pmpump3AlmLaser2VthLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 1, 25, 3),
    _Pmpump3AlmLaser2VthLowWarning_Type()
)
pmpump3AlmLaser2VthLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2VthLowWarning.setStatus("current")
_Pmpump3AlmLaser2VthHighWarning_Type = EkiOnOff
_Pmpump3AlmLaser2VthHighWarning_Object = MibScalar
pmpump3AlmLaser2VthHighWarning = _Pmpump3AlmLaser2VthHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 1, 25, 4),
    _Pmpump3AlmLaser2VthHighWarning_Type()
)
pmpump3AlmLaser2VthHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2VthHighWarning.setStatus("current")
_Pmpump3AlmLaser2OutputPwrLowWarning_Type = EkiOnOff
_Pmpump3AlmLaser2OutputPwrLowWarning_Object = MibScalar
pmpump3AlmLaser2OutputPwrLowWarning = _Pmpump3AlmLaser2OutputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 1, 25, 5),
    _Pmpump3AlmLaser2OutputPwrLowWarning_Type()
)
pmpump3AlmLaser2OutputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2OutputPwrLowWarning.setStatus("current")
_Pmpump3AlmLaser2OutputPwrHighWarning_Type = EkiOnOff
_Pmpump3AlmLaser2OutputPwrHighWarning_Object = MibScalar
pmpump3AlmLaser2OutputPwrHighWarning = _Pmpump3AlmLaser2OutputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 1, 25, 6),
    _Pmpump3AlmLaser2OutputPwrHighWarning_Type()
)
pmpump3AlmLaser2OutputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2OutputPwrHighWarning.setStatus("current")
_Pmpump3AlmLaser2BiasLowWarning_Type = EkiOnOff
_Pmpump3AlmLaser2BiasLowWarning_Object = MibScalar
pmpump3AlmLaser2BiasLowWarning = _Pmpump3AlmLaser2BiasLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 1, 25, 7),
    _Pmpump3AlmLaser2BiasLowWarning_Type()
)
pmpump3AlmLaser2BiasLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2BiasLowWarning.setStatus("current")
_Pmpump3AlmLaser2BiasHighWarning_Type = EkiOnOff
_Pmpump3AlmLaser2BiasHighWarning_Object = MibScalar
pmpump3AlmLaser2BiasHighWarning = _Pmpump3AlmLaser2BiasHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 1, 25, 8),
    _Pmpump3AlmLaser2BiasHighWarning_Type()
)
pmpump3AlmLaser2BiasHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2BiasHighWarning.setStatus("current")
_Pmpump3AlmLineUrg_ObjectIdentity = ObjectIdentity
pmpump3AlmLineUrg = _Pmpump3AlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 2)
)
_Pmpump3Almlaser2Alarms1_ObjectIdentity = ObjectIdentity
pmpump3Almlaser2Alarms1 = _Pmpump3Almlaser2Alarms1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 2, 24)
)
_Pmpump3AlmLaser2TempLowAlarm_Type = EkiOnOff
_Pmpump3AlmLaser2TempLowAlarm_Object = MibScalar
pmpump3AlmLaser2TempLowAlarm = _Pmpump3AlmLaser2TempLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 2, 24, 1),
    _Pmpump3AlmLaser2TempLowAlarm_Type()
)
pmpump3AlmLaser2TempLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2TempLowAlarm.setStatus("current")
_Pmpump3AlmLaser2TempHighAlarm_Type = EkiOnOff
_Pmpump3AlmLaser2TempHighAlarm_Object = MibScalar
pmpump3AlmLaser2TempHighAlarm = _Pmpump3AlmLaser2TempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 2, 24, 2),
    _Pmpump3AlmLaser2TempHighAlarm_Type()
)
pmpump3AlmLaser2TempHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2TempHighAlarm.setStatus("current")
_Pmpump3AlmLaser2VthLowAlarm_Type = EkiOnOff
_Pmpump3AlmLaser2VthLowAlarm_Object = MibScalar
pmpump3AlmLaser2VthLowAlarm = _Pmpump3AlmLaser2VthLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 2, 24, 3),
    _Pmpump3AlmLaser2VthLowAlarm_Type()
)
pmpump3AlmLaser2VthLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2VthLowAlarm.setStatus("current")
_Pmpump3AlmLaser2VthHighAlarm_Type = EkiOnOff
_Pmpump3AlmLaser2VthHighAlarm_Object = MibScalar
pmpump3AlmLaser2VthHighAlarm = _Pmpump3AlmLaser2VthHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 2, 24, 4),
    _Pmpump3AlmLaser2VthHighAlarm_Type()
)
pmpump3AlmLaser2VthHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2VthHighAlarm.setStatus("current")
_Pmpump3AlmLaser2OutputPwrLowAlarm_Type = EkiOnOff
_Pmpump3AlmLaser2OutputPwrLowAlarm_Object = MibScalar
pmpump3AlmLaser2OutputPwrLowAlarm = _Pmpump3AlmLaser2OutputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 2, 24, 5),
    _Pmpump3AlmLaser2OutputPwrLowAlarm_Type()
)
pmpump3AlmLaser2OutputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2OutputPwrLowAlarm.setStatus("current")
_Pmpump3AlmLaser2OutputPwrHighAlarm_Type = EkiOnOff
_Pmpump3AlmLaser2OutputPwrHighAlarm_Object = MibScalar
pmpump3AlmLaser2OutputPwrHighAlarm = _Pmpump3AlmLaser2OutputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 2, 24, 6),
    _Pmpump3AlmLaser2OutputPwrHighAlarm_Type()
)
pmpump3AlmLaser2OutputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2OutputPwrHighAlarm.setStatus("current")
_Pmpump3AlmLaser2BiasLowAlarm_Type = EkiOnOff
_Pmpump3AlmLaser2BiasLowAlarm_Object = MibScalar
pmpump3AlmLaser2BiasLowAlarm = _Pmpump3AlmLaser2BiasLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 2, 24, 7),
    _Pmpump3AlmLaser2BiasLowAlarm_Type()
)
pmpump3AlmLaser2BiasLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2BiasLowAlarm.setStatus("current")
_Pmpump3AlmLaser2BiasHighAlarm_Type = EkiOnOff
_Pmpump3AlmLaser2BiasHighAlarm_Object = MibScalar
pmpump3AlmLaser2BiasHighAlarm = _Pmpump3AlmLaser2BiasHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 2, 24, 8),
    _Pmpump3AlmLaser2BiasHighAlarm_Type()
)
pmpump3AlmLaser2BiasHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2BiasHighAlarm.setStatus("current")
_Pmpump3AlmLineCrit_ObjectIdentity = ObjectIdentity
pmpump3AlmLineCrit = _Pmpump3AlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 3)
)
_Pmpump3Almlaser2Alarms2_ObjectIdentity = ObjectIdentity
pmpump3Almlaser2Alarms2 = _Pmpump3Almlaser2Alarms2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 3, 27)
)
_Pmpump3AlmLaser2AlmCurrent_Type = EkiOnOff
_Pmpump3AlmLaser2AlmCurrent_Object = MibScalar
pmpump3AlmLaser2AlmCurrent = _Pmpump3AlmLaser2AlmCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 3, 27, 1),
    _Pmpump3AlmLaser2AlmCurrent_Type()
)
pmpump3AlmLaser2AlmCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2AlmCurrent.setStatus("current")
_Pmpump3AlmLaser2AlmTemp_Type = EkiOnOff
_Pmpump3AlmLaser2AlmTemp_Object = MibScalar
pmpump3AlmLaser2AlmTemp = _Pmpump3AlmLaser2AlmTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 3, 27, 2),
    _Pmpump3AlmLaser2AlmTemp_Type()
)
pmpump3AlmLaser2AlmTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2AlmTemp.setStatus("current")
_Pmpump3AlmLaser2AlmTecPower_Type = EkiOnOff
_Pmpump3AlmLaser2AlmTecPower_Object = MibScalar
pmpump3AlmLaser2AlmTecPower = _Pmpump3AlmLaser2AlmTecPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 3, 27, 3),
    _Pmpump3AlmLaser2AlmTecPower_Type()
)
pmpump3AlmLaser2AlmTecPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2AlmTecPower.setStatus("current")
_Pmpump3AlmLaser2AlmTecDev_Type = EkiOnOff
_Pmpump3AlmLaser2AlmTecDev_Object = MibScalar
pmpump3AlmLaser2AlmTecDev = _Pmpump3AlmLaser2AlmTecDev_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 3, 27, 4),
    _Pmpump3AlmLaser2AlmTecDev_Type()
)
pmpump3AlmLaser2AlmTecDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2AlmTecDev.setStatus("current")
_Pmpump3AlmLaser2OaDisconnectedLsd_Type = EkiOnOff
_Pmpump3AlmLaser2OaDisconnectedLsd_Object = MibScalar
pmpump3AlmLaser2OaDisconnectedLsd = _Pmpump3AlmLaser2OaDisconnectedLsd_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 3, 27, 5),
    _Pmpump3AlmLaser2OaDisconnectedLsd_Type()
)
pmpump3AlmLaser2OaDisconnectedLsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2OaDisconnectedLsd.setStatus("current")
_Pmpump3AlmLaser2ExtLsd_Type = EkiOnOff
_Pmpump3AlmLaser2ExtLsd_Object = MibScalar
pmpump3AlmLaser2ExtLsd = _Pmpump3AlmLaser2ExtLsd_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 2, 3, 3, 27, 6),
    _Pmpump3AlmLaser2ExtLsd_Type()
)
pmpump3AlmLaser2ExtLsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3AlmLaser2ExtLsd.setStatus("current")
_Pmpump3measures_ObjectIdentity = ObjectIdentity
pmpump3measures = _Pmpump3measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 3)
)
_Pmpump3MesrOther_ObjectIdentity = ObjectIdentity
pmpump3MesrOther = _Pmpump3MesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 3, 1)
)


class _Pmpump3MesrtempMeas_Type(Integer32):
    """Custom type pmpump3MesrtempMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmpump3MesrtempMeas_Type.__name__ = "Integer32"
_Pmpump3MesrtempMeas_Object = MibScalar
pmpump3MesrtempMeas = _Pmpump3MesrtempMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 3, 1, 74),
    _Pmpump3MesrtempMeas_Type()
)
pmpump3MesrtempMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3MesrtempMeas.setStatus("current")
_Pmpump3MesrClient_ObjectIdentity = ObjectIdentity
pmpump3MesrClient = _Pmpump3MesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 3, 2)
)


class _Pmpump3Mesrlaser1BiasMeas_Type(Integer32):
    """Custom type pmpump3Mesrlaser1BiasMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmpump3Mesrlaser1BiasMeas_Type.__name__ = "Integer32"
_Pmpump3Mesrlaser1BiasMeas_Object = MibScalar
pmpump3Mesrlaser1BiasMeas = _Pmpump3Mesrlaser1BiasMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 3, 2, 16),
    _Pmpump3Mesrlaser1BiasMeas_Type()
)
pmpump3Mesrlaser1BiasMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3Mesrlaser1BiasMeas.setStatus("current")


class _Pmpump3Mesrlaser1VthMeas_Type(Integer32):
    """Custom type pmpump3Mesrlaser1VthMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmpump3Mesrlaser1VthMeas_Type.__name__ = "Integer32"
_Pmpump3Mesrlaser1VthMeas_Object = MibScalar
pmpump3Mesrlaser1VthMeas = _Pmpump3Mesrlaser1VthMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 3, 2, 17),
    _Pmpump3Mesrlaser1VthMeas_Type()
)
pmpump3Mesrlaser1VthMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3Mesrlaser1VthMeas.setStatus("current")


class _Pmpump3Mesrlaser1Pwr_Type(Integer32):
    """Custom type pmpump3Mesrlaser1Pwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmpump3Mesrlaser1Pwr_Type.__name__ = "Integer32"
_Pmpump3Mesrlaser1Pwr_Object = MibScalar
pmpump3Mesrlaser1Pwr = _Pmpump3Mesrlaser1Pwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 3, 2, 36),
    _Pmpump3Mesrlaser1Pwr_Type()
)
pmpump3Mesrlaser1Pwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3Mesrlaser1Pwr.setStatus("current")


class _Pmpump3Mesrlaser1Temp_Type(Integer32):
    """Custom type pmpump3Mesrlaser1Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmpump3Mesrlaser1Temp_Type.__name__ = "Integer32"
_Pmpump3Mesrlaser1Temp_Object = MibScalar
pmpump3Mesrlaser1Temp = _Pmpump3Mesrlaser1Temp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 3, 2, 37),
    _Pmpump3Mesrlaser1Temp_Type()
)
pmpump3Mesrlaser1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3Mesrlaser1Temp.setStatus("current")
_Pmpump3MesrLine_ObjectIdentity = ObjectIdentity
pmpump3MesrLine = _Pmpump3MesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 3, 3)
)


class _Pmpump3Mesrlaser2BiasMeas_Type(Integer32):
    """Custom type pmpump3Mesrlaser2BiasMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmpump3Mesrlaser2BiasMeas_Type.__name__ = "Integer32"
_Pmpump3Mesrlaser2BiasMeas_Object = MibScalar
pmpump3Mesrlaser2BiasMeas = _Pmpump3Mesrlaser2BiasMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 3, 3, 24),
    _Pmpump3Mesrlaser2BiasMeas_Type()
)
pmpump3Mesrlaser2BiasMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3Mesrlaser2BiasMeas.setStatus("current")


class _Pmpump3Mesrlaser2VthMeas_Type(Integer32):
    """Custom type pmpump3Mesrlaser2VthMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmpump3Mesrlaser2VthMeas_Type.__name__ = "Integer32"
_Pmpump3Mesrlaser2VthMeas_Object = MibScalar
pmpump3Mesrlaser2VthMeas = _Pmpump3Mesrlaser2VthMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 3, 3, 25),
    _Pmpump3Mesrlaser2VthMeas_Type()
)
pmpump3Mesrlaser2VthMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3Mesrlaser2VthMeas.setStatus("current")


class _Pmpump3Mesrlaser2Pwr_Type(Integer32):
    """Custom type pmpump3Mesrlaser2Pwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmpump3Mesrlaser2Pwr_Type.__name__ = "Integer32"
_Pmpump3Mesrlaser2Pwr_Object = MibScalar
pmpump3Mesrlaser2Pwr = _Pmpump3Mesrlaser2Pwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 3, 3, 44),
    _Pmpump3Mesrlaser2Pwr_Type()
)
pmpump3Mesrlaser2Pwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3Mesrlaser2Pwr.setStatus("current")


class _Pmpump3Mesrlaser2Temp_Type(Integer32):
    """Custom type pmpump3Mesrlaser2Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmpump3Mesrlaser2Temp_Type.__name__ = "Integer32"
_Pmpump3Mesrlaser2Temp_Object = MibScalar
pmpump3Mesrlaser2Temp = _Pmpump3Mesrlaser2Temp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 3, 3, 45),
    _Pmpump3Mesrlaser2Temp_Type()
)
pmpump3Mesrlaser2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3Mesrlaser2Temp.setStatus("current")
_Pmpump3controlsWrite_ObjectIdentity = ObjectIdentity
pmpump3controlsWrite = _Pmpump3controlsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6)
)
_Pmpump3CtrlOther_ObjectIdentity = ObjectIdentity
pmpump3CtrlOther = _Pmpump3CtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 1)
)
_Pmpump3Ctrlsynth0_ObjectIdentity = ObjectIdentity
pmpump3Ctrlsynth0 = _Pmpump3Ctrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 1, 0)
)
_Pmpump3CtrlConfLoad_Type = EkiOnOff
_Pmpump3CtrlConfLoad_Object = MibScalar
pmpump3CtrlConfLoad = _Pmpump3CtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 1, 0, 1),
    _Pmpump3CtrlConfLoad_Type()
)
pmpump3CtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmpump3CtrlConfLoad.setStatus("current")
_Pmpump3CtrlConfFlash_Type = EkiOnOff
_Pmpump3CtrlConfFlash_Object = MibScalar
pmpump3CtrlConfFlash = _Pmpump3CtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 1, 0, 9),
    _Pmpump3CtrlConfFlash_Type()
)
pmpump3CtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmpump3CtrlConfFlash.setStatus("current")
_Pmpump3CtrlConfClear_Type = EkiOnOff
_Pmpump3CtrlConfClear_Object = MibScalar
pmpump3CtrlConfClear = _Pmpump3CtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 1, 0, 13),
    _Pmpump3CtrlConfClear_Type()
)
pmpump3CtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmpump3CtrlConfClear.setStatus("current")
_Pmpump3CtrlswMgnt_ObjectIdentity = ObjectIdentity
pmpump3CtrlswMgnt = _Pmpump3CtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 1, 5)
)
_Pmpump3CtrlColdReset_Type = EkiOnOff
_Pmpump3CtrlColdReset_Object = MibScalar
pmpump3CtrlColdReset = _Pmpump3CtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 1, 5, 2),
    _Pmpump3CtrlColdReset_Type()
)
pmpump3CtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmpump3CtrlColdReset.setStatus("current")
_Pmpump3CtrlWarmReset_Type = EkiOnOff
_Pmpump3CtrlWarmReset_Object = MibScalar
pmpump3CtrlWarmReset = _Pmpump3CtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 1, 5, 3),
    _Pmpump3CtrlWarmReset_Type()
)
pmpump3CtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmpump3CtrlWarmReset.setStatus("current")
_Pmpump3CtrlledTest_ObjectIdentity = ObjectIdentity
pmpump3CtrlledTest = _Pmpump3CtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 1, 73)
)
_Pmpump3CtrlGreenLed_Type = EkiOnOff
_Pmpump3CtrlGreenLed_Object = MibScalar
pmpump3CtrlGreenLed = _Pmpump3CtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 1, 73, 1),
    _Pmpump3CtrlGreenLed_Type()
)
pmpump3CtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmpump3CtrlGreenLed.setStatus("current")
_Pmpump3CtrlRedLed_Type = EkiOnOff
_Pmpump3CtrlRedLed_Object = MibScalar
pmpump3CtrlRedLed = _Pmpump3CtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 1, 73, 2),
    _Pmpump3CtrlRedLed_Type()
)
pmpump3CtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmpump3CtrlRedLed.setStatus("current")
_Pmpump3CtrlLedOff_Type = EkiOnOff
_Pmpump3CtrlLedOff_Object = MibScalar
pmpump3CtrlLedOff = _Pmpump3CtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 1, 73, 3),
    _Pmpump3CtrlLedOff_Type()
)
pmpump3CtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmpump3CtrlLedOff.setStatus("current")
_Pmpump3CtrlClient_ObjectIdentity = ObjectIdentity
pmpump3CtrlClient = _Pmpump3CtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 2)
)
_Pmpump3Ctrllaser1LaserOff_ObjectIdentity = ObjectIdentity
pmpump3Ctrllaser1LaserOff = _Pmpump3Ctrllaser1LaserOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 2, 32)
)
_Pmpump3CtrlLaser1LaserOff_Type = EkiOnOff
_Pmpump3CtrlLaser1LaserOff_Object = MibScalar
pmpump3CtrlLaser1LaserOff = _Pmpump3CtrlLaser1LaserOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 2, 32, 1),
    _Pmpump3CtrlLaser1LaserOff_Type()
)
pmpump3CtrlLaser1LaserOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmpump3CtrlLaser1LaserOff.setStatus("current")


class _Pmpump3Ctrllaser1EffPwrOutSettingValue_Type(Integer32):
    """Custom type pmpump3Ctrllaser1EffPwrOutSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmpump3Ctrllaser1EffPwrOutSettingValue_Type.__name__ = "Integer32"
_Pmpump3Ctrllaser1EffPwrOutSettingValue_Object = MibScalar
pmpump3Ctrllaser1EffPwrOutSettingValue = _Pmpump3Ctrllaser1EffPwrOutSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 2, 37),
    _Pmpump3Ctrllaser1EffPwrOutSettingValue_Type()
)
pmpump3Ctrllaser1EffPwrOutSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmpump3Ctrllaser1EffPwrOutSettingValue.setStatus("current")
_Pmpump3CtrlLine_ObjectIdentity = ObjectIdentity
pmpump3CtrlLine = _Pmpump3CtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 3)
)
_Pmpump3Ctrllaser2LaserOff_ObjectIdentity = ObjectIdentity
pmpump3Ctrllaser2LaserOff = _Pmpump3Ctrllaser2LaserOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 3, 40)
)
_Pmpump3CtrlLaser2LaserOff_Type = EkiOnOff
_Pmpump3CtrlLaser2LaserOff_Object = MibScalar
pmpump3CtrlLaser2LaserOff = _Pmpump3CtrlLaser2LaserOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 3, 40, 1),
    _Pmpump3CtrlLaser2LaserOff_Type()
)
pmpump3CtrlLaser2LaserOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmpump3CtrlLaser2LaserOff.setStatus("current")


class _Pmpump3Ctrllaser2EffPwrOutSettingValue_Type(Integer32):
    """Custom type pmpump3Ctrllaser2EffPwrOutSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmpump3Ctrllaser2EffPwrOutSettingValue_Type.__name__ = "Integer32"
_Pmpump3Ctrllaser2EffPwrOutSettingValue_Object = MibScalar
pmpump3Ctrllaser2EffPwrOutSettingValue = _Pmpump3Ctrllaser2EffPwrOutSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 6, 3, 45),
    _Pmpump3Ctrllaser2EffPwrOutSettingValue_Type()
)
pmpump3Ctrllaser2EffPwrOutSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmpump3Ctrllaser2EffPwrOutSettingValue.setStatus("current")
_Pmpump3ri_ObjectIdentity = ObjectIdentity
pmpump3ri = _Pmpump3ri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 7)
)
_Pmpump3riTable_ObjectIdentity = ObjectIdentity
pmpump3riTable = _Pmpump3riTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 7, 1)
)
_Pmpump3RinvLaser1Table_Object = MibTable
pmpump3RinvLaser1Table = _Pmpump3RinvLaser1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pmpump3RinvLaser1Table.setStatus("current")
_Pmpump3RinvLaser1Entry_Object = MibTableRow
pmpump3RinvLaser1Entry = _Pmpump3RinvLaser1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 7, 1, 1, 1)
)
pmpump3RinvLaser1Entry.setIndexNames(
    (0, "EKINOPS-PmPump3-MIB", "pmpump3RinvLaser1Index"),
)
if mibBuilder.loadTexts:
    pmpump3RinvLaser1Entry.setStatus("current")


class _Pmpump3RinvLaser1Index_Type(Integer32):
    """Custom type pmpump3RinvLaser1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmpump3RinvLaser1Index_Type.__name__ = "Integer32"
_Pmpump3RinvLaser1Index_Object = MibTableColumn
pmpump3RinvLaser1Index = _Pmpump3RinvLaser1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 7, 1, 1, 1, 1),
    _Pmpump3RinvLaser1Index_Type()
)
pmpump3RinvLaser1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3RinvLaser1Index.setStatus("current")
_Pmpump3RinvLaser1_Type = DisplayString
_Pmpump3RinvLaser1_Object = MibTableColumn
pmpump3RinvLaser1 = _Pmpump3RinvLaser1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 7, 1, 1, 1, 2),
    _Pmpump3RinvLaser1_Type()
)
pmpump3RinvLaser1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3RinvLaser1.setStatus("current")
_Pmpump3RinvLaser2Table_Object = MibTable
pmpump3RinvLaser2Table = _Pmpump3RinvLaser2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pmpump3RinvLaser2Table.setStatus("current")
_Pmpump3RinvLaser2Entry_Object = MibTableRow
pmpump3RinvLaser2Entry = _Pmpump3RinvLaser2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 7, 1, 2, 1)
)
pmpump3RinvLaser2Entry.setIndexNames(
    (0, "EKINOPS-PmPump3-MIB", "pmpump3RinvLaser2Index"),
)
if mibBuilder.loadTexts:
    pmpump3RinvLaser2Entry.setStatus("current")


class _Pmpump3RinvLaser2Index_Type(Integer32):
    """Custom type pmpump3RinvLaser2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmpump3RinvLaser2Index_Type.__name__ = "Integer32"
_Pmpump3RinvLaser2Index_Object = MibTableColumn
pmpump3RinvLaser2Index = _Pmpump3RinvLaser2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 7, 1, 2, 1, 1),
    _Pmpump3RinvLaser2Index_Type()
)
pmpump3RinvLaser2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3RinvLaser2Index.setStatus("current")
_Pmpump3RinvLaser2_Type = DisplayString
_Pmpump3RinvLaser2_Object = MibTableColumn
pmpump3RinvLaser2 = _Pmpump3RinvLaser2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 7, 1, 2, 1, 2),
    _Pmpump3RinvLaser2_Type()
)
pmpump3RinvLaser2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3RinvLaser2.setStatus("current")
_Pmpump3RinvReloadInventory_Type = EkiOnOff
_Pmpump3RinvReloadInventory_Object = MibScalar
pmpump3RinvReloadInventory = _Pmpump3RinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 7, 2),
    _Pmpump3RinvReloadInventory_Type()
)
pmpump3RinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmpump3RinvReloadInventory.setStatus("current")
_Pmpump3RinvHwPlatform_Type = DisplayString
_Pmpump3RinvHwPlatform_Object = MibScalar
pmpump3RinvHwPlatform = _Pmpump3RinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 7, 3),
    _Pmpump3RinvHwPlatform_Type()
)
pmpump3RinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3RinvHwPlatform.setStatus("current")
_Pmpump3RinvModulePlatform_Type = DisplayString
_Pmpump3RinvModulePlatform_Object = MibScalar
pmpump3RinvModulePlatform = _Pmpump3RinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 7, 4),
    _Pmpump3RinvModulePlatform_Type()
)
pmpump3RinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3RinvModulePlatform.setStatus("current")
_Pmpump3RinvSwPlatform_Type = DisplayString
_Pmpump3RinvSwPlatform_Object = MibScalar
pmpump3RinvSwPlatform = _Pmpump3RinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 7, 5),
    _Pmpump3RinvSwPlatform_Type()
)
pmpump3RinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3RinvSwPlatform.setStatus("current")
_Pmpump3Config_ObjectIdentity = ObjectIdentity
pmpump3Config = _Pmpump3Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 9)
)
_Pmpump3CfgNoValue_ObjectIdentity = ObjectIdentity
pmpump3CfgNoValue = _Pmpump3CfgNoValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 9, 1)
)
_Pmpump3tableclientStartup_ObjectIdentity = ObjectIdentity
pmpump3tableclientStartup = _Pmpump3tableclientStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 9, 1, 1)
)


class _Pmpump3Cfglaser1Ctrl_Type(Unsigned32):
    """Custom type pmpump3Cfglaser1Ctrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmpump3Cfglaser1Ctrl_Type.__name__ = "Unsigned32"
_Pmpump3Cfglaser1Ctrl_Object = MibScalar
pmpump3Cfglaser1Ctrl = _Pmpump3Cfglaser1Ctrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 9, 1, 1, 2),
    _Pmpump3Cfglaser1Ctrl_Type()
)
pmpump3Cfglaser1Ctrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmpump3Cfglaser1Ctrl.setStatus("current")
_Pmpump3CfgLineStartUp_ObjectIdentity = ObjectIdentity
pmpump3CfgLineStartUp = _Pmpump3CfgLineStartUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 9, 2)
)
_Pmpump3tablelineStartup_ObjectIdentity = ObjectIdentity
pmpump3tablelineStartup = _Pmpump3tablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 9, 2, 1)
)


class _Pmpump3Cfglaser2Ctrl_Type(Unsigned32):
    """Custom type pmpump3Cfglaser2Ctrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmpump3Cfglaser2Ctrl_Type.__name__ = "Unsigned32"
_Pmpump3Cfglaser2Ctrl_Object = MibScalar
pmpump3Cfglaser2Ctrl = _Pmpump3Cfglaser2Ctrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 9, 2, 1, 2),
    _Pmpump3Cfglaser2Ctrl_Type()
)
pmpump3Cfglaser2Ctrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmpump3Cfglaser2Ctrl.setStatus("current")
_Pmpump3CfgLabels_ObjectIdentity = ObjectIdentity
pmpump3CfgLabels = _Pmpump3CfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 9, 3)
)
_Pmpump3CfgLabelclientTable_Object = MibTable
pmpump3CfgLabelclientTable = _Pmpump3CfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pmpump3CfgLabelclientTable.setStatus("current")
_Pmpump3CfgLabelclientEntry_Object = MibTableRow
pmpump3CfgLabelclientEntry = _Pmpump3CfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 9, 3, 1, 1)
)
pmpump3CfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-PmPump3-MIB", "pmpump3CfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmpump3CfgLabelclientEntry.setStatus("current")


class _Pmpump3CfgLabelclientIndex_Type(Integer32):
    """Custom type pmpump3CfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmpump3CfgLabelclientIndex_Type.__name__ = "Integer32"
_Pmpump3CfgLabelclientIndex_Object = MibTableColumn
pmpump3CfgLabelclientIndex = _Pmpump3CfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 9, 3, 1, 1, 1),
    _Pmpump3CfgLabelclientIndex_Type()
)
pmpump3CfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3CfgLabelclientIndex.setStatus("current")


class _Pmpump3CfgLabelclientPortn_Type(DisplayString):
    """Custom type pmpump3CfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmpump3CfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pmpump3CfgLabelclientPortn_Object = MibTableColumn
pmpump3CfgLabelclientPortn = _Pmpump3CfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 9, 3, 1, 1, 3),
    _Pmpump3CfgLabelclientPortn_Type()
)
pmpump3CfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmpump3CfgLabelclientPortn.setStatus("current")
_Pmpump3CfgLabellineTable_Object = MibTable
pmpump3CfgLabellineTable = _Pmpump3CfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pmpump3CfgLabellineTable.setStatus("current")
_Pmpump3CfgLabellineEntry_Object = MibTableRow
pmpump3CfgLabellineEntry = _Pmpump3CfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 9, 3, 2, 1)
)
pmpump3CfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-PmPump3-MIB", "pmpump3CfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmpump3CfgLabellineEntry.setStatus("current")


class _Pmpump3CfgLabellineIndex_Type(Integer32):
    """Custom type pmpump3CfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmpump3CfgLabellineIndex_Type.__name__ = "Integer32"
_Pmpump3CfgLabellineIndex_Object = MibTableColumn
pmpump3CfgLabellineIndex = _Pmpump3CfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 9, 3, 2, 1, 1),
    _Pmpump3CfgLabellineIndex_Type()
)
pmpump3CfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3CfgLabellineIndex.setStatus("current")


class _Pmpump3CfgLabellinePortn_Type(DisplayString):
    """Custom type pmpump3CfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmpump3CfgLabellinePortn_Type.__name__ = "DisplayString"
_Pmpump3CfgLabellinePortn_Object = MibTableColumn
pmpump3CfgLabellinePortn = _Pmpump3CfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 9, 3, 2, 1, 3),
    _Pmpump3CfgLabellinePortn_Type()
)
pmpump3CfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmpump3CfgLabellinePortn.setStatus("current")
_Pmpump3CfgWriteConfiguration_Type = EkiOnOff
_Pmpump3CfgWriteConfiguration_Object = MibScalar
pmpump3CfgWriteConfiguration = _Pmpump3CfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 9, 257),
    _Pmpump3CfgWriteConfiguration_Type()
)
pmpump3CfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmpump3CfgWriteConfiguration.setStatus("current")
_Pmpump3traps_ObjectIdentity = ObjectIdentity
pmpump3traps = _Pmpump3traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 49, 10)
)


class _Pmpump3trapBoardNumber_Type(Integer32):
    """Custom type pmpump3trapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmpump3trapBoardNumber_Type.__name__ = "Integer32"
_Pmpump3trapBoardNumber_Object = MibScalar
pmpump3trapBoardNumber = _Pmpump3trapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 49, 10, 4),
    _Pmpump3trapBoardNumber_Type()
)
pmpump3trapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmpump3trapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pmpump3Laser2TrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 49, 10, 30)
)
pmpump3Laser2TrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-PmPump3-MIB", "pmpump3AlmLaser2Warning"),
        ("EKINOPS-PmPump3-MIB", "pmpump3trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmpump3Laser2TrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmpump3Laser2TrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 49, 10, 31)
)
pmpump3Laser2TrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-PmPump3-MIB", "pmpump3AlmLaser2Warning"),
        ("EKINOPS-PmPump3-MIB", "pmpump3trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmpump3Laser2TrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmpump3Laser2TrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 49, 10, 32)
)
pmpump3Laser2TrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmPump3-MIB", "pmpump3AlmLaser2Alm"),
        ("EKINOPS-PmPump3-MIB", "pmpump3trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmpump3Laser2TrapUrgentGoesOn.setStatus(
        "current"
    )

pmpump3Laser2TrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 49, 10, 33)
)
pmpump3Laser2TrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmPump3-MIB", "pmpump3AlmLaser2Alm"),
        ("EKINOPS-PmPump3-MIB", "pmpump3trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmpump3Laser2TrapUrgentGoesOff.setStatus(
        "current"
    )

pmpump3Laser2TrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 49, 10, 34)
)
pmpump3Laser2TrapCritGoesOn.setObjects(
      *(("EKINOPS-PmPump3-MIB", "pmpump3AlmLaser2Fail"),
        ("EKINOPS-PmPump3-MIB", "pmpump3AlmLaser2HwFail"),
        ("EKINOPS-PmPump3-MIB", "pmpump3trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmpump3Laser2TrapCritGoesOn.setStatus(
        "current"
    )

pmpump3Laser2TrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 49, 10, 35)
)
pmpump3Laser2TrapCritGoesOff.setObjects(
      *(("EKINOPS-PmPump3-MIB", "pmpump3AlmLaser2Fail"),
        ("EKINOPS-PmPump3-MIB", "pmpump3AlmLaser2HwFail"),
        ("EKINOPS-PmPump3-MIB", "pmpump3trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmpump3Laser2TrapCritGoesOff.setStatus(
        "current"
    )

pmpump3Laser1TrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 49, 10, 40)
)
pmpump3Laser1TrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-PmPump3-MIB", "pmpump3AlmLaser1Warning"),
        ("EKINOPS-PmPump3-MIB", "pmpump3trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmpump3Laser1TrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmpump3Laser1TrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 49, 10, 41)
)
pmpump3Laser1TrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-PmPump3-MIB", "pmpump3AlmLaser1Warning"),
        ("EKINOPS-PmPump3-MIB", "pmpump3trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmpump3Laser1TrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmpump3Laser1TrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 49, 10, 42)
)
pmpump3Laser1TrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmPump3-MIB", "pmpump3AlmLaser1Alm"),
        ("EKINOPS-PmPump3-MIB", "pmpump3trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmpump3Laser1TrapUrgentGoesOn.setStatus(
        "current"
    )

pmpump3Laser1TrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 49, 10, 43)
)
pmpump3Laser1TrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmPump3-MIB", "pmpump3AlmLaser1Alm"),
        ("EKINOPS-PmPump3-MIB", "pmpump3trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmpump3Laser1TrapUrgentGoesOff.setStatus(
        "current"
    )

pmpump3Laser1TrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 49, 10, 44)
)
pmpump3Laser1TrapCritGoesOn.setObjects(
      *(("EKINOPS-PmPump3-MIB", "pmpump3AlmLaser1Fail"),
        ("EKINOPS-PmPump3-MIB", "pmpump3AlmLaser1HwFail"),
        ("EKINOPS-PmPump3-MIB", "pmpump3trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmpump3Laser1TrapCritGoesOn.setStatus(
        "current"
    )

pmpump3Laser1TrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 49, 10, 45)
)
pmpump3Laser1TrapCritGoesOff.setObjects(
      *(("EKINOPS-PmPump3-MIB", "pmpump3AlmLaser1Fail"),
        ("EKINOPS-PmPump3-MIB", "pmpump3AlmLaser1HwFail"),
        ("EKINOPS-PmPump3-MIB", "pmpump3trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmpump3Laser1TrapCritGoesOff.setStatus(
        "current"
    )

pmpump3PowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 49, 10, 50)
)
pmpump3PowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmPump3-MIB", "pmpump3AlmDefFuseB"),
        ("EKINOPS-PmPump3-MIB", "pmpump3AlmDefFuseA"),
        ("EKINOPS-PmPump3-MIB", "pmpump3trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmpump3PowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmpump3PowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 49, 10, 51)
)
pmpump3PowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmPump3-MIB", "pmpump3AlmDefFuseB"),
        ("EKINOPS-PmPump3-MIB", "pmpump3AlmDefFuseA"),
        ("EKINOPS-PmPump3-MIB", "pmpump3trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmpump3PowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-PmPump3-MIB",
    **{"modulepmpump3": modulepmpump3,
       "pmpump3alarms": pmpump3alarms,
       "pmpump3AlmOther": pmpump3AlmOther,
       "pmpump3AlmOtherNurg": pmpump3AlmOtherNurg,
       "pmpump3AlmsynthAlm2": pmpump3AlmsynthAlm2,
       "pmpump3AlmConfTableSave": pmpump3AlmConfTableSave,
       "pmpump3AlmInvUpload": pmpump3AlmInvUpload,
       "pmpump3AlmConfTableLoad": pmpump3AlmConfTableLoad,
       "pmpump3AlmpmWarnings": pmpump3AlmpmWarnings,
       "pmpump3AlmTermpLowWarning": pmpump3AlmTermpLowWarning,
       "pmpump3AlmTempHighWarning": pmpump3AlmTempHighWarning,
       "pmpump3AlmOtherUrg": pmpump3AlmOtherUrg,
       "pmpump3AlmpmAlarms": pmpump3AlmpmAlarms,
       "pmpump3AlmTermpLowAlarm": pmpump3AlmTermpLowAlarm,
       "pmpump3AlmTempHighAlarm": pmpump3AlmTempHighAlarm,
       "pmpump3AlmOtherCrit": pmpump3AlmOtherCrit,
       "pmpump3AlmsynthAlm0": pmpump3AlmsynthAlm0,
       "pmpump3AlmModGlobFail": pmpump3AlmModGlobFail,
       "pmpump3AlmDefFuseA": pmpump3AlmDefFuseA,
       "pmpump3AlmDefFuseB": pmpump3AlmDefFuseB,
       "pmpump3AlmClient": pmpump3AlmClient,
       "pmpump3AlmClientNurg": pmpump3AlmClientNurg,
       "pmpump3Almlaser1Warnings": pmpump3Almlaser1Warnings,
       "pmpump3AlmLaser1TempLowWarning": pmpump3AlmLaser1TempLowWarning,
       "pmpump3AlmLaser1TempHighWarning": pmpump3AlmLaser1TempHighWarning,
       "pmpump3AlmLaser1VthLowWarning": pmpump3AlmLaser1VthLowWarning,
       "pmpump3AlmLaser1VthHighWarning": pmpump3AlmLaser1VthHighWarning,
       "pmpump3AlmLaser1OutputPwrLowWarning": pmpump3AlmLaser1OutputPwrLowWarning,
       "pmpump3AlmLaser1OutputPwrHighWarning": pmpump3AlmLaser1OutputPwrHighWarning,
       "pmpump3AlmLaser1BiasLowWarning": pmpump3AlmLaser1BiasLowWarning,
       "pmpump3AlmLaser1BiasHighWarning": pmpump3AlmLaser1BiasHighWarning,
       "pmpump3AlmClientUrg": pmpump3AlmClientUrg,
       "pmpump3Almlaser1Alarms1": pmpump3Almlaser1Alarms1,
       "pmpump3AlmLaser1TempLowAlarm": pmpump3AlmLaser1TempLowAlarm,
       "pmpump3AlmLaser1TempHighAlarm": pmpump3AlmLaser1TempHighAlarm,
       "pmpump3AlmLaser1VthLowAlarm": pmpump3AlmLaser1VthLowAlarm,
       "pmpump3AlmLaser1VthHighAlarm": pmpump3AlmLaser1VthHighAlarm,
       "pmpump3AlmLaser1OutputPwrLowAlarm": pmpump3AlmLaser1OutputPwrLowAlarm,
       "pmpump3AlmLaser1OutputPwrHighAlarm": pmpump3AlmLaser1OutputPwrHighAlarm,
       "pmpump3AlmLaser1BiasLowAlarm": pmpump3AlmLaser1BiasLowAlarm,
       "pmpump3AlmLaser1BiasHighAlarm": pmpump3AlmLaser1BiasHighAlarm,
       "pmpump3AlmClientCrit": pmpump3AlmClientCrit,
       "pmpump3AlmsynthAlmLaser1": pmpump3AlmsynthAlmLaser1,
       "pmpump3AlmLaser1InitNotCompl": pmpump3AlmLaser1InitNotCompl,
       "pmpump3AlmLaser1HwFail": pmpump3AlmLaser1HwFail,
       "pmpump3AlmLaser1TxOff": pmpump3AlmLaser1TxOff,
       "pmpump3AlmLaser1Oos": pmpump3AlmLaser1Oos,
       "pmpump3AlmLaser1Warning": pmpump3AlmLaser1Warning,
       "pmpump3AlmLaser1Alm": pmpump3AlmLaser1Alm,
       "pmpump3AlmLaser1Fail": pmpump3AlmLaser1Fail,
       "pmpump3AlmsynthAlmLaser2": pmpump3AlmsynthAlmLaser2,
       "pmpump3AlmLaser2InitNotCompl": pmpump3AlmLaser2InitNotCompl,
       "pmpump3AlmLaser2HwFail": pmpump3AlmLaser2HwFail,
       "pmpump3AlmLaser2TxOff": pmpump3AlmLaser2TxOff,
       "pmpump3AlmLaser2Oos": pmpump3AlmLaser2Oos,
       "pmpump3AlmLaser2Warning": pmpump3AlmLaser2Warning,
       "pmpump3AlmLaser2Alm": pmpump3AlmLaser2Alm,
       "pmpump3AlmLaser2Fail": pmpump3AlmLaser2Fail,
       "pmpump3Almlaser1Alarms2": pmpump3Almlaser1Alarms2,
       "pmpump3AlmLaser1AlmCurrent": pmpump3AlmLaser1AlmCurrent,
       "pmpump3AlmLaser1AlmTemp": pmpump3AlmLaser1AlmTemp,
       "pmpump3AlmLaser1AlmTecPower": pmpump3AlmLaser1AlmTecPower,
       "pmpump3AlmLaser1AlmTecDev": pmpump3AlmLaser1AlmTecDev,
       "pmpump3AlmLaser1OaDisconnectedLsd": pmpump3AlmLaser1OaDisconnectedLsd,
       "pmpump3AlmLaser1ExtLsd": pmpump3AlmLaser1ExtLsd,
       "pmpump3AlmLine": pmpump3AlmLine,
       "pmpump3AlmLineNurg": pmpump3AlmLineNurg,
       "pmpump3Almlaser2Warnings": pmpump3Almlaser2Warnings,
       "pmpump3AlmLaser2TempLowWarning": pmpump3AlmLaser2TempLowWarning,
       "pmpump3AlmLaser2TempHighWarning": pmpump3AlmLaser2TempHighWarning,
       "pmpump3AlmLaser2VthLowWarning": pmpump3AlmLaser2VthLowWarning,
       "pmpump3AlmLaser2VthHighWarning": pmpump3AlmLaser2VthHighWarning,
       "pmpump3AlmLaser2OutputPwrLowWarning": pmpump3AlmLaser2OutputPwrLowWarning,
       "pmpump3AlmLaser2OutputPwrHighWarning": pmpump3AlmLaser2OutputPwrHighWarning,
       "pmpump3AlmLaser2BiasLowWarning": pmpump3AlmLaser2BiasLowWarning,
       "pmpump3AlmLaser2BiasHighWarning": pmpump3AlmLaser2BiasHighWarning,
       "pmpump3AlmLineUrg": pmpump3AlmLineUrg,
       "pmpump3Almlaser2Alarms1": pmpump3Almlaser2Alarms1,
       "pmpump3AlmLaser2TempLowAlarm": pmpump3AlmLaser2TempLowAlarm,
       "pmpump3AlmLaser2TempHighAlarm": pmpump3AlmLaser2TempHighAlarm,
       "pmpump3AlmLaser2VthLowAlarm": pmpump3AlmLaser2VthLowAlarm,
       "pmpump3AlmLaser2VthHighAlarm": pmpump3AlmLaser2VthHighAlarm,
       "pmpump3AlmLaser2OutputPwrLowAlarm": pmpump3AlmLaser2OutputPwrLowAlarm,
       "pmpump3AlmLaser2OutputPwrHighAlarm": pmpump3AlmLaser2OutputPwrHighAlarm,
       "pmpump3AlmLaser2BiasLowAlarm": pmpump3AlmLaser2BiasLowAlarm,
       "pmpump3AlmLaser2BiasHighAlarm": pmpump3AlmLaser2BiasHighAlarm,
       "pmpump3AlmLineCrit": pmpump3AlmLineCrit,
       "pmpump3Almlaser2Alarms2": pmpump3Almlaser2Alarms2,
       "pmpump3AlmLaser2AlmCurrent": pmpump3AlmLaser2AlmCurrent,
       "pmpump3AlmLaser2AlmTemp": pmpump3AlmLaser2AlmTemp,
       "pmpump3AlmLaser2AlmTecPower": pmpump3AlmLaser2AlmTecPower,
       "pmpump3AlmLaser2AlmTecDev": pmpump3AlmLaser2AlmTecDev,
       "pmpump3AlmLaser2OaDisconnectedLsd": pmpump3AlmLaser2OaDisconnectedLsd,
       "pmpump3AlmLaser2ExtLsd": pmpump3AlmLaser2ExtLsd,
       "pmpump3measures": pmpump3measures,
       "pmpump3MesrOther": pmpump3MesrOther,
       "pmpump3MesrtempMeas": pmpump3MesrtempMeas,
       "pmpump3MesrClient": pmpump3MesrClient,
       "pmpump3Mesrlaser1BiasMeas": pmpump3Mesrlaser1BiasMeas,
       "pmpump3Mesrlaser1VthMeas": pmpump3Mesrlaser1VthMeas,
       "pmpump3Mesrlaser1Pwr": pmpump3Mesrlaser1Pwr,
       "pmpump3Mesrlaser1Temp": pmpump3Mesrlaser1Temp,
       "pmpump3MesrLine": pmpump3MesrLine,
       "pmpump3Mesrlaser2BiasMeas": pmpump3Mesrlaser2BiasMeas,
       "pmpump3Mesrlaser2VthMeas": pmpump3Mesrlaser2VthMeas,
       "pmpump3Mesrlaser2Pwr": pmpump3Mesrlaser2Pwr,
       "pmpump3Mesrlaser2Temp": pmpump3Mesrlaser2Temp,
       "pmpump3controlsWrite": pmpump3controlsWrite,
       "pmpump3CtrlOther": pmpump3CtrlOther,
       "pmpump3Ctrlsynth0": pmpump3Ctrlsynth0,
       "pmpump3CtrlConfLoad": pmpump3CtrlConfLoad,
       "pmpump3CtrlConfFlash": pmpump3CtrlConfFlash,
       "pmpump3CtrlConfClear": pmpump3CtrlConfClear,
       "pmpump3CtrlswMgnt": pmpump3CtrlswMgnt,
       "pmpump3CtrlColdReset": pmpump3CtrlColdReset,
       "pmpump3CtrlWarmReset": pmpump3CtrlWarmReset,
       "pmpump3CtrlledTest": pmpump3CtrlledTest,
       "pmpump3CtrlGreenLed": pmpump3CtrlGreenLed,
       "pmpump3CtrlRedLed": pmpump3CtrlRedLed,
       "pmpump3CtrlLedOff": pmpump3CtrlLedOff,
       "pmpump3CtrlClient": pmpump3CtrlClient,
       "pmpump3Ctrllaser1LaserOff": pmpump3Ctrllaser1LaserOff,
       "pmpump3CtrlLaser1LaserOff": pmpump3CtrlLaser1LaserOff,
       "pmpump3Ctrllaser1EffPwrOutSettingValue": pmpump3Ctrllaser1EffPwrOutSettingValue,
       "pmpump3CtrlLine": pmpump3CtrlLine,
       "pmpump3Ctrllaser2LaserOff": pmpump3Ctrllaser2LaserOff,
       "pmpump3CtrlLaser2LaserOff": pmpump3CtrlLaser2LaserOff,
       "pmpump3Ctrllaser2EffPwrOutSettingValue": pmpump3Ctrllaser2EffPwrOutSettingValue,
       "pmpump3ri": pmpump3ri,
       "pmpump3riTable": pmpump3riTable,
       "pmpump3RinvLaser1Table": pmpump3RinvLaser1Table,
       "pmpump3RinvLaser1Entry": pmpump3RinvLaser1Entry,
       "pmpump3RinvLaser1Index": pmpump3RinvLaser1Index,
       "pmpump3RinvLaser1": pmpump3RinvLaser1,
       "pmpump3RinvLaser2Table": pmpump3RinvLaser2Table,
       "pmpump3RinvLaser2Entry": pmpump3RinvLaser2Entry,
       "pmpump3RinvLaser2Index": pmpump3RinvLaser2Index,
       "pmpump3RinvLaser2": pmpump3RinvLaser2,
       "pmpump3RinvReloadInventory": pmpump3RinvReloadInventory,
       "pmpump3RinvHwPlatform": pmpump3RinvHwPlatform,
       "pmpump3RinvModulePlatform": pmpump3RinvModulePlatform,
       "pmpump3RinvSwPlatform": pmpump3RinvSwPlatform,
       "pmpump3Config": pmpump3Config,
       "pmpump3CfgNoValue": pmpump3CfgNoValue,
       "pmpump3tableclientStartup": pmpump3tableclientStartup,
       "pmpump3Cfglaser1Ctrl": pmpump3Cfglaser1Ctrl,
       "pmpump3CfgLineStartUp": pmpump3CfgLineStartUp,
       "pmpump3tablelineStartup": pmpump3tablelineStartup,
       "pmpump3Cfglaser2Ctrl": pmpump3Cfglaser2Ctrl,
       "pmpump3CfgLabels": pmpump3CfgLabels,
       "pmpump3CfgLabelclientTable": pmpump3CfgLabelclientTable,
       "pmpump3CfgLabelclientEntry": pmpump3CfgLabelclientEntry,
       "pmpump3CfgLabelclientIndex": pmpump3CfgLabelclientIndex,
       "pmpump3CfgLabelclientPortn": pmpump3CfgLabelclientPortn,
       "pmpump3CfgLabellineTable": pmpump3CfgLabellineTable,
       "pmpump3CfgLabellineEntry": pmpump3CfgLabellineEntry,
       "pmpump3CfgLabellineIndex": pmpump3CfgLabellineIndex,
       "pmpump3CfgLabellinePortn": pmpump3CfgLabellinePortn,
       "pmpump3CfgWriteConfiguration": pmpump3CfgWriteConfiguration,
       "pmpump3traps": pmpump3traps,
       "pmpump3trapBoardNumber": pmpump3trapBoardNumber,
       "pmpump3Laser2TrapNotUrgentGoesOn": pmpump3Laser2TrapNotUrgentGoesOn,
       "pmpump3Laser2TrapNotUrgentGoesOff": pmpump3Laser2TrapNotUrgentGoesOff,
       "pmpump3Laser2TrapUrgentGoesOn": pmpump3Laser2TrapUrgentGoesOn,
       "pmpump3Laser2TrapUrgentGoesOff": pmpump3Laser2TrapUrgentGoesOff,
       "pmpump3Laser2TrapCritGoesOn": pmpump3Laser2TrapCritGoesOn,
       "pmpump3Laser2TrapCritGoesOff": pmpump3Laser2TrapCritGoesOff,
       "pmpump3Laser1TrapNotUrgentGoesOn": pmpump3Laser1TrapNotUrgentGoesOn,
       "pmpump3Laser1TrapNotUrgentGoesOff": pmpump3Laser1TrapNotUrgentGoesOff,
       "pmpump3Laser1TrapUrgentGoesOn": pmpump3Laser1TrapUrgentGoesOn,
       "pmpump3Laser1TrapUrgentGoesOff": pmpump3Laser1TrapUrgentGoesOff,
       "pmpump3Laser1TrapCritGoesOn": pmpump3Laser1TrapCritGoesOn,
       "pmpump3Laser1TrapCritGoesOff": pmpump3Laser1TrapCritGoesOff,
       "pmpump3PowerTrapUrgentGoesOn": pmpump3PowerTrapUrgentGoesOn,
       "pmpump3PowerTrapUrgentGoesOff": pmpump3PowerTrapUrgentGoesOff}
)
