# SNMP MIB module (CISCO-FR-MFR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FR-MFR-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:28:30 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(mfrBundleEntry,
 mfrBundleIndex,
 mfrBundleLinkEntry) = mibBuilder.importSymbols(
    "FR-MFR-MIB",
    "mfrBundleEntry",
    "mfrBundleIndex",
    "mfrBundleLinkEntry")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoFrMfrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 328)
)
if mibBuilder.loadTexts:
    ciscoFrMfrMIB.setRevisions(
        ("2004-03-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoFrMfrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFrMfrMIBObjects = _CiscoFrMfrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 1)
)
_CiscoFrMfrMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoFrMfrMIBNotifications = _CiscoFrMfrMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 1, 0)
)
_CiscoFrMfrBundle_ObjectIdentity = ObjectIdentity
ciscoFrMfrBundle = _CiscoFrMfrBundle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 1, 1)
)
_CfrMfrBundleTable_Object = MibTable
cfrMfrBundleTable = _CfrMfrBundleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfrMfrBundleTable.setStatus("current")
_CfrMfrBundleEntry_Object = MibTableRow
cfrMfrBundleEntry = _CfrMfrBundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfrMfrBundleEntry.setStatus("current")


class _CfrMfrBundleAlarmState_Type(Bits):
    """Custom type cfrMfrBundleAlarmState based on Bits"""
    namedValues = NamedValues(
        *(("mfrBundleOtherError", 0),
          ("mfrBundleInsuffLinksNe", 1),
          ("mfrBundleInsuffLinksFe", 2))
    )

_CfrMfrBundleAlarmState_Type.__name__ = "Bits"
_CfrMfrBundleAlarmState_Object = MibTableColumn
cfrMfrBundleAlarmState = _CfrMfrBundleAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 1, 1, 1, 1, 1),
    _CfrMfrBundleAlarmState_Type()
)
cfrMfrBundleAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrMfrBundleAlarmState.setStatus("current")


class _CfrMfrBundleRestart_Type(TruthValue):
    """Custom type cfrMfrBundleRestart based on TruthValue"""
    defaultValue = 2


_CfrMfrBundleRestart_Type.__name__ = "TruthValue"
_CfrMfrBundleRestart_Object = MibTableColumn
cfrMfrBundleRestart = _CfrMfrBundleRestart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 1, 1, 1, 1, 2),
    _CfrMfrBundleRestart_Type()
)
cfrMfrBundleRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfrMfrBundleRestart.setStatus("current")
_CiscoFrMfrBundleLink_ObjectIdentity = ObjectIdentity
ciscoFrMfrBundleLink = _CiscoFrMfrBundleLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 1, 2)
)
_CfrMfrBundleLinkTable_Object = MibTable
cfrMfrBundleLinkTable = _CfrMfrBundleLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cfrMfrBundleLinkTable.setStatus("current")
_CfrMfrBundleLinkEntry_Object = MibTableRow
cfrMfrBundleLinkEntry = _CfrMfrBundleLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cfrMfrBundleLinkEntry.setStatus("current")


class _CfrMfrBundleLinkAlarmState_Type(Bits):
    """Custom type cfrMfrBundleLinkAlarmState based on Bits"""
    namedValues = NamedValues(
        *(("mfrBundleLinkOtherAlarm", 0),
          ("mfrBundleLinkUnknownVendor", 1),
          ("mfrBundleLinkLinkIdle", 2),
          ("mfrBundleLinkLinkDown", 3),
          ("mfrBundleLinkLinkDiffDelayExceed", 4),
          ("mfrBundleLinkLinkLoopDetected", 5),
          ("mfrBundleLinkLinkUnexpectAdd", 6),
          ("mfrBundleLinkLinkMisMatchBundleNe", 7),
          ("mfrBundleLinkLinkMisMatchBundleFe", 8))
    )

_CfrMfrBundleLinkAlarmState_Type.__name__ = "Bits"
_CfrMfrBundleLinkAlarmState_Object = MibTableColumn
cfrMfrBundleLinkAlarmState = _CfrMfrBundleLinkAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 1, 2, 1, 1, 1),
    _CfrMfrBundleLinkAlarmState_Type()
)
cfrMfrBundleLinkAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrMfrBundleLinkAlarmState.setStatus("current")
_CiscoFrMfrBundleMap_ObjectIdentity = ObjectIdentity
ciscoFrMfrBundleMap = _CiscoFrMfrBundleMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 1, 3)
)
_CfrMfrBundleLinkMappingTable_Object = MibTable
cfrMfrBundleLinkMappingTable = _CfrMfrBundleLinkMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cfrMfrBundleLinkMappingTable.setStatus("current")
_CfrMfrBundleLinkMappingEntry_Object = MibTableRow
cfrMfrBundleLinkMappingEntry = _CfrMfrBundleLinkMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 1, 3, 1, 1)
)
cfrMfrBundleLinkMappingEntry.setIndexNames(
    (0, "FR-MFR-MIB", "mfrBundleIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cfrMfrBundleLinkMappingEntry.setStatus("current")


class _CfrMfrBundleLinkState_Type(Integer32):
    """Custom type cfrMfrBundleLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CfrMfrBundleLinkState_Type.__name__ = "Integer32"
_CfrMfrBundleLinkState_Object = MibTableColumn
cfrMfrBundleLinkState = _CfrMfrBundleLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 1, 3, 1, 1, 1),
    _CfrMfrBundleLinkState_Type()
)
cfrMfrBundleLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrMfrBundleLinkState.setStatus("current")
_CiscoFrMfrMIBConformance_ObjectIdentity = ObjectIdentity
ciscoFrMfrMIBConformance = _CiscoFrMfrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 2)
)
_CiscoFrMfrMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoFrMfrMIBCompliances = _CiscoFrMfrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 2, 1)
)
_CiscoFrMfrMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFrMfrMIBGroups = _CiscoFrMfrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 2, 2)
)
mfrBundleEntry.registerAugmentions(
    ("CISCO-FR-MFR-MIB",
     "cfrMfrBundleEntry")
)
cfrMfrBundleEntry.setIndexNames(*mfrBundleEntry.getIndexNames())
mfrBundleLinkEntry.registerAugmentions(
    ("CISCO-FR-MFR-MIB",
     "cfrMfrBundleLinkEntry")
)
cfrMfrBundleLinkEntry.setIndexNames(*mfrBundleLinkEntry.getIndexNames())

# Managed Objects groups

ciscoFrMfrBundleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 2, 2, 1)
)
ciscoFrMfrBundleGroup.setObjects(
      *(("CISCO-FR-MFR-MIB", "cfrMfrBundleAlarmState"),
        ("CISCO-FR-MFR-MIB", "cfrMfrBundleRestart"))
)
if mibBuilder.loadTexts:
    ciscoFrMfrBundleGroup.setStatus("current")

ciscoFrMfrBundleLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 2, 2, 2)
)
ciscoFrMfrBundleLinkGroup.setObjects(
    ("CISCO-FR-MFR-MIB", "cfrMfrBundleLinkAlarmState")
)
if mibBuilder.loadTexts:
    ciscoFrMfrBundleLinkGroup.setStatus("current")

ciscoFrMfrBundleLinkMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 2, 2, 3)
)
ciscoFrMfrBundleLinkMappingGroup.setObjects(
    ("CISCO-FR-MFR-MIB", "cfrMfrBundleLinkState")
)
if mibBuilder.loadTexts:
    ciscoFrMfrBundleLinkMappingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoFrMfrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 328, 2, 1, 1)
)
ciscoFrMfrMIBCompliance.setObjects(
      *(("CISCO-FR-MFR-MIB", "ciscoFrMfrBundleGroup"),
        ("CISCO-FR-MFR-MIB", "ciscoFrMfrBundleLinkGroup"),
        ("CISCO-FR-MFR-MIB", "ciscoFrMfrBundleLinkMappingGroup"))
)
if mibBuilder.loadTexts:
    ciscoFrMfrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FR-MFR-MIB",
    **{"ciscoFrMfrMIB": ciscoFrMfrMIB,
       "ciscoFrMfrMIBObjects": ciscoFrMfrMIBObjects,
       "ciscoFrMfrMIBNotifications": ciscoFrMfrMIBNotifications,
       "ciscoFrMfrBundle": ciscoFrMfrBundle,
       "cfrMfrBundleTable": cfrMfrBundleTable,
       "cfrMfrBundleEntry": cfrMfrBundleEntry,
       "cfrMfrBundleAlarmState": cfrMfrBundleAlarmState,
       "cfrMfrBundleRestart": cfrMfrBundleRestart,
       "ciscoFrMfrBundleLink": ciscoFrMfrBundleLink,
       "cfrMfrBundleLinkTable": cfrMfrBundleLinkTable,
       "cfrMfrBundleLinkEntry": cfrMfrBundleLinkEntry,
       "cfrMfrBundleLinkAlarmState": cfrMfrBundleLinkAlarmState,
       "ciscoFrMfrBundleMap": ciscoFrMfrBundleMap,
       "cfrMfrBundleLinkMappingTable": cfrMfrBundleLinkMappingTable,
       "cfrMfrBundleLinkMappingEntry": cfrMfrBundleLinkMappingEntry,
       "cfrMfrBundleLinkState": cfrMfrBundleLinkState,
       "ciscoFrMfrMIBConformance": ciscoFrMfrMIBConformance,
       "ciscoFrMfrMIBCompliances": ciscoFrMfrMIBCompliances,
       "ciscoFrMfrMIBCompliance": ciscoFrMfrMIBCompliance,
       "ciscoFrMfrMIBGroups": ciscoFrMfrMIBGroups,
       "ciscoFrMfrBundleGroup": ciscoFrMfrBundleGroup,
       "ciscoFrMfrBundleLinkGroup": ciscoFrMfrBundleLinkGroup,
       "ciscoFrMfrBundleLinkMappingGroup": ciscoFrMfrBundleLinkMappingGroup}
)
