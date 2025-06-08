# SNMP MIB module (CISCO-ENTITY-PROVISIONING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-ENTITY-PROVISIONING-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:13:16 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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

(AutonomousType,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoEntityProvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 139)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoEntityProvMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEntityProvMIBObjects = _CiscoEntityProvMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 139, 1)
)
_CeProvContainerTable_Object = MibTable
ceProvContainerTable = _CeProvContainerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1)
)
if mibBuilder.loadTexts:
    ceProvContainerTable.setStatus("current")
_CeProvContainerEntry_Object = MibTableRow
ceProvContainerEntry = _CeProvContainerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1)
)
ceProvContainerEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ceProvContainerEntry.setStatus("current")


class _CeProvContainerStatus_Type(Integer32):
    """Custom type ceProvContainerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unequipped", 1),
          ("provisioned", 2),
          ("mismatched", 3),
          ("invalid", 4),
          ("equipped", 5),
          ("failed", 6))
    )


_CeProvContainerStatus_Type.__name__ = "Integer32"
_CeProvContainerStatus_Object = MibTableColumn
ceProvContainerStatus = _CeProvContainerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1, 1),
    _CeProvContainerStatus_Type()
)
ceProvContainerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceProvContainerStatus.setStatus("current")
_CeProvContainerEquipped_Type = AutonomousType
_CeProvContainerEquipped_Object = MibTableColumn
ceProvContainerEquipped = _CeProvContainerEquipped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1, 2),
    _CeProvContainerEquipped_Type()
)
ceProvContainerEquipped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceProvContainerEquipped.setStatus("current")
_CeProvContainerDetected_Type = AutonomousType
_CeProvContainerDetected_Object = MibTableColumn
ceProvContainerDetected = _CeProvContainerDetected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1, 3),
    _CeProvContainerDetected_Type()
)
ceProvContainerDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceProvContainerDetected.setStatus("current")
_CeProvMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
ceProvMIBNotificationsPrefix = _CeProvMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 139, 2)
)
_CeProvMIBNotifications_ObjectIdentity = ObjectIdentity
ceProvMIBNotifications = _CeProvMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 139, 2, 0)
)
_CeProvMIBConformance_ObjectIdentity = ObjectIdentity
ceProvMIBConformance = _CeProvMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 139, 3)
)
_CeProvMIBCompliances_ObjectIdentity = ObjectIdentity
ceProvMIBCompliances = _CeProvMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 1)
)
_CeProvMIBGroups_ObjectIdentity = ObjectIdentity
ceProvMIBGroups = _CeProvMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 2)
)

# Managed Objects groups

ceProvContainerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 2, 1)
)
ceProvContainerGroup.setObjects(
      *(("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerStatus"),
        ("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerEquipped"),
        ("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerDetected"))
)
if mibBuilder.loadTexts:
    ceProvContainerGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ceProvMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 1, 1)
)
ceProvMIBCompliance.setObjects(
    ("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerGroup")
)
if mibBuilder.loadTexts:
    ceProvMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-PROVISIONING-MIB",
    **{"ciscoEntityProvMIB": ciscoEntityProvMIB,
       "ciscoEntityProvMIBObjects": ciscoEntityProvMIBObjects,
       "ceProvContainerTable": ceProvContainerTable,
       "ceProvContainerEntry": ceProvContainerEntry,
       "ceProvContainerStatus": ceProvContainerStatus,
       "ceProvContainerEquipped": ceProvContainerEquipped,
       "ceProvContainerDetected": ceProvContainerDetected,
       "ceProvMIBNotificationsPrefix": ceProvMIBNotificationsPrefix,
       "ceProvMIBNotifications": ceProvMIBNotifications,
       "ceProvMIBConformance": ceProvMIBConformance,
       "ceProvMIBCompliances": ceProvMIBCompliances,
       "ceProvMIBCompliance": ceProvMIBCompliance,
       "ceProvMIBGroups": ceProvMIBGroups,
       "ceProvContainerGroup": ceProvContainerGroup}
)
