# SNMP MIB module (CISCO-SWITCH-USAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SWITCH-USAGE-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:55:06 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoSwitchUsageMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 201)
)
if mibBuilder.loadTexts:
    ciscoSwitchUsageMIB.setRevisions(
        ("2001-05-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSwitchUsageMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSwitchUsageMIBObjects = _CiscoSwitchUsageMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 201, 1)
)
_CiscoSwitchUsageStats_ObjectIdentity = ObjectIdentity
ciscoSwitchUsageStats = _CiscoSwitchUsageStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1)
)
_CswitchUsageStatTable_Object = MibTable
cswitchUsageStatTable = _CswitchUsageStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cswitchUsageStatTable.setStatus("current")
_CswitchUsageStatEntry_Object = MibTableRow
cswitchUsageStatEntry = _CswitchUsageStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1, 1, 1)
)
cswitchUsageStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cswitchUsageStatEntry.setStatus("current")
_CswitchUsageByIngrsIntfPkts_Type = Counter32
_CswitchUsageByIngrsIntfPkts_Object = MibTableColumn
cswitchUsageByIngrsIntfPkts = _CswitchUsageByIngrsIntfPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1, 1, 1, 1),
    _CswitchUsageByIngrsIntfPkts_Type()
)
cswitchUsageByIngrsIntfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswitchUsageByIngrsIntfPkts.setStatus("current")
_CswitchUsageByIngrsIntfHCPkts_Type = Counter64
_CswitchUsageByIngrsIntfHCPkts_Object = MibTableColumn
cswitchUsageByIngrsIntfHCPkts = _CswitchUsageByIngrsIntfHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1, 1, 1, 2),
    _CswitchUsageByIngrsIntfHCPkts_Type()
)
cswitchUsageByIngrsIntfHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswitchUsageByIngrsIntfHCPkts.setStatus("current")
_CswitchUsageByIngrsIntfOctets_Type = Counter32
_CswitchUsageByIngrsIntfOctets_Object = MibTableColumn
cswitchUsageByIngrsIntfOctets = _CswitchUsageByIngrsIntfOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1, 1, 1, 3),
    _CswitchUsageByIngrsIntfOctets_Type()
)
cswitchUsageByIngrsIntfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswitchUsageByIngrsIntfOctets.setStatus("current")
_CswitchUsageByIngrsIntfHCOctets_Type = Counter64
_CswitchUsageByIngrsIntfHCOctets_Object = MibTableColumn
cswitchUsageByIngrsIntfHCOctets = _CswitchUsageByIngrsIntfHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1, 1, 1, 4),
    _CswitchUsageByIngrsIntfHCOctets_Type()
)
cswitchUsageByIngrsIntfHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswitchUsageByIngrsIntfHCOctets.setStatus("current")
_CiscoSwitchUsageMIBNotifyPrefix_ObjectIdentity = ObjectIdentity
ciscoSwitchUsageMIBNotifyPrefix = _CiscoSwitchUsageMIBNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 201, 2)
)
_CiscoSwitchUsageMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoSwitchUsageMIBNotifications = _CiscoSwitchUsageMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 201, 2, 0)
)
_CiscoSwitchUsageMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSwitchUsageMIBConformance = _CiscoSwitchUsageMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 201, 3)
)
_CiscoSwitchUsageMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSwitchUsageMIBCompliances = _CiscoSwitchUsageMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 201, 3, 1)
)
_CiscoSwitchUsageMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSwitchUsageMIBGroups = _CiscoSwitchUsageMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 201, 3, 2)
)

# Managed Objects groups

ciscoSwitchUsageMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 201, 3, 2, 1)
)
ciscoSwitchUsageMIBGroup.setObjects(
      *(("CISCO-SWITCH-USAGE-MIB", "cswitchUsageByIngrsIntfPkts"),
        ("CISCO-SWITCH-USAGE-MIB", "cswitchUsageByIngrsIntfHCPkts"),
        ("CISCO-SWITCH-USAGE-MIB", "cswitchUsageByIngrsIntfOctets"),
        ("CISCO-SWITCH-USAGE-MIB", "cswitchUsageByIngrsIntfHCOctets"))
)
if mibBuilder.loadTexts:
    ciscoSwitchUsageMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSwitchUsageMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 201, 3, 1, 1)
)
ciscoSwitchUsageMIBCompliance.setObjects(
    ("CISCO-SWITCH-USAGE-MIB", "ciscoSwitchUsageMIBGroup")
)
if mibBuilder.loadTexts:
    ciscoSwitchUsageMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SWITCH-USAGE-MIB",
    **{"ciscoSwitchUsageMIB": ciscoSwitchUsageMIB,
       "ciscoSwitchUsageMIBObjects": ciscoSwitchUsageMIBObjects,
       "ciscoSwitchUsageStats": ciscoSwitchUsageStats,
       "cswitchUsageStatTable": cswitchUsageStatTable,
       "cswitchUsageStatEntry": cswitchUsageStatEntry,
       "cswitchUsageByIngrsIntfPkts": cswitchUsageByIngrsIntfPkts,
       "cswitchUsageByIngrsIntfHCPkts": cswitchUsageByIngrsIntfHCPkts,
       "cswitchUsageByIngrsIntfOctets": cswitchUsageByIngrsIntfOctets,
       "cswitchUsageByIngrsIntfHCOctets": cswitchUsageByIngrsIntfHCOctets,
       "ciscoSwitchUsageMIBNotifyPrefix": ciscoSwitchUsageMIBNotifyPrefix,
       "ciscoSwitchUsageMIBNotifications": ciscoSwitchUsageMIBNotifications,
       "ciscoSwitchUsageMIBConformance": ciscoSwitchUsageMIBConformance,
       "ciscoSwitchUsageMIBCompliances": ciscoSwitchUsageMIBCompliances,
       "ciscoSwitchUsageMIBCompliance": ciscoSwitchUsageMIBCompliance,
       "ciscoSwitchUsageMIBGroups": ciscoSwitchUsageMIBGroups,
       "ciscoSwitchUsageMIBGroup": ciscoSwitchUsageMIBGroup}
)
