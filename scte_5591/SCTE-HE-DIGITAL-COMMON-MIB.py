# SNMP MIB module (SCTE-HE-DIGITAL-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HE-DIGITAL-COMMON-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:31:05 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(heDigital,) = mibBuilder.importSymbols(
    "SCTE-HMS-HEADENDIDENT-MIB",
    "heDigital")

(HeClockSource,
 HeResetValue,
 HeTenthCentigrade) = mibBuilder.importSymbols(
    "SCTE-HMS-HEADENDIDENT-TC-MIB",
    "HeClockSource",
    "HeResetValue",
    "HeTenthCentigrade")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

heDigitalCommonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HeDigitalCommonMIBObjects_ObjectIdentity = ObjectIdentity
heDigitalCommonMIBObjects = _HeDigitalCommonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1)
)
_HeDigitalCommonConfig_ObjectIdentity = ObjectIdentity
heDigitalCommonConfig = _HeDigitalCommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 1)
)
_HeDigitalCommonClockTable_Object = MibTable
heDigitalCommonClockTable = _HeDigitalCommonClockTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    heDigitalCommonClockTable.setStatus("current")
_HeDigitalCommonClockEntry_Object = MibTableRow
heDigitalCommonClockEntry = _HeDigitalCommonClockEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 1, 1, 1)
)
heDigitalCommonClockEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    heDigitalCommonClockEntry.setStatus("current")
_HeDigitalCommonTime_Type = DateAndTime
_HeDigitalCommonTime_Object = MibTableColumn
heDigitalCommonTime = _HeDigitalCommonTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 1, 1, 1, 1),
    _HeDigitalCommonTime_Type()
)
heDigitalCommonTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heDigitalCommonTime.setStatus("current")
_HeDigitalCommonClockSource_Type = HeClockSource
_HeDigitalCommonClockSource_Object = MibTableColumn
heDigitalCommonClockSource = _HeDigitalCommonClockSource_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 1, 1, 1, 2),
    _HeDigitalCommonClockSource_Type()
)
heDigitalCommonClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heDigitalCommonClockSource.setStatus("current")
_HeDigitalCommonResetTable_Object = MibTable
heDigitalCommonResetTable = _HeDigitalCommonResetTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    heDigitalCommonResetTable.setStatus("current")
_HeDigitalCommonResetEntry_Object = MibTableRow
heDigitalCommonResetEntry = _HeDigitalCommonResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 1, 2, 1)
)
heDigitalCommonResetEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    heDigitalCommonResetEntry.setStatus("current")
_HeDigitalCommonSoftwareReset_Type = HeResetValue
_HeDigitalCommonSoftwareReset_Object = MibTableColumn
heDigitalCommonSoftwareReset = _HeDigitalCommonSoftwareReset_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 1, 2, 1, 1),
    _HeDigitalCommonSoftwareReset_Type()
)
heDigitalCommonSoftwareReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heDigitalCommonSoftwareReset.setStatus("current")
_HeDigitalCommonHardwareReset_Type = HeResetValue
_HeDigitalCommonHardwareReset_Object = MibTableColumn
heDigitalCommonHardwareReset = _HeDigitalCommonHardwareReset_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 1, 2, 1, 2),
    _HeDigitalCommonHardwareReset_Type()
)
heDigitalCommonHardwareReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heDigitalCommonHardwareReset.setStatus("current")
_HeDigitalCommonWarmReset_Type = HeResetValue
_HeDigitalCommonWarmReset_Object = MibTableColumn
heDigitalCommonWarmReset = _HeDigitalCommonWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 1, 2, 1, 3),
    _HeDigitalCommonWarmReset_Type()
)
heDigitalCommonWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heDigitalCommonWarmReset.setStatus("current")
_HeDigitalCommonStatus_ObjectIdentity = ObjectIdentity
heDigitalCommonStatus = _HeDigitalCommonStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 2)
)
_HeDigitalCommonTempTable_Object = MibTable
heDigitalCommonTempTable = _HeDigitalCommonTempTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    heDigitalCommonTempTable.setStatus("current")
_HeDigitalCommonTempEntry_Object = MibTableRow
heDigitalCommonTempEntry = _HeDigitalCommonTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 2, 1, 1)
)
heDigitalCommonTempEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    heDigitalCommonTempEntry.setStatus("current")
_HeDigitalCommonTemperature_Type = HeTenthCentigrade
_HeDigitalCommonTemperature_Object = MibTableColumn
heDigitalCommonTemperature = _HeDigitalCommonTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 2, 1, 1, 1),
    _HeDigitalCommonTemperature_Type()
)
heDigitalCommonTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heDigitalCommonTemperature.setStatus("current")
_HeDigitalCommonAlarms_ObjectIdentity = ObjectIdentity
heDigitalCommonAlarms = _HeDigitalCommonAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 3)
)
_HeDigitalCommonLog_ObjectIdentity = ObjectIdentity
heDigitalCommonLog = _HeDigitalCommonLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 1, 4)
)
_HeDigitalCommonConformance_ObjectIdentity = ObjectIdentity
heDigitalCommonConformance = _HeDigitalCommonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 2)
)
_HeDigitalCommonCompliances_ObjectIdentity = ObjectIdentity
heDigitalCommonCompliances = _HeDigitalCommonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 2, 1)
)
_HeDigitalCommonGroups_ObjectIdentity = ObjectIdentity
heDigitalCommonGroups = _HeDigitalCommonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 2, 2)
)
_HeDigitalQAM_ObjectIdentity = ObjectIdentity
heDigitalQAM = _HeDigitalQAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3)
)
_HeDigitalMPEG_ObjectIdentity = ObjectIdentity
heDigitalMPEG = _HeDigitalMPEG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4)
)

# Managed Objects groups

heDigitalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 2, 2, 1)
)
heDigitalConfigGroup.setObjects(
      *(("SCTE-HE-DIGITAL-COMMON-MIB", "heDigitalCommonTime"),
        ("SCTE-HE-DIGITAL-COMMON-MIB", "heDigitalCommonClockSource"),
        ("SCTE-HE-DIGITAL-COMMON-MIB", "heDigitalCommonSoftwareReset"),
        ("SCTE-HE-DIGITAL-COMMON-MIB", "heDigitalCommonHardwareReset"),
        ("SCTE-HE-DIGITAL-COMMON-MIB", "heDigitalCommonWarmReset"))
)
if mibBuilder.loadTexts:
    heDigitalConfigGroup.setStatus("current")

heDigitalStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 2, 2, 2)
)
heDigitalStatusGroup.setObjects(
    ("SCTE-HE-DIGITAL-COMMON-MIB", "heDigitalCommonTemperature")
)
if mibBuilder.loadTexts:
    heDigitalStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

heDigitalCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 2, 2, 1, 1)
)
heDigitalCompliance.setObjects(
      *(("SCTE-HE-DIGITAL-COMMON-MIB", "heDigitalConfigGroup"),
        ("SCTE-HE-DIGITAL-COMMON-MIB", "heDigitalStatusGroup"))
)
if mibBuilder.loadTexts:
    heDigitalCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HE-DIGITAL-COMMON-MIB",
    **{"heDigitalCommonMIB": heDigitalCommonMIB,
       "heDigitalCommonMIBObjects": heDigitalCommonMIBObjects,
       "heDigitalCommonConfig": heDigitalCommonConfig,
       "heDigitalCommonClockTable": heDigitalCommonClockTable,
       "heDigitalCommonClockEntry": heDigitalCommonClockEntry,
       "heDigitalCommonTime": heDigitalCommonTime,
       "heDigitalCommonClockSource": heDigitalCommonClockSource,
       "heDigitalCommonResetTable": heDigitalCommonResetTable,
       "heDigitalCommonResetEntry": heDigitalCommonResetEntry,
       "heDigitalCommonSoftwareReset": heDigitalCommonSoftwareReset,
       "heDigitalCommonHardwareReset": heDigitalCommonHardwareReset,
       "heDigitalCommonWarmReset": heDigitalCommonWarmReset,
       "heDigitalCommonStatus": heDigitalCommonStatus,
       "heDigitalCommonTempTable": heDigitalCommonTempTable,
       "heDigitalCommonTempEntry": heDigitalCommonTempEntry,
       "heDigitalCommonTemperature": heDigitalCommonTemperature,
       "heDigitalCommonAlarms": heDigitalCommonAlarms,
       "heDigitalCommonLog": heDigitalCommonLog,
       "heDigitalCommonConformance": heDigitalCommonConformance,
       "heDigitalCommonCompliances": heDigitalCommonCompliances,
       "heDigitalCompliance": heDigitalCompliance,
       "heDigitalCommonGroups": heDigitalCommonGroups,
       "heDigitalConfigGroup": heDigitalConfigGroup,
       "heDigitalStatusGroup": heDigitalStatusGroup,
       "heDigitalQAM": heDigitalQAM,
       "heDigitalMPEG": heDigitalMPEG}
)
