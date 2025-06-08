# SNMP MIB module (SCTE-HMS-HE-FAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-HE-FAN-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:31:48 2025
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

(HeFaultStatus,
 HeMilliAmp,
 heFans) = mibBuilder.importSymbols(
    "SCTE-HMS-HEADENDIDENT-MIB",
    "HeFaultStatus",
    "HeMilliAmp",
    "heFans")

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

heFanModuleMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HeFanMIBObjects_ObjectIdentity = ObjectIdentity
heFanMIBObjects = _HeFanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 1)
)
_HeFanUnitTable_Object = MibTable
heFanUnitTable = _HeFanUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    heFanUnitTable.setStatus("current")
_HeFanUnitEntry_Object = MibTableRow
heFanUnitEntry = _HeFanUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 1, 1, 1)
)
heFanUnitEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    heFanUnitEntry.setStatus("current")
_HeFanUnitAlarm_Type = HeFaultStatus
_HeFanUnitAlarm_Object = MibTableColumn
heFanUnitAlarm = _HeFanUnitAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 1, 1, 1, 1),
    _HeFanUnitAlarm_Type()
)
heFanUnitAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heFanUnitAlarm.setStatus("current")
_HeFanStatusTable_Object = MibTable
heFanStatusTable = _HeFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    heFanStatusTable.setStatus("current")
_HeFanStatusEntry_Object = MibTableRow
heFanStatusEntry = _HeFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 1, 2, 1)
)
heFanStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-HE-FAN-MIB", "heFanStatusIndex"),
)
if mibBuilder.loadTexts:
    heFanStatusEntry.setStatus("current")
_HeFanStatusIndex_Type = Unsigned32
_HeFanStatusIndex_Object = MibTableColumn
heFanStatusIndex = _HeFanStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 1, 2, 1, 1),
    _HeFanStatusIndex_Type()
)
heFanStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    heFanStatusIndex.setStatus("current")
_HeFanStatusCurrent_Type = HeMilliAmp
_HeFanStatusCurrent_Object = MibTableColumn
heFanStatusCurrent = _HeFanStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 1, 2, 1, 2),
    _HeFanStatusCurrent_Type()
)
heFanStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heFanStatusCurrent.setStatus("current")
if mibBuilder.loadTexts:
    heFanStatusCurrent.setUnits("milliamperes")
_HeFanStatusAlarm_Type = HeFaultStatus
_HeFanStatusAlarm_Object = MibTableColumn
heFanStatusAlarm = _HeFanStatusAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 1, 2, 1, 3),
    _HeFanStatusAlarm_Type()
)
heFanStatusAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heFanStatusAlarm.setStatus("current")
_HeFanMIBConformance_ObjectIdentity = ObjectIdentity
heFanMIBConformance = _HeFanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 2)
)
_HeFanMIBCompliances_ObjectIdentity = ObjectIdentity
heFanMIBCompliances = _HeFanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 2, 1)
)
_HeFanMIBGroups_ObjectIdentity = ObjectIdentity
heFanMIBGroups = _HeFanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 2, 2)
)

# Managed Objects groups

heFanUnitMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 2, 2, 1)
)
heFanUnitMandatoryGroup.setObjects(
    ("SCTE-HMS-HE-FAN-MIB", "heFanUnitAlarm")
)
if mibBuilder.loadTexts:
    heFanUnitMandatoryGroup.setStatus("current")

heFanStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 2, 2, 2)
)
heFanStatusGroup.setObjects(
      *(("SCTE-HMS-HE-FAN-MIB", "heFanStatusAlarm"),
        ("SCTE-HMS-HE-FAN-MIB", "heFanStatusCurrent"))
)
if mibBuilder.loadTexts:
    heFanStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

heFanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 2, 1, 1)
)
heFanCompliance.setObjects(
      *(("SCTE-HMS-HE-FAN-MIB", "heFanUnitMandatoryGroup"),
        ("SCTE-HMS-HE-FAN-MIB", "heFanStatusGroup"))
)
if mibBuilder.loadTexts:
    heFanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-HE-FAN-MIB",
    **{"heFanModuleMIB": heFanModuleMIB,
       "heFanMIBObjects": heFanMIBObjects,
       "heFanUnitTable": heFanUnitTable,
       "heFanUnitEntry": heFanUnitEntry,
       "heFanUnitAlarm": heFanUnitAlarm,
       "heFanStatusTable": heFanStatusTable,
       "heFanStatusEntry": heFanStatusEntry,
       "heFanStatusIndex": heFanStatusIndex,
       "heFanStatusCurrent": heFanStatusCurrent,
       "heFanStatusAlarm": heFanStatusAlarm,
       "heFanMIBConformance": heFanMIBConformance,
       "heFanMIBCompliances": heFanMIBCompliances,
       "heFanCompliance": heFanCompliance,
       "heFanMIBGroups": heFanMIBGroups,
       "heFanUnitMandatoryGroup": heFanUnitMandatoryGroup,
       "heFanStatusGroup": heFanStatusGroup}
)
