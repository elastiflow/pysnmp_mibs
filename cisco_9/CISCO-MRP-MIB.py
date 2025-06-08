# SNMP MIB module (CISCO-MRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-MRP-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:12:36 2025
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

ciscoMrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 850)
)
if mibBuilder.loadTexts:
    ciscoMrpMIB.setRevisions(
        ("2017-09-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoMrpMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoMrpMIBNotifs = _CiscoMrpMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 850, 0)
)
_CiscoMrpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMrpMIBObjects = _CiscoMrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 850, 1)
)
_CiscoMrpDomainTable_Object = MibTable
ciscoMrpDomainTable = _CiscoMrpDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoMrpDomainTable.setStatus("current")
_CiscoMrpDomainEntry_Object = MibTableRow
ciscoMrpDomainEntry = _CiscoMrpDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1)
)
ciscoMrpDomainEntry.setIndexNames(
    (0, "CISCO-MRP-MIB", "ciscoMrpDomainIndex"),
)
if mibBuilder.loadTexts:
    ciscoMrpDomainEntry.setStatus("current")
_CiscoMrpDomainIndex_Type = Unsigned32
_CiscoMrpDomainIndex_Object = MibTableColumn
ciscoMrpDomainIndex = _CiscoMrpDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1, 1),
    _CiscoMrpDomainIndex_Type()
)
ciscoMrpDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoMrpDomainIndex.setStatus("current")


class _CiscoMrpDomainID_Type(OctetString):
    """Custom type ciscoMrpDomainID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixedLength = 16


_CiscoMrpDomainID_Type.__name__ = "OctetString"
_CiscoMrpDomainID_Object = MibTableColumn
ciscoMrpDomainID = _CiscoMrpDomainID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1, 2),
    _CiscoMrpDomainID_Type()
)
ciscoMrpDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMrpDomainID.setStatus("current")
_CiscoMrpDomainName_Type = DisplayString
_CiscoMrpDomainName_Object = MibTableColumn
ciscoMrpDomainName = _CiscoMrpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1, 3),
    _CiscoMrpDomainName_Type()
)
ciscoMrpDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMrpDomainName.setStatus("current")


class _CiscoMrpDomainState_Type(Unsigned32):
    """Custom type ciscoMrpDomainState based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CiscoMrpDomainState_Type.__name__ = "Unsigned32"
_CiscoMrpDomainState_Object = MibTableColumn
ciscoMrpDomainState = _CiscoMrpDomainState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1, 4),
    _CiscoMrpDomainState_Type()
)
ciscoMrpDomainState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMrpDomainState.setStatus("current")
_CiscoMrpMIBConform_ObjectIdentity = ObjectIdentity
ciscoMrpMIBConform = _CiscoMrpMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 850, 2)
)
_CiscoMrpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoMrpMIBCompliances = _CiscoMrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 1)
)
_CiscoMrpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoMrpMIBGroups = _CiscoMrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 2)
)

# Managed Objects groups

ciscoMrpMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 2, 1)
)
ciscoMrpMIBMainObjectGroup.setObjects(
      *(("CISCO-MRP-MIB", "ciscoMrpDomainID"),
        ("CISCO-MRP-MIB", "ciscoMrpDomainName"),
        ("CISCO-MRP-MIB", "ciscoMrpDomainState"))
)
if mibBuilder.loadTexts:
    ciscoMrpMIBMainObjectGroup.setStatus("current")


# Notification objects

ciscoMrpRingOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 850, 0, 1)
)
ciscoMrpRingOpen.setObjects(
      *(("CISCO-MRP-MIB", "ciscoMrpDomainID"),
        ("CISCO-MRP-MIB", "ciscoMrpDomainName"),
        ("CISCO-MRP-MIB", "ciscoMrpDomainState"))
)
if mibBuilder.loadTexts:
    ciscoMrpRingOpen.setStatus(
        "current"
    )


# Notifications groups

ciscoMrpMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 2, 2)
)
ciscoMrpMIBNotificationGroup.setObjects(
    ("CISCO-MRP-MIB", "ciscoMrpRingOpen")
)
if mibBuilder.loadTexts:
    ciscoMrpMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoMrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 1, 1)
)
ciscoMrpMIBCompliance.setObjects(
      *(("CISCO-MRP-MIB", "ciscoMrpMIBMainObjectGroup"),
        ("CISCO-MRP-MIB", "ciscoMrpMIBNotificationGroup"))
)
if mibBuilder.loadTexts:
    ciscoMrpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MRP-MIB",
    **{"ciscoMrpMIB": ciscoMrpMIB,
       "ciscoMrpMIBNotifs": ciscoMrpMIBNotifs,
       "ciscoMrpRingOpen": ciscoMrpRingOpen,
       "ciscoMrpMIBObjects": ciscoMrpMIBObjects,
       "ciscoMrpDomainTable": ciscoMrpDomainTable,
       "ciscoMrpDomainEntry": ciscoMrpDomainEntry,
       "ciscoMrpDomainIndex": ciscoMrpDomainIndex,
       "ciscoMrpDomainID": ciscoMrpDomainID,
       "ciscoMrpDomainName": ciscoMrpDomainName,
       "ciscoMrpDomainState": ciscoMrpDomainState,
       "ciscoMrpMIBConform": ciscoMrpMIBConform,
       "ciscoMrpMIBCompliances": ciscoMrpMIBCompliances,
       "ciscoMrpMIBCompliance": ciscoMrpMIBCompliance,
       "ciscoMrpMIBGroups": ciscoMrpMIBGroups,
       "ciscoMrpMIBMainObjectGroup": ciscoMrpMIBMainObjectGroup,
       "ciscoMrpMIBNotificationGroup": ciscoMrpMIBNotificationGroup}
)
